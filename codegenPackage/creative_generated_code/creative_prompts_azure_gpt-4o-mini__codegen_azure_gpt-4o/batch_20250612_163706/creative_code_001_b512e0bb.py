"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Write a Python script to create a social-first network platform that facilitates real connections among founders and freelancers, inspired by Sync Connects.
Generated: DETERMINISTIC_b512e0bba32d390f
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store users and connections
# In a production environment, this would be replaced by a real database
users_db = {}
connections_db = {}

# Helper: Generate unique user ID (UUID would be ideal for production)
def generate_user_id():
    return f"user_{int(datetime.utcnow().timestamp() * 1000)}"

# Endpoint: Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Check for duplicate email
        if email in [user['email'] for user in users_db.values()]:
            return jsonify({"error": "Email already exists"}), 400

        # Create new user
        user_id = generate_user_id()
        users_db[user_id] = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "created_at": datetime.utcnow().isoformat()
        }

        return jsonify({"message": "User registered successfully", "user": users_db[user_id]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Create a connection between two users
@app.route('/connect', methods=['POST'])
def create_connection():
    try:
        data = request.get_json()
        user_id_1 = data.get('user_id_1')
        user_id_2 = data.get('user_id_2')

        if not user_id_1 or not user_id_2:
            return jsonify({"error": "Both user IDs are required"}), 400

        if user_id_1 not in users_db or user_id_2 not in users_db:
            return jsonify({"error": "One or both user IDs not found"}), 404

        # Check if connection already exists
        connection_id = f"{user_id_1}_{user_id_2}"
        if connection_id in connections_db:
            return jsonify({"error": "Connection already exists"}), 400

        # Create connection
        connections_db[connection_id] = {
            "connection_id": connection_id,
            "user_id_1": user_id_1,
            "user_id_2": user_id_2,
            "created_at": datetime.utcnow().isoformat()
        }

        return jsonify({"message": "Connection created successfully", "connection": connections_db[connection_id]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        return jsonify({"users": list(users_db.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get all connections
@app.route('/connections', methods=['GET'])
def get_connections():
    try:
        return jsonify({"connections": list(connections_db.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to start the Flask server
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production for better performance and security
```
