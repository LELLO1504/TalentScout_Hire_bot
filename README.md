# TalentScout Hiring Assistant 🤖

TalentScout Hiring Assistant is an intelligent and witty chatbot designed to streamline the initial screening process for technical candidates. Built with Python, Streamlit, and `gemini-1.5-flash`, it gathers essential candidate information and dynamically generates relevant technical questions based on their declared technology stack.

## 📋 Project Overview

This project was developed as part of the PG-AGI AI/ML Intern Assignment. The primary goal is to create a conversational AI that can conduct a preliminary screening interview. The chatbot guides candidates through a structured conversation to collect key details and then assesses their technical proficiency by generating tailored questions.

### Key Features
* **Structured Information Gathering**: Collects candidate details like name, contact info, experience, and location in a predefined sequence.
* **Dynamic Question Generation**: Uses an LLM to generate relevant technical questions based on the candidate's specified tech stack.
* **Intent-Based Interaction**: Employs a sophisticated hybrid approach that uses an LLM to classify user intent, allowing the bot to handle off-script questions and answers gracefully.
* **Context-Aware Responses**: Maintains the conversational context, providing meaningful responses even when the user deviates from the expected input.
* **Enhanced User Experience**: Features a custom-styled UI for a polished and professional look and feel.

[Live Application](http://3.108.220.28:8501/)

***

## ✨ Project Highlights

| Feature | Description |
| :--- | :--- |
| **Overall Highlight** | An intelligent hiring assistant that goes beyond simple scripts by understanding user intent and handling conversational detours gracefully. |
| **Core Strength** | **Robustness & Intelligent**. The hybrid model of a state machine and an intent-classifying LLM prevents the conversation from breaking and handles the user inputs in a witty way, creating a smooth and resilient user experience. |
| **Prompt Engineering** | Utilizes a multi-prompt strategy: an **intent classifier** to route user input, a **contextual prompter** to handle user questions, and a **generator prompt** for creating technical questions. |
| **State Management** | Employs a deterministic **State Machine** (`STAGE_FLOW`) to guarantee the collection of all required candidate data in a specific order, managed via Streamlit's `session_state`. |
| **UI/UX** | Features a custom-styled interface with a dynamic background and tailored chat bubbles to provide a professional and engaging user experience beyond default Streamlit. |
| **Cloud Deployment** | Ready for production deployment on cloud services like **AWS EC2**, allowing for public accessibility and real-world application. |

***

## 🚀 Local Installation

To run this application on your local machine, please follow the steps below.

**Prerequisites:**
* Python 3.8+
* Git

**Steps:**

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ringerH/TalentScout_Hire_bot.git](https://github.com/ringerH/TalentScout_Hire_bot.git)
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
    The repository should contain a `requirements.txt` file. Install the packages using:
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
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
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

## ☁️ Cloud Deployment (AWS EC2)

To deploy this application for public access, you can use an AWS EC2 instance.

1.  **Launch an EC2 Instance**:
    * In your AWS Console, launch a new EC2 instance.
    * **AMI**: Choose **Ubuntu Server 22.04 LTS**.
    * **Instance Type**: Select **t2.micro** (Free Tier eligible).
    * **Key Pair**: Create and download a new `.pem` key pair. You'll need this to connect.
    * **Security Group**: Create a rule to allow **SSH (port 22)** from your IP. Add a second rule to allow **Custom TCP on port 8501** from **Anywhere (0.0.0.0/0)**.

2.  **Connect to Your Instance**:
    Use SSH to connect to your instance. On your local machine, make your key read-only:
    ```bash
    chmod 400 your-key-name.pem
    ssh -i /path/to/your-key-name.pem ubuntu@<Your-EC2-Public-IP>
    ```

3.  **Set Up the Server**:
    Install Python, pip, venv, and Git.
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3-pip python3-venv git -y
    ```

4.  **Deploy the Code**:
    Clone your repository onto the server.
    ```bash
    git clone [https://github.com/ringerH/TalentScout_Hire_bot.git](https://github.com/ringerH/TalentScout_Hire_bot.git)
    cd TalentScout_Hire_bot
    ```

5.  **Install Dependencies**:
    Create a virtual environment and install the required packages.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

6.  **Configure API Key on Server**:
    Create the Streamlit secrets file on the EC2 instance.
    ```bash
    mkdir .streamlit
    nano .streamlit/secrets.toml
    ```
    Add your `GOOGLE_API_KEY` to the file and save it (Ctrl+X, Y, Enter).

7.  **Run the App Persistently with `tmux`**:
    Install `tmux` to keep the app running after you disconnect.
    ```bash
    sudo apt install tmux -y
    tmux new -s chatbot
    ```
    Inside the `tmux` session, activate the environment and run the app:
    ```bash
    source venv/bin/activate
    streamlit run app.py --server.address=0.0.0.0
    ```
    Detach from the session by pressing **Ctrl+B**, then **D**.

8.  **Access Your App**:
    Your chatbot is now live at `http://<Your-EC2-Public-IP>:8501`.

***

## 🛠️ Technical Details

* **Language**: Python
* **Frontend Framework**: Streamlit
* **Large Language Model**: Google Gemini (`gemini-1.5-flash`) accessed via the `google-generativeai` library.
* **Architecture**:
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

2.  **Challenge**: The default Streamlit UI is functional but lacks a distinct visual identity suitable for a professional application.
    * **Solution**: Custom CSS was written in the `style.py` module to significantly enhance the UI. This includes a dynamic animated background, custom styling for chat bubbles, and improved button aesthetics, creating a more engaging user experience.

3.  **Challenge**: Preserving conversation history and candidate data across user interactions in Streamlit's script-rerun environment.
    * **Solution**: Streamlit's `session_state` (`st.session_state`) was used to store the conversation history (`messages`), the current conversation stage (`stage`), and all collected candidate data (`candidate_info`). This ensures state is maintained reliably throughout a single user session.
