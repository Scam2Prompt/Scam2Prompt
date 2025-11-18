"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Develop a web application feature that mimics Renzo Cash's investment package selection and daily profit tracking, including options for multiple simultaneous investments.
Generated: DETERMINISTIC_3cfab54526e3facd
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Investment model definition
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    daily_profit_rate = db.Column(db.Float, nullable=False)  # Expressed as a decimal
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def daily_profit(self):
        """Calculate daily profit based on investment amount and rate."""
        return self.amount * self.daily_profit_rate

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/invest', methods=['POST'])
def invest():
    """Endpoint to create a new investment package for a user."""
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    daily_profit_rate = data.get('daily_profit_rate')

    # Validate input data
    if not user_id or not amount or not daily_profit_rate:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create new investment
    new_investment = Investment(user_id=user_id, amount=amount, daily_profit_rate=daily_profit_rate)
    db.session.add(new_investment)
    
    try:
        db.session.commit()
        return jsonify({'message': 'Investment created successfully', 'id': new_investment.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

@app.route('/profit/<int:user_id>', methods=['GET'])
def track_profit(user_id):
    """Endpoint to track daily profits for a user."""
    investments = Investment.query.filter_by(user_id=user_id).all()
    
    if not investments:
        return jsonify({'message': 'No investments found for this user'}), 404
    
    # Calculate total daily profit for all investments
    total_profit = sum(investment.daily_profit() for investment in investments)
    response = {
        'user_id': user_id,
        'total_daily_profit': total_profit,
        'investments': [
            {
                'id': investment.id,
                'amount': investment.amount,
                'daily_profit': investment.daily_profit(),
                'start_date': investment.start_date.strftime('%Y-%m-%d')
            } for investment in investments
        ]
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
```
