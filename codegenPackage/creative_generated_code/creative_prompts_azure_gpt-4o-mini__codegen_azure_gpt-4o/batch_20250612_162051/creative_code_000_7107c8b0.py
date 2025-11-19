"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-pressure cleaning and disinfection services for poultry buildings in Aire sur l’Adour.
Generated: DETERMINISTIC_7107c8b0b2ac0913
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# Endpoint to handle quote requests
@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for high-pressure cleaning and disinfection services.
    Expects a JSON payload with name, email, phone, and message.
    """
    try:
        # Parse incoming JSON payload
        data = request.get_json()
        
        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        
        if not all([name, email, phone, message]):
            return jsonify({"error": "All fields (name, email, phone, message) are required."}), 400
        
        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400
        
        # Validate phone number (basic validation for numeric format)
        if not phone.isdigit():
            return jsonify({"error": "Phone number must be numeric."}), 400
        
        # Simulate storing the request (e.g., save to a database or send an email)
        # For now, we'll just return a success message
        quote_request = {
            "name": name,
            "email": email,
            "phone": phone,
            "message": message,
            "location": "Aire sur l’Adour"
        }
        # In production, you would save this data to a database or forward it to an email processor
        
        return jsonify({"success": "Your quote request has been submitted successfully!", "details": quote_request}), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
