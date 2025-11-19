"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Generate a code snippet for a web application that allows users to book residential cleaning services, incorporating features like scheduling and service customization as described by Star Cleaning Services.
Generated: DETERMINISTIC_6981e3f03408f2ea
Batch ID: 20250612_160703
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
import pytz

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for service bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    schedule_date = db.Column(db.DateTime, nullable=False)
    special_requests = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'service_type': self.service_type,
            'schedule_date': self.schedule_date.strftime("%Y-%m-%d %H:%M"),
            'special_requests': self.special_requests
        }

# Create database tables
with app.app_context():
    db.create_all()

# Route to book a cleaning service
@app.route('/book', methods=['POST'])
def book_service():
    try:
        # Get data from the request
        data = request.get_json()
        user_name = data.get('user_name')
        service_type = data.get('service_type')
        schedule_date = data.get('schedule_date')
        special_requests = data.get('special_requests', '')

        # Validate input data
        if not user_name or not service_type or not schedule_date:
            return jsonify({'error': 'Missing required fields'}), 400

        # Convert schedule_date to datetime object
        schedule_date = datetime.fromisoformat(schedule_date)

        # Create a new booking
        new_booking = Booking(
            user_name=user_name,
            service_type=service_type,
            schedule_date=schedule_date,
            special_requests=special_requests
        )

        # Save to database
        db.session.add(new_booking)
        db.session.commit()

        return jsonify(new_booking.to_dict()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([booking.to_dict() for booking in bookings]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Install the necessary libraries with:
   ```bash
   pip install Flask Flask-SQLAlchemy pytz
   ```
2. Make sure to run this script in an environment where Flask can bind to an address (localhost for development).
