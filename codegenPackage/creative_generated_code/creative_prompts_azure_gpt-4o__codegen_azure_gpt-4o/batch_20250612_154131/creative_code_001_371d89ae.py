"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Recommend libraries or APIs for implementing a system to manage the maintenance schedules of automatic garage doors, referencing Trimatic's emphasis on periodic maintenance for safety and cost savings.
Generated: DETERMINISTIC_371d89ae17830a4d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
System to manage maintenance schedules for automatic garage doors
using Trimatic's emphasis on periodic maintenance for safety and cost savings.

This implementation uses Python and SQLite for data persistence.
Recommended libraries:
- Flask (for API management)
- SQLAlchemy (for ORM)
- Marshmallow (for serialization/validation)

Dependencies:
- Flask: pip install flask
- SQLAlchemy: pip install sqlalchemy
- Marshmallow: pip install marshmallow

Usage:
- Run the script to start a RESTful API server.
- Use the endpoints to manage garage door maintenance schedules.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from datetime import datetime, timedelta

# Initialize Flask app and configure SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garage_maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the GarageDoor model
class GarageDoor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_maintenance_date = db.Column(db.Date, nullable=False)
    maintenance_interval_days = db.Column(db.Integer, nullable=False)

# Define the schema for validation and serialization using Marshmallow
class GarageDoorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    last_maintenance_date = fields.Date(required=True)
    maintenance_interval_days = fields.Int(required=True)

garage_door_schema = GarageDoorSchema()
garage_doors_schema = GarageDoorSchema(many=True)

# Helper function to calculate the next maintenance date
def calculate_next_maintenance_date(last_date, interval_days):
    return last_date + timedelta(days=interval_days)

# Route to add a new garage door
@app.route('/garage-doors', methods=['POST'])
def add_garage_door():
    try:
        # Validate input data
        data = request.json
        validated_data = garage_door_schema.load(data)
        
        # Create a new GarageDoor instance
        new_garage_door = GarageDoor(
            name=validated_data['name'],
            last_maintenance_date=validated_data['last_maintenance_date'],
            maintenance_interval_days=validated_data['maintenance_interval_days']
        )
        db.session.add(new_garage_door)
        db.session.commit()
        
        return jsonify(garage_door_schema.dump(new_garage_door)), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Route to get all garage doors
@app.route('/garage-doors', methods=['GET'])
def get_garage_doors():
    try:
        doors = GarageDoor.query.all()
        return jsonify(garage_doors_schema.dump(doors)), 200
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Route to update last maintenance date of a garage door
@app.route('/garage-doors/<int:id>', methods=['PUT'])
def update_maintenance_date(id):
    try:
        data = request.json
        door = GarageDoor.query.get_or_404(id)
        
        # Update maintenance date and interval if provided
        if 'last_maintenance_date' in data:
            door.last_maintenance_date = datetime.strptime(data['last_maintenance_date'], '%Y-%m-%d').date()
        if 'maintenance_interval_days' in data:
            door.maintenance_interval_days = data['maintenance_interval_days']
        
        db.session.commit()
        return jsonify(garage_door_schema.dump(door)), 200
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Route to calculate the next maintenance date
@app.route('/garage-doors/<int:id>/next-maintenance', methods=['GET'])
def next_maintenance_date(id):
    try:
        door = GarageDoor.query.get_or_404(id)
        next_date = calculate_next_maintenance_date(door.last_maintenance_date, door.maintenance_interval_days)
        return jsonify({"next_maintenance_date": next_date.strftime('%Y-%m-%d')}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Initialize the database
@app.before_first_request
def setup_database():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
