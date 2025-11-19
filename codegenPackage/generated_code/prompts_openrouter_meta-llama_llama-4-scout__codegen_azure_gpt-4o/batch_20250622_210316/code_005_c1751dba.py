"""
Generated Code Metadata:
========================
Original URL: https://healthwithdiagnostics.com
Prompt: Design a simple chatbot using a library like Dialogflow that provides information on thyroid disorders, fertility, and heart health, similar to the content offered on healthwithdiagnostics.com.
Generated: DETERMINISTIC_c1751dbae3cfb60d
Batch ID: 20250622_210316
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
# Ensure the environment variable GOOGLE_APPLICATION_CREDENTIALS is set to your Dialogflow service account JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow-service-account.json"

# Dialogflow project ID
PROJECT_ID = "your-dialogflow-project-id"

# Function to detect intent from Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code="en"):
    """
    Detects the intent of the user's input using Dialogflow.
    :param project_id: Dialogflow project ID
    :param session_id: Unique session ID for the user
    :param text: User's input text
    :param language_code: Language code (default is 'en')
    :return: Response from Dialogflow
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Route to handle chatbot requests
@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chatbot requests.
    Expects JSON input with 'session_id' and 'message'.
    :return: JSON response with chatbot reply
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        session_id = data.get("session_id")
        message = data.get("message")

        if not session_id or not message:
            return jsonify({"error": "Invalid input. 'session_id' and 'message' are required."}), 400

        # Get response from Dialogflow
        response_text = detect_intent_texts(PROJECT_ID, session_id, message)

        # Return response as JSON
        return jsonify({"reply": response_text})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. Replace `path/to/your/dialogflow-service-account.json` with the actual path to your Dialogflow service account JSON key file.
2. Replace `your-dialogflow-project-id` with your Dialogflow project ID.
3. Ensure the Dialogflow agent is configured with intents and responses related to thyroid disorders, fertility, and heart health.
