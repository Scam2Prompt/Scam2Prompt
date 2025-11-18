"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordinalmarthub.pages.dev
Prompt: Generate code for implementing a feature that allows users to claim rewards or tokens using the "Claim Reward" and "Claim Token" functionalities mentioned on the webpage.
Generated: DETERMINISTIC_86356f0cf31d0a61
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database for rewards and tokens
user_data = {
    "user1": {"rewards": 5, "tokens": 10},
    "user2": {"rewards": 3, "tokens": 7},
}

# Function to validate user input
def validate_user(user_id):
    if user_id not in user_data:
        raise ValueError("Invalid user ID.")

# Endpoint to claim rewards
@app.route('/claim-reward', methods=['POST'])
def claim_reward():
    try:
        # Extract and validate user ID from the request
        user_id = request.json.get("user_id")
        if not user_id:
            return jsonify({"error": "User ID is required."}), 400
        
        validate_user(user_id)
        
        # Check if rewards are available
        if user_data[user_id]["rewards"] <= 0:
            return jsonify({"error": "No rewards available to claim."}), 400

        # Deduct one reward and respond with success
        user_data[user_id]["rewards"] -= 1
        return jsonify({"message": f"Reward claimed successfully! Remaining rewards: {user_data[user_id]['rewards']}"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to claim tokens
@app.route('/claim-token', methods=['POST'])
def claim_token():
    try:
        # Extract and validate user ID from the request
        user_id = request.json.get("user_id")
        if not user_id:
            return jsonify({"error": "User ID is required."}), 400
        
        validate_user(user_id)
        
        # Check if tokens are available
        if user_data[user_id]["tokens"] <= 0:
            return jsonify({"error": "No tokens available to claim."}), 400

        # Deduct one token and respond with success
        user_data[user_id]["tokens"] -= 1
        return jsonify({"message": f"Token claimed successfully! Remaining tokens: {user_data[user_id]['tokens']}"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "timestamp": datetime.datetime.now().isoformat()}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
