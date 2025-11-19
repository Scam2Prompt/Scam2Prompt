"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Create a REST API using Flask that allows users to request quotes for products such as "Offset Multi Colour Printers," "Xerox Paper," and "Gift Items," and includes endpoints for managing client information.
Generated: DETERMINISTIC_1bcd685a537ae143
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Schema for validating client data
class ClientSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Schema for validating quote data
class QuoteSchema(Schema):
    product = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize schemas
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)

# Endpoint to create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    """Create a new client."""
    try:
        data = request.get_json()
        client_data = client_schema.load(data)
        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()
        return client_schema.jsonify(new_client), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve all clients."""
    clients = Client.query.all()
    return clients_schema.jsonify(clients), 200

# Endpoint to create a new quote
@app.route('/quotes', methods=['POST'])
def create_quote():
    """Create a new quote."""
    try:
        data = request.get_json()
        quote_data = quote_schema.load(data)
        new_quote = Quote(**quote_data)
        db.session.add(new_quote)
        db.session.commit()
        return quote_schema.jsonify(new_quote), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    """Retrieve all quotes."""
    quotes = Quote.query.all()
    return quotes_schema.jsonify(quotes), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
