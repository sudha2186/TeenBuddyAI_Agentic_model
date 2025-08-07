import streamlit as st
from gemini_handler import ask_gemini
from pdf_reader import extract_text_from_pdf
from utils import get_download_link

# --- Sidebar ---
st.sidebar.title("🌟 TeenBuddyAI")
st.sidebar.markdown("#### 🤖 Your Study + Career Guide")
st.sidebar.markdown("Helping youth with:")
st.sidebar.markdown("- 📚 Study Support\n- 📝 Quick Exam Prep\n- 🧭 Career Guidance")
theme = st.sidebar.selectbox("🎨 Choose Theme", ["Light", "Dark"])  # ✅ Only one theme selector

# --- Theme Styling ---
if theme == "Dark":
    st.markdown("""
        <style>
        body {
            background-color: #121212;
        }
        .custom-container {
            background-color: #1e1e1e;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
            padding: 1rem;
            border-radius: 10px;
        }
        .custom-container h3 {
            color: #a3bffa;
        }
        .custom-container li {
            color: #e6e6e6;
            margin-bottom: 10px;
        }
        .custom-container strong {
            color: #87cefa;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .custom-container {
            background-color: #ffffff;
            color: #1e1e1e;
            font-family: 'Segoe UI', sans-serif;
            padding: 1rem;
            border-radius: 10px;
        }
        .custom-container h3 {
            color: #1a237e;
        }
        .custom-container li {
            color: #333333;
            margin-bottom: 10px;
        }
        .custom-container strong {
            color: #0d47a1;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Title ---
st.title("🧠 TeenBuddyAI Chatbot")

# --- User Choice ---
option = st.radio(
    "What would you like to do?",
    ("Ask a Question", "Quick Exam Prep", "Get Free Resources", "Upload PDF Notes", "Career Advice")
)

query = st.text_input("Enter your question/topic:")

uploaded_file = st.file_uploader("📄 Upload your notes (PDF)", type="pdf") if option == "Upload PDF Notes" else None

# --- Response Generation ---
if st.button("Submit"):
    if option == "Ask a Question":
        final_prompt = f"""
    You are a friendly educational chatbot called TeenBuddyAI helping students.

    Answer the following question in a clear, engaging tone.

    At the end of your answer, add a short, friendly follow-up sentence to keep the conversation going (like "Need help with anything else?" or "Want to explore something more?").

    QUESTION: {query}
    """
        response = ask_gemini(final_prompt)

    elif option == "Quick Exam Prep":
        prompt = f"Make a 5-point revision note, memory trick, and 1 MCQ with answer for: {query}"
        response = ask_gemini(prompt)
    elif option == "Career Advice":
        prompt = f"Give study/career advice for: {query}. Include possible paths or motivation tips."
        response = ask_gemini(prompt)
    elif option == "Get Free Resources":
        yt_link = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        response = f"""**Top Study Resources**  
🔗 YouTube: [{query}]({yt_link})  
📘 Khan Academy: https://www.khanacademy.org/  
📚 NCERT Books: https://ncert.nic.in/  
📖 BYJU'S: https://byjus.com"""
    elif option == "Upload PDF Notes":
        extracted_text = extract_text_from_pdf(uploaded_file)
        prompt = f"Summarize these notes and create an MCQ:\n{extracted_text}"
        response = ask_gemini(prompt)
    else:
        response = "Please enter a valid option."

    # --- Display Response ---
    st.markdown("### 🤖 TeenBuddyAI Says:")
    st.markdown(f"<div class='custom-container'>{response}</div>", unsafe_allow_html=True)
    st.markdown(get_download_link(response), unsafe_allow_html=True)
