"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velemeny.moriczdental.hu
Prompt: Develop a REST API endpoint that allows patients to submit their dental treatment evaluations, capturing details like "doctor's helpfulness" and "pain level during treatment," as seen on the Móricz Dental feedback platform.
Generated: DETERMINISTIC_185bfe0f60ddd7df
Batch ID: 20250612_162051
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

# In-memory database for storing evaluations (for demonstration purposes)
# In production, use a proper database system like PostgreSQL or MySQL.
evaluations = []

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "error": e.name,
            "message": e.description
        }).get_data()
        response.content_type = "application/json"
        return response
    else:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to submit dental treatment evaluations
@app.route('/submit-evaluation', methods=['POST'])
def submit_evaluation():
    """
    Accepts a POST request with JSON payload to submit a dental treatment evaluation.
    {
        "patient_name": "John Doe",
        "doctor_name": "Dr. Smith",
        "helpfulness": 4,       # Integer from 1 to 5
        "pain_level": 2,        # Integer from 1 to 5
        "comments": "Very professional and kind."
    }
    """
    try:
        # Parse JSON data from request
        data = request.get_json()

        # Input validation
        if not data:
            return jsonify({"error": "Invalid input", "message": "JSON data is required."}), 400

        required_fields = ["patient_name", "doctor_name", "helpfulness", "pain_level"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Invalid input", "message": f"'{field}' is required."}), 400

        if not isinstance(data["helpfulness"], int) or not (1 <= data["helpfulness"] <= 5):
            return jsonify({"error": "Invalid input", "message": "'helpfulness' must be an integer between 1 and 5."}), 400

        if not isinstance(data["pain_level"], int) or not (1 <= data["pain_level"] <= 5):
            return jsonify({"error": "Invalid input", "message": "'pain_level' must be an integer between 1 and 5."}), 400

        # Process the evaluation and store it (simulated with in-memory database)
        evaluation_id = len(evaluations) + 1
        new_evaluation = {
            "id": evaluation_id,
            "patient_name": data["patient_name"],
            "doctor_name": data["doctor_name"],
            "helpfulness": data["helpfulness"],
            "pain_level": data["pain_level"],
            "comments": data.get("comments", "")  # Optional field
        }
        evaluations.append(new_evaluation)

        # Return success response
        return jsonify({"message": "Evaluation submitted successfully.", "evaluation": new_evaluation}), 201

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to retrieve all evaluations (for testing purposes)
@app.route('/evaluations', methods=['GET'])
def get_evaluations():
    """
    Returns all submitted evaluations.
    """
    return jsonify({"evaluations": evaluations}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
