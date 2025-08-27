import streamlit as st

def load_css():
    """Loads custom CSS for a starry background and improved UI elements."""
    css = """
    <style>
        @keyframes move-twink-back {
            from {background-position:0 0;}
            to {background-position:-10000px 5000px;}
        }

        .stApp {
            background: #000 url(https://www.script-tutorials.com/demos/360/images/stars.png) repeat top center;
            animation: move-twink-back 200s linear infinite;
        }

        .stChatMessage {
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid transparent;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            backdrop-filter: blur(2px); /* Frosted glass effect for chat bubbles */
        }
        
        [data-testid="chat-message-container"]:has([data-testid="stChatMessageContent-assistant"]) {
            background-color: rgba(38, 39, 48, 0.7); /* Semi-transparent dark */
        }

        [data-testid="chat-message-container"]:has([data-testid="stChatMessageContent-user"]) {
             background-color: rgba(58, 63, 74, 0.7); /* Semi-transparent lighter */
        }
        
        h1 {
            color: #FFFFFF;
            text-shadow: 0 0 10px rgba(34, 167, 240, 0.5);
        }

        .stButton>button {
            width: 100%;
            border-radius: 8px;
            border: 1px solid #22a7f0;
            color: #22a7f0;
            background-color: transparent;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            border-color: #FFFFFF;
            color: #FFFFFF;
            background-color: #22a7f0;
        }
        .stButton>button:active {
            transform: scale(0.98);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)