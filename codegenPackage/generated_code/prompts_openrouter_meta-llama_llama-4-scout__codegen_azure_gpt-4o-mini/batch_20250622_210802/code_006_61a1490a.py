"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Create a chatbot using a library like Dialogflow to provide information on pariwisata and wisata kuliner in Purworejo Regency.
Generated: DETERMINISTIC_61a1490a2d3e229b
Batch ID: 20250622_210802
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
DIALOGFLOW_PROJECT_ID = 'your-dialogflow-project-id'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'current-user-session'

def detect_intent_texts(project_id, session_id, texts, language_code):
    """
    Detect intent from user input text using Dialogflow.

    Args:
        project_id (str): Dialogflow project ID.
        session_id (str): Unique session ID for the user.
        texts (list): List of user input texts.
        language_code (str): Language code for the request.

    Returns:
        str: Response text from Dialogflow.
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    responses = []
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            responses.append(response.query_result.fulfillment_text)
        except Exception as e:
            print(f"Error detecting intent: {e}")
            responses.append("Sorry, I couldn't process your request.")

    return responses

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat requests.

    Returns:
        JSON response with the chatbot's reply.
    """
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # Detect intent and get response from Dialogflow
        response_texts = detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, [user_input], DIALOGFLOW_LANGUAGE_CODE)
        return jsonify({"responses": response_texts}), 200

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- Replace `"path/to/your/dialogflow/credentials.json"` with the actual path to your Dialogflow service account key.
- Replace `'your-dialogflow-project-id'` with your actual Dialogflow project ID.
- Ensure you have the necessary libraries installed (`Flask` and `google-cloud-dialogflow`).
- This code is designed to run as a Flask web application and listens for POST requests at the `/chat` endpoint.
