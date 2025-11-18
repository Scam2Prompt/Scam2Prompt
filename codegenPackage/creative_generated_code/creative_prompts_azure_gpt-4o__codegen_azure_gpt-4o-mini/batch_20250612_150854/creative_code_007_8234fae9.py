"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Create an API that retrieves and ranks financial products based on ImmediateGains' transparent review criteria, such as user ratings, features, and cost-effectiveness.
Generated: DETERMINISTIC_8234fae93094d582
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Financial product model
class FinancialProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_rating = db.Column(db.Float, nullable=False)
    features = db.Column(db.String(500), nullable=False)
    cost_effectiveness = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_rating': self.user_rating,
            'features': self.features,
            'cost_effectiveness': self.cost_effectiveness
        }

# Error handler for database operations
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    response = {
        "success": False,
        "message": "Database error occurred.",
        "error": str(error)
    }
    return jsonify(response), 500

# Route to retrieve and rank financial products
@app.route('/api/financial-products', methods=['GET'])
def get_financial_products():
    try:
        # Get query parameters for filtering and sorting
        min_rating = request.args.get('min_rating', type=float, default=0)
        max_cost = request.args.get('max_cost', type=float, default=float('inf'))

        # Query the database for financial products
        products = FinancialProduct.query.filter(
            FinancialProduct.user_rating >= min_rating,
            FinancialProduct.cost_effectiveness <= max_cost
        ).all()

        # Rank products by user rating and cost-effectiveness
        ranked_products = sorted(products, key=lambda x: (x.user_rating, -x.cost_effectiveness), reverse=True)

        # Convert to dictionary format
        result = [product.to_dict() for product in ranked_products]

        return jsonify(result), 200

    except Exception as e:
        response = {
            "success": False,
            "message": "An error occurred while retrieving products.",
            "error": str(e)
        }
        return jsonify(response), 500

# Initialize the database (create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
