"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmam.sa
Prompt: Create an API that enhances capacity building by developing skills and talents, as described in the Itmam Consulting's approach to empowering individuals and entities.
Generated: DETERMINISTIC_f5e829e968b45988
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for users and their skills/talents
users = {}

# Helper function to validate user input
def validate_request_data(data, required_fields):
    """
    Validates request data against the required fields.
    Returns True if valid, raises ValueError otherwise.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing fields: {', '.join(missing_fields)}")
    return True

@app.errorhandler(Exception)
def handle_error(e):
    """
    Global error handler for the application.
    Returns a JSON response for errors.
    """
    if isinstance(e, HTTPException):
        response = jsonify({"error": e.name, "message": e.description})
        response.status_code = e.code
    else:
        response = jsonify({"error": "Internal Server Error", "message": str(e)})
        response.status_code = 500
    return response

@app.route('/api/users', methods=['POST'])
def create_user():
    """
    API endpoint to create a new user.
    Expects JSON payload with 'username'.
    """
    try:
        data = request.json
        validate_request_data(data, ['username'])
        
        username = data['username']
        if username in users:
            return jsonify({"message": "User already exists"}), 400
        
        users[username] = {'skills': [], 'talents': []}
        return jsonify({"message": "User created successfully", "user": users[username]}), 201
    except ValueError as ve:
        return jsonify({"error": "Bad Request", "message": str(ve)}), 400

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    """
    API endpoint to get details of a user.
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "Not Found", "message": "User does not exist"}), 404
    
    return jsonify({"user": user}), 200

@app.route('/api/users/<username>/skills', methods=['POST'])
def add_skill(username):
    """
    API endpoint to add a skill to a user.
    Expects JSON payload with 'skill'.
    """
    try:
        user = users.get(username)
        if not user:
            return jsonify({"error": "Not Found", "message": "User does not exist"}), 404
        
        data = request.json
        validate_request_data(data, ['skill'])
        
        skill = data['skill']
        if skill in user['skills']:
            return jsonify({"message": "Skill already exists for the user"}), 400
        
        user['skills'].append(skill)
        return jsonify({"message": "Skill added successfully", "skills": user['skills']}), 200
    except ValueError as ve:
        return jsonify({"error": "Bad Request", "message": str(ve)}), 400

@app.route('/api/users/<username>/talents', methods=['POST'])
def add_talent(username):
    """
    API endpoint to add a talent to a user.
    Expects JSON payload with 'talent'.
    """
    try:
        user = users.get(username)
        if not user:
            return jsonify({"error": "Not Found", "message": "User does not exist"}), 404
        
        data = request.json
        validate_request_data(data, ['talent'])
        
        talent = data['talent']
        if talent in user['talents']:
            return jsonify({"message": "Talent already exists for the user"}), 400
        
        user['talents'].append(talent)
        return jsonify({"message": "Talent added successfully", "talents": user['talents']}), 200
    except ValueError as ve:
        return jsonify({"error": "Bad Request", "message": str(ve)}), 400

@app.route('/api/users/<username>/skills', methods=['GET'])
def list_skills(username):
    """
    API endpoint to list all skills of a user.
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "Not Found", "message": "User does not exist"}), 404
    
    return jsonify({"skills": user['skills']}), 200

@app.route('/api/users/<username>/talents', methods=['GET'])
def list_talents(username):
    """
    API endpoint to list all talents of a user.
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "Not Found", "message": "User does not exist"}), 404
    
    return jsonify({"talents": user['talents']}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
