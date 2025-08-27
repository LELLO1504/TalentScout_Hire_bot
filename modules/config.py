MODEL_NAME = 'gemini-1.5-flash'

PROMPT_TEMPLATE = """
Generate 4 relevant and concise technical interview questions to assess practical knowledge 
for a candidate proficient in the following technologies: {tech_stack}.
"""

#Conversation Flow 

#Defines sequence in "x"->"y" manner
STAGE_FLOW = {
    "ASK_NAME": "ASK_EMAIL",
    "ASK_EMAIL": "ASK_PHONE",
    "ASK_PHONE": "ASK_EXPERIENCE",
    "ASK_EXPERIENCE": "ASK_POSITION",
    "ASK_POSITION": "ASK_LOCATION",
    "ASK_LOCATION": "ASK_TECH_STACK",
    "ASK_TECH_STACK": "GENERATE_QUESTIONS",
    "GENERATE_QUESTIONS": "CONVERSATION_END"
}

#Maps each stage to the question asked
STAGE_QUESTIONS = {
    "ASK_NAME": "Hello! I'm the TalentScout Hiring Assistant, here to help with the initial screening.\nWhat is your full name?",
    "ASK_EMAIL": "Great! What is your email address?",
    "ASK_PHONE": "Thank you. What is your phone number?",
    "ASK_EXPERIENCE": "Got it. How many years of professional experience do you have?",
    "ASK_POSITION": "What is the desired position you are applying for?",
    "ASK_LOCATION": "And what is your current location?",
    "ASK_TECH_STACK": "Almost done. Please list your primary tech stack (e.g., Python, React, SQL, AWS etc).",
    "GENERATE QUESTIONS": "Thank you for the details. Please wait a moment while I generate some technical questions for you.",
    "CONVERSATION_END": "Thank You, wish u all the best."
}

# Maps each stage to the key used to store the answer
STAGE_DATA_KEY = {
    "ASK_NAME": "full_name",
    "ASK_EMAIL": "email",
    "ASK_PHONE": "phone",
    "ASK_EXPERIENCE": "experience",
    "ASK_POSITION": "position",
    "ASK_LOCATION": "location",
    "ASK_TECH_STACK": "tech_stack"
}

INTENT_CLASSIFICATION_PROMPT = """
You are an AI intent-detection model for a hiring chatbot.

**Original question**: "{question}"
**User's response**: "{user_response}"

Analyze the user's response and classify it as one of the following:

* **ANSWER**: The user is addressing the question, even if indirectly.
* **QUESTION**: The user is asking for clarification or more information.
* **OFF-TOPIC**: The user's response is evasive or unrelated.

Return only the classification: ANSWER, QUESTION, or OFF-TOPIC.
"""

CONTEXTUAL_ANSWER_PROMPT = """
You are a witty and sharp AI hiring assistant for TalentScout.

**Situation**: The candidate asked a question instead of answering yours.

**Their question**: "{user_question}"
**Your original question**: "{original_question}"

**Your mission**:
In a single, clever sentence:
1.  Briefly answer their question.
2.  Smoothly steer the conversation back to your original question.

**Example Tone**:
* "Great question! The team size is around 15. Now, about that project you led..."
* "Good one! We offer hybrid work. Speaking of which, how do you approach remote collaboration?"

**Your response must be a single sentence.**
"""