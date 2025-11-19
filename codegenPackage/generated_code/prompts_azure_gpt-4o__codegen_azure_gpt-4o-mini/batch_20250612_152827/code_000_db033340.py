"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Write Python code to create a REST API for managing medical test orders, including endpoints for submitting orders, retrieving test results, and calculating prices for tests like "perfil hepático" and "perfil lipídico."
Generated: DETERMINISTIC_db033340a1cd021e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_tests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TestOrder model
class TestOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(100), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'test_name': self.test_name,
            'patient_name': self.patient_name,
            'result': self.result
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a new test order
@app.route('/orders', methods=['POST'])
def submit_order():
    data = request.get_json()
    if not data or 'test_name' not in data or 'patient_name' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_order = TestOrder(test_name=data['test_name'], patient_name=data['patient_name'])
    db.session.add(new_order)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create order'}), 500

    return jsonify(new_order.to_dict()), 201

# Endpoint to retrieve test results by order ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = TestOrder.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.to_dict()), 200

# Endpoint to calculate prices for specific tests
@app.route('/prices', methods=['GET'])
def calculate_price():
    test_name = request.args.get('test_name')
    prices = {
        'perfil hepático': 150.00,
        'perfil lipídico': 120.00
    }
    
    if test_name not in prices:
        return jsonify({'error': 'Test not found'}), 404

    return jsonify({'test_name': test_name, 'price': prices[test_name]}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
