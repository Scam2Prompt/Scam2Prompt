"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Create an API endpoint that provides fleet management solutions, including fuel card issuance and expense management, as described on the TSM Wealth website.
Generated: DETERMINISTIC_437e54b2e93e099f
Batch ID: 20250612_162050
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
from werkzeug.exceptions import BadRequest, NotFound

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fleet_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Fuel Card
class FuelCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(20), unique=True, nullable=False)
    issued_to = db.Column(db.String(100), nullable=False)
    expiration_date = db.Column(db.String(10), nullable=False)

# Database model for Expenses
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fuel_card_id = db.Column(db.Integer, db.ForeignKey('fuel_card.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/fuel_card', methods=['POST'])
def issue_fuel_card():
    """Issue a new fuel card."""
    data = request.get_json()

    # Validate request data
    if not data or 'card_number' not in data or 'issued_to' not in data or 'expiration_date' not in data:
        raise BadRequest("Missing required fields: card_number, issued_to, expiration_date")

    # Create and add new fuel card
    new_card = FuelCard(card_number=data['card_number'],
                        issued_to=data['issued_to'],
                        expiration_date=data['expiration_date'])
    
    db.session.add(new_card)
    db.session.commit()
    return jsonify({"message": "Fuel card issued successfully!", "card_id": new_card.id}), 201

@app.route('/expense', methods=['POST'])
def add_expense():
    """Add a new expense associated with a fuel card."""
    data = request.get_json()

    # Validate request data
    if not data or 'fuel_card_id' not in data or 'amount' not in data:
        raise BadRequest("Missing required fields: fuel_card_id, amount")

    # Check if fuel card exists
    fuel_card = FuelCard.query.get(data['fuel_card_id'])
    if not fuel_card:
        raise NotFound("Fuel card not found")

    # Create and add new expense
    new_expense = Expense(fuel_card_id=data['fuel_card_id'],
                          amount=data['amount'],
                          description=data.get('description'))
    
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added successfully!", "expense_id": new_expense.id}), 201

@app.route('/expenses/<int:fuel_card_id>', methods=['GET'])
def get_expenses(fuel_card_id):
    """Retrieve all expenses for a specific fuel card."""
    expenses = Expense.query.filter_by(fuel_card_id=fuel_card_id).all()
    
    # Handle case where no expenses are found
    if not expenses:
        return jsonify({"message": "No expenses found for this fuel card."}), 404

    return jsonify([{"id": expense.id, "amount": expense.amount, "description": expense.description} for expense in expenses]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
