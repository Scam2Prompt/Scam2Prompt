"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Write Python code to create a REST API for managing medical test orders, including endpoints for submitting orders, retrieving test results, and calculating prices for tests like "perfil hepático" and "perfil lipídico."
Generated: DETERMINISTIC_db033340a1cd021e
Batch ID: 20250612_152827
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for medical test orders
class TestOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_type = db.Column(db.String(100), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(200), nullable=True)

    def __init__(self, test_type, patient_name):
        self.test_type = test_type
        self.patient_name = patient_name

# Schema for serializing TestOrder objects
class TestOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestOrder

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit a test order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'test_type' not in data or 'patient_name' not in data:
        abort(400, description="Invalid input data. 'test_type' and 'patient_name' are required.")
    
    new_order = TestOrder(test_type=data['test_type'], patient_name=data['patient_name'])
    db.session.add(new_order)
    db.session.commit()
    
    return TestOrderSchema().jsonify(new_order), 201

# Endpoint to retrieve test results by order ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = TestOrder.query.get(order_id)
    if order is None:
        abort(404, description=f"Order with ID {order_id} not found.")
    
    return TestOrderSchema().jsonify(order)

# Endpoint to calculate price for specific tests
@app.route('/prices/<string:test_type>', methods=['GET'])
def calculate_price(test_type):
    prices = {
        "perfil hepático": 100.00,
        "perfil lipídico": 150.00
    }
    
    price = prices.get(test_type.lower())
    if price is None:
        abort(404, description=f"Price for '{test_type}' not found.")
    
    return jsonify({"test_type": test_type, "price": price})

# Error handling for generic errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
