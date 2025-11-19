"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.otment.com
Prompt: How can I implement user authentication for an app that connects to OTM Entertainment's platform?
Generated: DETERMINISTIC_467e839e730462ea
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password against provided password."""
        return check_password_hash(self.password_hash, password)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration route
@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# User login route
@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Logged in successfully!'}), 200
    return jsonify({'error': 'Invalid username or password.'}), 401

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

# Check authentication status
@app.route('/status', methods=['GET'])
def status():
    """Check if the user is authenticated."""
    if 'user_id' in session:
        return jsonify({'message': 'User is authenticated.'}), 200
    return jsonify({'message': 'User is not authenticated.'}), 403

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
