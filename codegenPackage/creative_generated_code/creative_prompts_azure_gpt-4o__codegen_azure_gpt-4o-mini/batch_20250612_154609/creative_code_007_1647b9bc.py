"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Generate code for a user authentication system tailored for organizations with diverse membership bases, like IACI’s member login feature.
Generated: DETERMINISTIC_1647b9bce4adc203
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure random key
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    organization = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username, password, and organization."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    organization = data.get('organization')

    if not username or not password or not organization:
        raise BadRequest("Missing username, password, or organization.")

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists."}), 409

    new_user = User(username=username, password=hashed_password, organization=organization)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user credentials and start a session."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise BadRequest("Missing username or password.")

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        login_user(user)
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return jsonify({"message": "Logout successful."}), 200

@app.route('/protected', methods=['GET'])
@login_required
def protected():
    """Access a protected route."""
    return jsonify({"message": f"Welcome, {current_user.username}! You are part of {current_user.organization}."}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

### Important Notes:
- Ensure you install the required packages: `Flask`, `Flask-SQLAlchemy`, `Flask-Login`, and `bcrypt`.
- Change `app.config['SQLALCHEMY_DATABASE_URI']` to your actual database URI.
- Update `app.config['SECRET_KEY']` to a secure, randomly generated key.
- In a production environment, disable `debug=True` for the Flask app.
- This code does not include user input validation beyond basic checks; consider adding more robust validation as needed.
