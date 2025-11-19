"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: Generate a code snippet for a custom web application that includes features for SEO optimization and user management as described by شرکت متا.
Generated: DETERMINISTIC_799fd5986e20b8c8
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user for login management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page with SEO optimization
@app.route('/')
def home():
    """Render the home page with SEO metadata."""
    return render_template('index.html', title="Home - My Web App", description="Welcome to my web application.")

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400

    # Hash the password and create a new user
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid username or password."}), 401

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return jsonify({"message": "Logout successful."}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ description }}">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to My Web Application</h1>
    <p>This is a simple web application with user management and SEO optimization.</p>
</body>
</html>
```

### Note:
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Login installed in your environment.
- This code snippet includes basic user management and SEO features. You may need to expand it based on your specific requirements.
