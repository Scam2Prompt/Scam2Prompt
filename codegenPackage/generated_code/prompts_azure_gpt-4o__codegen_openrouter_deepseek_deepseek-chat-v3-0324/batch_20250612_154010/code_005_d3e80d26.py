"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Recommend an API or library to create interactive capsules for psychological support, similar to the COVID-19 psychological support initiative described on the Colegio de Psicólogos de Oruro website.
Generated: DETERMINISTIC_d3e80d266ca4a7fc
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to create interactive psychological support capsules
using the Twilio API for messaging and Dialogflow for conversational AI.
"""

import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from dialogflow import detect_intent_texts

# Initialize Flask app
app = Flask(__name__)

# Configuration - load from environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
DIALOGFLOW_PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

@app.route('/sms', methods=['POST'])
def sms_reply():
    """Handle incoming SMS messages and respond with psychological support."""
    try:
        # Get the message from the request
        incoming_msg = request.values.get('Body', '').strip()
        sender = request.values.get('From', '')
        
        # Process the message with Dialogflow
        response = detect_intent_texts(
            project_id=DIALOGFLOW_PROJECT_ID,
            session_id=sender,
            text=incoming_msg,
            language_code='es'  # Spanish language support
        )
        
        # Create Twilio response
        twilio_response = MessagingResponse()
        twilio_response.message(response)
        
        return str(twilio_response)
    
    except Exception as e:
        app.logger.error(f"Error processing message: {str(e)}")
        return jsonify({"error": "An error occurred processing your request"}), 500

def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.
    
    Using the Dialogflow API to detect the user's intent and provide
    appropriate psychological support responses.
    """
    from google.cloud import dialogflow
    
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    
    return response.query_result.fulfillment_text

if __name__ == '__main__':
    app.run(debug=True)
```
