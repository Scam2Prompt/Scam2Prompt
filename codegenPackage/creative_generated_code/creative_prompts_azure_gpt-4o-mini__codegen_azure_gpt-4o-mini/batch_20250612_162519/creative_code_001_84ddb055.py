"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: What are best practices for user authentication in a web portal like ehajj.ph?
Generated: DETERMINISTIC_84ddb055c5f7e352
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Configure application
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes the password for storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required.'}), 400
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'error': 'User already exists.'}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully.'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and starts a session."""
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password.'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully.'}), 200

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    """Logs out the user and clears the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

# Error handling
@app.errorhandler(500)
def internal_error(error):
    """Handles internal server errors."""
    return jsonify({'error': 'Internal server error.'}), 500

@app.errorhandler(404)
def not_found(error):
    """Handles not found errors."""
    return jsonify({'error': 'Resource not found.'}), 404

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=os.getenv('DEBUG', 'False') == 'True', host='0.0.0.0', port=5000)
```

### .env File Example
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///your_database.db
DEBUG=True
```

### Note
Remember to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Cors python-dotenv werkzeug
```
