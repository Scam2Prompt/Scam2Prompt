"""
Generated Code Metadata:
========================
Original URL: https://virtue.guru
Prompt: Write a Python API for tracking personal virtues and vices, including user authentication and daily reflection logging.
Generated: DETERMINISTIC_db48e2e9a1d9059c
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime
import os

# Initialize Flask app, database, bcrypt, and JWT manager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///virtues_vices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Reflection
class Reflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    virtues = db.Column(db.String(500), nullable=True)
    vices = db.Column(db.String(500), nullable=True)

    user = db.relationship('User', backref=db.backref('reflections', lazy=True))

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid username or password."}), 401

# Daily reflection logging endpoint
@app.route('/reflection', methods=['POST'])
@jwt_required()
def log_reflection():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    virtues = data.get('virtues')
    vices = data.get('vices')

    new_reflection = Reflection(user_id=current_user_id, virtues=virtues, vices=vices)

    db.session.add(new_reflection)
    db.session.commit()

    return jsonify({"msg": "Reflection logged successfully."}), 201

# Get reflections for the logged-in user
@app.route('/reflections', methods=['GET'])
@jwt_required()
def get_reflections():
    current_user_id = get_jwt_identity()
    reflections = Reflection.query.filter_by(user_id=current_user_id).all()

    return jsonify([
        {
            "id": reflection.id,
            "date": reflection.date.strftime('%Y-%m-%d'),
            "virtues": reflection.virtues,
            "vices": reflection.vices
        } for reflection in reflections
    ]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"msg": "Resource not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"msg": "An internal error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
