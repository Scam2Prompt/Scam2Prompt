"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Create a sample API that allows users to book consultations for creative services, reflecting the user experience principles highlighted by Swell Creative Management.
Generated: DETERMINISTIC_21a49f66a020313e
Batch ID: 20250612_161235
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

app = Flask(__name__)

# In-memory database (for simplicity; use an actual database in production)
consultations = []

# Utility function to validate consultation data
def validate_consultation_data(data):
    required_fields = ['name', 'email', 'service_type', 'date_time']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False, "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."
    return True, None

@app.route("/consultations", methods=["POST"])
def book_consultation():
    """
    Endpoint to book a consultation.
    Expects JSON payload with 'name', 'email', 'service_type', and 'date_time'.
    """
    try:
        data = request.get_json()

        # Validate incoming data
        is_valid, error_message = validate_consultation_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate unique ID for the consultation
        consultation_id = str(uuid.uuid4())

        # Create consultation entry
        new_consultation = {
            "id": consultation_id,
            "name": data["name"],
            "email": data["email"],
            "service_type": data["service_type"],
            "date_time": data["date_time"],
            "created_at": datetime.now().isoformat()
        }

        consultations.append(new_consultation)

        return jsonify({"message": "Consultation booked successfully!", "consultation": new_consultation}), 201
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route("/consultations/<consultation_id>", methods=["GET"])
def get_consultation(consultation_id):
    """
    Endpoint to get details of a specific consultation by ID.
    """
    try:
        # Find consultation by ID
        consultation = next((c for c in consultations if c["id"] == consultation_id), None)
        if not consultation:
            return jsonify({"error": "Consultation not found."}), 404

        return jsonify({"consultation": consultation}), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route("/consultations", methods=["GET"])
def list_consultations():
    """
    Endpoint to list all consultations.
    """
    try:
        return jsonify({"consultations": consultations}), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
