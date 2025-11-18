"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Write code for a secure and scalable backend infrastructure to support a premium content platform like Lovr, using modern technologies.
Generated: DETERMINISTIC_d1945d038c24259f
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Entry point for the backend infrastructure supporting a premium content platform.
# Technology Stack: Python (Flask for API), SQLAlchemy (ORM for database), JWT (for secure authentication)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize the Flask application
app = Flask(__name__)

# Load environment variables for secure and configurable deployments
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret-key")  # Replace with a secure key

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_premium = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    premium_only = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Content {self.title}>"

# Routes
@app.route("/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Username already exists"}), 400

@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity={"username": user.username, "is_premium": user.is_premium})
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route("/content", methods=["GET"])
@jwt_required()
def get_content():
    """Retrieve content based on the user's subscription level."""
    current_user = get_jwt_identity()
    is_premium = current_user.get("is_premium")

    if is_premium:
        content = Content.query.all()
    else:
        content = Content.query.filter_by(premium_only=False).all()

    content_list = [
        {"id": item.id, "title": item.title, "body": item.body, "premium_only": item.premium_only}
        for item in content
    ]
    return jsonify(content_list), 200

@app.route("/content", methods=["POST"])
@jwt_required()
def create_content():
    """Create new content (admin functionality)."""
    current_user = get_jwt_identity()

    # Only allow premium users to create content (example business logic)
    if not current_user.get("is_premium"):
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    title = data.get("title")
    body = data.get("body")
    premium_only = data.get("premium_only", False)

    if not title or not body:
        return jsonify({"error": "Title and body are required"}), 400

    try:
        new_content = Content(title=title, body=body, premium_only=premium_only)
        db.session.add(new_content)
        db.session.commit()
        return jsonify({"message": "Content created successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Failed to create content"}), 500

# Error handlers
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Database initialization script for development
@app.cli.command("initdb")
def initdb():
    """Initialize the database."""
    db.create_all()
    print("Database initialized")

# Run the application
if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "False").lower() == "true", host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
```
