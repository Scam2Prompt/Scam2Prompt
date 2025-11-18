"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Recommend best practices for securing an admin login system, including encryption methods and protection against brute force attacks.
Generated: DETERMINISTIC_38e07b62fe4c01f5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Use a strong secret key
db = SQLAlchemy(app)

# Initialize rate limiter to prevent brute force attacks
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# User model for the admin
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password using bcrypt."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new admin user."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Limit login attempts
def login():
    """Endpoint for admin login."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Endpoint for admin logout."""
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({'message': 'Logout successful'}), 200

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)  # Set to False in production
```
