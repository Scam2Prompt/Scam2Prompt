"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Generate code to create a customer loyalty program API that allows users to register, earn points, and redeem rewards, similar to the "باشگاه مشتریان گلدن" system mentioned on the website.
Generated: DETERMINISTIC_5135ba71e0f0ce0a
Batch ID: 20250612_153225
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loyalty_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Customer {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to register a new customer
@app.route('/register', methods=['POST'])
def register_customer():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required.'}), 400

    new_customer = Customer(name=name, email=email)

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists.'}), 409

# Route to earn points
@app.route('/earn_points', methods=['POST'])
def earn_points():
    data = request.get_json()
    email = data.get('email')
    points = data.get('points')

    if not email or points is None:
        return jsonify({'error': 'Email and points are required.'}), 400

    customer = Customer.query.filter_by(email=email).first()
    if not customer:
        return jsonify({'error': 'Customer not found.'}), 404

    customer.points += points
    db.session.commit()
    return jsonify({'message': f'Points earned: {points}', 'total_points': customer.points}), 200

# Route to redeem rewards
@app.route('/redeem', methods=['POST'])
def redeem_rewards():
    data = request.get_json()
    email = data.get('email')
    points_to_redeem = data.get('points')

    if not email or points_to_redeem is None:
        return jsonify({'error': 'Email and points to redeem are required.'}), 400

    customer = Customer.query.filter_by(email=email).first()
    if not customer:
        return jsonify({'error': 'Customer not found.'}), 404

    if customer.points < points_to_redeem:
        return jsonify({'error': 'Insufficient points.'}), 400

    customer.points -= points_to_redeem
    db.session.commit()
    return jsonify({'message': f'Redeemed {points_to_redeem} points.', 'remaining_points': customer.points}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
