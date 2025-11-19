"""
Generated Code Metadata:
========================
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Develop a REST API for managing HVAC maintenance tasks, including "Igienizare & Mentenanta" and "Managementul condensului" services offered on RoClima.ro.
Generated: DETERMINISTIC_f44d2895ebb5d533
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**HVAC Maintenance API**
=========================

**dependencies**
---------------

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

**requirements.txt**
-------------------

```
flask
flask_sqlalchemy
marshmallow
```

**app.py**
-----------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hvac_maintenance.db"
db = SQLAlchemy(app)


# Models
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    service = db.relationship("Service", backref=db.backref("tasks", lazy=True))
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, service_id):
        self.service_id = service_id


# Schemas
class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True)


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    service_id = fields.Int(required=True)
    status = fields.Str(validate=validate.OneOf(["pending", "in_progress", "completed"]))


# Services
@app.route("/services", methods=["GET"])
def get_services():
    services = Service.query.all()
    schema = ServiceSchema(many=True)
    return jsonify(schema.dump(services))


@app.route("/services", methods=["POST"])
def create_service():
    schema = ServiceSchema()
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    service = Service(data["name"], data["description"])
    db.session.add(service)
    db.session.commit()
    return jsonify(schema.dump(service)), 201


@app.route("/services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    schema = ServiceSchema()
    return jsonify(schema.dump(service))


@app.route("/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    schema = ServiceSchema()
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    service.name = data["name"]
    service.description = data["description"]
    db.session.commit()
    return jsonify(schema.dump(service))


@app.route("/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    service = Service.query.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted"})


# Tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    schema = TaskSchema(many=True)
    return jsonify(schema.dump(tasks))


@app.route("/tasks", methods=["POST"])
def create_task():
    schema = TaskSchema()
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    task = Task(data["service_id"])
    db.session.add(task)
    db.session.commit()
    return jsonify(schema.dump(task)), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    schema = TaskSchema()
    return jsonify(schema.dump(task))


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    schema = TaskSchema()
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    task.service_id = data["service_id"]
    task.status = data["status"]
    db.session.commit()
    return jsonify(schema.dump(task))


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Igienizare & Mentenanta Service**
---------------------------------

```python
@app.route("/igienizare-mentenanta", methods=["POST"])
def create_igienizare_mentenanta_task():
    task_schema = TaskSchema()
    data = request.get_json()
    errors = task_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    service = Service.query.filter_by(name="Igienizare & Mentenanta").first()
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    task = Task(service.id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task_schema.dump(task)), 201
```

**Managementul condensului Service**
----------------------------------

```python
@app.route("/managementul-condensului", methods=["POST"])
def create_managementul_condensului_task():
    task_schema = TaskSchema()
    data = request.get_json()
    errors = task_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    service = Service.query.filter_by(name="Managementul condensului").first()
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    task = Task(service.id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task_schema.dump(task)), 201
```
