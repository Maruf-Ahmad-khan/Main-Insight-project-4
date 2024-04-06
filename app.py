import streamlit as st

email = st.text_input("Enter Email")
password = st.text_input("Enter Password")
gender = st.selectbox("Select Gender", ['male', 'female', 'others'])
Button = st.button("Please Login")

if Button:
     if email == "mk7446683@gmail.com" and password == "12345":
          # st.success("Login Successful")
          st.balloons()
          st.write(gender)
          
     else:
          st.error("Login Failed")
     