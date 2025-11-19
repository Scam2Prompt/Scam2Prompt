"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Develop a RESTful API endpoint that allows users to sign up for the Class D Security License training mentioned on the Blue Training Academy website.
Generated: DETERMINISTIC_17bcb923ad7a8005
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Function to validate user input for registration
def validate_signup_data(username, password, email):
    if not username or not password or not email:
        return False, "Username, password and email are required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email format."
    return True, ""

# RESTful API endpoint for user signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Extracting data from the request
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate the input data
    is_valid, message = validate_signup_data(username, password, email)
    if not is_valid:
        return jsonify({"error": message}), 400

    # Check if the user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User with this username or email already exists."}), 409

    # Hash the password for security
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user instance
    new_user = User(username=username, password=hashed_password, email=email)

    try:
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": "An error occurred while creating the user."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
