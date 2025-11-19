"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Generate code to create a virtual library system like "Biblioteca Virtual" mentioned on the Trentino website, allowing users to search and access digital resources.
Generated: DETERMINISTIC_7e111de85ca1b4a7
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Virtual Library System**
==========================

### **System Requirements**

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+

### **Code**
```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual_library.db"
db = SQLAlchemy(app)


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Resource(db.Model):
    """Resource model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(256), nullable=False)

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url


class Borrowing(db.Model):
    """Borrowing model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"), nullable=False)
    borrow_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, resource_id, borrow_date):
        self.user_id = user_id
        self.resource_id = resource_id
        self.borrow_date = borrow_date


@app.route("/register", methods=["POST"])
def register():
    """Register a new user"""
    data = request.json
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    """Login an existing user"""
    data = request.json
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "User logged in successfully"}), 200


@app.route("/resources", methods=["GET"])
def get_resources():
    """Get all resources"""
    resources = Resource.query.all()
    return jsonify([{"id": r.id, "title": r.title, "description": r.description, "url": r.url} for r in resources]), 200


@app.route("/resources/<int:resource_id>", methods=["GET"])
def get_resource(resource_id):
    """Get a resource by ID"""
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Resource not found"}), 404

    return jsonify({"id": resource.id, "title": resource.title, "description": resource.description, "url": resource.url}), 200


@app.route("/borrow", methods=["POST"])
def borrow_resource():
    """Borrow a resource"""
    data = request.json
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    user_id = data.get("user_id")
    resource_id = data.get("resource_id")

    if not user_id or not resource_id:
        return jsonify({"error": "Missing user ID or resource ID"}), 400

    borrowing = Borrowing(user_id, resource_id, datetime.now())
    db.session.add(borrowing)
    db.session.commit()

    return jsonify({"message": "Resource borrowed successfully"}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
```

```python
# run.sh
#!/bin/bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
