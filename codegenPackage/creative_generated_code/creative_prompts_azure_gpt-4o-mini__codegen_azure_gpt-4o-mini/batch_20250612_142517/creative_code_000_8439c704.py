"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: How can I implement a web3 rewarded ads platform similar to Everyworld that allows users to earn points and enter drawings for environmental charities?
Generated: DETERMINISTIC_8439c7043fd24d59
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from web3 import Web3
import json
import os

app = Flask(__name__)

# Initialize Web3
infura_url = os.getenv("INFURA_URL")  # Infura URL from environment variable
web3 = Web3(Web3.HTTPProvider(infura_url))

# Load smart contract ABI
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

# Smart contract address (replace with your contract address)
contract_address = os.getenv("CONTRACT_ADDRESS")
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# In-memory storage for user points (consider using a database for production)
user_points = {}

@app.route('/earn_points', methods=['POST'])
def earn_points():
    """
    Endpoint to allow users to earn points for watching ads.
    Expects JSON body with user_id and points.
    """
    try:
        data = request.get_json()
        user_id = data['user_id']
        points = data['points']

        # Validate input
        if points <= 0:
            return jsonify({"error": "Points must be greater than zero."}), 400

        # Update user points
        if user_id not in user_points:
            user_points[user_id] = 0
        user_points[user_id] += points

        return jsonify({"message": f"Earning {points} points successful.", "total_points": user_points[user_id]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/draw_entry', methods=['POST'])
def draw_entry():
    """
    Endpoint for users to enter a drawing for environmental charities.
    Expects JSON body with user_id.
    """
    try:
        data = request.get_json()
        user_id = data['user_id']

        # Check if user has enough points to enter the drawing
        if user_id not in user_points or user_points[user_id] < 10:
            return jsonify({"error": "Not enough points to enter the drawing."}), 400

        # Deduct points and process drawing logic (placeholder)
        user_points[user_id] -= 10

        # Here, you'd implement your drawing logic
        # For example, adding the user to a drawing list
        # ...

        return jsonify({"message": "Successfully entered the drawing.", "remaining_points": user_points[user_id]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/points', methods=['GET'])
def get_points():
    """
    Endpoint to retrieve the points of a user.
    Expects query parameter user_id.
    """
    user_id = request.args.get('user_id')

    if user_id not in user_points:
        return jsonify({"error": "User not found."}), 404

    return jsonify({"user_id": user_id, "points": user_points[user_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Note:** 
- Ensure to set up your environment variables (`INFURA_URL` and `CONTRACT_ADDRESS`).
- Consider a proper database solution for production instead of in-memory storage.
- Replace the drawing logic with actual implementation as needed.
- Don't forget to handle sensitive data and add authentication mechanisms in production.
