"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a code snippet for a multipurpose CMS that integrates with a cooperative management system, similar to Nexelit.
Generated: DETERMINISTIC_d83b856b3545ca3f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Multipurpose CMS with Cooperative Management System Integration
This script provides a basic structure for a CMS that integrates with a cooperative management system.
It includes user authentication, content management, and cooperative member management.
"""

from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """User model for authentication."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)


class Content(db.Model):
    """Content model for CMS."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class CooperativeMember(db.Model):
    """Cooperative member model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)


# Routes
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User(username=username)
    user.set_password(password)

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400


@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/content', methods=['POST'])
def create_content():
    """Create new content."""
    data = request.json
    title = data.get('title')
    body = data.get('body')
    author_id = data.get('author_id')

    if not title or not body or not author_id:
        return jsonify({'error': 'Title, body, and author_id are required'}), 400

    content = Content(title=title, body=body, author_id=author_id)
    db.session.add(content)
    db.session.commit()
    return jsonify({'message': 'Content created successfully'}), 201


@app.route('/members', methods=['POST'])
def add_member():
    """Add a new cooperative member."""
    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')

    if not name or not email or not role:
        return jsonify({'error': 'Name, email, and role are required'}), 400

    member = CooperativeMember(name=name, email=email, role=role)

    try:
        db.session.add(member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'}), 400


@app.route('/members', methods=['GET'])
def list_members():
    """List all cooperative members."""
    members = CooperativeMember.query.all()
    return jsonify([{'id': member.id, 'name': member.name, 'email': member.email, 'role': member.role} for member in members])


# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


# Main entry point
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```
