"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Create a registration system for a Hajj portal that includes user account creation with email and password validation.
Generated: DETERMINISTIC_eb94e05d0e054bb4
Batch ID: 20250612_145213
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
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# In-memory database to store user details (for demonstration purposes)
# In a production system, use a proper database like PostgreSQL, MySQL, etc.
user_db = {}

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Password validation rules
MIN_PASSWORD_LENGTH = 8
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'  # At least 1 letter, 1 number, and 8 characters

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user with email and password validation.
    """
    try:
        # Parse JSON input
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format"}), 400
        if not password or len(password) < MIN_PASSWORD_LENGTH or not re.match(PASSWORD_REGEX, password):
            return jsonify({
                "error": "Password must be at least 8 characters long, contain at least one letter and one number."
            }), 400
        if email in user_db:
            return jsonify({"error": "Email is already registered"}), 400

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Store user details in the database
        user_db[email] = {"email": email, "password": hashed_password}

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": "An error occurred during registration", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    # For production, use a WSGI server like Gunicorn instead of Flask's built-in server
    app.run(debug=True)
```
