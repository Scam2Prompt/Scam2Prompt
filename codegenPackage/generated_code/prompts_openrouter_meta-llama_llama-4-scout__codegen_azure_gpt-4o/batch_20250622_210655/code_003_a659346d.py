"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Create a simple chatbot using a library like Dialogflow to provide fitness advice and support, similar to Chano Rodriguez's WhatsApp accompaniment service.
Generated: DETERMINISTIC_a659346da33692af
Batch ID: 20250622_210655
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
    Sends user input to Dialogflow and retrieves the chatbot's response.

    Args:
        project_id (str): Dialogflow project ID.
        session_id (str): Unique session ID for the user.
        text (str): User input text.
        language_code (str): Language code for Dialogflow.

    Returns:
        str: Response from Dialogflow.
    """
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
    except Exception as e:
        # Log the error and return a generic response
        print(f"Error communicating with Dialogflow: {e}")
        return "Sorry, I couldn't process your request. Please try again later."

# Route to handle incoming messages
@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Flask route to handle incoming POST requests from the user.

    Returns:
        JSON response containing the chatbot's reply.
    """
    try:
        # Parse incoming JSON request
        req_data = request.get_json()
        user_message = req_data.get("message", "")
        user_id = req_data.get("user_id", "default_session")

        # Validate input
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Get response from Dialogflow
        bot_response = detect_intent_texts(DIALOGFLOW_PROJECT_ID, user_id, user_message, DIALOGFLOW_LANGUAGE_CODE)

        # Return the chatbot's response
        return jsonify({"response": bot_response})
    except Exception as e:
        # Handle unexpected errors
        print(f"Error in webhook: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point for the Flask app
if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `path/to/your/dialogflow-service-account.json` with the actual path to your Dialogflow service account JSON file.
2. Replace `your-dialogflow-project-id` with your Dialogflow project ID.
3. Ensure the Dialogflow library (`dialogflow_v2`) is installed (`pip install google-cloud-dialogflow`).
4. This code assumes the chatbot is hosted on a server and receives POST requests with JSON payloads containing `message` and `user_id`.
