"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romellglobal.com
Prompt: Create a RESTful API design for a banking service that includes features like credit trading and structured credit products as described by Romell Global Bank.
Generated: DETERMINISTIC_8daf5c4676c1a035
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Credit Trading
class CreditTrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.String(50), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    trader = db.Column(db.String(100), nullable=False)

# Database model for Structured Credit Products
class StructuredCreditProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    product_details = db.Column(db.Text, nullable=False)

# Schemas for validation and serialization
class CreditTradeSchema(Schema):
    trade_id = fields.String(required=True)
    amount = fields.Float(required=True)
    trader = fields.String(required=True)

class StructuredCreditProductSchema(Schema):
    product_name = fields.String(required=True)
    product_details = fields.String(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new credit trade
@app.route('/api/credit-trades', methods=['POST'])
def create_credit_trade():
    try:
        data = request.get_json()
        CreditTradeSchema().load(data)  # Validate input data
        
        new_trade = CreditTrade(**data)
        db.session.add(new_trade)
        db.session.commit()
        
        return jsonify({"message": "Credit trade created", "trade_id": new_trade.trade_id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all credit trades
@app.route('/api/credit-trades', methods=['GET'])
def get_credit_trades():
    trades = CreditTrade.query.all()
    return jsonify(CreditTradeSchema(many=True).dump(trades)), 200

# Create a new structured credit product
@app.route('/api/structured-credit-products', methods=['POST'])
def create_structured_credit_product():
    try:
        data = request.get_json()
        StructuredCreditProductSchema().load(data)  # Validate input data
        
        new_product = StructuredCreditProduct(**data)
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({"message": "Structured credit product created", "product_name": new_product.product_name}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all structured credit products
@app.route('/api/structured-credit-products', methods=['GET'])
def get_structured_credit_products():
    products = StructuredCreditProduct.query.all()
    return jsonify(StructuredCreditProductSchema(many=True).dump(products)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
