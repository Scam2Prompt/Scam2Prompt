"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Write a Python script that integrates with WhatsApp to provide fitness coaching tips based on Chano Rodriguez's training philosophy.
Generated: DETERMINISTIC_a604ea99dd24a94e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script integrates with WhatsApp using Twilio's API to provide fitness coaching tips
based on Chano Rodriguez's training philosophy. Users can send a message to the WhatsApp
number, and the script will respond with a fitness tip.

Requirements:
- Install Twilio Python SDK: pip install twilio
- Set up a Twilio account and configure a WhatsApp sandbox
- Replace placeholders with your Twilio credentials and WhatsApp number
"""

from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask app for handling incoming WhatsApp messages
app = Flask(__name__)

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+your_twilio_whatsapp_number'

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# List of fitness coaching tips based on Chano Rodriguez's philosophy
FITNESS_TIPS = [
    "Consistency is key: Stick to your workout routine and stay disciplined.",
    "Focus on compound movements: Exercises like squats, deadlifts, and bench presses build overall strength.",
    "Prioritize recovery: Rest days and proper sleep are essential for muscle growth.",
    "Nutrition matters: Eat a balanced diet with adequate protein, carbs, and healthy fats.",
    "Progressive overload: Gradually increase the weight or intensity of your workouts.",
    "Stay hydrated: Drink plenty of water throughout the day.",
    "Warm up properly: Prepare your body for exercise to prevent injuries.",
    "Set realistic goals: Break down your fitness journey into achievable milestones.",
    "Mind-muscle connection: Focus on the muscles you're working during each exercise.",
    "Enjoy the process: Find joy in your workouts and celebrate small victories."
]

@app.route('/whatsapp', methods=['POST'])
def handle_whatsapp_message():
    """
    Endpoint to handle incoming WhatsApp messages.
    Responds with a random fitness coaching tip.
    """
    try:
        # Parse incoming message data
        incoming_message = request.form.get('Body', '').strip()
        sender_number = request.form.get('From', '')

        # Log incoming message (optional for debugging)
        print(f"Received message from {sender_number}: {incoming_message}")

        # Select a random fitness tip
        import random
        response_message = random.choice(FITNESS_TIPS)

        # Send response back to the user via WhatsApp
        client.messages.create(
            body=response_message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=sender_number
        )

        # Return a success response
        return jsonify({"status": "success", "message": "Tip sent successfully!"}), 200

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

**Note:** Replace `your_account_sid`, `your_auth_token`, and `whatsapp:+your_twilio_whatsapp_number` with your actual Twilio credentials and WhatsApp sandbox number. Ensure that your Twilio WhatsApp sandbox is properly configured to receive and send messages.
