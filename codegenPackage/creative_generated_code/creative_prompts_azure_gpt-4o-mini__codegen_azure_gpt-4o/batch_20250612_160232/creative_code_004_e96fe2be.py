"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tata-cryptoapp.com
Prompt: Illustrate how to implement a personalized mentoring program using an API that matches users with investment education providers, similar to the services offered by Tata Crypto.
Generated: DETERMINISTIC_e96fe2be39061e20
Batch ID: 20250612_160232
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

# In-memory database to store users and mentors
users_db = {}
mentors_db = {
    "mentor1": {"name": "Alice", "expertise": "Cryptocurrency Basics", "availability": "Monday-Friday"},
    "mentor2": {"name": "Bob", "expertise": "Advanced Crypto Trading", "availability": "Weekends"},
    "mentor3": {"name": "Charlie", "expertise": "Blockchain Development", "availability": "Monday-Wednesday"},
}

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/register_user', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects a JSON payload with 'name' and 'learning_goal'.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        learning_goal = data.get('learning_goal')
        
        if not name or not learning_goal:
            return error_response("Both 'name' and 'learning_goal' are required fields.")

        user_id = str(uuid.uuid4())  # Generate a unique user ID
        users_db[user_id] = {"name": name, "learning_goal": learning_goal}
        
        return jsonify({"message": "User registered successfully!", "user_id": user_id}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

@app.route('/match_mentor/<user_id>', methods=['GET'])
def match_mentor(user_id):
    """
    Endpoint to match a user with a mentor based on learning goals.
    """
    try:
        user = users_db.get(user_id)
        if not user:
            return error_response("User not found.", 404)
        
        learning_goal = user["learning_goal"]
        matched_mentors = [
            mentor for mentor in mentors_db.values()
            if learning_goal.lower() in mentor["expertise"].lower()
        ]
        
        if not matched_mentors:
            return jsonify({"message": "No suitable mentors found for your learning goal."}), 404
        
        return jsonify({"user": user, "matched_mentors": matched_mentors}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

@app.route('/mentors', methods=['GET'])
def list_mentors():
    """
    Endpoint to list all available mentors.
    """
    try:
        return jsonify({"mentors": mentors_db}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

@app.route('/users', methods=['GET'])
def list_users():
    """
    Endpoint to list all registered users.
    """
    try:
        return jsonify({"users": users_db}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
