"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clarkconstructionllc.net
Prompt: Generate a code snippet for a web application that allows users to request a free estimate for home remodeling services, similar to the offerings of Clark Construction LLC.
Generated: DETERMINISTIC_ed05b2ed84da3ce0
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py
# Description: Web application for requesting free estimates for home remodeling services

from flask import Flask, request, jsonify

app = Flask(__name__)

# Error messages
INVALID_INPUT_ERROR = "Invalid input. Please provide all required fields."

# In-memory storage for demonstration purposes (use a proper database in production)
estimates = []

@app.route('/request-estimate', methods=['POST'])
def request_estimate():
    """
    Handles requests for free home remodeling estimates.
    Expects JSON input with keys: name, email, phone, and details.
    Example input:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "details": "Kitchen remodeling project"
    }
    """
    try:
        # Parse input JSON
        data = request.get_json()
        if not data:
            return jsonify({'error': INVALID_INPUT_ERROR}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'details']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f"{field.capitalize()} is required."}), 400

        # Add estimate request to storage
        estimate_request = {
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'details': data['details'],
        }
        estimates.append(estimate_request)

        # Return success response
        return jsonify({'message': 'Estimate request submitted successfully!', 'data': estimate_request}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({'error': str(e)}), 500


@app.route('/get-estimates', methods=['GET'])
def get_estimates():
    """
    Endpoint to retrieve all submitted estimate requests.
    Returns all the records stored in the estimates list.
    """
    return jsonify({'estimates': estimates}), 200


if __name__ == '__main__':
    # Start the development server
    app.run(debug=True)
```

### Notes:
- Install Flask before running this code: `pip install flask`
- Run the server: `python app.py`
- Test the endpoints:
  - `POST /request-estimate` with JSON body to submit requests.
  - `GET /get-estimates` to retrieve all submitted requests.
- Replace the in-memory storage (`estimates`) with a proper database (e.g., PostgreSQL, MySQL) for production use.
