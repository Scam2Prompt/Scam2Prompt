"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Create a REST API endpoint for Amir International Charity Organization that allows users to submit donations and specify the program they want to support (e.g., nutritional support, education assistance).
Generated: DETERMINISTIC_e927091cc47b4099
Batch ID: 20250612_152827
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

# In-memory storage for donated data (for simplicity; in production, use a database)
donations = []

# Supported charity programs
SUPPORTED_PROGRAMS = {"nutritional_support", "education_assistance"}

@app.route('/donate', methods=['POST'])
def donate():
    """
    REST API endpoint to submit donations.
    Expects JSON payload with 'name', 'email', 'amount', and 'program'.
    """
    try:
        # Validate request data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request payload. JSON data required."}), 400
        
        name = data.get('name')
        email = data.get('email')
        amount = data.get('amount')
        program = data.get('program')

        # Validate fields
        if not name or not email or not amount or not program:
            return jsonify({"error": "Missing required fields: name, email, amount, program."}), 400
        
        # Validate email format
        if "@" not in email or "." not in email:
            return jsonify({"error": "Invalid email format."}), 400
        
        # Validate donation amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Donation amount must be a positive number."}), 400
        
        # Validate program
        if program not in SUPPORTED_PROGRAMS:
            return jsonify({"error": f"Unsupported program. Supported programs are: {', '.join(SUPPORTED_PROGRAMS)}"}), 400

        # Add donation to the in-memory database
        donation_entry = {
            "name": name,
            "email": email,
            "amount": amount,
            "program": program
        }
        donations.append(donation_entry)

        # Return success response
        return jsonify({"message": "Donation submitted successfully.", "donation": donation_entry}), 201

    except Exception as e:
        # Log and handle unexpected errors
        return jsonify({"error": str(e), "message": "An unexpected error occurred."}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    return jsonify({"error": e.name, "message": e.description}), e.code

@app.errorhandler(404)
def handle_not_found(e):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Not Found", "message": "The requested resource could not be found."}), 404

@app.errorhandler(500)
def handle_internal_error(e):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
