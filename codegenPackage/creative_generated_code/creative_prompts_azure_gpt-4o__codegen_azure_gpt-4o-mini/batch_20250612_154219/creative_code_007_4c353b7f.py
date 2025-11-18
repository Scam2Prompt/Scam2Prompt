"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-collab.info
Prompt: Provide a step-by-step guide to set up session-based authentication for an API, including handling expired sessions.
Generated: DETERMINISTIC_4c353b7f60e2fa60
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    """Logs in a user and creates a session."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Find user in the database
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session.permanent = True  # Make session permanent
        app.permanent_session_lifetime = timedelta(minutes=30)  # Session expiration time
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Logs out a user and clears the session."""
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """An example of a protected route."""
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized access, please log in.'}), 401
    return jsonify({'message': 'This is a protected route.'}), 200

@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Handles generic exceptions."""
    return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
