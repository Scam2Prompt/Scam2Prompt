"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a sample API for a brand activation service that tracks customer engagement and product literacy, based on the experiential marketing strategies of Paradigm Group.
Generated: DETERMINISTIC_d7a89ea1b33f3c8d
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Brand Activation Service API**
================================

### Dependencies

* `flask`: For building the API
* `flask_sqlalchemy`: For database interactions
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///brand_activation.db"
db = SQLAlchemy(app)


# Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = db.relationship("Customer", backref=db.backref("engagements", lazy=True))
    engagement_type = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, customer_id, engagement_type, timestamp):
        self.customer_id = customer_id
        self.engagement_type = engagement_type
        self.timestamp = timestamp


class ProductLiteracy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = db.relationship("Customer", backref=db.backref("product_literacies", lazy=True))
    product_name = db.Column(db.String(100), nullable=False)
    literacy_level = db.Column(db.String(100), nullable=False)

    def __init__(self, customer_id, product_name, literacy_level):
        self.customer_id = customer_id
        self.product_name = product_name
        self.literacy_level = literacy_level


# Schemas
class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)


class EngagementSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    engagement_type = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    timestamp = fields.DateTime(required=True)


class ProductLiteracySchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    product_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    literacy_level = fields.Str(required=True, validate=validate.Length(min=1, max=100))


# API Endpoints
@app.route("/customers", methods=["GET", "POST"])
def customers():
    try:
        if request.method == "GET":
            customers = Customer.query.all()
            schema = CustomerSchema(many=True)
            return jsonify(schema.dump(customers))
        elif request.method == "POST":
            schema = CustomerSchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            customer = Customer(data["name"], data["email"])
            db.session.add(customer)
            db.session.commit()
            return jsonify(schema.dump(customer)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/engagements", methods=["GET", "POST"])
def engagements():
    try:
        if request.method == "GET":
            engagements = Engagement.query.all()
            schema = EngagementSchema(many=True)
            return jsonify(schema.dump(engagements))
        elif request.method == "POST":
            schema = EngagementSchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            engagement = Engagement(data["customer_id"], data["engagement_type"], data["timestamp"])
            db.session.add(engagement)
            db.session.commit()
            return jsonify(schema.dump(engagement)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/product-literacy", methods=["GET", "POST"])
def product_literacy():
    try:
        if request.method == "GET":
            product_literacies = ProductLiteracy.query.all()
            schema = ProductLiteracySchema(many=True)
            return jsonify(schema.dump(product_literacies))
        elif request.method == "POST":
            schema = ProductLiteracySchema()
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400
            product_literacy = ProductLiteracy(data["customer_id"], data["product_name"], data["literacy_level"])
            db.session.add(product_literacy)
            db.session.commit()
            return jsonify(schema.dump(product_literacy)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
