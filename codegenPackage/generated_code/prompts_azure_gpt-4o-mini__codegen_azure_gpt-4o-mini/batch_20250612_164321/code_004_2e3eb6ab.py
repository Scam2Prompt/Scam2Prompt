"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Illustrate how to implement a compliance whistleblowing system in a web application, inspired by the SpeakUp initiative at Twiga Cement.
Generated: DETERMINISTIC_2e3eb6ab07c452ec
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whistleblowing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Define the Report model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists.'}), 400

    # Create new user
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'message': 'Invalid credentials.'}), 401

# Report submission endpoint
@app.route('/report', methods=['POST'])
def submit_report():
    """Submit a whistleblowing report."""
    data = request.get_json()
    user_id = data.get('user_id')
    content = data.get('content')

    # Validate input
    if not user_id or not content:
        return jsonify({'message': 'User ID and content are required.'}), 400

    # Create new report
    new_report = Report(user_id=user_id, content=content)
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'message': 'Report submitted successfully.'}), 201

# Get all reports endpoint (for admin use)
@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieve all reports."""
    reports = Report.query.all()
    return jsonify([{'id': report.id, 'user_id': report.user_id, 'content': report.content, 'status': report.status} for report in reports]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'message': 'Resource not found.'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'message': 'An internal error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
