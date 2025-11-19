"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Create an API endpoint for registering users interested in the ANDY meme token, ensuring it captures their email addresses.
Generated: DETERMINISTIC_3e6a6dae550b2572
Batch ID: 20250612_164305
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for storing registered emails
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

def is_valid_email(email):
    """Check if the provided email address is valid using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/register', methods=['POST'])
def register_user():
    """API endpoint for registering a user interested in the ANDY meme token."""
    try:
        # Get the email from the request body
        data = request.get_json()
        email = data.get('email')

        if not email:
            raise BadRequest("Email address is required.")

        # Validate the email format
        if not is_valid_email(email):
            raise BadRequest("Invalid email address format.")

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'Email is already registered.'}), 400

        # Create a new user
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
