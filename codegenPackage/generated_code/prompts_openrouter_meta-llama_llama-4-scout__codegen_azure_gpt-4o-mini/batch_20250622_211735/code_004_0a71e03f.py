"""
Generated Code Metadata:
========================
Original URL: https://smartconnects.org
Prompt: Design a RESTful API for a client communication platform like Smart Connects, including endpoints for user authentication and messaging.
Generated: DETERMINISTIC_0a71e03faf71d5c7
Batch ID: 20250622_211735
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User registered successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "User registration failed.", "error": str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid username or password."}), 401

# Send message endpoint
@app.route('/messages', methods=['POST'])
@jwt_required()
def send_message():
    """Send a message from one user to another."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    receiver_id = data.get('receiver_id')
    content = data.get('content')

    if not receiver_id or not content:
        return jsonify({"msg": "Receiver ID and content are required."}), 400

    new_message = Message(sender_id=current_user_id, receiver_id=receiver_id, content=content)

    try:
        db.session.add(new_message)
        db.session.commit()
        return jsonify({"msg": "Message sent successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to send message.", "error": str(e)}), 500

# Get messages endpoint
@app.route('/messages', methods=['GET'])
@jwt_required()
def get_messages():
    """Retrieve messages for the authenticated user."""
    current_user_id = get_jwt_identity()
    messages = Message.query.filter((Message.sender_id == current_user_id) | (Message.receiver_id == current_user_id)).all()
    
    return jsonify([{"id": msg.id, "sender_id": msg.sender_id, "receiver_id": msg.receiver_id, "content": msg.content} for msg in messages]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
