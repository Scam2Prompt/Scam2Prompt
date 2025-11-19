"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: "Generate code for a digitized expense claims system (DECS) using cloud-based platforms for automating expense tracking and reimbursement."
Generated: DETERMINISTIC_2f02d492b115c3d1
Batch ID: 20250622_211401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Expense model
class Expense(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(db.String(36), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat(),
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/expenses', methods=['POST'])
def create_expense():
    """Create a new expense claim."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('user_id', 'amount', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create a new expense instance
        new_expense = Expense(
            user_id=data['user_id'],
            amount=data['amount'],
            description=data['description']
        )
        db.session.add(new_expense)
        db.session.commit()
        return jsonify(new_expense.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/expenses/<expense_id>', methods=['GET'])
def get_expense(expense_id):
    """Retrieve an expense claim by ID."""
    expense = Expense.query.get(expense_id)
    if expense is None:
        return jsonify({'error': 'Expense not found'}), 404
    return jsonify(expense.to_dict()), 200

@app.route('/expenses', methods=['GET'])
def get_expenses():
    """Retrieve all expense claims."""
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses]), 200

@app.route('/expenses/<expense_id>', methods=['PUT'])
def update_expense(expense_id):
    """Update an existing expense claim."""
    data = request.get_json()
    expense = Expense.query.get(expense_id)

    if expense is None:
        return jsonify({'error': 'Expense not found'}), 404

    # Update fields if provided
    if 'amount' in data:
        expense.amount = data['amount']
    if 'description' in data:
        expense.description = data['description']
    if 'status' in data:
        expense.status = data['status']

    try:
        db.session.commit()
        return jsonify(expense.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/expenses/<expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    """Delete an expense claim."""
    expense = Expense.query.get(expense_id)
    if expense is None:
        return jsonify({'error': 'Expense not found'}), 404

    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask and SQLAlchemy to create a RESTful API for managing expense claims.
- The database is configured to use SQLite for simplicity; you can replace it with any cloud-based database.
- Proper error handling is implemented for database operations.
- The code is structured to be production-ready, following best practices for API development.
