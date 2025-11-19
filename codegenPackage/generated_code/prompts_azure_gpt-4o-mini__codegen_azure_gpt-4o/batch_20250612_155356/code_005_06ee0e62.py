"""
Generated Code Metadata:
========================
Original URL: https://cma.or.ke
Prompt: Construct a web application that allows users to track their investments in collective investment schemes as per the CMA's licensing information.
Generated: DETERMINISTIC_06ee0e622462f30e
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a web application using Python's Flask framework for tracking investments in collective investment schemes. It includes error handling, comments, and follows best practices.

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity; replace with production-grade DB in real-world use)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scheme_name = db.Column(db.String(100), nullable=False)
    amount_invested = db.Column(db.Float, nullable=False)
    date_invested = db.Column(db.Date, nullable=False)
    user_email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'scheme_name': self.scheme_name,
            'amount_invested': self.amount_invested,
            'date_invested': self.date_invested.isoformat(),
            'user_email': self.user_email
        }

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route: Add a new investment
@app.route('/investments', methods=['POST'])
def add_investment():
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ('scheme_name', 'amount_invested', 'date_invested', 'user_email')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new investment record
        investment = Investment(
            scheme_name=data['scheme_name'],
            amount_invested=data['amount_invested'],
            date_invested=data['date_invested'],
            user_email=data['user_email']
        )
        db.session.add(investment)
        db.session.commit()
        return jsonify({'message': 'Investment added successfully', 'investment': investment.to_dict()}), 201
    except IntegrityError:
        db.session.rollback()
        logging.error("Database integrity error occurred.")
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Route: Get all investments
@app.route('/investments', methods=['GET'])
def get_investments():
    try:
        investments = Investment.query.all()
        return jsonify([investment.to_dict() for investment in investments]), 200
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Route: Get investment by ID
@app.route('/investments/<int:id>', methods=['GET'])
def get_investment_by_id(id):
    try:
        investment = Investment.query.get(id)
        if not investment:
            return jsonify({'error': 'Investment not found'}), 404
        return jsonify(investment.to_dict()), 200
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Route: Update an investment
@app.route('/investments/<int:id>', methods=['PUT'])
def update_investment(id):
    try:
        investment = Investment.query.get(id)
        if not investment:
            return jsonify({'error': 'Investment not found'}), 404

        data = request.json
        # Update fields if provided
        investment.scheme_name = data.get('scheme_name', investment.scheme_name)
        investment.amount_invested = data.get('amount_invested', investment.amount_invested)
        investment.date_invested = data.get('date_invested', investment.date_invested)
        investment.user_email = data.get('user_email', investment.user_email)

        db.session.commit()
        return jsonify({'message': 'Investment updated successfully', 'investment': investment.to_dict()}), 200
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Route: Delete an investment
@app.route('/investments/<int:id>', methods=['DELETE'])
def delete_investment(id):
    try:
        investment = Investment.query.get(id)
        if not investment:
            return jsonify({'error': 'Investment not found'}), 404

        db.session.delete(investment)
        db.session.commit()
        return jsonify({'message': 'Investment deleted successfully'}), 200
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Install dependencies using `pip install flask flask-sqlalchemy`.
2. Replace SQLite with a production-grade database (e.g., PostgreSQL) for deployment.
3. Use environment variables for sensitive configurations (e.g., database URI).
4. Add authentication and authorization for user-specific data access in production.
