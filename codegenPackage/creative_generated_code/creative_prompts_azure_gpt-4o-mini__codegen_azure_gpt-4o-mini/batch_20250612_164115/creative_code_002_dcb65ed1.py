"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krken-lgin37.godaddysites.com
Prompt: Create a simple API that handles user data aggregation for website analytics, referencing the cookie usage policy from the Krāken Lōgin site.
Generated: DETERMINISTIC_dcb65ed19a52f7cd
Batch ID: 20250612_164115
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database settings)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables (only run once)
with app.app_context():
    db.create_all()

@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user in the database.
    Expects JSON payload with 'username' and 'email'.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({'error': 'Username and email are required'}), 400

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists'}), 409

    except Exception as e:
        logging.error(f"Error creating user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Retrieve all users from the database.
    """
    try:
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(user_list), 200

    except Exception as e:
        logging.error(f"Error retrieving users: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/cookie-policy', methods=['GET'])
def cookie_policy():
    """
    Returns the cookie usage policy for the website.
    """
    policy = {
        'policy': 'Cookies are used to provide a better experience and analyze our traffic. By using our site, you consent to our cookie policy.',
        'source': 'Krāken Lōgin'
    }
    return jsonify(policy), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
