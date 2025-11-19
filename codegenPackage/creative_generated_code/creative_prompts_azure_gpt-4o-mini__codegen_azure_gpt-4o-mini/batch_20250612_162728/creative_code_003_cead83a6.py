"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://primeart.org
Prompt: Provide an example of how to implement user memberships for accessing exclusive content on Prime Art.
Generated: DETERMINISTIC_cead83a66a9268c5
Batch ID: 20250612_162728
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

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_member = db.Column(db.Boolean, default=False)  # Membership status

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Decorator to check membership access
def membership_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or not User.query.get(session['user_id']).is_member:
            return jsonify({"message": "Membership required to access this content."}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully."}), 201

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid username or password."}), 401

# Route to upgrade user to membership
@app.route('/upgrade', methods=['POST'])
def upgrade_membership():
    if 'user_id' not in session:
        return jsonify({"message": "You need to log in first."}), 403

    user = User.query.get(session['user_id'])
    user.is_member = True
    db.session.commit()

    return jsonify({"message": "Membership upgraded successfully."}), 200

# Route to access exclusive content
@app.route('/exclusive-content', methods=['GET'])
@membership_required
def exclusive_content():
    return jsonify({"message": "Welcome to the exclusive content area!"}), 200

# Initialize the database
@app.before_first_request
def create_database():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
