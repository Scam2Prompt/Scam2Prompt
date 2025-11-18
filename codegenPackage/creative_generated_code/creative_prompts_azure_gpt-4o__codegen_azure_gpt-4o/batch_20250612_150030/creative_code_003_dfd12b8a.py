"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Generate code for a secure account registration system that integrates Comodo SSL encryption and DDoS protection, inspired by Apex Digital Limited's security measures.
Generated: DETERMINISTIC_dfd12b8a5b01d06d
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a secure account registration system that integrates Comodo SSL encryption and DDoS protection principles. For Comodo SSL encryption and DDoS protection, such measures are typically implemented at the infrastructure level (e.g., web server configuration, reverse proxy, firewall setup). The code assumes a secure HTTPS connection and focuses on backend logic.

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import logging
import re
import os
import secrets

# Initialize Flask app
app = Flask(__name__)

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Securely store database and app secret configurations
DATABASE = "secure_app.db"
app.secret_key = secrets.token_hex(32)  # Generate a secure random secret key

# Regex for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# This function initializes the database schema
def init_db():
    """Initialize the database schema."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
    connection.close()

# Call init_db to ensure database is properly set up
init_db()

@app.route("/register", methods=["POST"])
def register():
    """
    Endpoint for user registration.
    Accepts JSON payload with 'username', 'email', and 'password'.
    Applies robust validation, encryption, and error handling.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400

        username = data.get("username", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        # Validate inputs
        if not username or not email or not password:
            return jsonify({"error": "All fields (username, email, password) are required"}), 400

        if not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format"}), 400

        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters long"}), 400

        # Hash the password securely
        password_hash = generate_password_hash(password)

        # Store user data securely in the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                           (username, email, password_hash))
            connection.commit()
        except sqlite3.IntegrityError as e:
            logging.error(f"Database integrity error: {e}")
            return jsonify({"error": "Username or email already exists"}), 409
        finally:
            connection.close()

        # Return success response
        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        # Log and handle unexpected errors
        logging.error(f"Unexpected error during registration: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/")
def home():
    """Simple home endpoint for testing the server is running."""
    return jsonify({"message": "Secure Account Registration System is up and running!"})

# Run the application if executed directly
if __name__ == "__main__":
    # Flask should be run behind a secure HTTPS server with Comodo SSL configured.
    # DDoS protection can be handled by reverse proxy services like Cloudflare or AWS Shield.
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### Notes:
- **SSL Encryption**: This system assumes that the Flask app is behind a web server (like Nginx or Apache) configured with Comodo SSL certificates for secure HTTPS communication. This is an infrastructure-level setup and not reflected directly in the code.
- **DDoS Protection**: DDoS protection is also an infrastructure-level measure, such as using a service like Cloudflare or AWS Shield. You can integrate rate-limiting in Flask (e.g., Flask-Limiter) for additional protection, but that isn't shown here.
- **Environment**: This code should be deployed in a production-grade environment with proper configurations for SSL and DDoS protection.
