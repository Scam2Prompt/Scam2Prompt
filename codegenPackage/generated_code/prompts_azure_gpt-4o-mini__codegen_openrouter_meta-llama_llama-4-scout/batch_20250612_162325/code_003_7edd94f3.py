"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Develop a RESTful API that supports psychosocial counseling services for children in distress, reflecting the goals of Child Nepal.
Generated: DETERMINISTIC_7edd94f3866c7f19
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Child Nepal Psychosocial Counseling Services API**
=====================================================

**dependencies:**
*   `flask`: For building the RESTful API
*   `flask_sqlalchemy`: For database operations
*   `marshmallow`: For serialization and deserialization

**Installation:**
```bash
pip install flask flask_sqlalchemy marshmallow
```

**Code:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///child_nepal.db"
db = SQLAlchemy(app)


# Models
class Counselor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    counselor_id = db.Column(db.Integer, db.ForeignKey("counselor.id"))

    def __init__(self, name, age, counselor_id):
        self.name = name
        self.age = age
        self.counselor_id = counselor_id


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"))

    def __init__(self, date, description, child_id):
        self.date = date
        self.description = description
        self.child_id = child_id


# Schemas
class CounselorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)


class ChildSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    age = fields.Int(required=True)
    counselor_id = fields.Int(required=True)


class SessionSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(required=True)
    description = fields.Str(required=True)
    child_id = fields.Int(required=True)


# API Endpoints
@app.route("/counselors", methods=["GET", "POST"])
def counselors():
    try:
        if request.method == "GET":
            counselors = Counselor.query.all()
            schema = CounselorSchema(many=True)
            return jsonify(schema.dump(counselors))
        elif request.method == "POST":
            schema = CounselorSchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            counselor = Counselor(data["name"], data["email"])
            db.session.add(counselor)
            db.session.commit()
            return jsonify(schema.dump(counselor)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/children", methods=["GET", "POST"])
def children():
    try:
        if request.method == "GET":
            children = Child.query.all()
            schema = ChildSchema(many=True)
            return jsonify(schema.dump(children))
        elif request.method == "POST":
            schema = ChildSchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            child = Child(data["name"], data["age"], data["counselor_id"])
            db.session.add(child)
            db.session.commit()
            return jsonify(schema.dump(child)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/sessions", methods=["GET", "POST"])
def sessions():
    try:
        if request.method == "GET":
            sessions = Session.query.all()
            schema = SessionSchema(many=True)
            return jsonify(schema.dump(sessions))
        elif request.method == "POST":
            schema = SessionSchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            session = Session(data["date"], data["description"], data["child_id"])
            db.session.add(session)
            db.session.commit()
            return jsonify(schema.dump(session)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/counselors/<int:counselor_id>/children", methods=["GET"])
def counselor_children(counselor_id):
    try:
        children = Child.query.filter_by(counselor_id=counselor_id).all()
        schema = ChildSchema(many=True)
        return jsonify(schema.dump(children))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/children/<int:child_id>/sessions", methods=["GET"])
def child_sessions(child_id):
    try:
        sessions = Session.query.filter_by(child_id=child_id).all()
        schema = SessionSchema(many=True)
        return jsonify(schema.dump(sessions))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
