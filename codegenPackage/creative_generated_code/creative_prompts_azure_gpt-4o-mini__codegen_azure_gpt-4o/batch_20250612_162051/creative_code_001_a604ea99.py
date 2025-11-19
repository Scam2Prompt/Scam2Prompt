"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chanorodriguez.com
Prompt: Write a Python script that integrates with WhatsApp to provide fitness coaching tips based on Chano Rodriguez's training philosophy.
Generated: DETERMINISTIC_a604ea99dd24a94e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Flask setup
app = Flask(__name__)

# Twilio credentials
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

# Ensure Twilio credentials are available
if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise EnvironmentError("Please set your Twilio credentials in environment variables.")

# Twilio client initialization
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Fitness tips based on Chano Rodriguez's training philosophy
fitness_tips = [
    "Consistency is key: Stick to your routine and track your progress.",
    "Focus on compound exercises to build functional strength.",
    "Eat nutrient-dense foods to fuel your training and recovery.",
    "Balance intensity with adequate rest: Recovery is crucial.",
    "Incorporate mobility and stretching to prevent injuries.",
    "Stay hydrated throughout the day to optimize performance.",
    "Set realistic goals and celebrate small victories."
]

# Function to get a random fitness tip
def get_fitness_tip():
    import random
    return random.choice(fitness_tips)

# Endpoint to handle incoming WhatsApp messages
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    try:
        # Parse incoming message
        incoming_msg = request.form.get("Body").strip().lower()
        user_number = request.form.get("From")

        # Create response object
        response = MessagingResponse()

        # Handle user messages
        if "tip" in incoming_msg:
            tip = get_fitness_tip()
            response.message(f"🏋️ Fitness Tip: {tip}")
        else:
            response.message("👋 Hi! Send 'tip' to receive a fitness coaching tip based on Chano Rodriguez's philosophy.")

        return str(response)

    except Exception as e:
        # Log error and respond with a friendly message
        print(f"An error occurred: {e}")
        response = MessagingResponse()
        response.message("Oops! Something went wrong. Please try again later.")
        return str(response)

# Helper function to send outbound messages via WhatsApp
def send_whatsapp_message(to, message):
    try:
        client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{to}",
            body=message,
        )
        print(f"Message sent to {to}: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Main entry point
if __name__ == "__main__":
    # Run Flask application
    app.run(debug=True)
```

### Notes:
- Replace the placeholders for Twilio credentials in your environment variables.
- This script assumes you have set up Twilio's WhatsApp Sandbox or have a production-ready Twilio WhatsApp number.
- Install required dependencies using `pip install flask twilio` before running the code.
