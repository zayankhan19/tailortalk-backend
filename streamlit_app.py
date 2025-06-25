import streamlit as st
import requests

st.title("🧵 TailorTalk - Book Your Appointment")
st.write("Chat with the assistant to schedule a meeting.")

history = st.session_state.get("history", [])

user_input = st.text_input("You:", key="input")
if user_input:
    response = requests.post("http://localhost:8000/book", json={"message": user_input})
    bot_reply = response.json()["response"]
    history.append((user_input, bot_reply))
    st.session_state.history = history

for user, bot in history:
    st.markdown(f"**You:** {user}")
    st.markdown(f"**TailorTalk:** {bot}")
import streamlit as st

st.set_page_config(page_title="Test App", layout="centered")

st.title("🎈 Hello, Streamlit!")
st.write("This is a test to check if your Streamlit is working correctly.")

# Optional: Add interaction
if st.button("Click Me"):
    st.success("Streamlit is working! 🎉")


