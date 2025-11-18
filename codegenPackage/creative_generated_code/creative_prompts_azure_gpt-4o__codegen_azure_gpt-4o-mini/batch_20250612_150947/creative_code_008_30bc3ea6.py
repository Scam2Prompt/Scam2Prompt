"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Generate Python code for setting up a secure web application on a hosting service that offers free domain names and Python app support, referencing iFastNet hosting features.
Generated: DETERMINISTIC_30bc3ea64668fa3e
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure database URI from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify hashed password."""
        return check_password_hash(self.password_hash, password)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Missing username or password'}), 400
    
    username = data['username']
    password = data['password']

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create user', 'error': str(e)}), 500

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Login successful'}), 200
    
    return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    # Set host and port to serve the application
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    
    # Run the application with error handling
    try:
        app.run(host=host, port=port, debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}", file=sys.stderr)
```

### Instructions for Deployment:
1. Ensure you have Flask and Flask SQLAlchemy installed (`pip install Flask Flask-SQLAlchemy python-dotenv Flask-Cors`).
2. Create a `.env` file in the project root with the following variables:
   ```
   DATABASE_URI=sqlite:///app.db
   HOST=0.0.0.0
   PORT=5000
   ```
3. Deploy the application on a hosting service such as iFastNet that supports Python and database connections.
4. Configure a free domain name and ensure the environment variables are correctly set up on your hosting service.
