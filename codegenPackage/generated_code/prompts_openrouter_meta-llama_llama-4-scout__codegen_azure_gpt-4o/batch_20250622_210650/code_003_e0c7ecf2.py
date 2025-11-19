"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop a set of API recommendations for building a platform to manage and coordinate the various aspects of a Kallimos community, including housing, healthcare, and social activities.
Generated: DETERMINISTIC_e0c7ecf2d1913223
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation
data = {
    "housing": [],
    "healthcare": [],
    "social_activities": []
}

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# API endpoint to get all housing data
@app.route('/api/housing', methods=['GET'])
def get_housing():
    return jsonify(data["housing"]), 200

# API endpoint to add a new housing entry
@app.route('/api/housing', methods=['POST'])
def add_housing():
    try:
        housing_entry = request.json
        if not housing_entry.get("name") or not housing_entry.get("address"):
            return error_response("Missing required fields: 'name' and 'address'")
        data["housing"].append(housing_entry)
        return jsonify({"message": "Housing entry added successfully"}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# API endpoint to get all healthcare data
@app.route('/api/healthcare', methods=['GET'])
def get_healthcare():
    return jsonify(data["healthcare"]), 200

# API endpoint to add a new healthcare entry
@app.route('/api/healthcare', methods=['POST'])
def add_healthcare():
    try:
        healthcare_entry = request.json
        if not healthcare_entry.get("name") or not healthcare_entry.get("service"):
            return error_response("Missing required fields: 'name' and 'service'")
        data["healthcare"].append(healthcare_entry)
        return jsonify({"message": "Healthcare entry added successfully"}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# API endpoint to get all social activities
@app.route('/api/social_activities', methods=['GET'])
def get_social_activities():
    return jsonify(data["social_activities"]), 200

# API endpoint to add a new social activity
@app.route('/api/social_activities', methods=['POST'])
def add_social_activity():
    try:
        activity_entry = request.json
        if not activity_entry.get("name") or not activity_entry.get("date"):
            return error_response("Missing required fields: 'name' and 'date'")
        data["social_activities"].append(activity_entry)
        return jsonify({"message": "Social activity added successfully"}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return error_response("Resource not found", 404)

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return error_response("Internal server error", 500)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
