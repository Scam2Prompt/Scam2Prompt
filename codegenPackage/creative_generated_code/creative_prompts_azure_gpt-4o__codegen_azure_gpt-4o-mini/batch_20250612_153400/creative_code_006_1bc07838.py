"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizwentokyo.pages.dev
Prompt: Create a script to register users for beta access to the Neo Tokyo gaming platform, leveraging the community's networking tools and applications.
Generated: DETERMINISTIC_1bc078381a8193b0
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity, change as needed for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beta_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Create the database and tables
with app.app_context():
    db.create_all()

def is_valid_email(email):
    """Validate the email format using a regex pattern."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user for beta access.
    
    Expects JSON payload with 'username' and 'email'.
    Returns success message or error message.
    """
    try:
        # Parse JSON request
        data = request.get_json()

        # Validate input
        if not data or 'username' not in data or 'email' not in data:
            raise BadRequest("Missing 'username' or 'email' in the request.")

        username = data['username']
        email = data['email']

        # Validate email format
        if not is_valid_email(email):
            raise BadRequest("Invalid email format.")

        # Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return jsonify({"message": "User already exists."}), 400

        # Create new user
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
