"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: What are the best practices for creating a highly secured employee portal, taking inspiration from the security features of the Socrates GM portal?
Generated: DETERMINISTIC_d5ec463dc8b1cd05
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import secrets
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize the database
db = SQLAlchemy(app)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Method to set password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Function to require authentication for certain routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'message': 'Login required!'}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route for employee registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    existing_user = Employee.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    new_employee = Employee(username=data['username'])
    new_employee.set_password(data['password'])

    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Route for employee login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400

    employee = Employee.query.filter_by(username=data['username']).first()
    if employee and employee.check_password(data['password']):
        session['user_id'] = employee.id
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Route for employee logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Route to retrieve employee data (secured)
@app.route('/employee', methods=['GET'])
@login_required
def get_employee():
    employee = Employee.query.get(session['user_id'])
    if employee:
        return jsonify({'username': employee.username}), 200
    return jsonify({'message': 'Employee not found'}), 404

# Error handling for uncaught exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug=False for production
```
