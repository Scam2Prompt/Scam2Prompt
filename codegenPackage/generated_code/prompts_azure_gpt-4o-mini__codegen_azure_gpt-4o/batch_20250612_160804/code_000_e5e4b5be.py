"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Generate a code snippet for an e-commerce website that allows users to customize their own styles for clothing items like those offered in the Capsule Cosmic Journey collections.
Generated: DETERMINISTIC_e5e4b5be2c847cdf
Batch ID: 20250612_160804
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

app = Flask(__name__)

# Sample data for clothing items
clothing_items = [
    {"id": 1, "name": "Cosmic T-Shirt", "base_price": 20.0, "available_styles": ["Galaxy", "Nebula", "Starburst"]},
    {"id": 2, "name": "Journey Hoodie", "base_price": 40.0, "available_styles": ["Aurora", "Meteor", "Comet"]},
]

# Endpoint to fetch available clothing items
@app.route('/clothing-items', methods=['GET'])
def get_clothing_items():
    """
    Returns a list of available clothing items with their details.
    """
    return jsonify(clothing_items), 200

# Endpoint to customize a clothing item
@app.route('/customize', methods=['POST'])
def customize_clothing_item():
    """
    Allows users to customize a clothing item by selecting a style.
    Expects JSON input with 'item_id' and 'style'.
    """
    try:
        # Parse the request data
        data = request.get_json()
        item_id = data.get('item_id')
        style = data.get('style')

        # Validate input
        if not item_id or not style:
            return jsonify({"error": "Missing 'item_id' or 'style' in request"}), 400

        # Find the clothing item
        item = next((item for item in clothing_items if item['id'] == item_id), None)
        if not item:
            return jsonify({"error": "Clothing item not found"}), 404

        # Check if the selected style is available for the item
        if style not in item['available_styles']:
            return jsonify({"error": f"Style '{style}' is not available for this item"}), 400

        # Calculate the final price (example: add $5 for customization)
        final_price = item['base_price'] + 5.0

        # Return the customized item details
        customized_item = {
            "item_id": item['id'],
            "name": item['name'],
            "selected_style": style,
            "final_price": final_price
        }
        return jsonify(customized_item), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
