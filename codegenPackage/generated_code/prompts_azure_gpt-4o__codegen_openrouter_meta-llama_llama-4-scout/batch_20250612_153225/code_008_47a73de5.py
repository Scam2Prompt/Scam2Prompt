"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Develop a REST API for a product return and exchange system, ensuring compliance with conditions like "امکان بازگشت کالا تا ۷ روز" for bulk purchases, as outlined on the website.
Generated: DETERMINISTIC_47a73de503d1a74f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Product Return and Exchange System REST API**
====================================================

**dependencies**
---------------

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

**Code**
------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///returns.db"
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, purchase_date, quantity):
        self.name = name
        self.purchase_date = purchase_date
        self.quantity = quantity


class ReturnRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    product = db.relationship("Product", backref=db.backref("returns", lazy=True))
    return_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, product_id, return_date):
        self.product_id = product_id
        self.return_date = return_date


class ExchangeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    return_request_id = db.Column(db.Integer, db.ForeignKey("return_request.id"), nullable=False)
    return_request = db.relationship("ReturnRequest", backref=db.backref("exchanges", lazy=True))
    exchange_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, return_request_id, exchange_date):
        self.return_request_id = return_request_id
        self.exchange_date = exchange_date


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    purchase_date = fields.DateTime(required=True)
    quantity = fields.Int(required=True)


class ReturnRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    return_date = fields.DateTime(required=True)
    status = fields.Str()


class ExchangeRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    return_request_id = fields.Int(required=True)
    exchange_date = fields.DateTime(required=True)
    status = fields.Str()


# Create the database tables
with app.app_context():
    db.create_all()


# API Endpoints
@app.route("/products", methods=["POST"])
def create_product():
    try:
        schema = ProductSchema()
        data = schema.load(request.json)
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return jsonify(schema.dump(product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@app.route("/products/<int:product_id>/returns", methods=["POST"])
def create_return_request(product_id):
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        schema = ReturnRequestSchema()
        data = schema.load(request.json)
        if (datetime.now() - product.purchase_date).days > 7 and product.quantity > 1:
            return jsonify({"error": "امکان بازگشت کالا تا ۷ روز برای خریدهای عمده وجود ندارد"}), 400

        return_request = ReturnRequest(product_id=product_id, return_date=data["return_date"])
        db.session.add(return_request)
        db.session.commit()
        return jsonify(schema.dump(return_request)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@app.route("/return-requests/<int:return_request_id>/exchanges", methods=["POST"])
def create_exchange_request(return_request_id):
    try:
        return_request = ReturnRequest.query.get(return_request_id)
        if not return_request:
            return jsonify({"error": "Return request not found"}), 404

        schema = ExchangeRequestSchema()
        data = schema.load(request.json)
        exchange_request = ExchangeRequest(return_request_id=return_request_id, exchange_date=data["exchange_date"])
        db.session.add(exchange_request)
        db.session.commit()
        return jsonify(schema.dump(exchange_request)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
