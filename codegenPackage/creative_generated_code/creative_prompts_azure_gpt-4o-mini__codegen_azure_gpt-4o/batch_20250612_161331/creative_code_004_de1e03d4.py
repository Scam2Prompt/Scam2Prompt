"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-idex.com
Prompt: Outline a RESTful API design for a fitness center that includes endpoints for managing equipment inventory, class schedules, and member registrations.
Generated: DETERMINISTIC_de1e03d47b9d2beb
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration purposes
equipment_inventory = [
    {"id": 1, "name": "Treadmill", "quantity": 5},
    {"id": 2, "name": "Dumbbells", "quantity": 20},
]

class_schedules = [
    {"id": 1, "name": "Yoga Class", "time": "10:00 AM"},
    {"id": 2, "name": "Spinning Class", "time": "2:00 PM"},
]

members = [
    {"id": 1, "name": "Alice", "membership_type": "Gold"},
    {"id": 2, "name": "Bob", "membership_type": "Silver"},
]

# Endpoint: Get all equipment inventory
@app.route('/equipment', methods=['GET'])
def get_equipment():
    return jsonify(equipment_inventory), 200

# Endpoint: Add new equipment
@app.route('/equipment', methods=['POST'])
def add_equipment():
    try:
        new_equipment = request.json
        new_equipment['id'] = len(equipment_inventory) + 1
        equipment_inventory.append(new_equipment)
        return jsonify(new_equipment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint: Get all class schedules
@app.route('/classes', methods=['GET'])
def get_classes():
    return jsonify(class_schedules), 200

# Endpoint: Add new class schedule
@app.route('/classes', methods=['POST'])
def add_class():
    try:
        new_class = request.json
        new_class['id'] = len(class_schedules) + 1
        class_schedules.append(new_class)
        return jsonify(new_class), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint: Get all members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

# Endpoint: Add new member
@app.route('/members', methods=['POST'])
def add_member():
    try:
        new_member = request.json
        new_member['id'] = len(members) + 1
        members.append(new_member)
        return jsonify(new_member), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handler for 404 (Route Not Found)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "An internal server error occurred"}), 500

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```
