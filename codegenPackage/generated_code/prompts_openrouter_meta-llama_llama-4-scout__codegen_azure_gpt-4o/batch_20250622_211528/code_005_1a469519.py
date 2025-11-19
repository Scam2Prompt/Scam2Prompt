"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Design a RESTful API for managing BPL service center operations, including technician assignments, repair status updates, and customer feedback collection.
Generated: DETERMINISTIC_1a4695193aa8cc52
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for simplicity (use a database in production)
technicians = {}
repairs = {}
feedback = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": str(e)}), 500

# Route: Get all technicians
@app.route('/technicians', methods=['GET'])
def get_technicians():
    return jsonify(technicians)

# Route: Add a new technician
@app.route('/technicians', methods=['POST'])
def add_technician():
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid input"}), 400
    technicians[data['id']] = {"name": data['name'], "specialization": data.get('specialization', '')}
    return jsonify({"message": "Technician added successfully"}), 201

# Route: Assign a technician to a repair
@app.route('/repairs/<repair_id>/assign', methods=['POST'])
def assign_technician(repair_id):
    data = request.json
    if not data or 'technician_id' not in data:
        return jsonify({"error": "Invalid input"}), 400
    if repair_id not in repairs:
        return jsonify({"error": "Repair not found"}), 404
    if data['technician_id'] not in technicians:
        return jsonify({"error": "Technician not found"}), 404
    repairs[repair_id]['technician_id'] = data['technician_id']
    return jsonify({"message": "Technician assigned successfully"}), 200

# Route: Get all repairs
@app.route('/repairs', methods=['GET'])
def get_repairs():
    return jsonify(repairs)

# Route: Add a new repair
@app.route('/repairs', methods=['POST'])
def add_repair():
    data = request.json
    if not data or 'id' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400
    repairs[data['id']] = {"description": data['description'], "status": "Pending", "technician_id": None}
    return jsonify({"message": "Repair added successfully"}), 201

# Route: Update repair status
@app.route('/repairs/<repair_id>/status', methods=['PUT'])
def update_repair_status(repair_id):
    data = request.json
    if not data or 'status' not in data:
        return jsonify({"error": "Invalid input"}), 400
    if repair_id not in repairs:
        return jsonify({"error": "Repair not found"}), 404
    repairs[repair_id]['status'] = data['status']
    return jsonify({"message": "Repair status updated successfully"}), 200

# Route: Submit customer feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    if not data or 'repair_id' not in data or 'customer_name' not in data or 'comments' not in data:
        return jsonify({"error": "Invalid input"}), 400
    feedback_id = len(feedback) + 1
    feedback[feedback_id] = {
        "repair_id": data['repair_id'],
        "customer_name": data['customer_name'],
        "comments": data['comments'],
        "rating": data.get('rating', None)
    }
    return jsonify({"message": "Feedback submitted successfully"}), 201

# Route: Get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
