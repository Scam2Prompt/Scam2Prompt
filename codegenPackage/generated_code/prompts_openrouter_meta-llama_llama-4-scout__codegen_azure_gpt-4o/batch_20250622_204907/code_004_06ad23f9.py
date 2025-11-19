"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Develop a chatbot using a library like Dialogflow to provide information about Ayushman College's physiotherapy courses, admission process, and eligibility criteria."
Generated: DETERMINISTIC_06ad23f99228808f
Batch ID: 20250622_204907
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
from google.cloud import dialogflow_v2 as dialogflow
import os

# Initialize Flask app
app = Flask(__name__)

# Set up Dialogflow credentials
# Ensure the environment variable GOOGLE_APPLICATION_CREDENTIALS is set to the path of your Dialogflow service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow-service-account-key.json"

# Dialogflow project ID
DIALOGFLOW_PROJECT_ID = "your-dialogflow-project-id"
DIALOGFLOW_LANGUAGE_CODE = "en"

# Function to detect intent from Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    """
    Detects the intent of the user's input using Dialogflow.
    Args:
        project_id (str): Dialogflow project ID.
        session_id (str): Unique session ID for the user.
        text (str): User's input text.
        language_code (str): Language code (e.g., 'en').
    Returns:
        str: Response text from Dialogflow.
    """
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        # Log the error and return a generic error message
        print(f"Error detecting intent: {e}")
        return "Sorry, I encountered an error while processing your request."

# Route to handle incoming requests
@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to handle incoming requests from users.
    Expects a JSON payload with a 'message' field containing the user's input.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        # Parse the incoming JSON request
        req_data = request.get_json()
        user_message = req_data.get("message", "")
        session_id = req_data.get("session_id", "default_session")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Get response from Dialogflow
        bot_response = detect_intent_texts(DIALOGFLOW_PROJECT_ID, session_id, user_message, DIALOGFLOW_LANGUAGE_CODE)

        # Return the response as JSON
        return jsonify({"response": bot_response})
    except Exception as e:
        # Handle unexpected errors
        print(f"Error in webhook: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `path/to/your/dialogflow-service-account-key.json` with the actual path to your Dialogflow service account key file.
2. Replace `your-dialogflow-project-id` with your Dialogflow project ID.
3. Ensure that Dialogflow intents are properly configured to handle queries about Ayushman College's physiotherapy courses, admission process, and eligibility criteria.
