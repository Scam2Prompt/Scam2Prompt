"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for construction services, focusing on the turnkey construction model highlighted by Bismillah Traders.
Generated: DETERMINISTIC_fe3d32155fc5a57e
Batch ID: 20250612_162051
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
from flask_marshmallow import Marshmallow
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Quote Model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=True)

    def __init__(self, name, email, service_type, message):
        self.name = name
        self.email = email
        self.service_type = service_type
        self.message = message

# Quote Schema
class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Get data from the request
        data = request.json
        
        # Validate incoming data
        if not all(key in data for key in ('name', 'email', 'service_type')):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new quote
        new_quote = Quote(
            name=data['name'],
            email=data['email'],
            service_type=data['service_type'],
            message=data.get('message', '')
        )

        # Add the quote to the session and commit
        db.session.add(new_quote)
        db.session.commit()

        # Serialize the response
        quote_schema = QuoteSchema()
        return jsonify(quote_schema.dump(new_quote)), 201

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running this code:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```
