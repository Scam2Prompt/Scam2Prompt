"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Develop a RESTful API for a service that provides quotes for retractable screens, similar to the customer support features of Ontario Screen Systems Inc.
Generated: DETERMINISTIC_23d4de03f2fa8766
Batch ID: 20250612_161435
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Quote model for the database
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    screen_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Quote {self.id}: {self.customer_name}, {self.screen_type}, ${self.price}>"

# Create a schema for serializing Quote objects
class QuoteSchema(Schema):
    id = fields.Int()
    customer_name = fields.Str(required=True)
    screen_type = fields.Str(required=True)
    price = fields.Float(required=True)

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)

# Endpoint to create a new quote
@app.route('/quotes', methods=['POST'])
def create_quote():
    """Create a new quote and store it in the database."""
    try:
        # Validate and deserialize input
        data = quote_schema.load(request.json)
        new_quote = Quote(**data)
        db.session.add(new_quote)
        db.session.commit()
        return quote_schema.dump(new_quote), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating quote: {str(e)}")
        return jsonify({"error": "Could not create quote."}), 500

# Endpoint to get all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    """Retrieve all quotes from the database."""
    try:
        quotes = Quote.query.all()
        return quotes_schema.dump(quotes), 200
    except Exception as e:
        logging.error(f"Error retrieving quotes: {str(e)}")
        return jsonify({"error": "Could not retrieve quotes."}), 500

# Endpoint to get a specific quote by ID
@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """Retrieve a specific quote by its ID."""
    try:
        quote = Quote.query.get_or_404(quote_id)
        return quote_schema.dump(quote), 200
    except Exception as e:
        logging.error(f"Error retrieving quote {quote_id}: {str(e)}")
        return jsonify({"error": "Could not retrieve quote."}), 500

# Endpoint to update a quote by ID
@app.route('/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    """Update an existing quote by its ID."""
    try:
        data = quote_schema.load(request.json)
        quote = Quote.query.get_or_404(quote_id)
        for key, value in data.items():
            setattr(quote, key, value)
        db.session.commit()
        return quote_schema.dump(quote), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating quote {quote_id}: {str(e)}")
        return jsonify({"error": "Could not update quote."}), 500

# Endpoint to delete a quote by ID
@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    """Delete a specific quote by its ID."""
    try:
        quote = Quote.query.get_or_404(quote_id)
        db.session.delete(quote)
        db.session.commit()
        return jsonify({"message": "Quote deleted."}), 204
    except Exception as e:
        logging.error(f"Error deleting quote {quote_id}: {str(e)}")
        return jsonify({"error": "Could not delete quote."}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
