import streamlit as st
import google.generativeai as genai
from modules.config import (
    MODEL_NAME, PROMPT_TEMPLATE, STAGE_FLOW, STAGE_QUESTIONS, STAGE_DATA_KEY,
    INTENT_CLASSIFICATION_PROMPT, CONTEXTUAL_ANSWER_PROMPT
)


EXIT_KEYWORDS = {'exit', 'quit', 'bye', 'goodbye'}
model = genai.GenerativeModel(MODEL_NAME) # Initialize the model once


def initialize_session_state():
    """Initializes session state variables."""
    if "stage" not in st.session_state:
        st.session_state.stage = "ASK_NAME"
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Initial greeting
        st.session_state.messages.append({"role": "assistant", "content": STAGE_QUESTIONS["ASK_NAME"]})
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {}



def get_initial_greeting():
    """Returns the initial greeting and sets the first stage."""
    st.session_state.stage = "ASK_NAME"
    return STAGE_QUESTIONS["ASK_NAME"]


def get_user_intent(question, user_response):
    """Uses LLM to classify intent."""
    prompt = INTENT_CLASSIFICATION_PROMPT.format(question=question, user_response=user_response)
    try:
        response = model.generate_content(prompt)
    
        intent = response.text.strip().upper()
        if intent in ["ANSWER", "QUESTION", "OFF-TOPIC"]:
            return intent
    except Exception as e:
        st.error(f"Error in intent classification: {e}")
    return "ANSWER" # Default if classification fails


def answer_user_question(user_question, original_question):
    """Uses the LLM to answer a user's question contextually."""
    prompt = CONTEXTUAL_ANSWER_PROMPT.format(user_question=user_question, original_question=original_question)
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error in generating contextual answer: {e}")
        return "I'm sorry, I can't answer that right now. " + original_question


def generate_technical_questions(tech_stack):
    """Calls the LLM to generate technical questions."""
    prompt = PROMPT_TEMPLATE.format(tech_stack=tech_stack)
    try:
        response = model.generate_content(prompt)
        closing_remark = "\n\nThank you for your time. A recruiter will review your information and be in touch soon."
        return response.text + closing_remark
    except Exception as e:
        st.error(f"Error generating technical questions: {e}")
        return "Sorry, I couldn't generate questions. A recruiter will contact you."


def process_user_input(user_input):
    """Processes user input using an intent-based hybrid approach."""
    # 1. Handle exit commands 
    if user_input.lower().strip() in EXIT_KEYWORDS:
        st.session_state.stage = "CONVERSATION_END"
        return "Thank you for your time. The conversation has now ended."

    current_stage = st.session_state.stage
    if current_stage == "CONVERSATION_END":
        return "The conversation has concluded. Please start a new one."

    # 2. bot's current question
    current_question = STAGE_QUESTIONS.get(current_stage, "")
    
    # 3. Classification of intent
    intent = get_user_intent(question=current_question, user_response=user_input)

    # 4. Action based on intent
    if intent == "ANSWER":
        # User is answering, proceeds with the state machine
        if data_key := STAGE_DATA_KEY.get(current_stage):
            st.session_state.candidate_info[data_key] = user_input
        
        next_stage = STAGE_FLOW.get(current_stage, "CONVERSATION_END")
        st.session_state.stage = next_stage
        
        if next_stage == "GENERATE_QUESTIONS":
            tech_stack = st.session_state.candidate_info.get("tech_stack", "general programming")
            return generate_technical_questions(tech_stack)
        else:
            return STAGE_QUESTIONS.get(next_stage, "Thank you.")

    elif intent == "QUESTION" or intent == "OFF-TOPIC":
        # question or is off-topic, answer and re-ask, state doesn't change
        return answer_user_question(user_question=user_input, original_question=current_question)