"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Design a RESTful API for managing equipment maintenance schedules for lifting and moving machinery, based on Tekroll Industrial's service offerings.
Generated: DETERMINISTIC_3348caafe9e25c32
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment_maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Models
class Equipment(db.Model):
    """
    Equipment model representing machinery in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Equipment name
    type = db.Column(db.String(100), nullable=False)  # Type of equipment
    maintenance_schedule = db.Column(db.String(100), nullable=False)  # Maintenance schedule (e.g., "Monthly")
    last_maintenance_date = db.Column(db.DateTime, nullable=True)  # Last maintenance date

    def to_dict(self):
        """
        Converts model instance to dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'maintenance_schedule': self.maintenance_schedule,
            'last_maintenance_date': self.last_maintenance_date.strftime('%Y-%m-%d') if self.last_maintenance_date else None
        }


# Routes
@app.route('/equipment', methods=['GET'])
def get_equipment():
    """
    Get a list of all equipment.
    """
    equipment = Equipment.query.all()
    return jsonify([e.to_dict() for e in equipment]), 200


@app.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment_details(equipment_id):
    """
    Get details of a specific equipment by ID.
    """
    equipment = Equipment.query.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404
    return jsonify(equipment.to_dict()), 200


@app.route('/equipment', methods=['POST'])
def add_equipment():
    """
    Add new equipment to the system.
    """
    data = request.get_json()

    # Validate required fields
    if not all(key in data for key in ('name', 'type', 'maintenance_schedule')):
        return jsonify({'error': 'Missing required fields'}), 400

    # Create and save new equipment
    new_equipment = Equipment(
        name=data['name'],
        type=data['type'],
        maintenance_schedule=data['maintenance_schedule'],
        last_maintenance_date=datetime.strptime(data['last_maintenance_date'], '%Y-%m-%d') if 'last_maintenance_date' in data else None
    )
    db.session.add(new_equipment)
    db.session.commit()

    return jsonify(new_equipment.to_dict()), 201


@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """
    Update an existing equipment's details.
    """
    equipment = Equipment.query.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404

    data = request.get_json()

    # Update equipment fields if provided
    equipment.name = data.get('name', equipment.name)
    equipment.type = data.get('type', equipment.type)
    equipment.maintenance_schedule = data.get('maintenance_schedule', equipment.maintenance_schedule)
    if 'last_maintenance_date' in data:
        equipment.last_maintenance_date = datetime.strptime(data['last_maintenance_date'], '%Y-%m-%d')

    db.session.commit()
    return jsonify(equipment.to_dict()), 200


@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """
    Delete an equipment from the system.
    """
    equipment = Equipment.query.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404

    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Equipment deleted successfully'}), 200


# Error handling
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({'error': 'Internal server error'}), 500


# Application entry point
if __name__ == '__main__':
    # Ensure database tables are created
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```
