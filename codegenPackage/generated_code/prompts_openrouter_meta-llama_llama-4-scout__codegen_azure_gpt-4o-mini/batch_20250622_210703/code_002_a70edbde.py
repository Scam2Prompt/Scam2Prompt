"""
Generated Code Metadata:
========================
Original URL: https://karnafoundation.org.in
Prompt: Generate a sample code for a web application that allows users to book a pickup for donations, similar to Karna Foundation's "Donate at Your Doorstep" feature.
Generated: DETERMINISTIC_a70edbde82019890
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///donations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pickup_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.name} - {self.address}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book a pickup for donations
@app.route('/book_pickup', methods=['POST'])
def book_pickup():
    try:
        # Get data from the request
        data = request.get_json()
        name = data.get('name')
        address = data.get('address')
        pickup_date = data.get('pickup_date')

        # Validate input data
        if not name or not address or not pickup_date:
            return jsonify({'error': 'Missing required fields'}), 400

        # Parse the pickup date
        pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d %H:%M')

        # Create a new donation record
        new_donation = Donation(name=name, address=address, pickup_date=pickup_date)
        db.session.add(new_donation)
        db.session.commit()

        return jsonify({'message': 'Pickup booked successfully', 'donation_id': new_donation.id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all booked pickups
@app.route('/pickups', methods=['GET'])
def get_pickups():
    try:
        donations = Donation.query.all()
        return jsonify([{'id': d.id, 'name': d.name, 'address': d.address, 'pickup_date': d.pickup_date.isoformat()} for d in donations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Ensure you have Flask and Flask-SQLAlchemy installed. You can install them using:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Set the `DATABASE_URL` environment variable for production use, or it will default to a SQLite database file named `donations.db`.
