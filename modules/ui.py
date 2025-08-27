import streamlit as st
from modules.conversation import get_initial_greeting


def display_chat_history():
    """Displays the entire chat history with avatars."""
    avatars = {"assistant": "🤖", "user": "🧑‍💻"}
    
    for message in st.session_state.messages:
        # Updated: Use the avatar corresponding to the message role
        with st.chat_message(message["role"], avatar=avatars.get(message["role"])):
            st.markdown(message["content"])


def reset_conversation():
    """Resets the conversation and shows a confirmation toast."""
    st.toast('Conversation has been reset!', icon='🔄')
    st.session_state.clear()
    
    
def render_sidebar():
    """Renders a more structured sidebar with a title and info."""
    with st.sidebar:
        st.title("Controls")
        st.info("Click the button below to clear the chat history and start a new conversation.")
        
        st.button("Start New Conversation", on_click=reset_conversation)


def display_initial_greeting():
    """Adds the initial greeting to the message list if it's empty."""
    if not st.session_state.messages:
        initial_message = get_initial_greeting()
        st.session_state.messages.append({"role": "assistant", "content": initial_message})