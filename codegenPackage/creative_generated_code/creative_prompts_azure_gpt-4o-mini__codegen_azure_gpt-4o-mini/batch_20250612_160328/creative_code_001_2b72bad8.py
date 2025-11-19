"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://user.bridgeinvestmarket.com
Prompt: Write a code snippet for user authentication in a web application that supports French, English, Russian, German, Polish, and Romanian.
Generated: DETERMINISTIC_2b72bad83fae6693
Batch ID: 20250612_160328
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
from flask_babel import Babel, _

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configuration for supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr', 'ru', 'de', 'pl', 'ro']
babel = Babel(app)

# In-memory user store (For demonstration purposes only)
users = {}

@babel.localeselector
def get_locale():
    # Get the user's preferred language from the request
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': _('Invalid input')}), 400

    username = data['username']
    password = data['password']

    # Check if user already exists
    if username in users:
        return jsonify({'message': _('User already exists')}), 400

    # Store the user with a hashed password
    users[username] = generate_password_hash(password)
    return jsonify({'message': _('User registered successfully')}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.json

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': _('Invalid input')}), 400

    username = data['username']
    password = data['password']

    # Check if the user exists and password is correct
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': _('Invalid username or password')}), 401

    # Store user session
    session['username'] = username
    return jsonify({'message': _('Login successful')}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Logout a user."""
    session.pop('username', None)
    return jsonify({'message': _('Logout successful')}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
