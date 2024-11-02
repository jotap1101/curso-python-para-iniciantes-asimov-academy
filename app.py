import pandas as pd
import plotly.express as px
import streamlit as st

# st.write("Hello world")

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer-reviews.csv")
df_top_100_books = pd.read_csv("datasets/top-100-trending-books.csv")

price_min = df_top_100_books["book price"].min()
price_max = df_top_100_books["book price"].max()

# price_range = st.sidebar.slider("Price Range", price_min, price_max, (price_min, price_max))
# df_top_100_books_filtered = df_top_100_books[df_top_100_books["book price"] <= price_range]

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

df_books = df_top_100_books[df_top_100_books["book price"] <= max_price]

df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)