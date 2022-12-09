import streamlit as st
from transformers import pipeline
classifier = pipeline(model="SkolkovoInstitute/russian_toxicity_classifier")
st.title("Приложение определения токсичный комментариве на русском языке")
name = st.text_input("Введите текст")
if(st.button('Отправить')):
    result = classifier(name)
    st.success(result)
