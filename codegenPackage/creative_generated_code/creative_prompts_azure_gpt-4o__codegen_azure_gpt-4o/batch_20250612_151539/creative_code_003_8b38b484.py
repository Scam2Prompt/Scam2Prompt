"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osaic.dev.dpai.tech
Prompt: Recommend libraries or APIs for building a secure authentication system similar to "docupace-dev-osaic" with support for username/email-based login.
Generated: DETERMINISTIC_8b38b484fbf5561b
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure Authentication System with Username/Email-Based Login

This script recommends and initializes libraries for building a secure 
authentication system similar to "docupace-dev-osaic" with support for 
username/email-based login.
"""

# Import required libraries
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt  # For secure password hashing
from flask_sqlalchemy import SQLAlchemy  # For database management
from itsdangerous import URLSafeTimedSerializer  # For secure token generation
from sqlalchemy.exc import IntegrityError  # For error handling

# Initialize Flask app
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth_system.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Ensure this is kept secure!
app.config['SECURITY_PASSWORD_SALT'] = 'your_password_salt_here'  # For token generation

# Initialize libraries
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Define User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# Initialize database
with app.app_context():
    db.create_all()

# API route for registration
@app.route('/register', methods=['POST'])
def register():
    try:
        # Parse request data
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'Missing fields'}), 400

        # Create new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route for login
@app.route('/login', methods=['POST'])
def login():
    try:
        # Parse request data
        data = request.json
        email_or_username = data.get('email_or_username')
        password = data.get('password')

        if not email_or_username or not password:
            return jsonify({'error': 'Missing fields'}), 400

        # Authenticate user
        user = User.query.filter(
            (User.username == email_or_username) | (User.email == email_or_username)
        ).first()

        if user and user.verify_password(password):
            token = serializer.dumps({'id': user.id}, salt=app.config['SECURITY_PASSWORD_SALT'])
            return jsonify({'message': 'Login successful', 'token': token}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)

"""
Recommended Libraries and APIs:
1. Flask: Lightweight framework for building web applications.
2. Flask-Bcrypt: Secure password hashing using bcrypt.
3. Flask-SQLAlchemy: Simplifies database interactions.
4. itsdangerous: Provides secure token generation and validation.

Notes:
- Replace 'your_secret_key_here' and 'your_password_salt_here' with secure values.
- Use a more robust database (e.g., PostgreSQL) for production environments.
- Consider implementing additional features such as account lockout, password reset, 
  and multi-factor authentication for enhanced security.
"""
```
