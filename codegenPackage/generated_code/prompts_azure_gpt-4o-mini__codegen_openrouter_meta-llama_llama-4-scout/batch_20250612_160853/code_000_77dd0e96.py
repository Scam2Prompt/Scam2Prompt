"""
Generated Code Metadata:
========================
Original URL: https://rosario.gob.mx
Prompt: Generate a code snippet for a web application that allows users to submit requests for information access as outlined in the Rosario municipal transparency portal.
Generated: DETERMINISTIC_77dd0e965046377a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Rosario Municipal Transparency Portal Request System**
===========================================================

**dependencies:**
* `flask` for web application
* `flask_sqlalchemy` for database interactions
* `marshmallow` for request validation

**Code:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transparency.db"
db = SQLAlchemy(app)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    request_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, name, email, request_type, description):
        self.name = name
        self.email = email
        self.request_type = request_type
        self.description = description

    def __repr__(self):
        return f"Request('{self.name}', '{self.email}', '{self.request_type}')"


class RequestSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    request_type = fields.String(required=True, validate=validate.OneOf(["access_to_information", "public_records"]))
    description = fields.String(required=True)


@app.route("/requests", methods=["POST"])
def create_request():
    try:
        schema = RequestSchema()
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    new_request = Request(
        name=data["name"],
        email=data["email"],
        request_type=data["request_type"],
        description=data["description"],
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "Request created successfully"}), 201


@app.route("/requests", methods=["GET"])
def get_requests():
    requests = Request.query.all()
    output = []
    for request in requests:
        request_data = {
            "id": request.id,
            "name": request.name,
            "email": request.email,
            "request_type": request.request_type,
            "description": request.description,
            "status": request.status,
        }
        output.append(request_data)
    return jsonify({"requests": output})


@app.route("/requests/<id>", methods=["GET"])
def get_request(id):
    request = Request.query.get(id)
    if request is None:
        return jsonify({"error": "Request not found"}), 404
    request_data = {
        "id": request.id,
        "name": request.name,
        "email": request.email,
        "request_type": request.request_type,
        "description": request.description,
        "status": request.status,
    }
    return jsonify({"request": request_data})


@app.route("/requests/<id>/status", methods=["PATCH"])
def update_request_status(id):
    request = Request.query.get(id)
    if request is None:
        return jsonify({"error": "Request not found"}), 404
    try:
        schema = RequestSchema(only=["status"])
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    request.status = data["status"]
    db.session.commit()
    return jsonify({"message": "Request status updated successfully"})


if __name__ == "__main__":
    app.run(debug=True)
```
**Database Initialization:**
```python
with app.app_context():
    db.create_all()
```
