"""
Generated Code Metadata:
========================
Original URL: https://farmaciasantiagoapostol.com
Prompt: Write a Python script to manage an online pharmacy store's inventory, including sections for noticias (news), tienda (store), and contacto (contact).
Generated: DETERMINISTIC_43933456c7dcce5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the inventory, news, and contact information
inventory = {
    "medicines": [],
}

news = [
    {"id": 1, "title": "New Medicine Available", "content": "We have added new medicines to our inventory."},
]

contact_info = {
    "email": "support@onlinepharmacy.com",
    "phone": "+1234567890",
}

# Endpoint to get the inventory of medicines
@app.route('/tienda/inventory', methods=['GET'])
def get_inventory():
    """Retrieve the current inventory of medicines."""
    return jsonify(inventory), 200

# Endpoint to add a new medicine to the inventory
@app.route('/tienda/inventory', methods=['POST'])
def add_medicine():
    """Add a new medicine to the inventory."""
    try:
        new_medicine = request.json
        if not new_medicine or 'name' not in new_medicine or 'quantity' not in new_medicine:
            return jsonify({"error": "Invalid medicine data"}), 400
        
        inventory['medicines'].append(new_medicine)
        return jsonify({"message": "Medicine added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get the latest news
@app.route('/noticias', methods=['GET'])
def get_news():
    """Retrieve the latest news from the pharmacy."""
    return jsonify(news), 200

# Endpoint to get contact information
@app.route('/contacto', methods=['GET'])
def get_contact_info():
    """Retrieve contact information for the pharmacy."""
    return jsonify(contact_info), 200

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
