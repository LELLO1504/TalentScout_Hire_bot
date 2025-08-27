# TalentScout Hiring Assistant 🤖

TalentScout Hiring Assistant is an intelligent and quite a witty chatbot designed to streamline the initial screening process for technical candidates. Built with Python, Streamlit, and gemini-1.5-flash, it gathers essential candidate information and dynamically generates relevant technical questions based on their declared technology stack. 

## 📋 Project Overview

This project was developed as part of the PG-AGI AI/ML Intern Assignment. The primary goal is to create a conversational AI that can conduct a preliminary screening interview. The chatbot guides candidates through a structured conversation to collect key details and then assesses their technical proficiency by generating tailored questions.

### Key Features
* **Structured Information Gathering**: Collects candidate details like name, contact info, experience, and location in a predefined sequence.
* **Dynamic Question Generation**: Uses an LLM to generate relevant technical questions based on the candidate's specified tech stack.
* **Intent-Based Interaction**: Employs a sophisticated hybrid approach that uses an LLM to classify user intent, allowing the bot to handle off-script questions and answers gracefully.
* **Context-Aware Responses**: Maintains the conversational context, providing meaningful responses even when the user deviates from the expected input.
* **Enhanced User Experience**: Features a custom-styled UI for a polished and professional look and feel.

***

## 🚀 Installation Instructions

To run this application locally, please follow the steps below.

**Prerequisites:**
* Python 3.8+
* Git

**Steps:**

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ringerH/TalentScout_Hire_bot.git](https://github.com/ringerHTalentScout_Hire_bot.git)
    cd TalentScout_Hire_bot
    ```

2.  **Create a Virtual Environment**
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Create a file named `requirements.txt` with the following content:
    ```
    streamlit
    google-generativeai
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key**
    The application uses Streamlit's secrets management for the Google API key. Create a secrets file:
    ```bash
    mkdir .streamlit
    touch .streamlit/secrets.toml
    ```
    Add your Google Gemini API key to the `secrets.toml` file:
    ```toml
    GOOGLE_API_KEY = "API_KEY"
    ```

***

## 💻 Usage Guide

1.  **Run the Application**
    From your terminal in the project's root directory, run the following command:
    ```bash
    streamlit run app.py
    ```

2.  **Interact with the Chatbot**
    * A browser window will open with the chat interface.
    * The chatbot will greet you and begin asking for your information.
    * Respond to each question in the chat input box.
    * After providing your tech stack, the bot will generate technical questions for you.
    * To end the conversation, you can type exit keywords like `bye` or `quit`.
    * To start over, use the "Start New Conversation" button in the sidebar.

***

## 🛠️ Technical Details

* **Language**: Python 
* **Frontend Framework**: Streamlit 
* **Large Language Model**: Google Gemini (`gemini-1.5-flash`) accessed via the `google-generativeai` library.
* **Architecture**:
    The application follows a modular and scalable design:
    * `app.py`: The main entry point that initializes the app and handles the chat loop.
    * `conversation.py`: Contains the core logic for processing user input, managing conversation state, and interacting with the LLM.
    * `config.py`: A centralized configuration file for prompts, conversation flow (`STAGE_FLOW`), and mappings, making the application easy to modify and extend.
    * `ui.py` & `style.py`: Modules dedicated to building the user interface and applying custom styling, separating presentation from logic.
    * **Hybrid State Management**: The architecture uses a deterministic state machine (`STAGE_FLOW` in `config.py`) to ensure all required data is collected. This is enhanced by an LLM-based intent classifier, creating a robust yet flexible conversational experience.

***

## 🧠 Prompt Design

The effectiveness of this chatbot relies on a multi-prompt strategy, where different prompts are designed for specific tasks.

1.  **`INTENT_CLASSIFICATION_PROMPT`**: This prompt acts as a router. Instead of simply feeding user input to the main logic, it first asks the LLM to classify the user's intent as one of `ANSWER`, `QUESTION`, or `OFF-TOPIC`. This is crucial for deciding whether to proceed in the conversation flow or handle an interruption.

2.  **`CONTEXTUAL_ANSWER_PROMPT`**: This prompt is triggered when the user's intent is classified as a `QUESTION`. Its mission is to generate a witty, single-sentence response that answers the user's question while smoothly steering the conversation back to the original topic. It uses examples to guide the LLM's tone and format.

3.  **`PROMPT_TEMPLATE`**: This is the final prompt in the main flow. It instructs the LLM to generate 4 concise technical interview questions based on the `{tech_stack}` variable collected from the user.

***

## 💡 Challenges & Solutions

1.  **Challenge**: Maintaining a structured conversation flow while still feeling natural. A purely scripted bot is brittle, while a purely generative one can easily be sidetracked.
    * **Solution**: A hybrid model was implemented. A deterministic state machine (defined in `config.py`) ensures all necessary data points are collected in order. The LLM-based intent classification layer provides the flexibility to handle user questions and off-topic remarks without breaking the primary screening flow.

2.  **Challenge**: Preserving conversation history and candidate data across user interactions in Streamlit's script-rerun environment.
    * **Solution**: Streamlit's `session_state` (`st.session_state`) was used to store the conversation history (`messages`), the current conversation stage (`stage`), and all collected candidate data (`candidate_info`). This ensures state is maintained reliably throughout a single user session.
