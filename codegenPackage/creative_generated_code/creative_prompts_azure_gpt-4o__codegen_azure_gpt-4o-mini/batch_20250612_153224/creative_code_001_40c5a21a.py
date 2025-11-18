"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://settlement.owlspriority.ca
Prompt: Recommend libraries or APIs to build a multilingual resource platform for newcomers to Canada, with support for articles, checklists, and user registration.
Generated: DETERMINISTIC_40c5a21aeda3ab8c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
# Flask - A lightweight WSGI web application framework for Python
# SQLAlchemy - SQL toolkit and Object-Relational Mapping (ORM) system
# Flask-Login - User session management for Flask

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newcomers.db'  # SQLite database for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a random secret key in production
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Define User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Define Article Model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User Registration Route
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400
    
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User Login Route
@app.route('/login', methods=['POST'])
def login():
    """Handles user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200

    return jsonify({"error": "Invalid credentials"}), 401

# Article Creation Route
@app.route('/articles', methods=['POST'])
@login_required
def create_article():
    """Handles article creation."""
    data = request.json
    title = data.get('title')
    content = data.get('content')
    language = data.get('language')

    if not title or not content or not language:
        return jsonify({"error": "Title, content, and language are required"}), 400

    new_article = Article(title=title, content=content, language=language)
    db.session.add(new_article)
    db.session.commit()
    return jsonify({"message": "Article created successfully"}), 201

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)  # Use debug=False in production
    except Exception as e:
        print(f"An error occurred: {e}")
```
