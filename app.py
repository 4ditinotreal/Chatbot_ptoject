import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Add it to your .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Aurora AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

.stChatMessage {
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 45px;
    font-size:16px;
}

section[data-testid="stSidebar"] {
    border-right:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;color:#4F8BF9;font-size:60px;'>
🤖 Aurora AI
</h1>

<p style='text-align:center;font-size:22px;color:gray;'>
Your Intelligent AI Assistant
</p>
""", unsafe_allow_html=True)

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
        width=100
    )

    st.title("Aurora AI")

    st.success("🟢 Online")

    st.markdown("---")

    st.subheader("Model")

    st.info("Gemini 2.5 Flash")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("Example Questions")

    st.markdown("""
- Explain Artificial Intelligence

- Write a Python Stack Program

- Create an HTML Login Page

- Difference between SQL and MySQL

- Write a Professional Resume

- Explain OOP Concepts

- Tell me a joke

- Write a cover letter
""")

    st.markdown("---")

    st.caption("Made with ❤️ using Streamlit & Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_ai_response(prompt):

    response = model.generate_content(prompt)

    return response.text

user_input = st.chat_input("💬 Ask me anything...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Aurora is thinking..."):

            try:
                reply = get_ai_response(user_input)
            except Exception as e:
                reply = f"❌ Error:\n\n{e}"

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )