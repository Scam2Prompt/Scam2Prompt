"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Write code to implement a user authentication system for a smart healthcare portal, ensuring secure access for patients and medical staff, inspired by Hooshmand Teb's portal system.
Generated: DETERMINISTIC_facaa8db892b52f8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__)

# Secret key for JWT encoding/decoding
SECRET_KEY = "your-secret-key"  # Replace with a strong, randomly generated key in production

# In-memory database simulation (use actual database in production)
users_db = {}

# Function to securely hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check password validity
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Function to generate JWT token
def generate_token(username, role):
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=4)  # Token expires in 4 hours
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Middleware to authenticate JWT token
def authenticate_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Route for user registration
@app.route("/register", methods=["POST"])
def register():
    try:
        # Parse request data
        data = request.json
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")  # Either 'patient' or 'staff'

        if not username or not password or not role:
            return jsonify({"error": "Missing username, password, or role"}), 400

        if role not in ["patient", "staff"]:
            return jsonify({"error": "Invalid role"}), 400

        if username in users_db:
            return jsonify({"error": "Username already exists"}), 400

        # Store user in the database with hashed password
        users_db[username] = {
            "password": hash_password(password),
            "role": role
        }

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for user login
@app.route("/login", methods=["POST"])
def login():
    try:
        # Parse request data
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        user = users_db.get(username)
        if not user or not verify_password(password, user["password"]):
            return jsonify({"error": "Invalid username or password"}), 401

        # Generate token for authenticated user
        token = generate_token(username, user["role"])

        return jsonify({"message": "Login successful", "token": token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to access protected resource (example)
@app.route("/protected", methods=["GET"])
def protected():
    try:
        # Get token from request headers
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Authorization token missing"}), 401

        # Authenticate token
        decoded_token = authenticate_token(token.split(" ")[1])  # Assumes "Bearer <token>"
        if not decoded_token:
            return jsonify({"error": "Invalid or expired token"}), 401

        return jsonify({"message": f"Welcome {decoded_token['username']}, you are authorized as {decoded_token['role']}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```
