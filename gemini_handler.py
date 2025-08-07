import streamlit as st
import google.generativeai as genai

# --- Prompt user for their Gemini API key ---
st.sidebar.title("🔐 API Key Setup")
user_api_key = st.sidebar.text_input("Enter your Gemini API key", type="password")

if user_api_key:
    try:
        genai.configure(api_key=user_api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        st.sidebar.success("✅ Gemini API configured!")
    except Exception as e:
        st.sidebar.error(f"Error configuring API: {str(e)}")
else:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to start.")
    st.stop()


def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
