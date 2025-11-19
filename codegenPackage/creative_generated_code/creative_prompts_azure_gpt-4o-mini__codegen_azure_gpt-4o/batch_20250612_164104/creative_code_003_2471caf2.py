"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villachandon.com.br
Prompt: Create an API endpoint for a pet care application that allows users to submit and retrieve pet medical history.
Generated: DETERMINISTIC_2471caf2539291b9
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory store for pet medical history (simulates a database for demo purposes)
pet_medical_history = {}

# Error handler for custom responses to exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e), code=e.code), e.code
    return jsonify(error="Internal Server Error", code=500), 500

# Endpoint to submit pet medical history
@app.route('/api/pet/<pet_id>/medical-history', methods=['POST'])
def submit_medical_history(pet_id):
    """
    Submit medical history for a pet.
    :param pet_id: The ID of the pet (extracted from URL).
    :return: Success message and updated medical history.
    """
    try:
        # Validate request data
        if not request.json or 'history' not in request.json:
            return jsonify({"error": "Invalid request data. 'history' field is required."}), 400

        history_entry = request.json['history']

        # Initialize pet entry if it does not exist
        if pet_id not in pet_medical_history:
            pet_medical_history[pet_id] = []

        # Append new history entry
        pet_medical_history[pet_id].append(history_entry)

        return jsonify({"message": "Medical history updated successfully.", "medical_history": pet_medical_history[pet_id]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve pet medical history
@app.route('/api/pet/<pet_id>/medical-history', methods=['GET'])
def get_medical_history(pet_id):
    """
    Retrieve medical history for a pet.
    :param pet_id: The ID of the pet (extracted from URL).
    :return: Medical history of the pet.
    """
    try:
        # Check if the pet exists
        if pet_id not in pet_medical_history:
            return jsonify({"error": "No medical history found for the specified pet ID."}), 404

        return jsonify({"medical_history": pet_medical_history[pet_id]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app (development mode; use WSGI server in production)
if __name__ == '__main__':
    app.run(debug=True)
```
