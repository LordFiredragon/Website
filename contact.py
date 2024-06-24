import streamlit as st
import smtplib, ssl


def send_email(message):
    global host, port, username, password
    host = "smtp.gmail.com"
    port = 465
    username = "firedragon2040@gmail.com"
    password = 'pcosskuiokymgfxj'
    receiver = "firedragon2040@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


st.header("CONTACT ME HERE THRU EM@IL")


with st.form(key="email_forms"):
    user_email = st.text_input("Add your email here")
    raw_message = st.text_area("Place your message here")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {raw_message}
"""
    button = st.form_submit_button("SUBMIT")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
