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

st.set_page_config(
    page_title="Aurora AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:3rem;
padding-right:3rem;
}

.stChatMessage{
border-radius:15px;
padding:15px;
margin-bottom:12px;
}

.stTextInput>div>div>input{
border-radius:15px;
}

.stButton>button{
border-radius:12px;
width:100%;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;color:#4F8BF9;'>
🤖 Aurora AI
</h1>

<p style='text-align:center;font-size:18px;color:gray;'>
Your Intelligent AI Assistant
</p>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_ai_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

user_input = st.chat_input("Ask me anything...")

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

        with st.spinner("Thinking..."):

            try:
                reply = get_ai_response(user_input)
            except Exception as e:
                reply = f"Error:\n\n{e}"

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
        width=90
    )

    st.title("Nova AI")

    st.success("🟢 Online")

    st.markdown("---")

    st.markdown("### Model")

    st.info("Gemini 2.5 Flash")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()

    st.markdown("---")

    st.markdown("### Suggestions")

    st.markdown("""
• Explain AI

• Write Python Code

• HTML Login Page

• Resume Builder

• SQL vs MySQL
""")