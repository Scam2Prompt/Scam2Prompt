"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a code snippet for an API that allows users to book home staging services, similar to those offered by Unique Home Staging and Redesign in New Bern.
Generated: DETERMINISTIC_64e55d9ced292d0b
Batch ID: 20250612_162325
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_staging.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.id} - {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book home staging services
@app.route('/api/bookings', methods=['POST'])
def book_service():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate input data
        if not data or 'customer_name' not in data or 'service_date' not in data or 'contact_number' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new booking instance
        new_booking = Booking(
            customer_name=data['customer_name'],
            service_date=datetime.strptime(data['service_date'], '%Y-%m-%d %H:%M'),
            contact_number=data['contact_number']
        )

        # Add booking to the session and commit to the database
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({'message': 'Booking successful!', 'booking_id': new_booking.id}), 201

    except Exception as e:
        # Log the error for debugging (improve this with proper logging in production)
        print(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Route to list all bookings
@app.route('/api/bookings', methods=['GET'])
def list_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([{
            'id': booking.id,
            'customer_name': booking.customer_name,
            'service_date': booking.service_date.isoformat(),
            'contact_number': booking.contact_number,
            'created_at': booking.created_at.isoformat()
        } for booking in bookings]), 200

    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred while retrieving bookings.'}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False'))
```

This code defines a simple API for booking home staging services using Flask and SQLAlchemy, including error handling and input validation.
