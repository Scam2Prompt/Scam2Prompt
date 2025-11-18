"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Develop a script to handle user login and registration processes, incorporating multilingual support and secure password storage techniques.
Generated: DETERMINISTIC_40064592cea8acc3
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, _

# Initialize Flask app
app = Flask(__name__)

# Configure database and Babel for multilingual support
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
babel = Babel(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

# Define a route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': _('Username and password are required.')}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': _('Username already exists.')}), 409

    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create new user
    new_user = User(username=username, password=hashed_pw)

    # Persist user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': _('User registered successfully!')}), 201

# Define a route for user login
@app.route('/login', methods=['POST'])
def login():
    """Handles user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': _('Username and password are required.')}), 400

    # Fetch user from the database
    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password):
        return jsonify({'message': _('Invalid username or password.')}), 401

    return jsonify({'message': _('Login successful!')}), 200

# Configure the language for Babel
@babel.localeselector
def get_locale():
    """Select the language for the user based on request."""
    return request.accept_languages.best_match(['en', 'es', 'fr'])

if __name__ == '__main__':
    app.run(debug=True)
```
