"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Generate code to create a customer loyalty program API that allows users to register, earn points, and redeem rewards, similar to the "باشگاه مشتریان گلدن" system mentioned on the website.
Generated: DETERMINISTIC_5135ba71e0f0ce0a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loyalty_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Customer {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to register a new customer
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    new_customer = Customer(name=name)

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer registered successfully", "customer_id": new_customer.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Customer with this name already exists"}), 409

# API endpoint to earn points
@app.route('/earn_points', methods=['POST'])
def earn_points():
    data = request.get_json()
    customer_id = data.get('customer_id')
    points = data.get('points', 0)

    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    if points < 0:
        return jsonify({"error": "Points must be a positive value"}), 400

    customer.points += points
    db.session.commit()

    return jsonify({"message": "Points earned successfully", "total_points": customer.points}), 200

# API endpoint to redeem rewards
@app.route('/redeem', methods=['POST'])
def redeem():
    data = request.get_json()
    customer_id = data.get('customer_id')
    points = data.get('points', 0)

    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    if points < 0:
        return jsonify({"error": "Points must be a positive value"}), 400

    if customer.points < points:
        return jsonify({"error": "Insufficient points"}), 400

    customer.points -= points
    db.session.commit()

    return jsonify({"message": "Rewards redeemed successfully", "remaining_points": customer.points}), 200

# API endpoint to get customer information
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify({"id": customer.id, "name": customer.name, "points": customer.points}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
