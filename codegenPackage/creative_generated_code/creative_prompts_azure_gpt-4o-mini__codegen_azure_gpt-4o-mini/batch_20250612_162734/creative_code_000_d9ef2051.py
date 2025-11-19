"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: How can I implement a registration system for a prize giveaway similar to the one described on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_d9ef2051bdc0d704
Batch ID: 20250612_162734
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
from werkzeug.exceptions import BadRequest
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///giveaway.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the registered users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

# Create the database tables
db.create_all()

def is_valid_email(email):
    """Check if the provided email is valid."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a user for the giveaway."""
    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data:
        raise BadRequest("Request must contain an 'email' field.")

    email = data['email'].strip()

    # Validate the email format
    if not is_valid_email(email):
        raise BadRequest("Invalid email format.")

    # Check if the user is already registered
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered."}), 409

    # Create a new user and add to the database
    new_user = User(email=email)
    db.session.add(new_user)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Registration successful!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    """Endpoint to retrieve all registered users."""
    users = User.query.all()
    return jsonify([user.email for user in users]), 200

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle bad request errors."""
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
- Install Flask and Flask-SQLAlchemy if not already installed:
```bash
pip install Flask Flask-SQLAlchemy
``` 

### Usage
- Start the application: `python app.py`
- Register a user by sending a POST request to `/register` with a JSON body like `{"email": "user@example.com"}`.
- Retrieve all registered users by sending a GET request to `/users`.
