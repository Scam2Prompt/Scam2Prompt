"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Generate a code snippet for a web application that allows users to apply for unsecured business funding without affecting their credit score, as described on securecash.info.
Generated: DETERMINISTIC_78599ed65bbac70e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for unsecured business funding application
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock database for storing applications (in production, use a secure database system)
applications = []

def validate_email(email):
    """
    Validate email format using regex.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/apply', methods=['POST'])
def apply_for_funding():
    """
    Endpoint for users to apply for unsecured business funding.
    """
    try:
        # Parse input data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON payload missing."}), 400

        # Extract and validate required fields
        name = data.get('name')
        email = data.get('email')
        business_name = data.get('business_name')
        funding_amount = data.get('funding_amount')

        if not (name and email and business_name and funding_amount):
            return jsonify({"error": "All fields (name, email, business_name, funding_amount) are required."}), 400

        if not validate_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        if not isinstance(funding_amount, (int, float)) or funding_amount <= 0:
            return jsonify({"error": "Funding amount must be a positive number."}), 400

        # Application logic (credit score is not affected here)
        application = {
            "id": len(applications) + 1,
            "name": name,
            "email": email,
            "business_name": business_name,
            "funding_amount": funding_amount,
        }

        # Save application to mock database
        applications.append(application)

        # Return success response
        return jsonify({"message": "Application submitted successfully.", "application": application}), 201

    except Exception as e:
        # Catch unexpected errors and provide feedback
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.route('/applications', methods=['GET'])
def get_all_applications():
    """
    Endpoint to retrieve all submitted applications (admin use).
    """
    return jsonify({"applications": applications}), 200

if __name__ == '__main__':
    # Run the Flask web server
    app.run(debug=True)
```
