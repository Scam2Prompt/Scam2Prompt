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
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database in production)
products = {
    1: "Offset Multi Colour Printers",
    2: "Xerox Paper",
    3: "Gift Items",
}
clients = {}
quotes = {}

# Helper function for validation
def validate_client_data(data):
    required_fields = ["name", "email", "phone"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

# Endpoint: View available products
@app.route('/api/products', methods=['GET'])
def get_products():
    """Return a list of available products"""
    return jsonify(products), 200

# Endpoint: Add a new client
@app.route('/api/clients', methods=['POST'])
def add_client():
    """
    Add a new client.
    Expects JSON payload with 'name', 'email', and 'phone'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    valid, error_message = validate_client_data(data)
    if not valid:
        return jsonify({"error": error_message}), 400

    client_id = str(uuid4())
    clients[client_id] = {
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"]
    }
    return jsonify({"client_id": client_id, "message": "Client added successfully"}), 201

# Endpoint: Request a quote for a product
@app.route('/api/quotes', methods=['POST'])
def request_quote():
    """
    Request a quote for a product.
    Expects JSON payload with 'client_id' and 'product_id'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    client_id = data.get("client_id")
    product_id = data.get("product_id")

    if client_id not in clients:
        return jsonify({"error": "Invalid client_id"}), 404
    if product_id not in products:
        return jsonify({"error": "Invalid product_id"}), 404

    quote_id = str(uuid4())
    quotes[quote_id] = {
        "client_id": client_id,
        "product_id": product_id,
        "product_name": products[product_id]
    }
    return jsonify({"quote_id": quote_id, "message": "Quote requested successfully"}), 201

# Endpoint: Get client information
@app.route('/api/clients/<client_id>', methods=['GET'])
def get_client(client_id):
    """Retrieve client details by client_id"""
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(client), 200

# Endpoint: Get quote information
@app.route('/api/quotes/<quote_id>', methods=['GET'])
def get_quote(quote_id):
    """Retrieve quote details by quote_id"""
    quote = quotes.get(quote_id)
    if not quote:
        return jsonify({"error": "Quote not found"}), 404
    return jsonify(quote), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
