import streamlit as st 
import pandas as pd 
import plotly.express as px 
st.set_page_config(layout="wide")


#monthly view / #visao mensal
#billing per unit / #faturamento por unidade
#best-selling product type / #tipo de produto mais vendido
#performance of payment methods / #desempenho das formas do pagamento
#how are the branch reviews? / #como estao as avaliações das filiais?  


st.success("✅ completed")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Date"])

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-"  + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtrer = df[df["Month"] == month]
df_filtrer

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtrer, x="Date", y="Total", color="City", title="billing per day")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtrer, x="Date", y="Product line", 
                  color="City", title="billing by product type",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtrer.groupby("City",) [["Total"]].sum().reset_index()
fig_city = px.bar(city_total,  x="City", y="Total", title="billing per branch")
col3.plotly_chart(fig_city, use_container_width=True)

city_total = df_filtrer.groupby("City",) [["Rating"]].mean().reset_index()
fig_kind = px.pie(df_filtrer,  values="Total", names="Payment", title="payment type")
col4.plotly_chart(fig_kind, use_container_width=True)


city_total = df_filtrer.groupby("City",) [["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtrer,  y="Rating", x="City", title="assessment")
col5.plotly_chart(fig_rating, use_container_width=True)