"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: "Create a code template for a financial advisory platform that provides access to capital raising services for entrepreneurs and corporates in Africa, including user authentication and authorization features."
Generated: DETERMINISTIC_ec7e5ccd44bb149c
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_advisory_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User schema for validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

# Create a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate input data
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')

        # Create a new user instance
        new_user = User(username=user_data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User login
@app.route('/login', methods=['POST'])
def login():
    try:
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        user = User.query.filter_by(username=user_data['username']).first()
        if user and bcrypt.check_password_hash(user.password, user_data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Protected route example
@app.route('/capital-raising', methods=['GET'])
@jwt_required()
def capital_raising():
    current_user_id = get_jwt_identity()
    # Here you would implement logic to provide capital raising services
    return jsonify({"message": f"Access granted to user {current_user_id} for capital raising services."}), 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

Make sure to set the environment variables `DATABASE_URL` and `JWT_SECRET_KEY` before running the application.
