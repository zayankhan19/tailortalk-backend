import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk Appointment", layout="centered")
st.title("👗 TailorTalk Appointment Chatbot")

# Store chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send request to FastAPI
    try:
        response = requests.post("http://localhost:8000/book", json={"message": user_input})
        if response.status_code == 200:
            reply = response.json().get("response", "🤖 No reply from server.")
        else:
            reply = "❌ Error contacting backend."
    except Exception as e:
        reply = f"❌ Backend connection error: {e}"

    st.session_state.messages.append({"role": "bot", "content": reply})

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

