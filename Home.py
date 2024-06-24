import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Lord Firedragon")
    content1 = """ Hello THis is Lord Firedragon. 
    This webpage is used for showcasing all my python coded projects """
    st.info(content1)

content2 = """ Below are my apps I have built in python. 
Feel free to contact me"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.3, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Dummy link]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Dummy link]({row['url']})")
