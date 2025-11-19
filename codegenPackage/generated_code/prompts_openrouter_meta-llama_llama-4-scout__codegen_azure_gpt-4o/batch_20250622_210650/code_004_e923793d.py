"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Design a basic chatbot that provides information about UMM FM's programs and events, using a library like Dialogflow.
Generated: DETERMINISTIC_e923793d7af0afaf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import dialogflow_v2 as dialogflow
import os

# Initialize Flask app
app = Flask(__name__)

# Set up Dialogflow credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow-service-account.json"

# Dialogflow project ID
DIALOGFLOW_PROJECT_ID = "your-dialogflow-project-id"
DIALOGFLOW_LANGUAGE_CODE = "en"

# Function to communicate with Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    """
    Detects the intent of the user's text using Dialogflow.
    Args:
        project_id (str): Dialogflow project ID.
        session_id (str): Unique session ID for the user.
        text (str): User's input text.
        language_code (str): Language code for the conversation.
    Returns:
        str: Response from Dialogflow.
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
    except Exception as e:
        return "Sorry, I encountered an error while processing your request."

# Route to handle incoming requests
@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to handle user messages and respond using Dialogflow.
    """
    try:
        # Parse incoming JSON request
        req_data = request.get_json()
        user_message = req_data.get("message", "")
        session_id = req_data.get("session_id", "default_session")

        # Validate input
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Get response from Dialogflow
        dialogflow_response = detect_intent_texts(
            DIALOGFLOW_PROJECT_ID, session_id, user_message, DIALOGFLOW_LANGUAGE_CODE
        )

        # Return response to the user
        return jsonify({"response": dialogflow_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

**Note:** Replace `path/to/your/dialogflow-service-account.json` and `your-dialogflow-project-id` with your actual Dialogflow credentials and project ID. Ensure the Dialogflow library is installed (`pip install google-cloud-dialogflow`) and properly configured.
