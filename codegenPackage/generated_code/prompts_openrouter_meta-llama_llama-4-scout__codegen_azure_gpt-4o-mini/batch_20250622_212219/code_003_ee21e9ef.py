"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Design an API for buying and redeeming $BHOG bonds with $HOG, incorporating AI-set premiums for holders and AI-set discounts for buyers.
Generated: DETERMINISTIC_ee21e9ef57231bac
Batch ID: 20250622_212219
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
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bonds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Bond
class Bond(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holder_id = db.Column(db.Integer, nullable=False)
    premium = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Bond {self.id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to buy a bond
@app.route('/buy_bond', methods=['POST'])
def buy_bond():
    data = request.json
    holder_id = data.get('holder_id')
    amount = data.get('amount')

    if not holder_id or not amount:
        return jsonify({"error": "holder_id and amount are required"}), 400

    # Simulate AI-set discount
    discount = random.uniform(0.05, 0.15)  # 5% to 15% discount
    bond = Bond(holder_id=holder_id, premium=amount * (1 - discount), discount=discount)

    try:
        db.session.add(bond)
        db.session.commit()
        return jsonify({"message": "Bond purchased successfully", "bond_id": bond.id, "premium": bond.premium}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to purchase bond"}), 500

# Endpoint to redeem a bond
@app.route('/redeem_bond/<int:bond_id>', methods=['POST'])
def redeem_bond(bond_id):
    bond = Bond.query.get(bond_id)

    if not bond:
        return jsonify({"error": "Bond not found"}), 404

    # Simulate AI-set premium
    premium = bond.premium * random.uniform(1.1, 1.3)  # 10% to 30% premium
    db.session.delete(bond)

    try:
        db.session.commit()
        return jsonify({"message": "Bond redeemed successfully", "premium_received": premium}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to redeem bond", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
