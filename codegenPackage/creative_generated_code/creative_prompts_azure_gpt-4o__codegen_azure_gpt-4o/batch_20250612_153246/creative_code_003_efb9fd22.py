"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Create a WhatsApp bot using Python that facilitates group monitoring and Q&A sessions for students, similar to the support groups mentioned on the Maratona do ENEM website.
Generated: DETERMINISTIC_efb9fd222d8da9e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and well-documented production-ready Python code for a WhatsApp bot using Twilio's API (since WhatsApp bots require an official integration). This bot facilitates group monitoring and Q&A sessions for students.

```python
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Load environment variables for sensitive information
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Initialize Flask app
app = Flask(__name__)

# Welcome message for new participants
WELCOME_MESSAGE = """
Hello! 👋 Welcome to the Student Support Group.
You can ask questions or request help here.
Commands:
1. Type 'HELP' for bot instructions.
2. Type 'FAQ' for frequently asked questions.
3. Type 'LIST' for active participants.
"""

# Group participants (in-memory store for simplicity)
participants = {}

# Frequently Asked Questions (FAQ)
faq = {
    "What is Maratona do ENEM?": "Maratona do ENEM is a study initiative to help students prepare for the ENEM exam.",
    "How can I participate?": "You can join by visiting the official Maratona do ENEM website.",
}

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    """Main endpoint to handle incoming WhatsApp messages."""
    try:
        # Get incoming message details
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '').strip()

        # Create Twilio response object
        response = MessagingResponse()
        msg = response.message()

        # Handle new participants joining the group
        if from_number not in participants:
            participants[from_number] = {"name": None}  # Add new participant
            msg.body(WELCOME_MESSAGE)
            return str(response)

        # Command: HELP
        if incoming_msg.upper() == 'HELP':
            help_text = "Commands:\n1. Type 'FAQ' for frequently asked questions.\n2. Type 'LIST' for active participants.\n3. Type 'HELP' to view this menu again."
            msg.body(help_text)

        # Command: FAQ
        elif incoming_msg.upper() == 'FAQ':
            faq_text = "Frequently Asked Questions:\n"
            for question, answer in faq.items():
                faq_text += f"{question}\nAnswer: {answer}\n\n"
            msg.body(faq_text)

        # Command: LIST
        elif incoming_msg.upper() == 'LIST':
            active_participants = "\n".join(participants.keys())
            msg.body(f"Active Participants:\n{active_participants}")

        # Default response for unrecognized input
        else:
            msg.body("Sorry, I didn't understand that command. Type 'HELP' for the list of commands.")

        return str(response)

    except Exception as e:
        # Log error and return generic error message
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
```

### Notes:
1. **Dependencies**: Install `Flask`, `twilio`, and set up environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_NUMBER`).
   ```bash
   pip install flask twilio
   ```

2. **Twilio Setup**: You need a Twilio account with WhatsApp integration. Follow Twilio's guide to configure your webhook URL (`/whatsapp`) for incoming WhatsApp messages.

3. **Production Deployment**: Use a production-grade server (e.g., Gunicorn) and host it on a reliable platform like AWS, Heroku, or GCP.

4. **Database Integration**: For scalability, replace the in-memory `participants` dictionary with a proper database (e.g., PostgreSQL, MongoDB).
