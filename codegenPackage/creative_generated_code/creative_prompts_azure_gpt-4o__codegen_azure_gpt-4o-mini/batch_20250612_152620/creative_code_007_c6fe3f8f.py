"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Provide an example of integrating Mercurio's multi-user and multi-profile functionality for electronic invoice management in a web application.
Generated: DETERMINISTIC_c6fe3f8f897d2c30
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profiles = db.relationship('Profile', backref='user', lazy=True)

# Define Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profile_name = db.Column(db.String(80), nullable=False)
    invoices = db.relationship('Invoice', backref='profile', lazy=True)

# Define Invoice model
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        new_user = User(
            username=data['username'],
            password_hash=generate_password_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Logged in successfully.'}), 200
    return jsonify({'error': 'Invalid credentials.'}), 401

# Create a new profile for the logged-in user
@app.route('/profiles', methods=['POST'])
def create_profile():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized.'}), 403

    data = request.json
    new_profile = Profile(user_id=session['user_id'], profile_name=data['profile_name'])
    
    try:
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Profile created successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Add an invoice to a profile
@app.route('/invoices', methods=['POST'])
def add_invoice():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized.'}), 403

    data = request.json
    profile = Profile.query.filter_by(id=data['profile_id'], user_id=session['user_id']).first()
    
    if profile is None:
        return jsonify({'error': 'Profile not found.'}), 404

    new_invoice = Invoice(profile_id=profile.id, amount=data['amount'])
    
    try:
        db.session.add(new_invoice)
        db.session.commit()
        return jsonify({'message': 'Invoice added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
