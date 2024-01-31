# streamlit run app.py

import streamlit as st

st.header("Welcome to GenAI!", divider="rainbow")


query = st.text_input("Query : ")
if query:
    st.write("You entered : ", query)
    
button_result = st.button("Run")
if button_result:
    st.write("Running...")