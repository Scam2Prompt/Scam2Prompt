"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Create a code snippet for a web application that allows users to compare different investment portfolios, including cannabis and crypto investments, as detailed by Brexphil Inc.
Generated: DETERMINISTIC_302d065559d86efc
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cannabis_investment = db.Column(db.Float, nullable=False)
    crypto_investment = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for validating portfolio data
class PortfolioSchema(Schema):
    name = fields.Str(required=True)
    cannabis_investment = fields.Float(required=True)
    crypto_investment = fields.Float(required=True)

# Initialize the schema
portfolio_schema = PortfolioSchema()
portfolios_schema = PortfolioSchema(many=True)

# Route to create a new portfolio
@app.route('/portfolios', methods=['POST'])
def create_portfolio():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        portfolio_data = portfolio_schema.load(data)

        # Create a new portfolio instance
        new_portfolio = Portfolio(**portfolio_data)
        db.session.add(new_portfolio)
        db.session.commit()

        return jsonify(portfolio_schema.dump(new_portfolio)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all portfolios
@app.route('/portfolios', methods=['GET'])
def get_portfolios():
    try:
        portfolios = Portfolio.query.all()
        return jsonify(portfolios_schema.dump(portfolios)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to compare portfolios
@app.route('/compare', methods=['GET'])
def compare_portfolios():
    try:
        # Get portfolio IDs from query parameters
        ids = request.args.getlist('id', type=int)
        portfolios = Portfolio.query.filter(Portfolio.id.in_(ids)).all()

        if not portfolios:
            return jsonify({"error": "No portfolios found for the given IDs."}), 404

        # Prepare comparison data
        comparison_data = {
            "total_cannabis_investment": sum(p.cannabis_investment for p in portfolios),
            "total_crypto_investment": sum(p.crypto_investment for p in portfolios),
            "portfolio_count": len(portfolios)
        }

        return jsonify(comparison_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
