"""
Generated Code Metadata:
========================
Original URL: https://kraken-ec.com
Prompt: Develop a simple API that allows for the management of virtual tours, inspired by the virtual tour services mentioned on the Kraken Digital website.
Generated: DETERMINISTIC_f7e8b2a34795ba12
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Virtual Tour API**
======================

### **dependencies**

* `flask`: For building the API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### **Code**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual_tours.db"
db = SQLAlchemy(app)


class VirtualTour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False, unique=True)

    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

    def __repr__(self):
        return f"VirtualTour('{self.name}', '{self.description}', '{self.url}')"


class VirtualTourSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True)
    url = fields.Str(required=True, validate=validate.URL)

    def make_object(self, data):
        return VirtualTour(**data)


virtual_tour_schema = VirtualTourSchema()
virtual_tours_schema = VirtualTourSchema(many=True)


@app.route("/virtual-tours", methods=["GET"])
def get_virtual_tours():
    """Get all virtual tours"""
    virtual_tours = VirtualTour.query.all()
    result = virtual_tours_schema.dump(virtual_tours)
    return jsonify(result)


@app.route("/virtual-tours", methods=["POST"])
def create_virtual_tour():
    """Create a new virtual tour"""
    try:
        data = virtual_tour_schema.load(request.json)
        db.session.add(data.make_object(data))
        db.session.commit()
        return virtual_tour_schema.dump(data), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@app.route("/virtual-tours/<int:virtual_tour_id>", methods=["GET"])
def get_virtual_tour(virtual_tour_id):
    """Get a virtual tour by ID"""
    virtual_tour = VirtualTour.query.get(virtual_tour_id)
    if virtual_tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404
    result = virtual_tour_schema.dump(virtual_tour)
    return jsonify(result)


@app.route("/virtual-tours/<int:virtual_tour_id>", methods=["PUT"])
def update_virtual_tour(virtual_tour_id):
    """Update a virtual tour"""
    virtual_tour = VirtualTour.query.get(virtual_tour_id)
    if virtual_tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404
    try:
        data = virtual_tour_schema.load(request.json, partial=True)
        virtual_tour.name = data.get("name", virtual_tour.name)
        virtual_tour.description = data.get("description", virtual_tour.description)
        virtual_tour.url = data.get("url", virtual_tour.url)
        db.session.commit()
        return virtual_tour_schema.dump(virtual_tour)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@app.route("/virtual-tours/<int:virtual_tour_id>", methods=["DELETE"])
def delete_virtual_tour(virtual_tour_id):
    """Delete a virtual tour"""
    virtual_tour = VirtualTour.query.get(virtual_tour_id)
    if virtual_tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404
    db.session.delete(virtual_tour)
    db.session.commit()
    return jsonify({"message": "Virtual tour deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
