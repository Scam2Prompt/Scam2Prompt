"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for city-to-city moving services in Antalya, including options for small item transport and elevator-assisted moving.
Generated: DETERMINISTIC_22f18237aeb6bddf
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_city = db.Column(db.String(100), nullable=False)
    to_city = db.Column(db.String(100), nullable=False)
    small_item_transport = db.Column(db.Boolean, default=False)
    elevator_assisted = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class QuoteSchema(Schema):
    from_city = fields.Str(required=True)
    to_city = fields.Str(required=True)
    small_item_transport = fields.Bool(missing=False)
    elevator_assisted = fields.Bool(missing=False)

quote_schema = QuoteSchema()

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a moving quote.
    Expects JSON data with from_city, to_city, small_item_transport, and elevator_assisted.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = quote_schema.load(data)

        # Create a new Quote instance
        new_quote = Quote(**validated_data)

        # Add the new quote to the database
        db.session.add(new_quote)
        db.session.commit()

        return jsonify({"message": "Quote requested successfully!", "quote_id": new_quote.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Log the exception (in a real application, use logging)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
