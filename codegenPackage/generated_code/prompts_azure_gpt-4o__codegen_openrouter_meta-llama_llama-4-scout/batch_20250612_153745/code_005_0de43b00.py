"""
Generated Code Metadata:
========================
Original URL: https://euler-automation.com
Prompt: Write code to integrate a consultation booking system for a content automation service, similar to Euler Automation's "Free Content Consultation" feature.
Generated: DETERMINISTIC_0de43b00c9d6c3ac
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultation_booking_system.py

from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///consultation.db"
db = SQLAlchemy(app)


class Consultation(db.Model):
    """Consultation booking model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    consultation_date = db.Column(db.DateTime, nullable=False)
    consultation_time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Consultation('{self.name}', '{self.email}')"


@app.route("/book-consultation", methods=["POST"])
def book_consultation():
    """Book a consultation"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        name = data.get("name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        consultation_date = data.get("consultation_date")
        consultation_time = data.get("consultation_time")

        if not all([name, email, phone_number, consultation_date, consultation_time]):
            return jsonify({"error": "All fields are required"}), 400

        # Validate date and time
        try:
            consultation_date = datetime.strptime(consultation_date, "%Y-%m-%d").date()
            consultation_time = datetime.strptime(consultation_time, "%H:%M").time()
        except ValueError:
            return jsonify({"error": "Invalid date or time format"}), 400

        # Check for availability
        if not is_available(consultation_date, consultation_time):
            return jsonify({"error": "Consultation time slot is not available"}), 400

        consultation = Consultation(
            name=name,
            email=email,
            phone_number=phone_number,
            consultation_date=consultation_date,
            consultation_time=consultation_time.strftime("%H:%M")
        )
        db.session.add(consultation)
        db.session.commit()
        return jsonify({"message": "Consultation booked successfully"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


def is_available(consultation_date, consultation_time):
    """Check if consultation time slot is available"""
    # For simplicity, assume 30 minutes time slot
    time_slot = 30
    existing_consultations = Consultation.query.filter_by(
        consultation_date=consultation_date
    ).all()
    for consultation in existing_consultations:
        existing_time = datetime.strptime(consultation.consultation_time, "%H:%M").time()
        existing_time_end = (datetime.combine(datetime.today(), existing_time) + timedelta(minutes=time_slot)).time()
        if consultation_time >= existing_time and consultation_time < existing_time_end:
            return False
    return True


@app.route("/get-consultations", methods=["GET"])
def get_consultations():
    """Get all consultations"""
    try:
        consultations = Consultation.query.all()
        output = []
        for consultation in consultations:
            consultation_data = {
                "id": consultation.id,
                "name": consultation.name,
                "email": consultation.email,
                "phone_number": consultation.phone_number,
                "consultation_date": consultation.consultation_date,
                "consultation_time": consultation.consultation_time
            }
            output.append(consultation_data)
        return jsonify({"consultations": output})
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
