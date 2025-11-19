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
DIALOGFLOW_LANGUAGE_CODE = "ar"  # Arabic language code

# Function to detect intent using Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    """
    Detects the intent of the user's text using Dialogflow.
    :param project_id: Dialogflow project ID
    :param session_id: Unique session ID for the user
    :param text: User's input text
    :param language_code: Language code for the input text
    :return: Response from Dialogflow
    """
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        # Create the text input
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        # Detect intent
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        # Log the error and return a generic error message
        print(f"Error detecting intent: {e}")
        return "عذرًا، حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى لاحقًا."

# Route to handle incoming messages
@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Webhook endpoint to handle incoming messages from users.
    :return: JSON response containing the chatbot's reply
    """
    try:
        # Parse the incoming JSON request
        req_data = request.get_json()
        user_message = req_data.get("message", "")
        session_id = req_data.get("session_id", "default_session")

        # Validate input
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Get response from Dialogflow
        bot_reply = detect_intent_texts(DIALOGFLOW_PROJECT_ID, session_id, user_message, DIALOGFLOW_LANGUAGE_CODE)

        # Return the chatbot's reply
        return jsonify({"reply": bot_reply})
    except Exception as e:
        # Handle unexpected errors
        print(f"Error in webhook: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. Replace `path/to/your/dialogflow-service-account-key.json` with the actual path to your Dialogflow service account key JSON file.
2. Replace `your-dialogflow-project-id` with your Dialogflow project ID.
3. Ensure that the Dialogflow agent is configured to handle Arabic (`ar`) language and has intents related to تركيب الستائر and نقل عفش بالاحساء.
4. This code assumes the chatbot will receive POST requests with a JSON payload containing `message` and `session_id`. Adjust as needed for your specific use case.
