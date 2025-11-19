"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: What are the best practices for handling user registrations and prize claims in a web application, based on the process outlined on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_aeabd050d43bd550
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready code implementation for handling user registrations and prize claims in a web application using Python's Flask framework.

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# In-memory database (replace with an actual database in production)
users_db = {}
prizes_db = {}

# User registration endpoint
@app.route("/register", methods=["POST"])
def register_user():
    """
    Endpoint to handle user registration.
    Expects JSON payload with 'username', 'email', and 'password'.
    """
    try:
        data = request.json
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Validate input
        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        if email in users_db:
            return jsonify({"error": "Email already registered"}), 409

        # Generate hashed password for security
        hashed_password = generate_password_hash(password)

        # Store user info in the database
        user_id = str(uuid.uuid4())
        users_db[email] = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "password": hashed_password,
        }

        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


# Prize claim endpoint
@app.route("/claim-prize", methods=["POST"])
def claim_prize():
    """
    Endpoint to handle prize claims.
    Expects JSON payload with 'email' and 'prize_code'.
    """
    try:
        data = request.json
        email = data.get("email")
        prize_code = data.get("prize_code")

        # Validate input
        if not email or not prize_code:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if user exists
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Check if prize code has already been claimed
        if prize_code in prizes_db:
            return jsonify({"error": "Prize already claimed"}), 409

        # Store prize claim in the database
        prizes_db[prize_code] = {
            "user_id": user["user_id"],
            "email": email,
            "prize_code": prize_code,
        }

        return jsonify({"message": "Prize claimed successfully", "prize_code": prize_code}), 200
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes on Best Practices
- **Password Hashing**: Always hash passwords before storing them. In this code, `generate_password_hash` is used from `werkzeug.security`.
- **Input Validation**: Ensure all required fields are provided and properly validate them.
- **Error Handling**: Include error handling for unexpected issues.
- **UUID**: Use UUIDs for unique user IDs to avoid predictable sequences.
- **In-Memory Storage**: Replace `users_db` and `prizes_db` with a robust database in production (e.g., PostgreSQL, MySQL).
- **HTTP Status Codes**: Use appropriate HTTP status codes for responses (e.g., 201 for creation, 400 for bad requests, etc.).
- **Security**: This is a basic example; implement further security measures (e.g., rate limiting, input sanitization) for production-grade applications.
