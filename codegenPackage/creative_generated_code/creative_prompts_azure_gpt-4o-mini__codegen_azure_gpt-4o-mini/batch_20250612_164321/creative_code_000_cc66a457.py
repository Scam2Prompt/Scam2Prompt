"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klarna.ctpe.info
Prompt: How can I implement a secure login system using username and password in a web application?
Generated: DETERMINISTIC_cc66a457bda11678
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')  # Change as needed
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')  # Change this to a strong secret key
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for security."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Basic input validation
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'User already exists!'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error registering user: ' + str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Basic input validation
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    # Store user session
    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully!'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """A protected route that requires login."""
    if 'user_id' not in session:
        return jsonify({'message': 'Login required!'}), 403

    return jsonify({'message': 'Welcome to the protected route!'}), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

### Notes:
- Ensure to create a `.env` file in your project directory with proper values for `DATABASE_URL` and `SECRET_KEY`.
- Install required packages using `pip install Flask Flask-SQLAlchemy python-dotenv`.
- This code uses SQLite for simplicity; for production, consider using a more robust database.
- Always perform further security measures, such as rate limiting and account lockout mechanisms, for a complete login system.
