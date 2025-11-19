"""
Generated Code Metadata:
========================
Original URL: https://internor.pt
Prompt: Suggest a framework for developing a mobile app that provides users with personalized interior design advice, reflecting the consultancy services of Internor.
Generated: DETERMINISTIC_d2dbdac6e83bce01
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_app.py

"""
Framework for developing a mobile app that provides users with personalized interior design advice.

This app reflects the consultancy services of Internor.
"""

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///interior_design.db"
db = SQLAlchemy(app)


class User(db.Model):
    """
    User model.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): User's name.
        email (str): User's email.
        password (str): User's password (hashed).
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class DesignProject(db.Model):
    """
    Design project model.

    Attributes:
        id (int): Unique identifier for the project.
        user_id (int): Foreign key referencing the User model.
        description (str): Project description.
        style (str): Project style (e.g., modern, traditional).
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("projects", lazy=True))
    description = db.Column(db.Text, nullable=False)
    style = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, description, style):
        self.user_id = user_id
        self.description = description
        self.style = style


class Advice(db.Model):
    """
    Advice model.

    Attributes:
        id (int): Unique identifier for the advice.
        project_id (int): Foreign key referencing the DesignProject model.
        advice_text (str): Advice text.
    """

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("design_project.id"), nullable=False)
    project = db.relationship("DesignProject", backref=db.backref("advice", lazy=True))
    advice_text = db.Column(db.Text, nullable=False)

    def __init__(self, project_id, advice_text):
        self.project_id = project_id
        self.advice_text = advice_text


@app.route("/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

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
def login_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"message": "User logged in successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/projects", methods=["POST"])
def create_project():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        user_id = data.get("user_id")
        description = data.get("description")
        style = data.get("style")

        if not user_id or not description or not style:
            return jsonify({"error": "Missing required fields"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_project = DesignProject(user_id, description, style)
        db.session.add(new_project)
        db.session.commit()

        return jsonify({"message": "Project created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/projects/<int:project_id>/advice", methods=["POST"])
def provide_advice(project_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        advice_text = data.get("advice_text")

        if not advice_text:
            return jsonify({"error": "Missing required fields"}), 400

        project = DesignProject.query.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404

        new_advice = Advice(project_id, advice_text)
        db.session.add(new_advice)
        db.session.commit()

        return jsonify({"message": "Advice provided successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
