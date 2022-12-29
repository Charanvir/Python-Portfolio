import streamlit as st

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")

    # is a Boolean type, button is either True or False
    submit_button = st.form_submit_button("Send")
    if submit_button:
        print(user_email)
        print(message)
