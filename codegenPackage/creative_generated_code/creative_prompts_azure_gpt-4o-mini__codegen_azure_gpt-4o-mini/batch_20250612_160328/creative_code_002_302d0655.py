"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Create a code snippet for a web application that allows users to compare different investment portfolios, including cannabis and crypto investments, as detailed by Brexphil Inc.
Generated: DETERMINISTIC_302d065559d86efc
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initializing Flask application
app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Investment Portfolio
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    cannabis_investment = db.Column(db.Float, nullable=False)
    crypto_investment = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Portfolio {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new investment portfolio
@app.route('/portfolio', methods=['POST'])
def create_portfolio():
    data = request.get_json()
    try:
        new_portfolio = Portfolio(
            name=data['name'],
            cannabis_investment=data['cannabis_investment'],
            crypto_investment=data['crypto_investment']
        )
        db.session.add(new_portfolio)
        db.session.commit()
        return jsonify({'message': 'Portfolio created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Portfolio name must be unique.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to compare existing portfolios
@app.route('/compare', methods=['GET'])
def compare_portfolios():
    portfolios = Portfolio.query.all()
    comparison = [
        {
            'name': portfolio.name,
            'cannabis_investment': portfolio.cannabis_investment,
            'crypto_investment': portfolio.crypto_investment
        }
        for portfolio in portfolios
    ]
    return jsonify(comparison), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found.'}), 404

# Running the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
