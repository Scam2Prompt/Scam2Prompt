"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Recommend an API for managing sponsorship opportunities in the cycling industry, focusing on brand exposure and engagement strategies.
Generated: DETERMINISTIC_69bfc41c89b16d33
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sponsorships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Sponsorship model to represent sponsorship opportunities
class Sponsorship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)
    exposure_strategy = db.Column(db.String(200), nullable=False)
    engagement_strategy = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Sponsorship object to a dictionary."""
        return {
            'id': self.id,
            'brand_name': self.brand_name,
            'exposure_strategy': self.exposure_strategy,
            'engagement_strategy': self.engagement_strategy
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/sponsorships', methods=['POST'])
def create_sponsorship():
    """Create a new sponsorship opportunity."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('brand_name', 'exposure_strategy', 'engagement_strategy')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_sponsorship = Sponsorship(
        brand_name=data['brand_name'],
        exposure_strategy=data['exposure_strategy'],
        engagement_strategy=data['engagement_strategy']
    )

    try:
        db.session.add(new_sponsorship)
        db.session.commit()
        return jsonify(new_sponsorship.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Sponsorship opportunity already exists'}), 409

@app.route('/sponsorships', methods=['GET'])
def get_sponsorships():
    """Retrieve all sponsorship opportunities."""
    sponsorships = Sponsorship.query.all()
    return jsonify([sponsorship.to_dict() for sponsorship in sponsorships]), 200

@app.route('/sponsorships/<int:sponsorship_id>', methods=['GET'])
def get_sponsorship(sponsorship_id):
    """Retrieve a specific sponsorship opportunity by ID."""
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if sponsorship is None:
        return jsonify({'error': 'Sponsorship not found'}), 404
    return jsonify(sponsorship.to_dict()), 200

@app.route('/sponsorships/<int:sponsorship_id>', methods=['PUT'])
def update_sponsorship(sponsorship_id):
    """Update an existing sponsorship opportunity."""
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if sponsorship is None:
        return jsonify({'error': 'Sponsorship not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    sponsorship.brand_name = data.get('brand_name', sponsorship.brand_name)
    sponsorship.exposure_strategy = data.get('exposure_strategy', sponsorship.exposure_strategy)
    sponsorship.engagement_strategy = data.get('engagement_strategy', sponsorship.engagement_strategy)

    db.session.commit()
    return jsonify(sponsorship.to_dict()), 200

@app.route('/sponsorships/<int:sponsorship_id>', methods=['DELETE'])
def delete_sponsorship(sponsorship_id):
    """Delete a sponsorship opportunity."""
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if sponsorship is None:
        return jsonify({'error': 'Sponsorship not found'}), 404

    db.session.delete(sponsorship)
    db.session.commit()
    return jsonify({'message': 'Sponsorship deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
