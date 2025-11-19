"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Generate a code snippet for a web application that allows users to customize and order motorized blinds from a selection of styles like Sheer Elegance and Honeycell.
Generated: DETERMINISTIC_3b25aba74d765532
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for blind styles and customization options
BLIND_STYLES = [
    {"id": 1, "name": "Sheer Elegance", "price_per_unit": 150},
    {"id": 2, "name": "Honeycell", "price_per_unit": 120},
]

CUSTOMIZATION_OPTIONS = [
    {"id": 1, "name": "Motorized", "additional_cost": 50},
    {"id": 2, "name": "Manual", "additional_cost": 0},
]

# Endpoint to get available blind styles
@app.route('/api/blind-styles', methods=['GET'])
def get_blind_styles():
    """
    Returns a list of available blind styles.
    """
    return jsonify({"blind_styles": BLIND_STYLES}), 200

# Endpoint to get customization options
@app.route('/api/customization-options', methods=['GET'])
def get_customization_options():
    """
    Returns a list of available customization options.
    """
    return jsonify({"customization_options": CUSTOMIZATION_OPTIONS}), 200

# Endpoint to place an order
@app.route('/api/order', methods=['POST'])
def place_order():
    """
    Allows users to place an order for motorized blinds.
    Expects JSON payload with 'style_id', 'customization_id', and 'quantity'.
    """
    try:
        # Parse the request JSON
        data = request.get_json()
        style_id = data.get('style_id')
        customization_id = data.get('customization_id')
        quantity = data.get('quantity')

        # Validate input
        if not style_id or not customization_id or not quantity:
            return jsonify({"error": "Missing required fields: style_id, customization_id, quantity"}), 400

        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Quantity must be a positive integer"}), 400

        # Find the selected blind style
        style = next((s for s in BLIND_STYLES if s['id'] == style_id), None)
        if not style:
            return jsonify({"error": "Invalid style_id"}), 404

        # Find the selected customization option
        customization = next((c for c in CUSTOMIZATION_OPTIONS if c['id'] == customization_id), None)
        if not customization:
            return jsonify({"error": "Invalid customization_id"}), 404

        # Calculate total cost
        base_cost = style['price_per_unit'] * quantity
        additional_cost = customization['additional_cost'] * quantity
        total_cost = base_cost + additional_cost

        # Return order summary
        order_summary = {
            "style": style['name'],
            "customization": customization['name'],
            "quantity": quantity,
            "total_cost": total_cost
        }
        return jsonify({"order_summary": order_summary}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
