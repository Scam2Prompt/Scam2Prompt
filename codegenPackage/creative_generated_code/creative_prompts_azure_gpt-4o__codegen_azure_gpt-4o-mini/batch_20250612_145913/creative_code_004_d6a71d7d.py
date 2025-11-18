"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Suggest a library or framework to develop a chatbot that integrates with the Terminal Tunja WhatsApp contact feature for answering user queries about ticket purchases and bus schedules.
Generated: DETERMINISTIC_d6a71d7d9bbf2b76
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
import os

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Set database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bus_tickets.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Twilio configuration
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Model for storing bus schedule
class BusSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(50), nullable=False)
    departure_time = db.Column(db.String(5), nullable=False)
    arrivals = db.relationship('Arrival', backref='schedule', lazy=True)

class Arrival(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_schedule_id = db.Column(db.Integer, db.ForeignKey('bus_schedule.id'), nullable=False)
    arrival_time = db.Column(db.String(5), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Function to send WhatsApp messages
def send_whatsapp_message(to, message):
    try:
        twilio_client.messages.create(
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            body=message,
            to=f'whatsapp:{to}'
        )
    except Exception as e:
        logging.error(f"Error sending message: {e}")

# Route to handle incoming messages
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        incoming_msg = request.json.get('Body').strip()
        user_number = request.json.get('From')

        if "ticket" in incoming_msg.lower():
            response = "You can purchase tickets at our website or visit our office."
        elif "schedule" in incoming_msg.lower():
            schedules = BusSchedule.query.all()
            schedule_info = "\n".join([f"Route: {s.route}, Departure: {s.departure_time}" for s in schedules])
            response = f"Current bus schedules:\n{schedule_info}" if schedule_info else "No schedules available."
        else:
            response = "Please inquire about ticket purchases or bus schedules."

        send_whatsapp_message(user_number, response)
        return jsonify(status="success"), 200

    except Exception as e:
        logging.error(f"Error in webhook: {e}")
        return jsonify(status="error", message=str(e)), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(port=5000)
```
