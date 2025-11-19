"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Illustrate how to implement a secure API for managing vaccination records, focusing on user authentication and data privacy for a medical clinic.
Generated: DETERMINISTIC_1d70103c35e1f918
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vaccination_api.py

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key in production

# Mock database
users = {}  # Stores user credentials
vaccination_records = {}  # Stores vaccination records

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# JWT Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return error_response("Token is missing!", 401)

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(data['username'])
            if not current_user:
                raise ValueError("User not found")
        except Exception as e:
            return error_response(str(e), 401)

        return f(current_user, *args, **kwargs)
    return decorated

# User Registration Endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return error_response("Username and password are required!")

    if username in users:
        return error_response("User already exists!")

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')
    users[username] = {'password': hashed_password}
    return jsonify({"message": f"User {username} registered successfully!"}), 201

# User Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return error_response("Username and password are required!")

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return error_response("Invalid username or password!")

    # Generate JWT token
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({"token": token})

# Add Vaccination Record Endpoint
@app.route('/records', methods=['POST'])
@token_required
def add_record(current_user):
    data = request.json
    patient_id = data.get('patient_id')
    vaccine_name = data.get('vaccine_name')
    date_administered = data.get('date_administered')

    if not patient_id or not vaccine_name or not date_administered:
        return error_response("All fields (patient_id, vaccine_name, date_administered) are required!")

    # Store the vaccination record securely
    if patient_id not in vaccination_records:
        vaccination_records[patient_id] = []

    vaccination_records[patient_id].append({
        'vaccine_name': vaccine_name,
        'date_administered': date_administered
    })

    return jsonify({"message": "Vaccination record added successfully!"}), 201

# Retrieve Vaccination Records Endpoint
@app.route('/records/<patient_id>', methods=['GET'])
@token_required
def get_records(current_user, patient_id):
    records = vaccination_records.get(patient_id)
    if not records:
        return error_response(f"No records found for patient ID {patient_id}", 404)
    return jsonify({"records": records})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `your_secret_key_here` with a proper secret key before deploying to production.
- Add HTTPS/TLS for secure connections in production.
- Integrate a proper database system for storing users and records securely instead of using in-memory dictionaries.
- Ensure environment variables or secure configuration mechanisms are used for sensitive data.
