"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-quality windows and doors from a menu distribution service in Oise and Val d'Oise.
Generated: DETERMINISTIC_f85acc57e15a4c0a
Batch ID: 20250612_140107
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
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class QuoteSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    product_type = fields.Str(required=True, validate=lambda p: p in ["windows", "doors"])
    message = fields.Str(required=False)

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    # Parse and validate the incoming JSON data
    try:
        data = request.get_json()
        quote_schema = QuoteSchema()
        validated_data = quote_schema.load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    # Create a new quote entry
    new_quote = Quote(
        name=validated_data['name'],
        email=validated_data['email'],
        product_type=validated_data['product_type'],
        message=validated_data.get('message')
    )

    # Add the new quote to the database
    try:
        db.session.add(new_quote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save quote. Please try again later."}), 500

    # Return a success response
    return jsonify({"message": "Quote request submitted successfully!"}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
