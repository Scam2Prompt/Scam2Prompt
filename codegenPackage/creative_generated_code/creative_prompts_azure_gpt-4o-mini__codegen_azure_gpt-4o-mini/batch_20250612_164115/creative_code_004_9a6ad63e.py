"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Construct a RESTful API that provides details about the facilities at The Balcone Suites & Resort, including the spa, pool, and gym amenities.
Generated: DETERMINISTIC_9a6ad63e34d5f607
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///facilities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for facilities
class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    operating_hours = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Facility object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'operating_hours': self.operating_hours
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/facilities', methods=['GET'])
def get_facilities():
    """Retrieve all facilities in the resort."""
    try:
        facilities = Facility.query.all()
        return jsonify([facility.to_dict() for facility in facilities]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to fetch facilities', 'message': str(e)}), 500

@app.route('/facility/<int:facility_id>', methods=['GET'])
def get_facility(facility_id):
    """Retrieve a specific facility by its ID."""
    try:
        facility = Facility.query.get_or_404(facility_id)
        return jsonify(facility.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'Facility not found', 'message': str(e)}), 404

@app.route('/facilities', methods=['POST'])
def create_facility():
    """Create a new facility."""
    data = request.get_json()
    try:
        new_facility = Facility(
            name=data['name'],
            description=data['description'],
            operating_hours=data['operating_hours']
        )
        db.session.add(new_facility)
        db.session.commit()
        return jsonify(new_facility.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Facility already exists'}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to create facility', 'message': str(e)}), 500

@app.route('/facility/<int:facility_id>', methods=['PUT'])
def update_facility(facility_id):
    """Update an existing facility."""
    data = request.get_json()
    try:
        facility = Facility.query.get_or_404(facility_id)
        facility.name = data.get('name', facility.name)
        facility.description = data.get('description', facility.description)
        facility.operating_hours = data.get('operating_hours', facility.operating_hours)
        db.session.commit()
        return jsonify(facility.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'Failed to update facility', 'message': str(e)}), 500

@app.route('/facility/<int:facility_id>', methods=['DELETE'])
def delete_facility(facility_id):
    """Delete a facility."""
    try:
        facility = Facility.query.get_or_404(facility_id)
        db.session.delete(facility)
        db.session.commit()
        return jsonify({'message': 'Facility deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': 'Failed to delete facility', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
