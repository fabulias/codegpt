import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


codegpt_agent_id = os.getenv("CODEGPT_AGENT_ID")
codegpt_api_key = os.getenv("CODEGPT_API_KEY")
codegpt_api_base = os.getenv("CODEGPT_API_BASE")
# Function to handle agent interaction:
def process_message(message):
    url = f'{codegpt_api_base}/chat/completions'
    headers = {
        "accept": "application/json",
        "authorization": f'Bearer {codegpt_api_key}' 
    }
    payload = {
        "agentId": codegpt_agent_id,
        "messages": [
            {
                "content": message,
                "role": "user"
            }
        ],
        "format": "json",
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = json.loads(response.text)
        return data["choices"][0]["message"]["content"]  # Extract agent response

    except (requests.exceptions.RequestException, KeyError) as e:
        st.error("Error contacting the agent:", e)
        return "An error occurred. Please try again later."
    
# Function which define a chat UI for codeGPT agent
def chat_ui():
    st.title("Chat with your agent")

    # Input field for message:
    user_message = st.text_input("Type your question here...", key="user_message")

    # Submit button to send message:
    if st.button("Send", key="send_button"):
        agent_response = process_message(user_message)
        st.write(agent_response)

def page2():
    st.title("Work in progress")


#sidebar
PAGES = {
    "Chat with your agent": chat_ui,
    "Readme": page2
}

st.sidebar.title('Main page')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page()