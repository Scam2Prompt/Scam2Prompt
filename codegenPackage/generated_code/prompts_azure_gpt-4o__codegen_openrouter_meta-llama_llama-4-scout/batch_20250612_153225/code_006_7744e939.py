"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application that integrates investment portfolio tracking and analysis tools, allowing users to monitor long-term investment performance, as described in TSM Wealth's services.
Generated: DETERMINISTIC_7744e93928b73879
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_tracker.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import yfinance as yf
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Investment('{self.symbol}', '{self.name}', {self.purchase_price}, {self.purchase_date}, {self.quantity})"

class Portfolio:
    def __init__(self):
        self.investments = []

    def add_investment(self, investment):
        self.investments.append(investment)

    def get_investments(self):
        return self.investments

    def calculate_total_value(self):
        total_value = 0
        for investment in self.investments:
            current_price = yf.Ticker(investment.symbol).info['currentPrice']
            total_value += current_price * investment.quantity
        return total_value

    def calculate_total_return(self):
        total_return = 0
        for investment in self.investments:
            current_price = yf.Ticker(investment.symbol).info['currentPrice']
            purchase_price = investment.purchase_price
            total_return += ((current_price - purchase_price) / purchase_price) * investment.quantity
        return total_return

@app.route('/investments', methods=['POST'])
def create_investment():
    try:
        data = request.get_json()
        investment = Investment(
            symbol=data['symbol'],
            name=data['name'],
            purchase_price=data['purchase_price'],
            purchase_date=datetime.strptime(data['purchase_date'], '%Y-%m-%d'),
            quantity=data['quantity']
        )
        db.session.add(investment)
        db.session.commit()
        return jsonify({'message': 'Investment created successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@app.route('/investments', methods=['GET'])
def get_investments():
    try:
        investments = Investment.query.all()
        portfolio = Portfolio()
        for investment in investments:
            portfolio.add_investment(investment)
        return jsonify([{
            'symbol': investment.symbol,
            'name': investment.name,
            'purchase_price': investment.purchase_price,
            'purchase_date': investment.purchase_date,
            'quantity': investment.quantity,
            'current_price': yf.Ticker(investment.symbol).info['currentPrice'],
            'current_value': yf.Ticker(investment.symbol).info['currentPrice'] * investment.quantity
        } for investment in portfolio.get_investments()])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    try:
        investments = Investment.query.all()
        portfolio = Portfolio()
        for investment in investments:
            portfolio.add_investment(investment)
        return jsonify({
            'total_value': portfolio.calculate_total_value(),
            'total_return': portfolio.calculate_total_return()
        })
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt

Flask
Flask-SQLAlchemy
yfinance
```

```sql
-- schema.sql

CREATE TABLE investments (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL,
    purchase_price REAL NOT NULL,
    purchase_date TEXT NOT NULL,
    quantity INTEGER NOT NULL
);
```
