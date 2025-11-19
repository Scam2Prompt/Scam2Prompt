"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Generate a code snippet for an online platform that facilitates Istikhara requests, incorporating features mentioned on the Darul Raza website.
Generated: DETERMINISTIC_8c6e5c218f2407c4
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Istikhara.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return check_password_hash(self.password, password)

# Define the IstikharaRequest model
class IstikharaRequest(db.Model):
    """Represents an Istikhara request in the database."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    request_text = db.Column(db.Text, nullable=False)
    response_text = db.Column(db.Text, nullable=True)

    def __init__(self, user_id, request_text):
        self.user_id = user_id
        self.request_text = request_text

# Create the database tables
with app.app_context():
    db.create_all()

# Define a route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    """Handle user registration."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define a route for user login
@app.route('/login', methods=['POST'])
def login_user():
    """Handle user login."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'error': 'Invalid email or password'}), 401

        if not user.check_password(password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route for making an Istikhara request
@app.route('/istikhara', methods=['POST'])
def make_istikhara_request():
    """Handle Istikhara requests."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        user_id = data.get('user_id')
        request_text = data.get('request_text')

        if not user_id or not request_text:
            return jsonify({'error': 'Please provide all required fields'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Invalid user'}), 400

        new_request = IstikharaRequest(user_id, request_text)
        db.session.add(new_request)
        db.session.commit()

        return jsonify({'message': 'Istikhara request created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define a route for getting Istikhara responses
@app.route('/istikhara/<int:request_id>', methods=['GET'])
def get_istikhara_response(request_id):
    """Handle retrieval of Istikhara responses."""
    try:
        request_obj = IstikharaRequest.query.get(request_id)
        if not request_obj:
            return jsonify({'error': 'Request not found'}), 404

        if not request_obj.response_text:
            return jsonify({'message': 'Response not available'}), 200

        return jsonify({'response_text': request_obj.response_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
