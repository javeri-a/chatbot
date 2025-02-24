import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize chat model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI Styling
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; }
        .title { color: #ff7f50; text-align: center; font-size: 40px; font-weight: bold; }
        .footer { color: gray; text-align: center; margin-top: 50px; }
        .review-box { background-color: #f4f4f4; padding: 10px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🤖 Gemini AI Chatbot</div>", unsafe_allow_html=True)
st.subheader("🚀 Chat with an advanced AI powered by Gemini!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    response = model.generate_content(user_input)
    ai_reply = response.text

    # Display AI response
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

# User Review Section
st.divider()
st.subheader("🌟 User Reviews")
review = st.text_area("Leave a review for Gemini AI:", placeholder="Write your feedback here...")
if st.button("Submit Review"):
    if review:
        st.success("Thank you for your review! 💖")
    else:
        st.warning("Please write something before submitting!")

# Footer
st.markdown("<div class='footer'>✨ Made with ❤️ by <b>Javeria</b> ✨</div>", unsafe_allow_html=True)
