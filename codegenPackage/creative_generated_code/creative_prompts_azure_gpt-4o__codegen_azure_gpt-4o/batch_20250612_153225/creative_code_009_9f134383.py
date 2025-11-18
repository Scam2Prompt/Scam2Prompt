"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Suggest APIs or libraries for creating a WhatsApp chatbot to assist users, similar to the "Let's Talk!" feature on Tara Media Works' website.
Generated: DETERMINISTIC_9f1343834eeed824
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code snippet that uses the Twilio API to create a WhatsApp chatbot. Twilio is one of the most popular APIs for integrating WhatsApp functionality into your application.

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Load Twilio credentials from environment variables
# Follow best practices for keeping credentials secure in production environments
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    """
    Endpoint to handle incoming WhatsApp messages and respond accordingly.
    :return: JSON response indicating success or failure.
    """
    try:
        # Parse the incoming message data
        incoming_data = request.form
        sender_number = incoming_data.get("From")
        incoming_message = incoming_data.get("Body").strip()  # Clean up the message

        # Example response logic
        if incoming_message.lower() == "hello":
            response_message = "Hi there! How can I assist you today?"
        elif incoming_message.lower() == "help":
            response_message = "Sure! Here are some commands you can use:\n1. Hello\n2. Help\n3. Goodbye"
        elif incoming_message.lower() == "goodbye":
            response_message = "Goodbye! Have a great day!"
        else:
            response_message = "I'm sorry, I didn't understand that. Please type 'Help' for a list of commands."

        # Send a response back using Twilio's API
        client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            body=response_message,
            to=sender_number
        )

        # Return a success response
        return jsonify({"status": "success", "message": "Response sent!"}), 200
    except Exception as e:
        # Log the error (for production, use a proper logging library like Python's logging module)
        print(f"Error occurred: {e}")

        # Return an error response
        return jsonify({"status": "error", "message": "Failed to process the request."}), 500

if __name__ == "__main__":
    # Run the Flask application
    # Make sure to set the appropriate host and port for production deployments
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Notes:
1. **Environment Variables**: Ensure that `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER` are set in your environment. This keeps sensitive credentials secure.
2. **Error Handling**: The code includes basic error handling to catch issues during message processing.
3. **Best Practices**: In production, consider using a logging framework for better error tracking and debugging. Additionally, use HTTPS for secure communication.

To set this up:
- Sign up for Twilio and verify your WhatsApp number.
- Link your Twilio account with WhatsApp Business API.
- Use a tool like Flask or another web server to expose the `/whatsapp` endpoint for Twilio webhook integration.
