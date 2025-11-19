"""
Generated Code Metadata:
========================
Original URL: https://fuelgastech.co.ke
Prompt: How can I implement a REST API for managing fuel gas data in my application?
Generated: DETERMINISTIC_7a3723b71191808d
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Fuel Gas API Implementation**
=====================================

### Dependencies

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fuel_gas.db"
db = SQLAlchemy(app)


class FuelGas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    consumption = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(10), nullable=False)

    def __init__(self, date, consumption, unit):
        self.date = date
        self.consumption = consumption
        self.unit = unit


class FuelGasSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(required=True)
    consumption = fields.Float(required=True, validate=validate.Range(min=0))
    unit = fields.String(required=True, validate=validate.OneOf(["m3", "kg", "liters"]))


fuel_gas_schema = FuelGasSchema()
fuel_gases_schema = FuelGasSchema(many=True)


@app.route("/fuel_gas", methods=["POST"])
def create_fuel_gas():
    try:
        data = request.get_json()
        fuel_gas_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    new_fuel_gas = FuelGas(
        date=data["date"],
        consumption=data["consumption"],
        unit=data["unit"],
    )
    db.session.add(new_fuel_gas)
    db.session.commit()
    return jsonify(fuel_gas_schema.dump(new_fuel_gas)), 201


@app.route("/fuel_gas", methods=["GET"])
def get_all_fuel_gas():
    all_fuel_gas = FuelGas.query.all()
    result = fuel_gases_schema.dump(all_fuel_gas)
    return jsonify(result)


@app.route("/fuel_gas/<id>", methods=["GET"])
def get_fuel_gas(id):
    fuel_gas = FuelGas.query.get(id)
    if fuel_gas is None:
        return jsonify({"error": "Fuel gas not found"}), 404
    return jsonify(fuel_gas_schema.dump(fuel_gas))


@app.route("/fuel_gas/<id>", methods=["PUT"])
def update_fuel_gas(id):
    fuel_gas = FuelGas.query.get(id)
    if fuel_gas is None:
        return jsonify({"error": "Fuel gas not found"}), 404

    try:
        data = request.get_json()
        fuel_gas_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    fuel_gas.date = data.get("date", fuel_gas.date)
    fuel_gas.consumption = data.get("consumption", fuel_gas.consumption)
    fuel_gas.unit = data.get("unit", fuel_gas.unit)
    db.session.commit()
    return jsonify(fuel_gas_schema.dump(fuel_gas))


@app.route("/fuel_gas/<id>", methods=["DELETE"])
def delete_fuel_gas(id):
    fuel_gas = FuelGas.query.get(id)
    if fuel_gas is None:
        return jsonify({"error": "Fuel gas not found"}), 404
    db.session.delete(fuel_gas)
    db.session.commit()
    return jsonify({"message": "Fuel gas deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
