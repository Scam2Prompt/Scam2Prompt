"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Generate an API design for KEK Insurance Brokers that allows users to request quotes for various insurance services, such as construction risk management or marine insurance, as outlined on their webpage.
Generated: DETERMINISTIC_9725d00682269f5d
Batch ID: 20250612_151811
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance_quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insurance_type = db.Column(db.String(50), nullable=False)
    coverage_amount = db.Column(db.Float, nullable=False)
    user_contact = db.Column(db.String(100), nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

# Define the Quote Schema for input validation
class QuoteSchema(Schema):
    insurance_type = fields.String(required=True)
    coverage_amount = fields.Float(required=True)
    user_contact = fields.String(required=True)

quote_schema = QuoteSchema()

@app.route('/api/quotes', methods=['POST'])
def request_quote():
    """
    API endpoint to request a new insurance quote.
    Expects a JSON payload with insurance_type, coverage_amount, and user_contact.
    """
    try:
        # Validate input data
        data = request.get_json(force=True)
        validated_data = quote_schema.load(data)

        # Create a new Quote instance
        new_quote = Quote(
            insurance_type=validated_data['insurance_type'],
            coverage_amount=validated_data['coverage_amount'],
            user_contact=validated_data['user_contact']
        )

        # Save the quote to the database
        db.session.add(new_quote)
        db.session.commit()

        logging.info(f"New quote requested: {new_quote.id}")

        return jsonify({"message": "Quote requested successfully!", "quote_id": new_quote.id}), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """
    API endpoint to retrieve a specific insurance quote by its ID.
    """
    try:
        quote = Quote.query.get_or_404(quote_id)
        return jsonify({
            "id": quote.id,
            "insurance_type": quote.insurance_type,
            "coverage_amount": quote.coverage_amount,
            "user_contact": quote.user_contact
        }), 200
    except Exception as e:
        logging.error(f"Error retrieving quote: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=False)
```
