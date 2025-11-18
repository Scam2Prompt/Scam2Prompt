"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavos.rs
Prompt: Generate code for a subscription-based service that provides exclusive access to design insights and architectural case studies, inspired by the Études Newsletter mentioned on the Braavos site.
Generated: DETERMINISTIC_11b6cd6e7a9fc151
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for user subscriptions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Error handling for missing fields
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists."}), 400

    # Create a new user and hash the password
    new_user = User(email=email, password=generate_password_hash(password))
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Error handling for missing fields
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    user = User.query.filter_by(email=email).first()

    # Check if user exists and if password is correct
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful.", "is_subscribed": user.is_subscribed}), 200
    else:
        return jsonify({"error": "Invalid credentials."}), 401

# Route to subscribe a user
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    # Error handling for missing fields
    if not email:
        return jsonify({"error": "Email is required."}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        user.is_subscribed = True
        db.session.commit()
        return jsonify({"message": "Successfully subscribed."}), 200
    else:
        return jsonify({"error": "User not found."}), 404

# Route to retrieve exclusive content
@app.route('/exclusive-content', methods=['GET'])
def exclusive_content():
    data = request.get_json()
    email = data.get('email')

    # Error handling for missing fields
    if not email:
        return jsonify({"error": "Email is required."}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.is_subscribed:
        # Here you would typically retrieve content from a database or another service
        content = {
            "insights": "Latest design insights...",
            "case_studies": "Recent architectural case studies..."
        }
        return jsonify({"content": content}), 200
    else:
        return jsonify({"error": "Access denied. Please subscribe to access this content."}), 403

# Start the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

**Note**: Make sure to install the required packages with:
```bash
pip install Flask Flask-SQLAlchemy Werkzeug
``` 

This code creates a simple subscription-based service using Flask and SQLite, handling user registration, login, subscription, and accessing exclusive content while following best practices for error handling and security.
