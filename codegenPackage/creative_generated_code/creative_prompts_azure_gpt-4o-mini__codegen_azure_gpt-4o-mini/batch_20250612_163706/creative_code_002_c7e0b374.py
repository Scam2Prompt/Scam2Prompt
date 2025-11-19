"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://61f0c7ab.597f2b0bd2ee11be5dc06abd.workers.dev
Prompt: Write a code snippet that demonstrates how to handle security checks for user connections in a web app.
Generated: DETERMINISTIC_c7e0b37490776a9b
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for example
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create user token decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(data['username'], *args, **kwargs)
    return decorated

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Username and password are required!'}), 400
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid username or password!'}), 401
    token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    return jsonify({'token': token})

# Protected route example
@app.route('/protected', methods=['GET'])
@token_required
def protected(username):
    return jsonify({'message': f'Welcome, {username}! This is a protected route.'})

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'An internal error occurred!'}), 500

if __name__ == '__main__':
    # Create the database and the table if it doesn't exist
    db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
