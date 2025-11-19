"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpl-liner.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for air freight services from MPL.
Generated: DETERMINISTIC_78f3fb29c3088d09
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airfreight_quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pickup_location = db.Column(db.String(200), nullable=False)
    delivery_location = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)

# Define the schema for request validation
class QuoteSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    pickup_location = fields.Str(required=True)
    delivery_location = fields.Str(required=True)
    weight = fields.Float(required=True)

quote_schema = QuoteSchema()

# Endpoint to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Validate and deserialize input data
        data = quote_schema.load(request.json)

        # Create a new Quote entry
        new_quote = Quote(**data)

        # Add the new quote to the session and commit to the database
        db.session.add(new_quote)
        db.session.commit()

        return jsonify({"message": "Quote request submitted successfully!", "id": new_quote.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
