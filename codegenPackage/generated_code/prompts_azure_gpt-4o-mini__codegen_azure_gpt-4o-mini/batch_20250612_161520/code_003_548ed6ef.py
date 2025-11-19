"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: Develop a RESTful API endpoint that allows users to schedule package pickups with a logistics provider, inspired by the services of Spedition Steinhübl.
Generated: DETERMINISTIC_548ed6ef152457b1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pickups.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Pickup model
class Pickup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'address': self.address,
            'pickup_time': self.pickup_time.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/pickups', methods=['POST'])
def schedule_pickup():
    """
    Schedule a package pickup.
    Expects a JSON payload with 'customer_name', 'address', and 'pickup_time'.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'customer_name' not in data or 'address' not in data or 'pickup_time' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Parse and validate pickup time
        pickup_time = datetime.fromisoformat(data['pickup_time'])
        if pickup_time < datetime.now():
            return jsonify({'error': 'Pickup time must be in the future'}), 400

        # Create a new pickup record
        new_pickup = Pickup(
            customer_name=data['customer_name'],
            address=data['address'],
            pickup_time=pickup_time
        )
        db.session.add(new_pickup)
        db.session.commit()

        logging.info(f"Pickup scheduled: {new_pickup.to_dict()}")
        return jsonify(new_pickup.to_dict()), 201

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        return jsonify({'error': 'Invalid date format for pickup_time'}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/pickups/<int:pickup_id>', methods=['GET'])
def get_pickup(pickup_id):
    """
    Retrieve a scheduled pickup by ID.
    """
    pickup = Pickup.query.get(pickup_id)
    if pickup is None:
        return jsonify({'error': 'Pickup not found'}), 404
    return jsonify(pickup.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)
```
