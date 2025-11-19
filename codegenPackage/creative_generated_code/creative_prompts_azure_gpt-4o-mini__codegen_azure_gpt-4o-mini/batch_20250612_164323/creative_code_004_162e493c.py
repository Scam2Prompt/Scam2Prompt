"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Suggest a REST API design for a company like Apos that allows users to request quotes for thermal paper products.
Generated: DETERMINISTIC_162e493ce3df51c3
Batch ID: 20250612_164323
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy(app)

# Database model for a Quote request
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Schema for validating and serializing Quote requests
class QuoteSchema(Schema):
    customer_name = fields.String(required=True)
    product_type = fields.String(required=True)
    quantity = fields.Integer(required=True, validate=lambda n: n > 0)
    email = fields.Email(required=True)

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)

@app.before_first_request
def create_tables():
    """Create database tables on the first request."""
    db.create_all()

@app.route('/api/quotes', methods=['POST'])
def request_quote():
    """Endpoint to request a quote for thermal paper products."""
    # Validate input data
    try:
        data = request.get_json()
        validated_data = quote_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new Quote instance
    new_quote = Quote(**validated_data)

    # Save to the database
    try:
        db.session.add(new_quote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Quote requested successfully", "quote_id": new_quote.id}), 201

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    """Endpoint to retrieve all requested quotes."""
    try:
        quotes = Quote.query.all()
        return quotes_schema.dump(quotes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """Endpoint to retrieve a specific quote by ID."""
    try:
        quote = Quote.query.get_or_404(quote_id)
        return quote_schema.dump(quote), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
