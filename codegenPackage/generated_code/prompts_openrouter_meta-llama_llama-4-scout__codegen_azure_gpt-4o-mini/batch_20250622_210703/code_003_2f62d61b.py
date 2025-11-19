"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Create a simple chatbot using a library like Dialogflow to provide customer support for a company offering services like تركيب الستائر and نقل عفش بالاحساء.
Generated: DETERMINISTIC_2f62d61bded70ec0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from google.cloud import dialogflow_v2 as dialogflow

# Initialize Flask app
app = Flask(__name__)

# Set up Dialogflow credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow/credentials.json"

# Dialogflow project ID
PROJECT_ID = 'your-dialogflow-project-id'

def detect_intent_texts(project_id, session_id, text, language_code):
    """
    Detects intent from user input text using Dialogflow.

    Args:
        project_id (str): The Dialogflow project ID.
        session_id (str): The session ID for the conversation.
        text (str): The user input text.
        language_code (str): The language code (e.g., 'en-US').

    Returns:
        str: The response text from Dialogflow.
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        print(f"Error detecting intent: {e}")
        return "Sorry, I couldn't process your request at the moment."

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to handle incoming messages from the user.

    Returns:
        JSON response with the chatbot's reply.
    """
    try:
        req = request.get_json(silent=True, force=True)
        session_id = req.get('sessionId', 'default-session')
        user_message = req.get('message', '')

        # Detect intent and get response from Dialogflow
        response_text = detect_intent_texts(PROJECT_ID, session_id, user_message, 'ar')
        
        return jsonify({'reply': response_text})
    except Exception as e:
        print(f"Error in webhook: {e}")
        return jsonify({'reply': "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Notes:
- Replace `"path/to/your/dialogflow/credentials.json"` with the actual path to your Dialogflow service account key.
- Replace `'your-dialogflow-project-id'` with your actual Dialogflow project ID.
- Ensure you have the necessary libraries installed (`Flask` and `google-cloud-dialogflow`).
- This code is designed to run as a Flask web application and listens for POST requests at the `/webhook` endpoint.
