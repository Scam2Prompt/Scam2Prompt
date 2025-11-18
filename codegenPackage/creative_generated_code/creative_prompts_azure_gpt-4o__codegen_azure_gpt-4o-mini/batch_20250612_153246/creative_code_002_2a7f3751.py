"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Recommend a library or API for creating a web-based ablak árajánlat kérő (window quote request) program, similar to the one described on ablakvaros.hu.
Generated: DETERMINISTIC_2a7f37519bf7caa8
Batch ID: 20250612_153246
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    window_type = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(50), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)

# Create a schema for validation
class QuoteSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    window_type = fields.Str(required=True)
    dimensions = fields.Str(required=True)
    additional_info = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a quote request
@app.route('/api/quote', methods=['POST'])
def create_quote():
    try:
        # Validate the incoming JSON data
        quote_schema = QuoteSchema()
        quote_data = quote_schema.load(request.json)

        # Create a new Quote instance
        new_quote = Quote(
            name=quote_data['name'],
            email=quote_data['email'],
            window_type=quote_data['window_type'],
            dimensions=quote_data['dimensions'],
            additional_info=quote_data.get('additional_info', '')
        )

        # Add and commit the new quote to the database
        db.session.add(new_quote)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Quote request submitted successfully!"}), 201

    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400

    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to retrieve all quotes
@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    try:
        quotes = Quote.query.all()
        quote_schema = QuoteSchema(many=True)
        result = quote_schema.dump(quotes)
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"An error occurred while retrieving quotes: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
