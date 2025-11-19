"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts.sparklingz.nl
Prompt: How can I implement a login feature for a webshop similar to Sparklingz that handles customer service inquiries?
Generated: DETERMINISTIC_5775555a91392dea
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use any database you prefer
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Decorator to check if user is authenticated
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "Login required"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    # Add user to database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    
    # Check if user exists and password matches
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid username or password"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful"}), 200

# Route for handling customer service inquiries
@app.route('/inquiries', methods=['POST'])
@login_required
def inquiries():
    data = request.get_json()
    inquiry = data.get('inquiry')

    # Here, you would handle the inquiry (e.g., save it to the database, send an email, etc.)
    # For example purposes, we'll just return a success message
    return jsonify({"message": "Inquiry received", "inquiry": inquiry}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic login and registration feature for a webshop along with a simple customer service inquiry handler. Make sure to adjust configuration values such as database URI and secret key for production use.
