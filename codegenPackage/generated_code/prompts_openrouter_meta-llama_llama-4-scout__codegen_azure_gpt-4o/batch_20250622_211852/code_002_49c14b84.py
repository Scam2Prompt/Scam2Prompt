"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Design a simple API to suggest suitable Spinetress products (e.g., mattress, topper, pillow) for customers based on their inputted preferences for firmness, material, and budget.
Generated: DETERMINISTIC_49c14b84c31793a7
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product database
PRODUCTS = [
    {"id": 1, "name": "Soft Mattress", "type": "mattress", "firmness": "soft", "material": "memory foam", "price": 500},
    {"id": 2, "name": "Firm Mattress", "type": "mattress", "firmness": "firm", "material": "latex", "price": 800},
    {"id": 3, "name": "Medium Pillow", "type": "pillow", "firmness": "medium", "material": "down", "price": 50},
    {"id": 4, "name": "Soft Topper", "type": "topper", "firmness": "soft", "material": "memory foam", "price": 150},
    {"id": 5, "name": "Firm Pillow", "type": "pillow", "firmness": "firm", "material": "latex", "price": 70},
]

@app.route('/suggest-products', methods=['POST'])
def suggest_products():
    """
    API endpoint to suggest Spinetress products based on user preferences.
    Expects a JSON payload with 'firmness', 'material', and 'budget'.
    """
    try:
        # Parse user input from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. Please provide a JSON payload."}), 400

        firmness = data.get("firmness")
        material = data.get("material")
        budget = data.get("budget")

        # Validate input
        if not firmness or not material or budget is None:
            return jsonify({"error": "Missing required fields: 'firmness', 'material', or 'budget'."}), 400

        # Filter products based on user preferences
        suggested_products = [
            product for product in PRODUCTS
            if product["firmness"] == firmness and product["material"] == material and product["price"] <= budget
        ]

        # Return suggestions
        if suggested_products:
            return jsonify({"suggested_products": suggested_products}), 200
        else:
            return jsonify({"message": "No products match your preferences."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
