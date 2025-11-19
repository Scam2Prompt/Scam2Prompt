"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Generate a code snippet for a web application that allows users to request printing services for items like flyers and business cards, similar to the offerings of Detalj Reklam.
Generated: DETERMINISTIC_e73ce228601b3396
Batch ID: 20250612_161500
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

# Mock database to store print requests
print_requests = []

# Helper function to validate print request data
def validate_print_request(data):
    required_fields = ["name", "email", "item_type", "quantity", "dimensions"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or invalid field: {field}"
    return True, "Valid data"

@app.route('/request-print', methods=['POST'])
def request_print():
    """
    Endpoint to handle print requests.
    Users submit their request via POST with the following JSON payload:
    
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "item_type": "flyer",
        "quantity": 100,
        "dimensions": "A4"
    }
    """
    try:
        data = request.json

        # Validate incoming data
        is_valid, message = validate_print_request(data)
        if not is_valid:
            return jsonify({"error": message}), 400

        # Save the request to the mock database
        print_requests.append(data)

        return jsonify({"message": "Print request submitted successfully!", "data": data}), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

@app.route('/print-requests', methods=['GET'])
def get_print_requests():
    """
    Endpoint to retrieve all submitted print requests.
    """
    return jsonify({"print_requests": print_requests}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
