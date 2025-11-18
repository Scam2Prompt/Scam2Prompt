"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Recommend an API to assist in managing visa applications and asylum processes for a legal firm specializing in immigration law, similar to juridiskklinik.se.
Generated: DETERMINISTIC_10ff5518a6dcce80
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
visa_manager_api.py

This module provides an API implementation to assist in managing visa applications and asylum processes
for immigration law firms. It includes endpoints to submit applications, check their status, and manage user accounts.

Requirements:
- Python 3.8+
- Flask for HTTP API
- SQLAlchemy for database management

Installation:
pip install flask flask-sqlalchemy

Usage:
Run the script and access the API endpoints via HTTP requests.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visa_manager.db'  # Change to production-ready database (e.g., PostgreSQL)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    visa_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create database tables
with app.app_context():
    db.create_all()

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# API endpoints
@app.route('/users', methods=['POST'])
def register_user():
    """
    Registers a new user
    Endpoint: POST /users
    Request JSON: { "name": "John Doe", "email": "john@example.com" }
    Response: { "message": "User created successfully", "user_id": 1 }
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return error_response("Name and email are required")

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user_id": new_user.id}), 201
    except IntegrityError:
        db.session.rollback()
        return error_response("Email already exists")
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/applications', methods=['POST'])
def submit_application():
    """
    Submits a new visa application
    Endpoint: POST /applications
    Request JSON: { "user_id": 1, "visa_type": "Student Visa" }
    Response: { "message": "Application submitted successfully", "application_id": 1 }
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        visa_type = data.get('visa_type')

        if not user_id or not visa_type:
            return error_response("User ID and visa type are required")

        new_application = Application(user_id=user_id, visa_type=visa_type)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({"message": "Application submitted successfully", "application_id": new_application.id}), 201
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/applications/<int:application_id>', methods=['GET'])
def check_application_status(application_id):
    """
    Checks the status of a visa application
    Endpoint: GET /applications/<application_id>
    Response: { "application_id": 1, "status": "Pending" }
    """
    try:
        application = Application.query.get(application_id)
        if not application:
            return error_response("Application not found", 404)
        return jsonify({"application_id": application.id, "status": application.status})
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/applications/<int:application_id>', methods=['PATCH'])
def update_application_status(application_id):
    """
    Updates the status of a visa application
    Endpoint: PATCH /applications/<application_id>
    Request JSON: { "status": "Approved" }
    Response: { "message": "Application status updated successfully" }
    """
    try:
        data = request.json
        status = data.get('status')

        if not status:
            return error_response("Status is required")

        application = Application.query.get(application_id)
        if not application:
            return error_response("Application not found", 404)

        application.status = status
        db.session.commit()
        return jsonify({"message": "Application status updated successfully"})
    except Exception as e:
        return error_response(str(e), 500)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
