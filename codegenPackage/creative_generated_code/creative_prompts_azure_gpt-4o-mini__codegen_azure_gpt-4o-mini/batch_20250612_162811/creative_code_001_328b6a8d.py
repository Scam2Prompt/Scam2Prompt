"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investmentbrokertransactions.com
Prompt: Write a code snippet for a technical team to develop an MVP for a startup, referencing the full technical services provided by Investment Brokers.
Generated: DETERMINISTIC_328b6a8dbec9fed5
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Broker MVP Application

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_brokers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Investor
class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'<Investor {self.name}>'

# Model for Investment
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investor_id = db.Column(db.Integer, db.ForeignKey('investor.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    investment_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Investment {self.amount} by Investor ID {self.investor_id}>'

# Error handling for the application
@app.errorhandler(HTTPException)
def handle_error(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description})
    response.content_type = "application/json"
    return response

# Route to add a new investor
@app.route('/investors', methods=['POST'])
def add_investor():
    """Add a new investor to the database."""
    data = request.json
    try:
        new_investor = Investor(name=data['name'], email=data['email'])
        db.session.add(new_investor)
        db.session.commit()
        return jsonify({"message": "Investor added successfully!", "investor_id": new_investor.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all investors
@app.route('/investors', methods=['GET'])
def get_investors():
    """Get a list of all investors."""
    investors = Investor.query.all()
    return jsonify([{"id": inv.id, "name": inv.name, "email": inv.email} for inv in investors]), 200

# Route to add a new investment
@app.route('/investments', methods=['POST'])
def add_investment():
    """Add a new investment to an investor."""
    data = request.json
    try:
        new_investment = Investment(
            investor_id=data['investor_id'],
            amount=data['amount'],
            investment_type=data['investment_type']
        )
        db.session.add(new_investment)
        db.session.commit()
        return jsonify({"message": "Investment added successfully!", "investment_id": new_investment.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all investments for a specific investor
@app.route('/investments/<int:investor_id>', methods=['GET'])
def get_investments(investor_id):
    """Get all investments for a specific investor."""
    investments = Investment.query.filter_by(investor_id=investor_id).all()
    return jsonify([{"id": inv.id, "amount": inv.amount, "investment_type": inv.investment_type} for inv in investments]), 200

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
