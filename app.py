import streamlit as st
import joblib
model = joblib.load('Email_model')
st.title('Spam Ham Classifier')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
