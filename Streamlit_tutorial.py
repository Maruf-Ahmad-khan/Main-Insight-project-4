import streamlit as st
import pandas as pd
import time
st.title("Startup Dashboard")
st.header("I am learning Streamlit")
st.subheader("Maruf khan")
st.write("This is a normal text")

st.markdown("""
            #### My favorite book
                 Python data analytics
                 Automate boring stuff
                 Python Robust
          """)

st.code("""
def func(input):
    return func**2

x = func(2)

        """)

st.latex('x^2 + y^2 + 2 = 0')

# Display DataFrame

df = pd.DataFrame({
     "Name" : ['Maruf', 'Farhan', 'Amir'],
     'Course' : ["Engineering", "Pharmacy", "Pharmacy"]
    , "Duration": ["4 Years", "4 Years", "4 Years"]
})
st.dataframe(df)
st.metric("Revenue", "Rs 3L", "-3%")
st.json({
     "Name" : ['Maruf', 'Farhan', 'Amir'],
     'Course' : ["Engineering", "Pharmacy", "Pharmacy"]
    , "Duration": ["4 Years", "4 Years", "4 Years"]
})

# Display Media
st.image('Compaign Report Dashboard.png')
st.video('Artificial Intelligence.mp4')

# Creating Layout
# sidebar and columns
st.sidebar.title('Sidebar ka Title')
col1, col2 = st.columns(2)
# Text manager
with col1:
     st.image('Compaign Report Dashboard.png')
with col2:
     st.video("Artificial Intelligence.mp4")
     
# Showing status
st.error("login failed")
st.success("login success")
st.info("Login successful")
st.warning("loging successful")

# progress bar
bar = st.progress(0)
for i in range(1, 101):
     time.sleep(0.1)
     bar.progress(i)
     
# Taking user input
email = st.text_input("Enter email")
numbers = st.number_input("Enter age")
Date = st.date_input("Enter Registration date")




