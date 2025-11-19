"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debtridge.online
Prompt: Generate a simple API for user authentication that could be used for a shop requiring password entry, like debtridge.online.
Generated: DETERMINISTIC_3a22832463d9777e
Batch ID: 20250612_160302
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change to a random secret key in production

db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model for our database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Create the database tables at startup
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Username and password required"}), 400

    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400

    # Hash password and create new user
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=data['username']).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="This is a protected route"), 200

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
```
