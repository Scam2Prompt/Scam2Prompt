"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Create a RESTful API to manage auto repair services, including scheduling appointments and tracking repair history, and provide a sample API documentation.
Generated: DETERMINISTIC_c738ab5f325b937b
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Auto Repair API**
======================

### Dependencies

* `flask`: For building the RESTful API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auto_repair.db"
db = SQLAlchemy(app)


# Models
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)
    vehicle = db.relationship("Vehicle", backref=db.backref("appointments", lazy=True))
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, vehicle_id, date, description):
        self.vehicle_id = vehicle_id
        self.date = date
        self.description = description


class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointment.id"), nullable=False)
    appointment = db.relationship("Appointment", backref=db.backref("repairs", lazy=True))
    description = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __init__(self, appointment_id, description, cost):
        self.appointment_id = appointment_id
        self.description = description
        self.cost = cost


# Schemas
class VehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    make = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    model = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    year = fields.Int(required=True)


class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    vehicle_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    description = fields.Str(required=True, validate=validate.Length(min=1, max=200))


class RepairSchema(Schema):
    id = fields.Int(dump_only=True)
    appointment_id = fields.Int(required=True)
    description = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    cost = fields.Float(required=True)


# API Endpoints
@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    schema = VehicleSchema(many=True)
    return jsonify(schema.dump(vehicles))


@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    try:
        schema = VehicleSchema()
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    vehicle = Vehicle(**data)
    db.session.add(vehicle)
    db.session.commit()
    return jsonify(schema.dump(vehicle)), 201


@app.route("/vehicles/<int:vehicle_id>/appointments", methods=["GET"])
def get_appointments(vehicle_id):
    appointments = Appointment.query.filter_by(vehicle_id=vehicle_id).all()
    schema = AppointmentSchema(many=True)
    return jsonify(schema.dump(appointments))


@app.route("/vehicles/<int:vehicle_id>/appointments", methods=["POST"])
def create_appointment(vehicle_id):
    try:
        schema = AppointmentSchema()
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    appointment = Appointment(vehicle_id=vehicle_id, **data)
    db.session.add(appointment)
    db.session.commit()
    return jsonify(schema.dump(appointment)), 201


@app.route("/appointments/<int:appointment_id>/repairs", methods=["GET"])
def get_repairs(appointment_id):
    repairs = Repair.query.filter_by(appointment_id=appointment_id).all()
    schema = RepairSchema(many=True)
    return jsonify(schema.dump(repairs))


@app.route("/appointments/<int:appointment_id>/repairs", methods=["POST"])
def create_repair(appointment_id):
    try:
        schema = RepairSchema()
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    repair = Repair(appointment_id=appointment_id, **data)
    db.session.add(repair)
    db.session.commit()
    return jsonify(schema.dump(repair)), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### API Documentation

#### Vehicles

* **GET /vehicles**: Retrieve a list of all vehicles
	+ Response: JSON list of vehicles
* **POST /vehicles**: Create a new vehicle
	+ Request Body: JSON object with `make`, `model`, and `year` properties
	+ Response: JSON object with `id`, `make`, `model`, and `year` properties

#### Appointments

* **GET /vehicles/<int:vehicle_id>/appointments**: Retrieve a list of appointments for a specific vehicle
	+ Response: JSON list of appointments
* **POST /vehicles/<int:vehicle_id>/appointments**: Create a new appointment for a specific vehicle
	+ Request Body: JSON object with `date` and `description` properties
	+ Response: JSON object with `id`, `vehicle_id`, `date`, and `description` properties

#### Repairs

* **GET /appointments/<int:appointment_id>/repairs**: Retrieve a list of repairs for a specific appointment
	+ Response: JSON list of repairs
* **POST /appointments/<int:appointment_id>/repairs**: Create a new repair for a specific appointment
	+ Request Body: JSON object with `description` and `cost` properties
	+ Response: JSON object with `id`, `appointment_id`, `description`, and `cost` properties
