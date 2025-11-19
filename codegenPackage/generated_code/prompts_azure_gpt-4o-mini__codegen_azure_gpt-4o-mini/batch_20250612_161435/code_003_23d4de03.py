"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Develop a RESTful API for a service that provides quotes for retractable screens, similar to the customer support features of Ontario Screen Systems Inc.
Generated: DETERMINISTIC_23d4de03f2fa8766
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    screen_type = db.Column(db.String(100), nullable=False)
    quote_amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Quote object to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'screen_type': self.screen_type,
            'quote_amount': self.quote_amount
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/quotes', methods=['POST'])
def create_quote():
    """Create a new quote."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'customer_name' not in data or 'screen_type' not in data or 'quote_amount' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_quote = Quote(
        customer_name=data['customer_name'],
        screen_type=data['screen_type'],
        quote_amount=data['quote_amount']
    )

    try:
        db.session.add(new_quote)
        db.session.commit()
        return jsonify(new_quote.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create quote'}), 500

@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """Retrieve a quote by its ID."""
    quote = Quote.query.get(quote_id)
    if quote is None:
        return jsonify({'error': 'Quote not found'}), 404
    return jsonify(quote.to_dict()), 200

@app.route('/quotes', methods=['GET'])
def get_quotes():
    """Retrieve all quotes."""
    quotes = Quote.query.all()
    return jsonify([quote.to_dict() for quote in quotes]), 200

@app.route('/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    """Update an existing quote."""
    data = request.get_json()
    quote = Quote.query.get(quote_id)

    if quote is None:
        return jsonify({'error': 'Quote not found'}), 404

    if 'customer_name' in data:
        quote.customer_name = data['customer_name']
    if 'screen_type' in data:
        quote.screen_type = data['screen_type']
    if 'quote_amount' in data:
        quote.quote_amount = data['quote_amount']

    db.session.commit()
    return jsonify(quote.to_dict()), 200

@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    """Delete a quote by its ID."""
    quote = Quote.query.get(quote_id)
    if quote is None:
        return jsonify({'error': 'Quote not found'}), 404

    db.session.delete(quote)
    db.session.commit()
    return jsonify({'message': 'Quote deleted successfully'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
