import streamlit as st
from send_email import send_email
import pandas


topics = pandas.read_csv("topics.csv")

with st.form("Contact Us"):
    user_email = st.text_input("Enter Your email address")
    option = st.selectbox("What topic do you want to discuss",
                          (topics["topic"]))
    user_message = st.text_area("Enter Your message")
    button =  st.form_submit_button("Submit")
    if button:
        message = f"""
        Subject: {option}
        From: {user_email}
        {user_message}
        """
        send_email(message)
        st.info("Message was send succesfully")
