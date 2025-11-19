"""
Generated Code Metadata:
========================
Original URL: https://blockguild.pages.dev
Prompt: Design a RESTful API for a blockchain-based marketplace, including endpoints for connecting wallets, viewing marketplace listings, and tracking sales categories.
Generated: DETERMINISTIC_6c81b47e2132e853
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data storage for demonstration purposes
wallets = {}
marketplace_listings = []
sales_categories = {}

# Error messages
ERROR_WALLET_NOT_FOUND = "Wallet not found."
ERROR_INVALID_REQUEST = "Invalid request data."

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Endpoint: Connect Wallet
@app.route('/api/wallets/connect', methods=['POST'])
def connect_wallet():
    """
    Connect a new wallet to the marketplace.
    Request Body: { "wallet_address": "string" }
    Response: { "wallet_id": "string", "wallet_address": "string" }
    """
    data = request.get_json()
    if not data or 'wallet_address' not in data:
        return jsonify({"error": ERROR_INVALID_REQUEST}), 400

    wallet_id = generate_id()
    wallet_address = data['wallet_address']
    wallets[wallet_id] = wallet_address

    return jsonify({"wallet_id": wallet_id, "wallet_address": wallet_address}), 201

# Endpoint: View Marketplace Listings
@app.route('/api/marketplace/listings', methods=['GET'])
def view_marketplace_listings():
    """
    View all marketplace listings.
    Response: [{ "listing_id": "string", "title": "string", "price": "float", "category": "string" }]
    """
    return jsonify(marketplace_listings), 200

# Endpoint: Add Marketplace Listing
@app.route('/api/marketplace/listings', methods=['POST'])
def add_marketplace_listing():
    """
    Add a new listing to the marketplace.
    Request Body: { "title": "string", "price": "float", "category": "string" }
    Response: { "listing_id": "string", "title": "string", "price": "float", "category": "string" }
    """
    data = request.get_json()
    if not data or 'title' not in data or 'price' not in data or 'category' not in data:
        return jsonify({"error": ERROR_INVALID_REQUEST}), 400

    listing_id = generate_id()
    listing = {
        "listing_id": listing_id,
        "title": data['title'],
        "price": data['price'],
        "category": data['category']
    }
    marketplace_listings.append(listing)

    # Update sales categories
    if data['category'] in sales_categories:
        sales_categories[data['category']] += 1
    else:
        sales_categories[data['category']] = 1

    return jsonify(listing), 201

# Endpoint: Track Sales Categories
@app.route('/api/sales/categories', methods=['GET'])
def track_sales_categories():
    """
    Track sales categories and their counts.
    Response: { "category_name": "count" }
    """
    return jsonify(sales_categories), 200

# Error Handling: 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Endpoint not found."}), 404

# Error Handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
