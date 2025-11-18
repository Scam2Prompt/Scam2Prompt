"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idcmu.com
Prompt: Develop a backend system for managing VIP user privileges and investments on a cryptocurrency platform, inspired by the VIP section of idcmu.com.
Generated: DETERMINISTIC_04b41cbd4b7b5d6f
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# backend_system.py

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import logging
import json

# Initialize Flask app
app = Flask(__name__)

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# In-memory database (for demonstration purposes)
# In production, use a robust database like PostgreSQL or MongoDB
DATABASE = {
    "users": [],  # List to store VIP user data
    "investments": []  # List to store investment data
}

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    logger.error(f"HTTP error occurred: {e.description}")
    return jsonify({"error": e.description}), e.code

# Error handling for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    logger.error(f"An unexpected error occurred: {str(e)}")
    return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to add a new VIP user
@app.route('/vip/users', methods=['POST'])
def add_vip_user():
    try:
        data = request.json
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid user data"}), 400
        
        # Create new user with default privileges
        new_user = {
            "id": len(DATABASE["users"]) + 1,
            "username": data["username"],
            "email": data["email"],
            "privileges": data.get("privileges", []),
            "created_at": data.get("created_at", json.dumps(data))
        }
        DATABASE["users"].append(new_user)
        logger.info(f"VIP user added: {new_user['username']}")
        return jsonify({"message": "VIP user added successfully", "user": new_user}), 201

    except Exception as e:
        logger.error(f"Error adding VIP user: {str(e)}")
        return jsonify({"error": "Failed to add VIP user"}), 500

# Endpoint to add an investment for a VIP user
@app.route('/vip/investments', methods=['POST'])
def add_investment():
    try:
        data = request.json
        if not data or 'user_id' not in data or 'amount' not in data:
            return jsonify({"error": "Invalid investment data"}), 400
        
        # Check if user exists
        user = next((u for u in DATABASE["users"] if u["id"] == data["user_id"]), None)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Create new investment record
        new_investment = {
            "id": len(DATABASE["investments"]) + 1,
            "user_id": data["user_id"],
            "amount": data["amount"],
            "currency": data.get("currency", "USD"),
            "created_at": data.get("created_at", "N/A"),
        }
        DATABASE["investments"].append(new_investment)
        logger.info(f"Investment added for user {data['user_id']}: {new_investment}")
        return jsonify({"message": "Investment added successfully", "investment": new_investment}), 201

    except Exception as e:
        logger.error(f"Error adding investment: {str(e)}")
        return jsonify({"error": "Failed to add investment"}), 500

# Endpoint to fetch all VIP users
@app.route('/vip/users', methods=['GET'])
def get_all_vip_users():
    try:
        return jsonify({"users": DATABASE["users"]}), 200
    except Exception as e:
        logger.error(f"Error fetching VIP users: {str(e)}")
        return jsonify({"error": "Failed to fetch VIP users"}), 500

# Endpoint to fetch all investments for a specific VIP user
@app.route('/vip/investments/<int:user_id>', methods=['GET'])
def get_investments_by_user(user_id):
    try:
        # Filter investments for the given user_id
        user_investments = [i for i in DATABASE["investments"] if i["user_id"] == user_id]
        return jsonify({"investments": user_investments}), 200
    except Exception as e:
        logger.error(f"Error fetching investments for user {user_id}: {str(e)}")
        return jsonify({"error": "Failed to fetch investments"}), 500

# Main entry point to run the Flask server
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development; disable in production
```
