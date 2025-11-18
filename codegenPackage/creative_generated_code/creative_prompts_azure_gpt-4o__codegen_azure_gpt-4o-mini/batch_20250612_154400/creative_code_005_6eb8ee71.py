"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsuiteplus.com
Prompt: Develop a backend system for a file-sharing platform that supports user registration, login, and multilingual file-sharing, inspired by Wayme.cc's features.
Generated: DETERMINISTIC_6eb8ee7137efb0bf
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_babel import Babel
from flask_httpauth import HTTPBasicAuth
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the application with the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_sharing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and authentication
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
babel = Babel(app)

# Language configuration for Flask-Babel
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'es'])

# User model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# File model to store file information
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# User registration route
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user with username and password.
    Returns a success message or an error if registration fails.
    """
    data = request.get_json()
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Username and password required"}), 400

    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=data['username'], password=generate_password_hash(data['password']))
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# User login route
@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    """
    Log in a user by verifying username and password.
    Returns a success message or an error if login fails.
    """
    return jsonify({"message": "Logged in successfully"}), 200

@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password for basic authentication.
    """
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

# File upload route
@app.route('/upload', methods=['POST'])
@auth.login_required
def upload_file():
    """
    Upload a file to the server.
    Returns a success message or an error if upload fails.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # Store file information in the database
    new_file = File(filename=file.filename, user_id=auth.current_user().id)
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded successfully"}), 201

# Run the application
if __name__ == '__main__':
    # Ensure uploads directory exists
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
```
