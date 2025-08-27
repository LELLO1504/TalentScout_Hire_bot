import streamlit as st
import google.generativeai as genai

from modules.conversation import initialize_session_state, process_user_input
from modules.ui import display_chat_history, render_sidebar, display_initial_greeting
from modules.style import load_css

# Page and model configuration 
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")
st.title("TalentScout Hiring Assistant 🤖")

load_css()

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error(f"Error configuring the AI model: {e}", icon="🚨")
    st.stop()

#initialization
initialize_session_state()
render_sidebar()

#Display Chat
display_initial_greeting()
display_chat_history()

# Interactiom Logic
if user_input := st.chat_input("Your response..."):
    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process input and get bot response
    with st.spinner("Thinking..."):
        bot_response = process_user_input(user_input)

    # Add and display bot response
    if bot_response:  # Only add if there's a response
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)