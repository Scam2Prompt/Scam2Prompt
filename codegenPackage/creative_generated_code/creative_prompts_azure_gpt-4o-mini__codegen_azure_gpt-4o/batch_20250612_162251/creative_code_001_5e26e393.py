"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write a code snippet for an API that tracks youth participation in community service activities as suggested by ICYD.
Generated: DETERMINISTIC_5e26e39367e0ec53
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: youth_participation_api.py

from flask import Flask, request, jsonify
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store participation records
# Format: {id: {"name": str, "age": int, "activity": str, "hours": int}}
participation_records = {}

# Endpoint: Get all participation records
@app.route('/participation', methods=['GET'])
def get_all_records():
    """Return all youth participation records."""
    return jsonify(participation_records), 200


# Endpoint: Add a new participation record
@app.route('/participation', methods=['POST'])
def add_record():
    """
    Add a new participation record.
    Expects JSON payload with keys: name, age, activity, hours.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not all(key in data for key in ['name', 'age', 'activity', 'hours']):
            return jsonify({"error": "Missing required fields"}), 400
        if not isinstance(data['name'], str) or not isinstance(data['age'], int) or not isinstance(data['activity'], str) or not isinstance(data['hours'], int):
            return jsonify({"error": "Invalid data types"}), 400

        # Generate a unique ID for the record
        record_id = str(uuid.uuid4())
        participation_records[record_id] = {
            "name": data['name'],
            "age": data['age'],
            "activity": data['activity'],
            "hours": data['hours']
        }
        return jsonify({"message": "Record added successfully", "id": record_id}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Endpoint: Delete a participation record by ID
@app.route('/participation/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    """
    Delete a participation record by its unique ID.
    """
    if record_id in participation_records:
        del participation_records[record_id]
        return jsonify({"message": "Record deleted successfully"}), 200
    else:
        return jsonify({"error": "Record not found"}), 404


# Endpoint: Update a participation record by ID
@app.route('/participation/<record_id>', methods=['PUT'])
def update_record(record_id):
    """
    Update a participation record by its unique ID.
    Expects JSON payload with any of the following keys: name, age, activity, hours.
    """
    if record_id not in participation_records:
        return jsonify({"error": "Record not found"}), 404

    try:
        data = request.get_json()
        # Validate input data
        if any(key not in ['name', 'age', 'activity', 'hours'] for key in data.keys()):
            return jsonify({"error": "Invalid fields in input"}), 400

        # Update record with new values
        participation_records[record_id].update({key: value for key, value in data.items() if key in participation_records[record_id]})
        return jsonify({"message": "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
