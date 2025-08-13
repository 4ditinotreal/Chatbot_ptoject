import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="✨",
    layout="centered"
)

API_KEY = "AIzaSyD1zCTZTZiGmhnW8_KVckza8Rx6S6UQJAQ"

genai.configure(api_key=API_KEY)

st.title("My First AI Chatbot :rocket:")
st.write("Welcome! Ask me anything and I'll help you.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

def get_ai_response(user_question):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_question)
        return response.text
    except Exception as e:
        return "Sorry, I'm having trouble right now. Please try again!"

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(user_input)
            st.write(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")
st.markdown("""
### Try asking:
- Tell me a joke
- Explain what AI is
- Help me with math problems
- Write a short story
- What's the weather like? (Note: I can't access real-time data)
""")