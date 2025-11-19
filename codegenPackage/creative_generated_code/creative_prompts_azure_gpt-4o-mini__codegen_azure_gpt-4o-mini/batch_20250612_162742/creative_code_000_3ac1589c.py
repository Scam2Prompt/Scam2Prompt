"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyal.credit
Prompt: What are the key features of the loyalty program offered by Loyal Credit, and how can I implement a similar API for managing customer rewards?
Generated: DETERMINISTIC_3ac1589cbbdc4ba7
Batch ID: 20250612_162742
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loyalty_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'points': self.points
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Error handling for invalid requests
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request."}), 400

# Endpoint to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    if not request.json or 'name' not in request.json:
        abort(400)

    new_customer = Customer(name=request.json['name'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201

# Endpoint to add points to a customer
@app.route('/customers/<int:customer_id>/add_points', methods=['POST'])
def add_points(customer_id):
    if not request.json or 'points' not in request.json:
        abort(400)

    customer = Customer.query.get(customer_id)
    if customer is None:
        abort(404)

    customer.points += request.json['points']
    db.session.commit()
    return jsonify(customer.to_dict()), 200

# Endpoint to redeem points
@app.route('/customers/<int:customer_id>/redeem', methods=['POST'])
def redeem_points(customer_id):
    if not request.json or 'points' not in request.json:
        abort(400)

    customer = Customer.query.get(customer_id)
    if customer is None:
        abort(404)

    if request.json['points'] > customer.points:
        return jsonify({"error": "Insufficient points."}), 400

    customer.points -= request.json['points']
    db.session.commit()
    return jsonify(customer.to_dict()), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
