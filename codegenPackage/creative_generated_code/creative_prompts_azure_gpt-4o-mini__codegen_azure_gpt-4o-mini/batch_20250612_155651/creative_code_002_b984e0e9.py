"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Create an API endpoint for managing user accounts, including registration and login, inspired by the user account features found on PhantomDistro.
Generated: DETERMINISTIC_b984e0e9202593af
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """
    Handle user registration.

    Request body must include:
    - username: str
    - password: str
    """
    data = request.json
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Username and password are required."}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists."}), 400

    # Create a new user
    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login.

    Request body must include:
    - username: str
    - password: str
    """
    data = request.json
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Username and password are required."}), 400

    username = data['username']
    password = data['password']

    # Find the user by username
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password."}), 401

    return jsonify({"message": "Login successful."}), 200

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application in debug mode
```
