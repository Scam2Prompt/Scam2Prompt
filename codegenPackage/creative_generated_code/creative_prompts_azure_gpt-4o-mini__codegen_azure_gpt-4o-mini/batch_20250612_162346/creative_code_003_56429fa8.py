"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gapkindo.org
Prompt: Develop a REST API that provides access to rubber price statistics and trends as outlined by GAPKINDO for developers interested in the rubber market.
Generated: DETERMINISTIC_56429fa8cc206200
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the database; replace with your own configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///rubber_prices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Rubber Price
class RubberPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    price_per_kg = db.Column(db.Float, nullable=False)

# Schema for validating input/output data
class RubberPriceSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    price_per_kg = fields.Float(required=True)

rubber_price_schema = RubberPriceSchema()
rubber_prices_schema = RubberPriceSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all rubber prices
@app.route('/api/rubber-prices', methods=['GET'])
def get_rubber_prices():
    prices = RubberPrice.query.all()
    return jsonify(rubber_prices_schema.dump(prices)), 200

# Endpoint to get rubber price by ID
@app.route('/api/rubber-prices/<int:id>', methods=['GET'])
def get_rubber_price(id):
    price = RubberPrice.query.get(id)
    if price is None:
        abort(404, description="Rubber price not found")
    return jsonify(rubber_price_schema.dump(price)), 200

# Endpoint to create a new rubber price
@app.route('/api/rubber-prices', methods=['POST'])
def create_rubber_price():
    try:
        data = request.get_json()
        rubber_price_schema.load(data)  # Validate input data
        new_price = RubberPrice(**data)
        db.session.add(new_price)
        db.session.commit()
        return jsonify(rubber_price_schema.dump(new_price)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Endpoint to update a rubber price
@app.route('/api/rubber-prices/<int:id>', methods=['PUT'])
def update_rubber_price(id):
    price = RubberPrice.query.get(id)
    if price is None:
        abort(404, description="Rubber price not found")

    try:
        data = request.get_json()
        rubber_price_schema.load(data)  # Validate input data
        for key, value in data.items():
            setattr(price, key, value)
        db.session.commit()
        return jsonify(rubber_price_schema.dump(price)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Endpoint to delete a rubber price
@app.route('/api/rubber-prices/<int:id>', methods=['DELETE'])
def delete_rubber_price(id):
    price = RubberPrice.query.get(id)
    if price is None:
        abort(404, description="Rubber price not found")

    db.session.delete(price)
    db.session.commit()
    return jsonify({"message": "Rubber price deleted successfully"}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": str(error)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
