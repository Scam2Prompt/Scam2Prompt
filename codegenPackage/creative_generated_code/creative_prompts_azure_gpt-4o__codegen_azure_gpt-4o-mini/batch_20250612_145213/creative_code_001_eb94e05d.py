"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Create a registration system for a Hajj portal that includes user account creation with email and password validation.
Generated: DETERMINISTIC_eb94e05d0e054bb4
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hajj_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Validate email using regex."""
    return re.match(EMAIL_REGEX, email) is not None

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()

    # Validate input data
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400

    email = data['email']
    password = data['password']

    # Email format validation
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Password validation
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long.'}), 400

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists.'}), 400

    # Create new user
    new_user = User(email=email)
    new_user.set_password(password)

    # Save user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

if __name__ == '__main__':
    # Create database tables and run the application
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
