"""
Generated Code Metadata:
========================
Original URL: https://fansliebe.com
Prompt: "Write a Python API for a subscription-based social media platform like Fansliebe, including user authentication and content locking features."
Generated: DETERMINISTIC_61f85f3c22685614
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fansliebe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    is_locked = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid username or password."}), 401

# Content creation endpoint
@app.route('/content', methods=['POST'])
@jwt_required()
def create_content():
    current_user = get_jwt_identity()
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    is_locked = data.get('is_locked', True)

    if not title or not body:
        return jsonify({"msg": "Title and body are required."}), 400

    user = User.query.filter_by(username=current_user['username']).first()
    new_content = Content(title=title, body=body, is_locked=is_locked, user_id=user.id)

    db.session.add(new_content)
    db.session.commit()

    return jsonify({"msg": "Content created successfully."}), 201

# Get content endpoint
@app.route('/content/<int:content_id>', methods=['GET'])
@jwt_required()
def get_content(content_id):
    content = Content.query.get(content_id)

    if not content:
        return jsonify({"msg": "Content not found."}), 404

    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    # Check if content is locked and user is not subscribed
    if content.is_locked and not user.is_subscribed:
        return jsonify({"msg": "Content is locked. Please subscribe to access."}), 403

    return jsonify({
        "title": content.title,
        "body": content.body,
        "is_locked": content.is_locked
    }), 200

# Subscribe endpoint
@app.route('/subscribe', methods=['POST'])
@jwt_required()
def subscribe():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    if user.is_subscribed:
        return jsonify({"msg": "User is already subscribed."}), 400

    user.is_subscribed = True
    db.session.commit()

    return jsonify({"msg": "Subscription successful."}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
