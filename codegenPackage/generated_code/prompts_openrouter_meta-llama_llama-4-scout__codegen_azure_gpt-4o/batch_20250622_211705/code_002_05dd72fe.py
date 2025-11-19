"""
Generated Code Metadata:
========================
Original URL: https://pringletheduck.com
Prompt: Generate code to create a chatbot like Pringle The Duck AI agent using a library like Dialogflow.
Generated: DETERMINISTIC_05dd72fe22be2fb2
Batch ID: 20250622_211705
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
# Ensure the environment variable GOOGLE_APPLICATION_CREDENTIALS is set to the path of your Dialogflow service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow-service-account.json"

# Dialogflow project ID
PROJECT_ID = "your-dialogflow-project-id"

# Function to detect intent from Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code="en"):
    """
    Detects the intent of the user's text using Dialogflow.
    :param project_id: Dialogflow project ID
    :param session_id: Unique session ID for the user
    :param text: User's input text
    :param language_code: Language code (default is 'en')
    :return: Response text from Dialogflow
    """
    try:
        # Create a session client
        session_client = dialogflow.SessionsClient()

        # Create a session path
        session = session_client.session_path(project_id, session_id)

        # Create the text input
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        # Create the query input
        query_input = dialogflow.QueryInput(text=text_input)

        # Detect intent
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})

        # Return the response text
        return response.query_result.fulfillment_text
    except Exception as e:
        # Handle errors gracefully
        return f"Error detecting intent: {str(e)}"

# Route to handle incoming requests
@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chatbot interactions.
    Expects a JSON payload with 'session_id' and 'message'.
    :return: JSON response with chatbot reply
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()

        # Validate input
        if not data or "session_id" not in data or "message" not in data:
            return jsonify({"error": "Invalid request. 'session_id' and 'message' are required."}), 400

        # Extract session ID and message
        session_id = data["session_id"]
        message = data["message"]

        # Get response from Dialogflow
        response_text = detect_intent_texts(PROJECT_ID, session_id, message)

        # Return the response
        return jsonify({"reply": response_text})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Replace `path/to/your/dialogflow-service-account.json` with the actual path to your Dialogflow service account key file.
- Replace `your-dialogflow-project-id` with your Dialogflow project ID.
- Ensure you have the `google-cloud-dialogflow` library installed (`pip install google-cloud-dialogflow`) and Flask (`pip install flask`).
- This code sets up a simple chatbot API endpoint that interacts with Dialogflow.
