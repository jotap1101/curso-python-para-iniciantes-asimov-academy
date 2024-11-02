import pandas as pd
import streamlit as st

# st.write("Hello world")

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer-reviews.csv")
df_top_100_books = pd.read_csv("datasets/top-100-trending-books.csv")

books = df_top_100_books["book title"].unique()
book = st.sidebar.selectbox("Select a book", books)

df_book_filtered = df_top_100_books[df_top_100_books["book title"] == book]
df_reviews_filtered = df_reviews[df_reviews["book name"] == book]

book_title = df_book_filtered["book title"].iloc[0]
book_genre = df_book_filtered["genre"].iloc[0]
book_price = f'${df_book_filtered["book price"].iloc[0]:,.2f}' 
book_rating = df_book_filtered["rating"].iloc[0]
book_year_of_publication = df_book_filtered["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)

col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year_of_publication)

st.divider()

for row in df_reviews_filtered.values:
    message = st.chat_message(str(row[4]))

    message.write(f'**{row[2]}**')
    message.write(f'<div style="text-align: justify;">{row[5]}</div>', unsafe_allow_html=True)