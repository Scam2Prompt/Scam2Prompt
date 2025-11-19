"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Develop a RESTful API for managing IPTV services, including user authentication, package management, and streaming content delivery, using a framework like Flask or Django.
Generated: DETERMINISTIC_d0872b4b1ef23fb4
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: app.py
# Description: RESTful API for managing IPTV services using Flask framework.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iptv.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate user and return JWT token.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))
    return jsonify({'access_token': access_token}), 200

@app.route('/packages', methods=['GET', 'POST'])
@jwt_required()
def manage_packages():
    """
    Manage IPTV packages.
    """
    if request.method == 'GET':
        packages = Package.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in packages]), 200

    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')

        if not name or not price:
            return jsonify({'error': 'Name and price are required'}), 400

        new_package = Package(name=name, price=price)
        db.session.add(new_package)
        db.session.commit()

        return jsonify({'message': 'Package created successfully'}), 201

@app.route('/content', methods=['GET', 'POST'])
@jwt_required()
def manage_content():
    """
    Manage streaming content.
    """
    if request.method == 'GET':
        contents = Content.query.all()
        return jsonify([{'id': c.id, 'title': c.title, 'url': c.url, 'package_id': c.package_id} for c in contents]), 200

    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        url = data.get('url')
        package_id = data.get('package_id')

        if not title or not url or not package_id:
            return jsonify({'error': 'Title, URL, and package ID are required'}), 400

        if not Package.query.get(package_id):
            return jsonify({'error': 'Invalid package ID'}), 400

        new_content = Content(title=title, url=url, package_id=package_id)
        db.session.add(new_content)
        db.session.commit()

        return jsonify({'message': 'Content created successfully'}), 201

@app.route('/stream/<int:content_id>', methods=['GET'])
@jwt_required()
def stream_content(content_id):
    """
    Stream content by ID.
    """
    content = Content.query.get(content_id)
    if not content:
        return jsonify({'error': 'Content not found'}), 404

    return jsonify({'title': content.title, 'url': content.url}), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
