"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Create a registration system for new users, ensuring it includes validation for required fields, as seen on the Diverbox website.
Generated: DETERMINISTIC_bec9781a25e9ab04
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code for a user registration system, implemented in Python using Flask for a web application:

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import re

# Initialize Flask app
app = Flask(__name__)

# In-memory storage (use a database in production)
users = []

# Function to validate email using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate password strength
def is_valid_password(password):
    # Password must be at least 8 characters, contain uppercase, lowercase, and a number
    return len(password) >= 8 and \
           any(char.isdigit() for char in password) and \
           any(char.isupper() for char in password) and \
           any(char.islower() for char in password)

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expected JSON format:
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    """
    try:
        # Parse JSON request
        data = request.json

        # Validate required fields
        if not data or 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        username = data['username']
        email = data['email']
        password = data['password']

        # Validate username
        if len(username) < 3:
            return jsonify({"error": "Username must be at least 3 characters"}), 400
        
        # Validate email
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate password
        if not is_valid_password(password):
            return jsonify({
                "error": "Password must be at least 8 characters long, "
                         "contain an uppercase letter, a lowercase letter, and a number"
            }), 400

        # Check if email is already registered
        if any(user['email'] == email for user in users):
            return jsonify({"error": "Email is already registered"}), 400

        # Hash the password for storage (do not store plaintext passwords)
        hashed_password = generate_password_hash(password)

        # Save the user
        users.append({
            "username": username,
            "email": email,
            "password": hashed_password
        })

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred during registration", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**Notes:**
- Replace the in-memory `users` list with a proper database in production.
- Use HTTPS for secure communication.
- Consider adding rate-limiting and captcha for security against automated abuse.
- Ensure proper logging and monitoring in a production environment.
