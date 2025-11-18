"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Suggest APIs or tools to create a mobile app for renters and homeowners to manage insurance plans, inspired by the features highlighted on the Recuperación JC website.
Generated: DETERMINISTIC_c2e1fb15971f4e15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python code snippet that uses Flask to create a RESTful API for a mobile app that allows renters and homeowners to manage insurance plans. It integrates features inspired by the Recuperación JC website. This example includes endpoints for user authentication, viewing insurance plans, and managing claims.

```python
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# Mock Database
users_db = {}
insurance_plans_db = {}
claims_db = {}

# Error handling middleware
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal server error"), 500

# Utility functions
def validate_user_input(data, required_fields):
    """
    Validates user input against required fields.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user. Requires 'username' and 'password'.
    """
    data = request.get_json()
    is_valid, error = validate_user_input(data, ['username', 'password'])
    if not is_valid:
        return jsonify(error=error), 400

    username = data['username']
    password = data['password']

    if username in users_db:
        return jsonify(error="Username already exists"), 400

    users_db[username] = {
        'id': str(uuid.uuid4()),
        'username': username,
        'password_hash': generate_password_hash(password)
    }
    return jsonify(message="User registered successfully"), 201

@app.route('/login', methods=['POST'])
def login_user():
    """
    Log in a user. Requires 'username' and 'password'.
    """
    data = request.get_json()
    is_valid, error = validate_user_input(data, ['username', 'password'])
    if not is_valid:
        return jsonify(error=error), 400

    username = data['username']
    password = data['password']

    user = users_db.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify(error="Invalid credentials"), 401

    return jsonify(message="Login successful", user_id=user['id']), 200

@app.route('/insurance-plans', methods=['GET'])
def get_insurance_plans():
    """
    Retrieve all insurance plans.
    """
    return jsonify(insurance_plans=insurance_plans_db), 200

@app.route('/insurance-plans', methods=['POST'])
def add_insurance_plan():
    """
    Add a new insurance plan. Requires 'name', 'coverage', and 'price'.
    """
    data = request.get_json()
    is_valid, error = validate_user_input(data, ['name', 'coverage', 'price'])
    if not is_valid:
        return jsonify(error=error), 400

    plan_id = str(uuid.uuid4())
    insurance_plans_db[plan_id] = {
        'id': plan_id,
        'name': data['name'],
        'coverage': data['coverage'],
        'price': data['price']
    }
    return jsonify(message="Insurance plan added successfully", plan_id=plan_id), 201

@app.route('/claims', methods=['POST'])
def file_claim():
    """
    File a new insurance claim. Requires 'user_id', 'plan_id', and 'description'.
    """
    data = request.get_json()
    is_valid, error = validate_user_input(data, ['user_id', 'plan_id', 'description'])
    if not is_valid:
        return jsonify(error=error), 400

    user_id = data['user_id']
    plan_id = data['plan_id']
    description = data['description']

    if user_id not in [user['id'] for user in users_db.values()]:
        return jsonify(error="Invalid user ID"), 400

    if plan_id not in insurance_plans_db:
        return jsonify(error="Invalid insurance plan ID"), 400

    claim_id = str(uuid.uuid4())
    claims_db[claim_id] = {
        'id': claim_id,
        'user_id': user_id,
        'plan_id': plan_id,
        'description': description,
        'status': 'Pending'
    }
    return jsonify(message="Claim filed successfully", claim_id=claim_id), 201

@app.route('/claims/<claim_id>', methods=['GET'])
def get_claim_status(claim_id):
    """
    Retrieve the status of a specific claim.
    """
    claim = claims_db.get(claim_id)
    if not claim:
        return jsonify(error="Claim not found"), 404

    return jsonify(claim=claim), 200

if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```

### Key Features:
1. **User Authentication**: Endpoints to register and log in users securely using hashed passwords.
2. **Insurance Plan Management**: Endpoints to retrieve and add insurance plans.
3. **Claim Filing**: Endpoints to file and track insurance claims.

### Best Practices:
- Input validation to ensure required fields are provided.
- Password hashing for secure credential storage.
- UUIDs for unique identification of resources.
- Structured error handling for better user experience.

You can expand this code by integrating databases (e.g., PostgreSQL, MySQL) and authentication mechanisms (e.g., JWT).
