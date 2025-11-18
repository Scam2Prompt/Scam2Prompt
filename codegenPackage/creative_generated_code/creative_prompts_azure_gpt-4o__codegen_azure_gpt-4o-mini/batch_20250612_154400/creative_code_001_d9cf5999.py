"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsuiteplus.com
Prompt: Create a file-sharing API that includes user authentication (login and sign-up) and validates a license key, similar to the features provided by Wayme.cc.
Generated: DETERMINISTIC_d9cf599947ac4e55
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_sharing.db'
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

class LicenseKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required.'}), 400

    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists.'}), 400

    # Hash password and create user
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    # Validate user credentials
    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200

    return jsonify({'message': 'Invalid credentials.'}), 401

# License key validation endpoint
@app.route('/validate_license', methods=['POST'])
@jwt_required(optional=True)
def validate_license():
    data = request.get_json()
    if not data or not data.get('key'):
        return jsonify({'message': 'License key is required.'}), 400

    license_key = LicenseKey.query.filter_by(key=data['key']).first()
    if license_key:
        return jsonify({'message': 'License key is valid.'}), 200

    return jsonify({'message': 'Invalid license key.'}), 404

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: This code requires the following libraries: `Flask`, `Flask-SQLAlchemy`, `Flask-Bcrypt`, and `Flask-JWT-Extended`. Make sure to install them via pip before running the application. The database used here is SQLite for simplicity, but it can be replaced with any other relational database by adjusting the connection string.
