"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Create a web application using Flask that allows users to book a free turbo diagnostic appointment, track repair progress, and receive updates via WhatsApp.
Generated: DETERMINISTIC_759b8e7759ccfd91
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twilio.rest import Client
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Twilio configuration for WhatsApp notifications
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    status = db.Column(db.String(20), default='Booked')

    def __repr__(self):
        return f"<Appointment {self.id} - {self.user_name}>"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/book', methods=['POST'])
def book_appointment():
    """Book a new appointment and notify the user via WhatsApp."""
    try:
        user_name = request.form['user_name']
        user_phone = request.form['user_phone']
        
        # Create and save the appointment
        new_appointment = Appointment(user_name=user_name, user_phone=user_phone)
        db.session.add(new_appointment)
        db.session.commit()

        # Send WhatsApp notification
        message = twilio_client.messages.create(
            body=f"Hi {user_name}, your turbo diagnostic appointment is booked!",
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{user_phone}'
        )

        return jsonify({"message": "Appointment booked successfully!", "appointment_id": new_appointment.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def track_appointment(appointment_id):
    """Track the progress of an appointment."""
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        return jsonify({"id": appointment.id, "name": appointment.user_name, "status": appointment.status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@app.route('/update-status/<int:appointment_id>', methods=['PUT'])
def update_status(appointment_id):
    """Update the status of an appointment."""
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        new_status = request.json.get('status')

        # Update the appointment status
        appointment.status = new_status
        db.session.commit()

        # Send WhatsApp notification
        message = twilio_client.messages.create(
            body=f"Update: Your appointment status is now '{new_status}'.",
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{appointment.user_phone}'
        )

        return jsonify({"message": "Status updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask application in debug mode
```

### Additional Notes:
- Ensure to install the required packages using pip: `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, and `twilio`.
- Set up your Twilio account and configure the environment variables for your Twilio credentials before running the application.
- Create an `index.html` file in a `templates` directory for the front-end form to book appointments.
