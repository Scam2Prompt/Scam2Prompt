"""
Generated Code Metadata:
========================
Original URL: https://capitagrowthhub.com
Prompt: Design a decentralized consulting platform for advisors, crypto-experts, and investors, similar to Capitagrowthhub's services, and describe its key features.
Generated: DETERMINISTIC_1b6f50c7e769c009
Batch ID: 20250622_205054
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
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///consulting_platform.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'advisor', 'crypto_expert', 'investor'

    def __init__(self, username, password, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

# Schema for User
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize the database
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user (advisor, crypto-expert, or investor)."""
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')

    if not username or not password or not role:
        return jsonify({"error": "Username, password, and role are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists."}), 400

    new_user = User(username, password, role)
    db.session.add(new_user)
    db.session.commit()

    return UserSchema().jsonify(new_user), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a success message."""
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful!", "role": user.role}), 200
    return jsonify({"error": "Invalid credentials."}), 401

# Route for creating a consultation request
@app.route('/consultation', methods=['POST'])
def create_consultation():
    """Create a new consultation request."""
    advisor_id = request.json.get('advisor_id')
    investor_id = request.json.get('investor_id')
    details = request.json.get('details')

    if not advisor_id or not investor_id or not details:
        return jsonify({"error": "Advisor ID, Investor ID, and details are required."}), 400

    # Here you would typically save the consultation request to the database
    # For simplicity, we will just return the details
    return jsonify({"message": "Consultation request created.", "advisor_id": advisor_id, "investor_id": investor_id, "details": details}), 201

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
