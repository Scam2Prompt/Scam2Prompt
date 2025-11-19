"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Design a RESTful API for managing equipment maintenance schedules for lifting and moving machinery, based on Tekroll Industrial's service offerings.
Generated: DETERMINISTIC_3348caafe9e25c32
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance_schedules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the MaintenanceSchedule model
class MaintenanceSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    maintenance_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'equipment_name': self.equipment_name,
            'maintenance_date': self.maintenance_date.isoformat(),
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Create a new maintenance schedule
@app.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    if not data or 'equipment_name' not in data or 'maintenance_date' not in data:
        abort(400)  # Bad request

    new_schedule = MaintenanceSchedule(
        equipment_name=data['equipment_name'],
        maintenance_date=datetime.fromisoformat(data['maintenance_date']),
        description=data.get('description')
    )
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify(new_schedule.to_dict()), 201

# Retrieve all maintenance schedules
@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = MaintenanceSchedule.query.all()
    return jsonify([schedule.to_dict() for schedule in schedules]), 200

# Retrieve a specific maintenance schedule by ID
@app.route('/schedules/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    schedule = MaintenanceSchedule.query.get(schedule_id)
    if schedule is None:
        abort(404)  # Not found
    return jsonify(schedule.to_dict()), 200

# Update a maintenance schedule
@app.route('/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    schedule = MaintenanceSchedule.query.get(schedule_id)
    if schedule is None:
        abort(404)  # Not found

    data = request.get_json()
    if not data:
        abort(400)  # Bad request

    schedule.equipment_name = data.get('equipment_name', schedule.equipment_name)
    schedule.maintenance_date = datetime.fromisoformat(data.get('maintenance_date', schedule.maintenance_date.isoformat()))
    schedule.description = data.get('description', schedule.description)

    db.session.commit()
    return jsonify(schedule.to_dict()), 200

# Delete a maintenance schedule
@app.route('/schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    schedule = MaintenanceSchedule.query.get(schedule_id)
    if schedule is None:
        abort(404)  # Not found

    db.session.delete(schedule)
    db.session.commit()
    return jsonify({'result': True}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
