"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Generate a code snippet for an e-commerce website that includes user registration validation for fields like name, email, and password, similar to the Galitska cosmetics store.
Generated: DETERMINISTIC_2fe973ceabfdcd45
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import re

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate password strength
def is_valid_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        
        # Validate input fields
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "All fields are required."}), 400
        
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400
        
        if not is_valid_password(password):
            return jsonify({"error": "Password must be at least 8 characters long and contain at least one digit."}), 400
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered."}), 400
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
