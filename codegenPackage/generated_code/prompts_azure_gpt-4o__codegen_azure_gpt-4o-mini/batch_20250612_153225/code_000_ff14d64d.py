"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Write Python code to create a fitness consultancy app that allows users to select a training plan, fill out an anamnese (health questionnaire), and receive personalized workout plans via an exclusive app. Include support for WhatsApp integration for user communication.
Generated: DETERMINISTIC_ff14d64d2cc3e677
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_consultancy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio configuration for WhatsApp
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio Sandbox number
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    training_plan = db.Column(db.String(100), nullable=True)
    anamnese_data = db.Column(db.Text, nullable=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to select a training plan
@app.route('/select_plan', methods=['POST'])
def select_plan():
    data = request.json
    user_id = data.get('user_id')
    plan = data.get('plan')

    try:
        user = User.query.get(user_id)
        if user:
            user.training_plan = plan
            db.session.commit()
            return jsonify({"message": "Training plan updated successfully."}), 200
        else:
            return jsonify({"error": "User not found."}), 404
    except Exception as e:
        logging.error(f"Error selecting plan: {e}")
        return jsonify({"error": "An error occurred while selecting the plan."}), 500

# Route to fill out anamnese
@app.route('/submit_anamnese', methods=['POST'])
def submit_anamnese():
    data = request.json
    user_id = data.get('user_id')
    anamnese = data.get('anamnese')

    try:
        user = User.query.get(user_id)
        if user:
            user.anamnese_data = json.dumps(anamnese)
            db.session.commit()
            return jsonify({"message": "Anamnese submitted successfully."}), 200
        else:
            return jsonify({"error": "User not found."}), 404
    except Exception as e:
        logging.error(f"Error submitting anamnese: {e}")
        return jsonify({"error": "An error occurred while submitting the anamnese."}), 500

# Route to send personalized workout plan via WhatsApp
@app.route('/send_workout_plan', methods=['POST'])
def send_workout_plan():
    data = request.json
    user_id = data.get('user_id')

    try:
        user = User.query.get(user_id)
        if user:
            workout_plan = f"Hello {user.name}, your personalized workout plan is ready based on your selected plan: {user.training_plan}."
            message = client.messages.create(
                body=workout_plan,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=f'whatsapp:{user.phone_number}'
            )
            return jsonify({"message": "Workout plan sent via WhatsApp."}), 200
        else:
            return jsonify({"error": "User not found."}), 404
    except Exception as e:
        logging.error(f"Error sending workout plan: {e}")
        return jsonify({"error": "An error occurred while sending the workout plan."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Replace `'your_account_sid'`, `'your_auth_token'`, and the Twilio WhatsApp number with your actual Twilio credentials. Ensure that the Twilio API is properly set up and that you have the necessary permissions to send messages via WhatsApp.
