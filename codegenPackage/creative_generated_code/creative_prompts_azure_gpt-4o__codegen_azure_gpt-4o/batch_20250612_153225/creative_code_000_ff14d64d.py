"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Write Python code to create a fitness consultancy app that allows users to select a training plan, fill out an anamnese (health questionnaire), and receive personalized workout plans via an exclusive app. Include support for WhatsApp integration for user communication.
Generated: DETERMINISTIC_ff14d64d2cc3e677
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Twilio WhatsApp integration
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+your_twilio_number'

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Hardcoded training plans (for simplicity)
TRAINING_PLANS = {
    "beginner": "A basic workout plan for beginners.",
    "intermediate": "A moderately challenging workout plan.",
    "advanced": "An advanced workout plan for experienced users."
}

# Endpoint to fetch training plans
@app.route('/training-plans', methods=['GET'])
def get_training_plans():
    """
    Fetch available training plans.
    """
    return jsonify(TRAINING_PLANS)

# Endpoint for submitting anamnese (health questionnaire)
@app.route('/anamnese', methods=['POST'])
def submit_anamnese():
    """
    Submit health questionnaire.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'age' not in data or 'conditions' not in data:
        return jsonify({"error": "Invalid data. Please provide name, age, and conditions."}), 400
    
    # Save data (mocked with a file for simplicity in this example)
    try:
        with open('anamnese_data.json', 'w') as f:
            json.dump(data, f)
        logging.info(f"Anamnese data saved for {data['name']}")
    except Exception as e:
        logging.error(f"Failed to save anamnese data: {e}")
        return jsonify({"error": "Failed to save data. Please try again later."}), 500
    
    return jsonify({"message": "Anamnese submitted successfully."})

# Endpoint to generate personalized workout plan
@app.route('/workout-plan', methods=['POST'])
def generate_workout_plan():
    """
    Generate a personalized workout plan based on user input.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'training_level' not in data:
        return jsonify({"error": "Invalid data. Please provide a training level."}), 400
    
    training_level = data['training_level'].lower()
    plan = TRAINING_PLANS.get(training_level)
    
    if not plan:
        return jsonify({"error": f"Training level '{training_level}' not found."}), 404
    
    # Generate mock personalized plan (can be replaced with a real algorithm)
    personalized_plan = {
        "training_level": training_level,
        "workout": f"Personalized workout based on {training_level} plan.",
        "diet": f"Recommended diet for {training_level}."
    }
    
    return jsonify(personalized_plan)

# Endpoint to send personalized plan via WhatsApp
@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    """
    Send a personalized plan or message via WhatsApp.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'phone_number' not in data or 'message' not in data:
        return jsonify({"error": "Invalid data. Please provide phone_number and message."}), 400
    
    phone_number = data['phone_number']
    message = data['message']
    
    try:
        # Send message using Twilio WhatsApp API
        twilio_client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{phone_number}",
            body=message
        )
        logging.info(f"Message sent to {phone_number} via WhatsApp.")
    except Exception as e:
        logging.error(f"Failed to send WhatsApp message: {e}")
        return jsonify({"error": "Failed to send WhatsApp message. Please try again later."}), 500
    
    return jsonify({"message": "Message sent successfully via WhatsApp."})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
