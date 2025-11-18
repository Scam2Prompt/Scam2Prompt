"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Develop a REST API in Flask that allows users to schedule consultations for foot and ankle conditions, including bunions, Achilles tendon injuries, and ankle arthritis.
Generated: DETERMINISTIC_4afd45e43ded9f2c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

# Initialize the Flask app
app = Flask(__name__)

# In-memory database for storing consultations
consultations = []

# Available conditions for scheduling consultations
CONDITIONS = ["bunions", "Achilles tendon injuries", "ankle arthritis"]

@app.route('/consultations', methods=['POST'])
def schedule_consultation():
    """
    Endpoint to schedule a consultation.
    Accepts JSON payload and returns confirmation.
    """
    try:
        data = request.json
        # Validate input
        if 'name' not in data or 'email' not in data or 'condition' not in data or 'date' not in data:
            return jsonify({"error": "Missing required fields: name, email, condition, or date"}), 400
        
        # Check if the condition is valid
        if data['condition'] not in CONDITIONS:
            return jsonify({"error": f"Invalid condition. Must be one of {CONDITIONS}"}), 400
        
        # Validate and parse the date
        try:
            consultation_date = datetime.strptime(data['date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
        
        # Create a unique consultation ID
        consultation_id = str(uuid.uuid4())
        
        # Store the consultation
        consultation = {
            "id": consultation_id,
            "name": data['name'],
            "email": data['email'],
            "condition": data['condition'],
            "date": consultation_date.strftime('%Y-%m-%d')
        }
        consultations.append(consultation)
        
        return jsonify({"message": "Consultation scheduled successfully", "consultation": consultation}), 201
    
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/consultations', methods=['GET'])
def get_consultations():
    """
    Endpoint to retrieve all scheduled consultations.
    Returns JSON with the list of consultations.
    """
    return jsonify({"consultations": consultations}), 200

@app.route('/consultations/<consultation_id>', methods=['GET'])
def get_consultation_by_id(consultation_id):
    """
    Endpoint to retrieve a specific consultation by ID.
    Returns JSON with the consultation details.
    """
    try:
        consultation = next((c for c in consultations if c['id'] == consultation_id), None)
        if not consultation:
            return jsonify({"error": "Consultation not found"}), 404
        
        return jsonify({"consultation": consultation}), 200
    
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/consultations/<consultation_id>', methods=['DELETE'])
def delete_consultation(consultation_id):
    """
    Endpoint to delete a consultation by ID.
    Returns confirmation message if successful.
    """
    try:
        global consultations
        consultation = next((c for c in consultations if c['id'] == consultation_id), None)
        if not consultation:
            return jsonify({"error": "Consultation not found"}), 404
        
        consultations = [c for c in consultations if c['id'] != consultation_id]
        return jsonify({"message": "Consultation deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
