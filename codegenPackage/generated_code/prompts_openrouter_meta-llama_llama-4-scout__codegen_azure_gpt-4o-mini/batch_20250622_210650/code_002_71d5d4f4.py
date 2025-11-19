"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Design a basic web application using agile methodology for a retail business to digitalize their transaction system."
Generated: DETERMINISTIC_71d5d4f49b7f6686
Batch ID: 20250622_210650
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
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///transactions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id}: {self.item_name} - {self.quantity} @ {self.price}>'

# Route to create a new transaction
@app.route('/transactions', methods=['POST'])
def create_transaction():
    try:
        data = request.get_json()
        # Validate input data
        if not all(key in data for key in ('item_name', 'quantity', 'price')):
            return jsonify({'error': 'Missing data'}), 400
        
        # Create a new transaction
        transaction = Transaction(
            item_name=data['item_name'],
            quantity=data['quantity'],
            price=data['price'],
            total=data['quantity'] * data['price']
        )
        db.session.add(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction created', 'transaction_id': transaction.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    try:
        transactions = Transaction.query.all()
        return jsonify([{
            'id': t.id,
            'item_name': t.item_name,
            'quantity': t.quantity,
            'price': t.price,
            'total': t.total
        } for t in transactions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific transaction by ID
@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    try:
        transaction = Transaction.query.get_or_404(transaction_id)
        return jsonify({
            'id': transaction.id,
            'item_name': transaction.item_name,
            'quantity': transaction.quantity,
            'price': transaction.price,
            'total': transaction.total
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a transaction
@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        transaction = Transaction.query.get_or_404(transaction_id)
        db.session.delete(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction deleted'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Instructions for Running the Application
1. Ensure you have Python installed on your machine.
2. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
3. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Use a tool like Postman or curl to interact with the API.
