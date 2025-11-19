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
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
equipment_db = {}

# Helper function to validate equipment data
def validate_equipment_data(data):
    required_fields = ['name', 'type', 'last_maintenance_date', 'maintenance_interval_days']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.strptime(data['last_maintenance_date'], '%Y-%m-%d')
        int(data['maintenance_interval_days'])
    except ValueError:
        return False, "Invalid date format or maintenance interval"
    return True, None

@app.route('/equipment', methods=['POST'])
def add_equipment():
    """
    Add a new piece of equipment to the maintenance schedule.
    """
    data = request.json
    is_valid, error_message = validate_equipment_data(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    equipment_id = str(uuid.uuid4())
    equipment_db[equipment_id] = {
        'id': equipment_id,
        'name': data['name'],
        'type': data['type'],
        'last_maintenance_date': data['last_maintenance_date'],
        'maintenance_interval_days': int(data['maintenance_interval_days'])
    }
    return jsonify({'message': 'Equipment added successfully', 'equipment_id': equipment_id}), 201

@app.route('/equipment', methods=['GET'])
def list_equipment():
    """
    List all equipment in the maintenance schedule.
    """
    return jsonify(list(equipment_db.values())), 200

@app.route('/equipment/<equipment_id>', methods=['GET'])
def get_equipment(equipment_id):
    """
    Retrieve details of a specific piece of equipment.
    """
    equipment = equipment_db.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404
    return jsonify(equipment), 200

@app.route('/equipment/<equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """
    Update details of a specific piece of equipment.
    """
    equipment = equipment_db.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404

    data = request.json
    is_valid, error_message = validate_equipment_data(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    equipment_db[equipment_id].update({
        'name': data['name'],
        'type': data['type'],
        'last_maintenance_date': data['last_maintenance_date'],
        'maintenance_interval_days': int(data['maintenance_interval_days'])
    })
    return jsonify({'message': 'Equipment updated successfully'}), 200

@app.route('/equipment/<equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """
    Delete a specific piece of equipment from the maintenance schedule.
    """
    equipment = equipment_db.pop(equipment_id, None)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404
    return jsonify({'message': 'Equipment deleted successfully'}), 200

@app.route('/equipment/<equipment_id>/next-maintenance', methods=['GET'])
def calculate_next_maintenance(equipment_id):
    """
    Calculate the next maintenance date for a specific piece of equipment.
    """
    equipment = equipment_db.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404

    try:
        last_maintenance_date = datetime.strptime(equipment['last_maintenance_date'], '%Y-%m-%d')
        maintenance_interval_days = equipment['maintenance_interval_days']
        next_maintenance_date = last_maintenance_date + timedelta(days=maintenance_interval_days)
        return jsonify({'next_maintenance_date': next_maintenance_date.strftime('%Y-%m-%d')}), 200
    except Exception as e:
        return jsonify({'error': f'Error calculating next maintenance date: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
