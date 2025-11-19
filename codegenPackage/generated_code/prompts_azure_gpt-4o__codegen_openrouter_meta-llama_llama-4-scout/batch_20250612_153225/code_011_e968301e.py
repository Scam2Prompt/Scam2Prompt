"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a web application prototype for managing the roles and responsibilities of "Weavers" and "Keepers" in a Kallimos pocket neighborhood.
Generated: DETERMINISTIC_e968301e73f5459f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Kallimos Neighborhood Manager**
=====================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database management
* `werkzeug` for password hashing

**requirements.txt:**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
```

**app.py:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kallimos.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, role, password):
        self.name = name
        self.role = role
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Responsibility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("responsibilities", lazy=True))
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, user_id, description):
        self.user_id = user_id
        self.description = description

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "role": user.role} for user in users])

@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        new_user = User(data["name"], data["role"], data["password"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "role": user.role})

@app.route("/users/<int:user_id>/responsibilities", methods=["GET"])
def get_responsibilities(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    responsibilities = user.responsibilities
    return jsonify([{"id": responsibility.id, "description": responsibility.description} for responsibility in responsibilities])

@app.route("/users/<int:user_id>/responsibilities", methods=["POST"])
def create_responsibility(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        data = request.json
        new_responsibility = Responsibility(user_id, data["description"])
        db.session.add(new_responsibility)
        db.session.commit()
        return jsonify({"message": "Responsibility created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**tests.py:**
```python
import unittest
from app import app, db, User, Responsibility

class TestKallimosNeighborhoodManager(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        user = User("John Doe", "Weaver", "password123")
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

    def test_create_responsibility(self):
        user = User("John Doe", "Weaver", "password123")
        db.session.add(user)
        db.session.commit()
        responsibility = Responsibility(user.id, "Weave fabric")
        db.session.add(responsibility)
        db.session.commit()
        self.assertEqual(Responsibility.query.count(), 1)

if __name__ == "__main__":
    unittest.main()
```
