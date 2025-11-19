"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Develop a secure backend system using Flask or Django to handle title service order submissions, including transaction type and special instructions, based on the workflow described on the Superior Title Montana website.
Generated: DETERMINISTIC_d1d6f17c78bac357
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure Backend System using Flask**
=====================================

### Requirements

* Python 3.9+
* Flask 2.2+
* Flask-SQLAlchemy 2.5+
* Flask-Marshmallow 0.14+

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///title_service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(100), nullable=False)
    special_instructions = db.Column(db.Text, nullable=True)

    def __init__(self, transaction_type, special_instructions=None):
        self.transaction_type = transaction_type
        self.special_instructions = special_instructions

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        
        transaction_type = data.get('transaction_type')
        if not transaction_type:
            return jsonify({'message': 'Transaction type is required'}), 400
        
        special_instructions = data.get('special_instructions')
        
        new_order = Order(transaction_type, special_instructions)
        db.session.add(new_order)
        db.session.commit()
        
        return order_schema.jsonify(new_order), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return orders_schema.jsonify(orders)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/orders/<id>', methods=['GET'])
def get_order(id):
    try:
        order = Order.query.get(id)
        if not order:
            return jsonify({'message': 'Order not found'}), 404
        
        return order_schema.jsonify(order)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    try:
        order = Order.query.get(id)
        if not order:
            return jsonify({'message': 'Order not found'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        
        transaction_type = data.get('transaction_type')
        if transaction_type:
            order.transaction_type = transaction_type
        
        special_instructions = data.get('special_instructions')
        if special_instructions is not None:
            order.special_instructions = special_instructions
        
        db.session.commit()
        
        return order_schema.jsonify(order)
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@app.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    try:
        order = Order.query.get(id)
        if not order:
            return jsonify({'message': 'Order not found'}), 404
        
        db.session.delete(order)
        db.session.commit()
        
        return jsonify({'message': 'Order deleted'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### API Endpoints

* `POST /orders`: Create a new order
* `GET /orders`: Get all orders
* `GET /orders/<id>`: Get an order by ID
* `PUT /orders/<id>`: Update an order
* `DELETE /orders/<id>`: Delete an order

### Request/Response Examples

* `POST /orders`:
```json
{
    "transaction_type": "Title Search",
    "special_instructions": "Please include all lien holders"
}
```
Response:
```json
{
    "id": 1,
    "transaction_type": "Title Search",
    "special_instructions": "Please include all lien holders"
}
```
* `GET /orders`:
```json
[
    {
        "id": 1,
        "transaction_type": "Title Search",
        "special_instructions": "Please include all lien holders"
    },
    {
        "id": 2,
        "transaction_type": "Title Commitment",
        "special_instructions": null
    }
]
```
