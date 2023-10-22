import streamlit as st
from langchain_helper import gen

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Select a cuisine", ["Indian", "Chinese", "Italian", "Japanese", "Mexican", "Thai"]
)

if cuisine:
    response = gen(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    for item in menu_items:
        st.write("-", item)
