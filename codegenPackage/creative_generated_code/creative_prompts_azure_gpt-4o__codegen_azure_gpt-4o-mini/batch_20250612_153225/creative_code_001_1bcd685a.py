"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Create a REST API using Flask that allows users to request quotes for products such as "Offset Multi Colour Printers," "Xerox Paper," and "Gift Items," and includes endpoints for managing client information.
Generated: DETERMINISTIC_1bcd685a537ae143
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Product Quotes
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for serializing Quote objects
class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote

# Model for Clients
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

# Schema for serializing Client objects
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to get all product quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    """Retrieve all product quotes."""
    quotes = Quote.query.all()
    quote_schema = QuoteSchema(many=True)
    return jsonify(quote_schema.dump(quotes)), 200

# Endpoint to add a new product quote
@app.route('/quotes', methods=['POST'])
def add_quote():
    """Add a new product quote."""
    product_name = request.json.get('product_name')
    price = request.json.get('price')

    if not product_name or price is None:
        abort(400, description="Product name and price are required.")

    new_quote = Quote(product_name=product_name, price=price)
    db.session.add(new_quote)
    db.session.commit()

    return jsonify(QuoteSchema().dump(new_quote)), 201

# Endpoint to manage client information
@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve all clients."""
    clients = Client.query.all()
    client_schema = ClientSchema(many=True)
    return jsonify(client_schema.dump(clients)), 200

@app.route('/clients', methods=['POST'])
def add_client():
    """Add a new client."""
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        abort(400, description="Client name and email are required.")

    new_client = Client(name=name, email=email)
    db.session.add(new_client)
    db.session.commit()

    return jsonify(ClientSchema().dump(new_client)), 201

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
