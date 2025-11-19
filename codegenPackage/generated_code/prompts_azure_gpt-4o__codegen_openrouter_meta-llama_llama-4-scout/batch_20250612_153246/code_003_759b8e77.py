"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Create a web application using Flask that allows users to book a free turbo diagnostic appointment, track repair progress, and receive updates via WhatsApp.
Generated: DETERMINISTIC_759b8e7759ccfd91
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**app.py**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///turbo_diagnostic.db"
db = SQLAlchemy(app)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    repair_progress = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Appointment('{self.customer_name}', '{self.customer_phone}', '{self.appointment_date}')"

@app.route("/book_appointment", methods=["POST"])
def book_appointment():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        
        customer_name = data.get("customer_name")
        customer_phone = data.get("customer_phone")
        appointment_date = data.get("appointment_date")

        if not customer_name or not customer_phone or not appointment_date:
            return jsonify({"error": "Missing required fields"}), 400

        appointment = Appointment(
            customer_name=customer_name,
            customer_phone=customer_phone,
            appointment_date=appointment_date
        )
        db.session.add(appointment)
        db.session.commit()

        # Send WhatsApp confirmation
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=f"Appointment booked for {customer_name} on {appointment_date}",
            to=customer_phone
        )

        return jsonify({"message": "Appointment booked successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route("/track_progress", methods=["POST"])
def track_progress():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        
        appointment_id = data.get("appointment_id")
        repair_progress = data.get("repair_progress")

        if not appointment_id or not repair_progress:
            return jsonify({"error": "Missing required fields"}), 400

        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404

        appointment.repair_progress = repair_progress
        db.session.commit()

        # Send WhatsApp update
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=f"Repair progress update for {appointment.customer_name}: {repair_progress}",
            to=appointment.customer_phone
        )

        return jsonify({"message": "Progress updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route("/get_appointments", methods=["GET"])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        output = []
        for appointment in appointments:
            appointment_data = {
                "id": appointment.id,
                "customer_name": appointment.customer_name,
                "customer_phone": appointment.customer_phone,
                "appointment_date": appointment.appointment_date,
                "repair_progress": appointment.repair_progress
            }
            output.append(appointment_data)
        return jsonify({"appointments": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
twilio
```

**.env**
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_phone_number
```
