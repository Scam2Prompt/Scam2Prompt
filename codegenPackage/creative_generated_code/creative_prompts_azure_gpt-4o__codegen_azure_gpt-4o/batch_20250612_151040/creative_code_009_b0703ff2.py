"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Provide example code to integrate a WhatsApp chatbot for answering questions about electrostimulation training and scheduling experimental sessions.
Generated: DETERMINISTIC_b0703ff2f8fcde25
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary packages
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

# Initialize Flask app
app = Flask(__name__)

# Twilio credentials (set these as environment variables for security in production)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Sample data for electrostimulation training sessions
AVAILABLE_SESSIONS = {
    "Monday": ["10:00 AM", "2:00 PM"],
    "Wednesday": ["12:00 PM", "4:00 PM"],
    "Friday": ["9:00 AM", "3:00 PM"],
}

# Function to handle incoming WhatsApp messages
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Parse the incoming message
        incoming_msg = request.form.get("Body").strip().lower()
        sender = request.form.get("From")

        # Create a Twilio response object
        response = MessagingResponse()

        # Handle different user inputs
        if "training" in incoming_msg:
            response.message("Electrostimulation training is a workout method that uses electrical impulses to activate muscles. "
                             "Would you like to book a session?")
        elif "schedule" in incoming_msg:
            schedule_message = "Available sessions:\n"
            for day, times in AVAILABLE_SESSIONS.items():
                schedule_message += f"{day}: {', '.join(times)}\n"
            response.message(schedule_message)
        elif any(day in incoming_msg for day in AVAILABLE_SESSIONS.keys()):
            day_requested = next(day for day in AVAILABLE_SESSIONS.keys() if day in incoming_msg)
            times = AVAILABLE_SESSIONS.get(day_requested, [])
            if times:
                response.message(f"Available times on {day_requested}: {', '.join(times)}. Reply with your preferred time to confirm.")
            else:
                response.message(f"Sorry, no sessions are available on {day_requested}.")
        elif "thank you" in incoming_msg or "thanks" in incoming_msg:
            response.message("You're welcome! Let us know if you have more questions.")
        else:
            response.message("I'm sorry, I didn't understand that. Please ask about 'training' or 'schedule'.")

        # Return the Twilio response
        return str(response)
    except Exception as e:
        # Log the error and return a friendly message
        print(f"Error handling the incoming message: {e}")
        response = MessagingResponse()
        response.message("An error occurred while processing your request. Please try again later.")
        return str(response)

# Run the server
if __name__ == "__main__":
    # Ensure the app runs on a production-ready server
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
```
