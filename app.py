import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.title("AI Document Assistant")

if not api_key:
    st.error("⚠️ `GOOGLE_API_KEY` is missing! Please make sure your `.env` file has `GOOGLE_API_KEY=your_api_key`.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.5-flash")

    question = st.text_input("Ask anything:")

    if st.button("Generate"):
        if question:
            with st.spinner("Generating response..."):
                try:
                    response = model.generate_content(question)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question first.")
            