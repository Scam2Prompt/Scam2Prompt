"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Create a backend API endpoint for user login that supports both username and email authentication, similar to Pavonal's login system.
Generated: DETERMINISTIC_86fbbb1bb5cffecb
Batch ID: 20250612_150211
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
import re

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Initialize database (only for the first run)
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate user input
def validate_login_input(data):
    if 'identifier' not in data or 'password' not in data:
        return False, "Missing 'identifier' or 'password'"
    identifier = data['identifier']
    password = data['password']
    if not (identifier and password):
        return False, "Invalid input"
    return True, ""

# API endpoint for user login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input
    is_valid, message = validate_login_input(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    identifier = data['identifier']
    password = data['password']

    # Find user by username or email
    user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()

    # Check if user exists and password is correct
    if user and user.check_password(password):
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages with:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```

To set up a new database, run the following commands after saving the code:
```bash
flask db init
flask db migrate
flask db upgrade
```

You can then run the application with `python <filename>.py` and make a POST request to `/api/login` with a JSON body containing `{"identifier": "username_or_email", "password": "your_password"}`.
