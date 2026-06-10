import streamlit as st
st.title("My first streamlit app")
n=st.text_input("Enter your name")
if st.button("Submit"):
  st.write("Hai {n} welcome")
