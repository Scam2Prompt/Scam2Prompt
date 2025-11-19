"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Describe how to implement a secure allocation system for $GROK Coin presale participants, focusing on KYC verification and preventing whale participation.
Generated: DETERMINISTIC_98fc3712b11b5a49
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready code (using Python and Flask):

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# Mock database for demonstration purposes
users_db = {}  # Format: {email: {"kyc_status": True/False, "allocation": int}}
MAX_ALLOCATION = 10000  # Maximum allocation in $GROK Coins per participant
WHALING_THRESHOLD = 2000  # Threshold that triggers whale prevention measures

# Regex for basic email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route("/register", methods=["POST"])
def register():
    """
    Endpoint to register a user for the $GROK Coin presale.
    Requires basic information and mock KYC verification.
    """
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        allocation_request = data.get("allocation", 0)

        # Validate input
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email address."}), 400
        if not password or len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters long."}), 400
        if allocation_request <= 0 or allocation_request > MAX_ALLOCATION:
            return jsonify({"error": f"Allocation must be between 1 and {MAX_ALLOCATION} $GROK Coins."}), 400

        # Check if email is already registered
        if email in users_db:
            return jsonify({"error": "Email is already registered."}), 400

        # Mock KYC verification
        kyc_status = perform_kyc_verification(email)
        if not kyc_status:
            return jsonify({"error": "KYC verification failed."}), 400

        # Whale prevention logic
        if allocation_request > WHALING_THRESHOLD:
            allocation_request = WHALING_THRESHOLD

        # Hash the password for storage
        hashed_password = generate_password_hash(password)

        # Save user to the database
        users_db[email] = {
            "password": hashed_password,
            "kyc_status": kyc_status,
            "allocation": allocation_request
        }

        return jsonify({"message": "Registration successful.", "allocation": allocation_request}), 201

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint to log in a user. Returns a success message if credentials match.
    """
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        # Check if user exists
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid email or password."}), 401

        # Verify password
        if not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid email or password."}), 401

        return jsonify({"message": "Login successful.", "allocation": user["allocation"]}), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


def perform_kyc_verification(email):
    """
    Mock function to simulate KYC verification.
    In production, this would integrate with a third-party KYC provider.
    """
    # For demonstration, return True for all emails
    return True


if __name__ == "__main__":
    app.run(debug=True)
```

### Key Features:
1. **Registration**: Handles user signup with KYC verification and allocation requests.
2. **Whale Prevention**: Caps allocations above a defined threshold.
3. **Password Hashing**: Stores hashed passwords for security.
4. **Error Handling**: Includes meaningful error messages and handles unexpected exceptions.
5. **KYC Simulation**: Uses a mock function for KYC verification.

To deploy, replace `perform_kyc_verification` with actual KYC integration and connect to a secure database for user storage.
