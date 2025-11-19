"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Create a simple API endpoint in Python for user registration that includes input validation, similar to the registration process on diverbox.com.pe.
Generated: DETERMINISTIC_f717b854662519fe
Batch ID: 20250612_163408
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

# Helper function to validate email format
def is_valid_email(email):
    # Regular expression to match valid email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Helper function to validate password strength
def is_valid_password(password):
    # Password must be at least 8 characters, contain at least one number, one uppercase letter, and one symbol
    password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_regex, password) is not None

@app.route('/register', methods=['POST'])
def register_user():
    """
    API endpoint for user registration.
    Accepts JSON input with 'username', 'email', and 'password' fields.
    Validates input and returns appropriate response.
    """
    try:
        # Get JSON data from request
        data = request.json

        # Input validation
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        # Check for missing fields
        if not username or not email or not password:
            return jsonify({"error": "All fields (username, email, password) are required."}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate password strength
        if not is_valid_password(password):
            return jsonify({
                "error": "Password must be at least 8 characters long, include one uppercase letter, one number, and one special character."
            }), 400

        # Simulate user registration success (e.g., save to database)
        # In a real application, you would interact with a database here
        return jsonify({"message": "User registered successfully!"}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
