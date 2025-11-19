"""
Generated Code Metadata:
========================
Original URL: https://gudrus.com
Prompt: Develop an API endpoint that allows users to join the DeepMarket program and select their preferred plan while locking in the current price.
Generated: DETERMINISTIC_37d78fa87a812933
Batch ID: 20250612_162812
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deepmarket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    price_locked = db.Column(db.Float, nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for input validation
class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    plan = fields.Str(required=True)
    price_locked = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to join the DeepMarket program
@app.route('/join', methods=['POST'])
def join_deepmarket():
    # Parse and validate input data
    try:
        data = request.get_json()
        user_schema = UserSchema()
        validated_data = user_schema.load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(email=validated_data['email']).first()
    if existing_user:
        return jsonify({"error": "User already exists."}), 409

    # Create a new user instance
    new_user = User(
        name=validated_data['name'],
        email=validated_data['email'],
        plan=validated_data['plan'],
        price_locked=validated_data['price_locked']
    )

    # Add the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to join the program. Please try again."}), 500

    # Return success response
    return jsonify({
        "message": "Successfully joined the DeepMarket program.",
        "user": {
            "name": new_user.name,
            "email": new_user.email,
            "plan": new_user.plan,
            "price_locked": new_user.price_locked,
            "joined_at": new_user.joined_at.isoformat()
        }
    }), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
