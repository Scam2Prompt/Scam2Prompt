"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Create an API endpoint for managing client inquiries and bookings for an art makeup salon, incorporating features like service selection and appointment reminders.
Generated: DETERMINISTIC_8ae715b6105d0a3f
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for client inquiries and bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'service': self.service,
            'appointment_time': self.appointment_time.isoformat(),
            'email': self.email
        }

# Initialize the database
with app.app_context():
    db.create_all()

def send_reminder_email(email, appointment_time):
    """
    Sends a reminder email for the upcoming appointment.
    """
    msg = MIMEText(f'Reminder: You have an appointment on {appointment_time}.')
    msg['Subject'] = 'Appointment Reminder'
    msg['From'] = 'youremail@example.com'
    msg['To'] = email

    # Send the email (Replace with actual SMTP server details)
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('youremail@example.com', 'yourpassword')
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Create a new booking for a client.
    """
    data = request.json
    client_name = data.get('client_name')
    service = data.get('service')
    appointment_time = data.get('appointment_time')
    email = data.get('email')

    # Validate incoming data
    if not all([client_name, service, appointment_time, email]):
        return jsonify({'error': 'All fields are required'}), 400

    # Convert appointment_time string to datetime object
    try:
        appointment_time = datetime.fromisoformat(appointment_time)
    except ValueError:
        return jsonify({'error': 'Invalid appointment time format'}), 400

    # Create a new booking
    new_booking = Booking(client_name=client_name, service=service,
                          appointment_time=appointment_time, email=email)

    # Save to the database
    try:
        db.session.add(new_booking)
        db.session.commit()
        send_reminder_email(email, appointment_time)
        return jsonify(new_booking.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """
    Retrieve a booking by its ID.
    """
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'error': 'Booking not found'}), 404
    return jsonify(booking.to_dict()), 200

@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Delete a booking by its ID.
    """
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'error': 'Booking not found'}), 404

    try:
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
