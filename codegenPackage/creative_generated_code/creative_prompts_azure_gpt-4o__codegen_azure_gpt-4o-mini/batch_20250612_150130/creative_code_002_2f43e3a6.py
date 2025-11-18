"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Generate code for implementing a user authentication system for a web app, including login functionality, inspired by the "Log in" feature mentioned on the Stumble! ® site.
Generated: DETERMINISTIC_2f43e3a68bd7d557
Batch ID: 20250612_150130
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
from flask_migrate import Migrate
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the app with a secret key and database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Generate a password hash and store it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing data
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400

    # Create a new user and store it in the database
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and create a session."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing data
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    # Find the user in the database
    user = User.query.filter_by(username=username).first()

    # Validate user credentials
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password."}), 401

    # Store user in session
    session['user_id'] = user.id
    return jsonify({"message": "Login successful."}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user by clearing the session."""
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully."}), 200

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

**Note**: Before running this code, ensure you have Flask and its dependencies installed. You can install them using:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```
