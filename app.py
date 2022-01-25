import streamlit as st
import joblib
st.title('Sentiment Analysis')
test_model=joblib.load('sentiment_analysis')
ip=st.text_input('Enter your message')
op=test_model.predict([ip])
if st.button('Predict'):
  st.title(op) 
