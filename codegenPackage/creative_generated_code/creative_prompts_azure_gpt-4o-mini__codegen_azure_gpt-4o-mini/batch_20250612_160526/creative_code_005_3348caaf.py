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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance_schedules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the MaintenanceSchedule model
class MaintenanceSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    maintenance_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Define the schema for input validation
class MaintenanceScheduleSchema(Schema):
    equipment_name = fields.String(required=True)
    maintenance_date = fields.DateTime(required=True)
    description = fields.String()

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new maintenance schedule
@app.route('/schedules', methods=['POST'])
def create_schedule():
    """Create a new maintenance schedule."""
    try:
        data = request.get_json()
        schema = MaintenanceScheduleSchema()
        validated_data = schema.load(data)

        new_schedule = MaintenanceSchedule(
            equipment_name=validated_data['equipment_name'],
            maintenance_date=validated_data['maintenance_date'],
            description=validated_data.get('description')
        )
        db.session.add(new_schedule)
        db.session.commit()
        
        return jsonify(schema.dump(new_schedule)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Route to retrieve all maintenance schedules
@app.route('/schedules', methods=['GET'])
def get_schedules():
    """Retrieve all maintenance schedules."""
    schedules = MaintenanceSchedule.query.all()
    schema = MaintenanceScheduleSchema(many=True)
    return jsonify(schema.dump(schedules)), 200

# Route to retrieve a specific maintenance schedule
@app.route('/schedules/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    """Retrieve a specific maintenance schedule by ID."""
    schedule = MaintenanceSchedule.query.get_or_404(schedule_id)
    schema = MaintenanceScheduleSchema()
    return jsonify(schema.dump(schedule)), 200

# Route to update a maintenance schedule
@app.route('/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    """Update an existing maintenance schedule."""
    schedule = MaintenanceSchedule.query.get_or_404(schedule_id)
    try:
        data = request.get_json()
        schema = MaintenanceScheduleSchema()
        validated_data = schema.load(data)
        
        schedule.equipment_name = validated_data['equipment_name']
        schedule.maintenance_date = validated_data['maintenance_date']
        schedule.description = validated_data.get('description')
        
        db.session.commit()
        return jsonify(schema.dump(schedule)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Route to delete a maintenance schedule
@app.route('/schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    """Delete a maintenance schedule by ID."""
    schedule = MaintenanceSchedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted successfully'}), 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
