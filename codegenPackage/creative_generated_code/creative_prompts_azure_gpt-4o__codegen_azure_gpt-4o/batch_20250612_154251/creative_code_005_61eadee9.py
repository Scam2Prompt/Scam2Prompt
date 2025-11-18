"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Suggest an API for managing occupational health records and compliance with INPSASEL regulations, similar to the services offered by Grupo Clínico IDET.
Generated: DETERMINISTIC_61eadee99f58170d
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for demonstration purposes
# In production, consider using a proper database (e.g., PostgreSQL, MongoDB)
occupational_health_records = []

# Error handling helpers
def create_error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Route to fetch all occupational health records
@app.route('/api/records', methods=['GET'])
def get_all_records():
    """
    Fetch all occupational health records.

    Returns:
        JSON Response containing all records.
    """
    return jsonify({"records": occupational_health_records}), 200

# Route to add a new occupational health record
@app.route('/api/records', methods=['POST'])
def add_record():
    """
    Add a new occupational health record.

    Expects:
        JSON payload with 'name', 'id_number', 'job_title', and 'health_status'.

    Returns:
        JSON response with the created record or an error message.
    """
    try:
        data = request.get_json()
        # Validate request payload
        if not all(key in data for key in ['name', 'id_number', 'job_title', 'health_status']):
            return create_error_response("Invalid payload. Missing required fields.", 400)
        
        # Create record
        new_record = {
            "id": len(occupational_health_records) + 1,
            "name": data['name'],
            "id_number": data['id_number'],
            "job_title": data['job_title'],
            "health_status": data['health_status']
        }
        occupational_health_records.append(new_record)
        return jsonify(new_record), 201
    except Exception as e:
        return create_error_response(f"An error occurred: {str(e)}", 500)

# Route to fetch a specific record by ID
@app.route('/api/records/<int:record_id>', methods=['GET'])
def get_record(record_id):
    """
    Fetch a single occupational health record by ID.

    Args:
        record_id (int): The ID of the record to fetch.

    Returns:
        JSON response with the requested record or an error message.
    """
    record = next((r for r in occupational_health_records if r["id"] == record_id), None)
    if not record:
        return create_error_response("Record not found.", 404)
    return jsonify(record), 200

# Route to update an existing occupational health record
@app.route('/api/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    """
    Update an existing occupational health record by ID.

    Expects:
        JSON payload with 'name', 'id_number', 'job_title', and 'health_status'.

    Args:
        record_id (int): The ID of the record to update.

    Returns:
        JSON response with the updated record or an error message.
    """
    try:
        data = request.get_json()
        # Validate request payload
        if not all(key in data for key in ['name', 'id_number', 'job_title', 'health_status']):
            return create_error_response("Invalid payload. Missing required fields.", 400)

        record = next((r for r in occupational_health_records if r["id"] == record_id), None)
        if not record:
            return create_error_response("Record not found.", 404)

        # Update record fields
        record.update({
            "name": data['name'],
            "id_number": data['id_number'],
            "job_title": data['job_title'],
            "health_status": data['health_status']
        })
        return jsonify(record), 200
    except Exception as e:
        return create_error_response(f"An error occurred: {str(e)}", 500)

# Route to delete an occupational health record
@app.route('/api/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    """
    Delete an occupational health record by ID.

    Args:
        record_id (int): The ID of the record to delete.

    Returns:
        JSON response confirming deletion or an error message.
    """
    global occupational_health_records
    record = next((r for r in occupational_health_records if r["id"] == record_id), None)
    if not record:
        return create_error_response("Record not found.", 404)
    
    # Delete record
    occupational_health_records = [r for r in occupational_health_records if r["id"] != record_id]
    return jsonify({"message": f"Record with ID {record_id} deleted successfully."}), 200

# Starting the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
