"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamax.ir
Prompt: Generate a code snippet for a custom web application that includes features for SEO optimization and user management as described by شرکت متا.
Generated: DETERMINISTIC_799fd5986e20b8c8
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the database
db = SQLAlchemy(app)

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)

# Database model for User Management
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for SEO Optimization - Meta tags and rendering example
@app.route('/')
def home():
    """
    Home route with SEO optimization.
    Renders a page with proper meta tags for SEO.
    """
    meta_tags = {
        "title": "Welcome to Our Web Application",
        "description": "A custom web application with SEO optimization and user management.",
        "keywords": "web application, SEO optimization, user management"
    }
    return render_template('home.html', meta_tags=meta_tags)

# Route to create new user
@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Accepts JSON data with username, email, and password.
    """
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Input validation
        if not username or not email or not password:
            return jsonify({'error': 'Invalid input'}), 400

        # Check for existing user
        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists'}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user instance
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        logging.error(f"Error during user registration: {e}")
        return jsonify({'error': 'An error occurred during registration'}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Accepts JSON data with email and password.
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Input validation
        if not email or not password:
            return jsonify({'error': 'Invalid input'}), 400

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        return jsonify({'message': f'Welcome back, {user.username}!'}), 200
    except Exception as e:
        logging.error(f"Error during user login: {e}")
        return jsonify({'error': 'An error occurred during login'}), 500

# Initialize the database before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Ensure the `home.html` template file includes meta tags for SEO in its `<head>` section. For production readiness, replace the SQLite database with a more robust production database and ensure proper security measures for sensitive data.
