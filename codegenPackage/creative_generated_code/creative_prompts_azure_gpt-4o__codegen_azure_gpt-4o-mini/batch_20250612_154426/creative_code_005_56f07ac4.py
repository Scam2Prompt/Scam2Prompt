"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Create an API to manage debit card transactions while traveling, based on Genesis Investment Credit Union's debit card services.
Generated: DETERMINISTIC_56f07ac4eb19fda1
Batch ID: 20250612_154426
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)  # ISO currency code
    location = db.Column(db.String(100), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Transaction Schema for validation
class TransactionSchema(Schema):
    amount = fields.Float(required=True)
    currency = fields.String(required=True, validate=lambda s: len(s) == 3)
    location = fields.String(required=True)
    transaction_date = fields.DateTime(required=True)

transaction_schema = TransactionSchema()

@app.route('/transactions', methods=['POST'])
def create_transaction():
    """
    Create a new transaction for a debit card.
    ---
    request:
        - amount: Amount of transaction
        - currency: Currency code (ISO 4217)
        - location: Location of transaction
        - transaction_date: Date and time of transaction
    response:
        - 201 Created with transaction details
        - 400 Bad Request on validation errors
    """
    try:
        # Validate and deserialize input data
        transaction_data = request.json
        validated_data = transaction_schema.load(transaction_data)

        # Create new transaction
        new_transaction = Transaction(**validated_data)
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify(transaction_schema.dump(new_transaction)), 201

    except ValidationError as ve:
        return jsonify(ve.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Retrieve a transaction by its ID.
    ---
    response:
        - 200 OK with transaction details
        - 404 Not Found if transaction does not exist
    """
    transaction = Transaction.query.get(transaction_id)

    if transaction is None:
        return jsonify({"error": "Transaction not found"}), 404

    return jsonify(transaction_schema.dump(transaction)), 200

if __name__ == '__main__':
    app.run(debug=True)
```
