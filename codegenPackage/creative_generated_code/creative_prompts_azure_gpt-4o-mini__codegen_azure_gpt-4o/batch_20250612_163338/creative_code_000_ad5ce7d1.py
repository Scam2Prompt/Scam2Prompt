"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Generate a code snippet for a web application that allows users to submit inquiries about traditional building restoration services offered by Inaka Revive Solutions.
Generated: DETERMINISTIC_ad5ce7d1e3f6b942
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Simulated database for storing inquiries
inquiry_database = []

# Helper function to validate email
def is_valid_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to handle user inquiries submission about traditional building restoration services.
    """
    try:
        # Parse JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400

        # Extract and validate required fields
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "Missing required fields: name, email, message"}), 400
        
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Store the inquiry in the simulated database
        inquiry_database.append({
            "name": name,
            "email": email,
            "message": message
        })

        # Respond with confirmation
        return jsonify({"message": "Inquiry submitted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred. Please try again later", "details": str(e)}), 500

@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """
    Endpoint to retrieve all submitted inquiries (for administrative purposes).
    """
    # Return all submitted inquiries
    return jsonify(inquiry_database), 200

if __name__ == '__main__':
    # Run the Flask application on localhost with debugging disabled for production-ready code
    app.run(host='0.0.0.0', port=5000, debug=False)
```
