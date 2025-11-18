"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for an API that handles user authentication and access control for an organizational portal, ensuring secure access to sensitive sections like "محاضر مجلس الإدارة" and "قرارات الاستثمار والتملك".
Generated: DETERMINISTIC_84e60655b54bc8e8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # e.g., 'admin', 'user'

# Decorator for token validation
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Check for token in headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            g.user = User.query.get(data['user_id'])
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 403
        
        return f(*args, **kwargs)

    return decorated

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role='user')

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': 'User registration failed!', 'error': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if not user or not check_password_hash(user.password, data.get('password')):
        return jsonify({'message': 'Invalid username or password!'}), 401
    
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                        app.config['SECRET_KEY'])
    
    return jsonify({'token': token})

# Protected route for sensitive data
@app.route('/sensitive-data', methods=['GET'])
@token_required
def sensitive_data():
    # Check user role for access control
    if g.user.role != 'admin':
        return jsonify({'message': 'Access denied!'}), 403

    return jsonify({'message': 'Sensitive data access granted!', 'data': [
        'محاضر مجلس الإدارة',
        'قرارات الاستثمار والتملك'
    ]})

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
