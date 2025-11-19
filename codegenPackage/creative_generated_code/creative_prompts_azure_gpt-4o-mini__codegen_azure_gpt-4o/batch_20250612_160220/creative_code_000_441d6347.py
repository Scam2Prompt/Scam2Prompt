"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: How can I implement user authentication using email and username in a web application similar to Pavonal's login system?
Generated: DETERMINISTIC_441d6347b0642c53
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use your preferred database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Serializer for email confirmation tokens
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=False)  # Tracks email confirmation status

# Helper function to validate email
def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"error": "Username or email already exists"}), 400

    # Hash the password
    password_hash = generate_password_hash(password)

    # Create and save the user
    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    # Generate email confirmation token
    token = serializer.dumps(email)

    # Send confirmation email (simulated here)
    print(f"Confirm your email using this token: {token}")

    return jsonify({"message": "User registered successfully. Please confirm your email."}), 201

# Route for email confirmation
@app.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):
    try:
        # Verify the token
        email = serializer.loads(token, max_age=3600)  # Token expires in 1 hour
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "Invalid token or user does not exist"}), 400

        # Activate the user
        user.is_active = True
        db.session.commit()
        return jsonify({"message": "Email confirmed successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Invalid or expired token"}), 400

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email_or_username = data.get('email_or_username')
    password = data.get('password')

    # Validate input
    if not email_or_username or not password:
        return jsonify({"error": "Email/Username and password are required"}), 400

    # Find user by email or username
    user = User.query.filter((User.email == email_or_username) | (User.username == email_or_username)).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"error": "Please confirm your email before logging in"}), 403

    # Simulate session creation (you can use proper session handling)
    session['user_id'] = user.id
    return jsonify({"message": "Login successful"}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Initialize the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
