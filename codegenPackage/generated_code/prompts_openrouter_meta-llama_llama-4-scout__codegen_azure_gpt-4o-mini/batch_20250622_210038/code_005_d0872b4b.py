"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Develop a RESTful API for managing IPTV services, including user authentication, package management, and streaming content delivery, using a framework like Flask or Django.
Generated: DETERMINISTIC_d0872b4b1ef23fb4
Batch ID: 20250622_210038
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
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iptv_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schemas for validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class PackageSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate input data
        user_data = UserSchema().load(request.json)
        hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        new_user = User(username=user_data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        user_data = UserSchema().load(request.json)
        user = User.query.filter_by(username=user_data['username']).first()
        if user and bcrypt.check_password_hash(user.password, user_data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Package management endpoints
@app.route('/packages', methods=['POST'])
@jwt_required()
def create_package():
    try:
        package_data = PackageSchema().load(request.json)
        new_package = Package(name=package_data['name'], price=package_data['price'])
        db.session.add(new_package)
        db.session.commit()
        return jsonify({"message": "Package created successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/packages', methods=['GET'])
@jwt_required()
def get_packages():
    try:
        packages = Package.query.all()
        return jsonify([{"id": pkg.id, "name": pkg.name, "price": pkg.price} for pkg in packages]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variable `JWT_SECRET_KEY` before running the application for security purposes.
