"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Generate a code snippet for a web application that allows users to sign up for folk dance classes in Nürnberg and Erlangen, focusing on Turkish folk dances.
Generated: DETERMINISTIC_a88bdf46500bcac3
Batch ID: 20250612_160302
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

# In-memory database for simplicity (use a real database in production)
dance_classes = [
    {"id": 1, "location": "Nürnberg", "dance_type": "Turkish Folk Dance"},
    {"id": 2, "location": "Erlangen", "dance_type": "Turkish Folk Dance"}
]

registrations = []  # Store user registrations

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Endpoint to list available dance classes
@app.route('/classes', methods=['GET'])
def get_classes():
    """
    Get a list of available dance classes.
    """
    return jsonify(dance_classes), 200

# Endpoint to register for a dance class
@app.route('/register', methods=['POST'])
def register():
    """
    Register a user for a dance class.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "class_id": 1
    }
    """
    try:
        data = request.get_json()
        # Validate input
        if not data or 'name' not in data or 'email' not in data or 'class_id' not in data:
            return jsonify({"error": "Invalid input. 'name', 'email', and 'class_id' are required."}), 400

        # Check if class exists
        dance_class = next((cls for cls in dance_classes if cls['id'] == data['class_id']), None)
        if not dance_class:
            return jsonify({"error": "Dance class not found."}), 404

        # Register user
        registration = {
            "id": len(registrations) + 1,
            "name": data['name'],
            "email": data['email'],
            "class_id": data['class_id']
        }
        registrations.append(registration)

        return jsonify({"message": "Registration successful.", "registration": registration}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Endpoint to list all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    Get a list of all registrations.
    """
    return jsonify(registrations), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
