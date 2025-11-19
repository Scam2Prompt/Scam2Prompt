"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Create an API endpoint for user registration that includes bonus incentives, reflecting the quick sign-up process mentioned on the BaxBet site.
Generated: DETERMINISTIC_3ce1a59303982e1a
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data storage (for demonstration purposes; replace with a database in production)
users = {}

# Function to calculate bonus incentive
def calculate_bonus():
    return 50  # Fixed bonus amount for quick sign-ups (customize as needed)

# Helper function to validate input data
def validate_registration_data(data):
    required_fields = ['username', 'password', 'email']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty field: {field}"
    return True, None

@app.route('/api/register', methods=['POST'])
def register_user():
    """
    API endpoint for user registration.
    ---
    Request Format:
    {
        "username": "example_user",
        "password": "secure_password",
        "email": "user@example.com"
    }
    Response Format:
    Success:
    {
        "status": "success",
        "message": "User registered successfully.",
        "user_id": "<generated_user_id>",
        "bonus": <bonus_amount>
    }
    Error:
    {
        "status": "error",
        "message": "<error_message>"
    }
    """
    try:
        # Parse request data
        data = request.json

        # Validate input data
        is_valid, error_message = validate_registration_data(data)
        if not is_valid:
            return jsonify({"status": "error", "message": error_message}), 400

        # Generate unique user ID
        user_id = str(uuid.uuid4())

        # Calculate bonus incentive
        bonus = calculate_bonus()

        # Store user in the database (in-memory for demonstration)
        users[user_id] = {
            "username": data['username'],
            "password": data['password'],  # NOTE: Hash passwords in production
            "email": data['email'],
            "bonus": bonus
        }

        # Respond with success message and bonus incentive
        return jsonify({
            "status": "success",
            "message": "User registered successfully.",
            "user_id": user_id,
            "bonus": bonus
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
