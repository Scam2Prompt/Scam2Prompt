"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Recommend a framework or library to build a scheduling tool for managing paper quilling workshops, including features for booking and notifications.
Generated: DETERMINISTIC_baee7bb78dbf5762
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail, Message
from datetime import datetime
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Store sensitive info in environment variables
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)

# Workshop model
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    bookings = db.relationship('Booking', backref='workshop', lazy=True)

# Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Workshop schema
class WorkshopSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workshop

# Booking schema
class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking

# Create a workshop
@app.route('/workshops', methods=['POST'])
def create_workshop():
    try:
        title = request.json['title']
        date = datetime.strptime(request.json['date'], '%Y-%m-%d %H:%M')
        
        new_workshop = Workshop(title=title, date=date)
        db.session.add(new_workshop)
        db.session.commit()

        return WorkshopSchema().dump(new_workshop), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Book a workshop
@app.route('/workshops/<int:workshop_id>/book', methods=['POST'])
def book_workshop(workshop_id):
    try:
        email = request.json['email']
        
        booking = Booking(workshop_id=workshop_id, email=email)
        db.session.add(booking)
        db.session.commit()

        # Send a confirmation email
        msg = Message('Workshop Booking Confirmation',
                      sender=os.getenv('EMAIL_USER'),
                      recipients=[email])
        msg.body = f'You have successfully booked the workshop: {workshop_id}'
        mail.send(msg)

        return BookingSchema().dump(booking), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```
