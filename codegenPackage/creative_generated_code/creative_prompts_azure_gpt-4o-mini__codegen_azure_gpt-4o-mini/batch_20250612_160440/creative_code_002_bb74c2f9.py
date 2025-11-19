"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Create a REST API endpoint that allows users to submit their investment details and receive a breakdown of expected profits according to the plans provided by RapidCoinTrades.
Generated: DETERMINISTIC_bb74c2f91542879c
Batch ID: 20250612_160440
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)

# Investment schema for validation
class InvestmentSchema(Schema):
    amount = fields.Float(required=True)
    plan_type = fields.String(required=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/investments', methods=['POST'])
def submit_investment():
    """Endpoint to submit investment details and receive profit breakdown."""
    json_data = request.get_json()

    # Validate request data
    schema = InvestmentSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Store investment in the database
    investment = Investment(amount=data['amount'], plan_type=data['plan_type'])
    db.session.add(investment)
    db.session.commit()

    # Calculate expected profits based on plan type
    profit = calculate_profit(data['amount'], data['plan_type'])

    # Return the investment details along with the expected profit
    return jsonify({
        "id": investment.id,
        "amount": investment.amount,
        "plan_type": investment.plan_type,
        "expected_profit": profit
    }), 201

def calculate_profit(amount, plan_type):
    """Calculate expected profit based on the investment plan type."""
    # Define profit percentages for different plans
    profit_plan = {
        'basic': 0.05,        # 5% profit for basic plan
        'premium': 0.1,       # 10% profit for premium plan
        'vip': 0.15           # 15% profit for VIP plan
    }

    # Calculate profit based on provided plan type
    profit_percentage = profit_plan.get(plan_type.lower())
    if profit_percentage is None:
        raise ValueError("Invalid plan type provided.")
    
    return amount * profit_percentage

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
