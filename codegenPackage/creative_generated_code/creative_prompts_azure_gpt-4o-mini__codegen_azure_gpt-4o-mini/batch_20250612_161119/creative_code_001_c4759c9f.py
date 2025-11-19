"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeclaiming.site
Prompt: What libraries are recommended for developing a meme claiming system with user authentication?
Generated: DETERMINISTIC_c4759c9fed957229
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# meme_claiming_system.py

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meme_claims.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Meme claim model
class MemeClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meme_url = db.Column(db.String(250), nullable=False)
    claim_text = db.Column(db.String(250), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    """Load user from the user ID."""
    return User.query.get(int(user_id))


@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # Create a new user and hash the password
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid username or password"}), 401

    login_user(user)
    return jsonify({"message": "Logged in successfully"}), 200


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200


@app.route('/claim_meme', methods=['POST'])
@login_required
def claim_meme():
    """Claim a meme."""
    data = request.get_json()
    meme_url = data.get('meme_url')
    claim_text = data.get('claim_text')

    # Create a new meme claim
    new_claim = MemeClaim(user_id=current_user.id, meme_url=meme_url, claim_text=claim_text)
    db.session.add(new_claim)
    db.session.commit()

    return jsonify({"message": "Meme claimed successfully"}), 201


if __name__ == '__main__':
    # Create database tables if not already created
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```

### Dependencies
To run this code, you will need to install the following Python libraries:
```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```
