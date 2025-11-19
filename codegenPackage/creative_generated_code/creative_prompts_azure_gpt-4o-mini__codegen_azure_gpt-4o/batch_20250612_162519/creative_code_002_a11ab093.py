"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Can you provide code examples for creating a registration feature for a travel-related web application?
Generated: DETERMINISTIC_a11ab093e026fd3f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code written in Python using the Flask framework to create a registration feature for a travel-related web application. The code includes proper error handling, comments, and adheres to best practices.

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

# Mock database (use a real database such as SQLAlchemy in production)
users_db = {}

# Utility function: Validate email
def is_valid_email(email):
    """Validate the email format using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# Utility function: Validate password
def is_valid_password(password):
    """Check if the password meets complexity requirements."""
    return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)

# Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """
    Handle user registration requests.
    Expected JSON payload: {
        "username": "example_user",
        "email": "example@example.com",
        "password": "securepassword123"
    }
    """
    try:
        # Parse the JSON payload
        data = request.get_json()

        # Validate required fields
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"error": "All fields (username, email, password) are required."}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate password complexity
        if not is_valid_password(password):
            return jsonify({"error": "Password must be at least 8 characters long, contain letters and numbers."}), 400

        # Check if the username or email is already registered
        if email in users_db:
            return jsonify({"error": "Email is already registered."}), 409

        # Hash the password for storage
        hashed_password = generate_password_hash(password)

        # Store user in the database
        users_db[email] = {
            "username": username,
            "email": email,
            "password": hashed_password
        }

        # Return success response
        return jsonify({"message": "User registered successfully."}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

### Notes for Production Use:
- Replace the `users_db` dictionary with a proper database implementation (e.g., SQLAlchemy or another ORM).
- Use environment variables for sensitive information such as the Flask secret.
- Implement rate-limiting and CSRF protection for security.
- Disable `debug=True` in production environments.
