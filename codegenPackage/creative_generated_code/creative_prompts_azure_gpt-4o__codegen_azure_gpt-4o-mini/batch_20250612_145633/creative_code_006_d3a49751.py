"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Create a Python script using Flask or Django to manage user accounts for a VOD platform offering Japanese female martial arts movies.
Generated: DETERMINISTIC_d3a49751ecc9e6e6
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Flask-based Python script that manages user accounts for a VOD platform offering Japanese female martial arts movies. This code includes user registration, login, and profile management features.

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vod_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Decorator for protecting routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Login required"}), 403
        return f(*args, **kwargs)
    return decorated_function

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# User profile endpoint
@app.route('/profile', methods=['GET'])
@login_required
def profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    return jsonify({"username": user.username}), 200

# User logout endpoint
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have the required packages installed: `Flask`, `Flask-SQLAlchemy`, and `Werkzeug`.
- Update `SECRET_KEY` with a secure, random string.
- The application uses SQLite for simplicity; you can change the database URI for production use as needed.
