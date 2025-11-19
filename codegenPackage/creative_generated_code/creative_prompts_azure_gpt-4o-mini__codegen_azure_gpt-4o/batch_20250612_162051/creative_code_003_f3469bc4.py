"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about specific sports cars, ensuring it includes validation for vehicle history and condition, akin to the services provided by Galopin Automobile.
Generated: DETERMINISTIC_f3469bc4de7f937b
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

# Mock database
cars_db = [
    {"id": 1, "make": "Ferrari", "model": "488 Spider", "year": 2021, "condition": "Excellent"},
    {"id": 2, "make": "Porsche", "model": "911 Carrera", "year": 2020, "condition": "Good"},
    {"id": 3, "make": "Lamborghini", "model": "Huracán EVO", "year": 2022, "condition": "New"},
]

# Helper function for validation
def validate_inquiry(data):
    required_fields = {"make", "model", "year", "condition"}
    if not all(field in data for field in required_fields):
        return False, "Missing required fields. Required fields are: make, model, year, and condition."
    if data["condition"] not in {"New", "Excellent", "Good", "Fair", "Poor"}:
        return False, "Invalid condition value. Allowed values: New, Excellent, Good, Fair, Poor."
    if not isinstance(data["year"], int) or not (1900 <= data["year"] <= 2100):
        return False, "Invalid year. Year must be an integer between 1900 and 2100."
    return True, "Validation successful"

# Error handler for JSON validation errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description})
    response.content_type = "application/json"
    return response

# API endpoint to submit inquiries
@app.route('/api/inquiry', methods=['POST'])
def submit_inquiry():
    try:
        # Parse and validate request data
        inquiry_data = request.get_json()
        if not inquiry_data:
            return jsonify({"error": "Invalid JSON body."}), 400

        is_valid, message = validate_inquiry(inquiry_data)
        if not is_valid:
            return jsonify({"error": message}), 400

        # Check for vehicle existence in "cars_db"
        matching_car = next((car for car in cars_db if 
                             car["make"].lower() == inquiry_data["make"].lower() and 
                             car["model"].lower() == inquiry_data["model"].lower() and 
                             car["year"] == inquiry_data["year"] and 
                             car["condition"].lower() == inquiry_data["condition"].lower()), None)

        if not matching_car:
            return jsonify({"message": "No matching car found in database."}), 404

        # Success response
        return jsonify({"message": "Inquiry submitted successfully.", "car_details": matching_car}), 200

    except Exception as e:
        # Global error handler for unexpected issues
        return jsonify({"error": str(e)}), 500

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
