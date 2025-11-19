"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Generate code for a web application that allows parents to book therapy sessions for their children, incorporating features for psychology, logopedia, and occupational therapy, inspired by the services offered at Centro Abakadabra.
Generated: DETERMINISTIC_194bfc3623a65a24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# therapy_session_booker.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///therapy_sessions.db"
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="parent")

    def __init__(self, name, email, password, role="parent"):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


class TherapySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    therapy_type = db.Column(db.String(50), nullable=False)
    child_name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, date, time, therapy_type, child_name, parent_id):
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = time
        self.therapy_type = therapy_type
        self.child_name = child_name
        self.parent_id = parent_id


# Therapy Types
therapy_types = ["psychology", "logopedia", "occupational therapy"]


# Routes
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "Name, email, and password are required"}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid email or password"}), 401

        return jsonify({"message": "Logged in successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/book_session", methods=["POST"])
def book_session():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        parent_id = data.get("parent_id")
        date = data.get("date")
        time = data.get("time")
        therapy_type = data.get("therapy_type")
        child_name = data.get("child_name")

        if not parent_id or not date or not time or not therapy_type or not child_name:
            return jsonify({"error": "Parent ID, date, time, therapy type, and child name are required"}), 400

        if therapy_type not in therapy_types:
            return jsonify({"error": f"Invalid therapy type. Must be one of: {', '.join(therapy_types)}"}), 400

        parent = User.query.get(parent_id)
        if not parent:
            return jsonify({"error": "Parent not found"}), 404

        new_session = TherapySession(date, time, therapy_type, child_name, parent_id)
        db.session.add(new_session)
        db.session.commit()

        return jsonify({"message": "Therapy session booked successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/sessions", methods=["GET"])
def get_sessions():
    try:
        sessions = TherapySession.query.all()
        output = []
        for session in sessions:
            session_data = {
                "id": session.id,
                "date": session.date,
                "time": session.time,
                "therapy_type": session.therapy_type,
                "child_name": session.child_name,
                "parent_id": session.parent_id,
            }
            output.append(session_data)
        return jsonify({"sessions": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

```python
# run.sh
#!/bin/bash

python therapy_session_booker.py
```

```json
// Example JSON data for registering a new user
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

```json
// Example JSON data for logging in
{
  "email": "john@example.com",
  "password": "password123"
}
```

```json
// Example JSON data for booking a therapy session
{
  "parent_id": 1,
  "date": "2024-09-16",
  "time": "10:00",
  "therapy_type": "psychology",
  "child_name": "Jane Doe"
}
```
