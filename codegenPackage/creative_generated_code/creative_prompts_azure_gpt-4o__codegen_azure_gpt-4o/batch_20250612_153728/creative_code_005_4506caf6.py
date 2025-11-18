"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Create a REST API for managing architectural consulting services, including endpoints for booking consultations and showcasing expertise, as described on Celestia's site.
Generated: DETERMINISTIC_4506caf626015778
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory data storage for simplicity
consultations = []
expertise = [
    {"id": 1, "name": "Modern Architecture", "description": "Specialized in contemporary designs."},
    {"id": 2, "name": "Sustainable Architecture", "description": "Expertise in environmentally friendly structures."},
    {"id": 3, "name": "Restoration", "description": "Focus on preserving historical buildings."},
]

# Endpoint: Get all expertise
@app.route('/expertise', methods=['GET'])
def get_expertise():
    """
    GET /expertise
    Returns a list of available expertise areas.
    """
    return jsonify({"expertise": expertise}), 200

# Endpoint: Book a consultation
@app.route('/consultations', methods=['POST'])
def book_consultation():
    """
    POST /consultations
    Books a consultation with the architectural consulting service.
    
    JSON Body:
    {
        "name": <str>,  # Client's name
        "email": <str>, # Client's email
        "expertise_id": <int>, # ID of expertise to book
        "date": <str>   # Desired consultation date in YYYY-MM-DD format
    }
    """
    try:
        # Validate and parse the input
        data = request.json
        name = data.get('name')
        email = data.get('email')
        expertise_id = data.get('expertise_id')
        date = data.get('date')

        # Ensure required fields are provided
        if not name or not email or not expertise_id or not date:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate expertise_id
        selected_expertise = next((e for e in expertise if e['id'] == expertise_id), None)
        if not selected_expertise:
            return jsonify({"error": "Invalid expertise ID"}), 404

        # Validate date format
        try:
            consultation_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create and store the new consultation
        consultation_id = len(consultations) + 1
        new_consultation = {
            "id": consultation_id,
            "name": name,
            "email": email,
            "expertise": selected_expertise,
            "date": consultation_date.isoformat()
        }
        consultations.append(new_consultation)

        # Return the newly created consultation
        return jsonify({"message": "Consultation booked successfully", "consultation": new_consultation}), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint: View all booked consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    """
    GET /consultations
    Returns a list of all booked consultations.
    """
    return jsonify({"consultations": consultations}), 200

# Error handler for 404 (route not found)
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 405 (method not allowed)
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handles 405 errors for disallowed HTTP methods.
    """
    return jsonify({"error": "Method not allowed"}), 405

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
