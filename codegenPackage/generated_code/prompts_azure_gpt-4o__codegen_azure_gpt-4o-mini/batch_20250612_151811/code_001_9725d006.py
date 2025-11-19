"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Generate an API design for KEK Insurance Brokers that allows users to request quotes for various insurance services, such as construction risk management or marine insurance, as outlined on their webpage.
Generated: DETERMINISTIC_9725d00682269f5d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance_quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Insurance Quote
class InsuranceQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    quote_amount = db.Column(db.Float, nullable=False)

# Schema for validating input data
class InsuranceQuoteSchema(Schema):
    service_type = fields.String(required=True)
    user_name = fields.String(required=True)
    user_email = fields.Email(required=True)
    quote_amount = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to request a quote
@app.route('/api/quotes', methods=['POST'])
def request_quote():
    # Validate and deserialize input data
    schema = InsuranceQuoteSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new quote entry
    new_quote = InsuranceQuote(
        service_type=data['service_type'],
        user_name=data['user_name'],
        user_email=data['user_email'],
        quote_amount=data['quote_amount']
    )

    # Add to the database and commit
    db.session.add(new_quote)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save quote", "details": str(e)}), 500

    # Return the created quote as a response
    return jsonify({"message": "Quote requested successfully", "quote": schema.dump(new_quote)}), 201

# API endpoint to retrieve all quotes
@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    quotes = InsuranceQuote.query.all()
    schema = InsuranceQuoteSchema(many=True)
    return jsonify(schema.dump(quotes)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
