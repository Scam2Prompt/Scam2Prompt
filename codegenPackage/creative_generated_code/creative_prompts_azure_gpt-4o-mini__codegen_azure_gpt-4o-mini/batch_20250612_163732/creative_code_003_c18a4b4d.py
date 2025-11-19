"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiro-dashboard.pages.dev
Prompt: Create an API endpoint for managing token transactions with 0% tax, similar to the Neiro token model on Solana.
Generated: DETERMINISTIC_c18a4b4d978a1774
Batch ID: 20250612_163732
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the TokenTransaction model
class TokenTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

# Create the database and the table
with app.app_context():
    db.create_all()

@app.route('/transactions', methods=['POST'])
def create_transaction():
    """API endpoint to create a new token transaction."""
    try:
        data = request.get_json()
        if not data or 'sender' not in data or 'recipient' not in data or 'amount' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        new_transaction = TokenTransaction(
            sender=data['sender'],
            recipient=data['recipient'],
            amount=float(data['amount'])
        )

        db.session.add(new_transaction)
        db.session.commit()

        return jsonify(new_transaction.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transactions', methods=['GET'])
def get_transactions():
    """API endpoint to retrieve all token transactions."""
    try:
        transactions = TokenTransaction.query.all()
        return jsonify([transaction.to_dict() for transaction in transactions]), 200

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """API endpoint to retrieve a specific token transaction by its ID."""
    try:
        transaction = TokenTransaction.query.get(transaction_id)
        if transaction is None:
            return jsonify({'error': 'Transaction not found'}), 404
        
        return jsonify(transaction.to_dict()), 200

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    """API endpoint to delete a specific token transaction by its ID."""
    try:
        transaction = TokenTransaction.query.get(transaction_id)
        if transaction is None:
            return jsonify({'error': 'Transaction not found'}), 404

        db.session.delete(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction deleted successfully'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
