"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for iron and aluminum carpentry services, similar to those offered by Aluivars.
Generated: DETERMINISTIC_3289c3ea9602be5e
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
    material = db.Column(db.String(50), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class QuoteSchema(Schema):
    material = fields.String(required=True)
    service_type = fields.String(required=True)
    customer_name = fields.String(required=True)
    customer_email = fields.Email(required=True)

quote_schema = QuoteSchema()

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for carpentry services.
    Expects a JSON payload with material, service_type, customer_name, and customer_email.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = quote_schema.load(data)

        # Create a new Quote instance
        new_quote = Quote(
            material=validated_data['material'],
            service_type=validated_data['service_type'],
            customer_name=validated_data['customer_name'],
            customer_email=validated_data['customer_email']
        )

        # Add the new quote to the database
        db.session.add(new_quote)
        db.session.commit()

        return jsonify({"message": "Quote request submitted successfully!", "quote_id": new_quote.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
