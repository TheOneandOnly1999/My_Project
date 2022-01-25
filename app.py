import streamlit as st
import joblib
st.title('Spam Ham Deployment')
test_model=joblib.load('spam_ham')
ip=st.text_input('Enter your message')
op=test_model.predict([ip])
if st.button('Predict'):
  st.title(op)