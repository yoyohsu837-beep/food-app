import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("📸 拍照測熱量")
api_key = st.text_input("請輸入你的 Google API Key", type="password")

uploaded_file = st.file_uploader("選擇食物照片...", type=["jpg", "png", "jpeg"])

if uploaded_file and api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    image = Image.open(uploaded_file)
    st.image(image, caption='已上傳照片', use_column_width=True)

    if st.button("開始分析"):
        response = model.generate_content(["請分析這份食物的熱量與營養成分", image])
        st.write(response.text)
