"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-store-en.pages.dev
Prompt: Create an API endpoint that allows users to list their products on the Pushd marketplace, ensuring compliance with the platform's decentralized governance model.
Generated: DETERMINISTIC_88b6723f6ca8078b
Batch ID: 20250612_161617
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

# In-memory database to store products (For production, use a persistent database)
products = []

# Function to validate product data based on governance model
def validate_product(data):
    # Example governance rules:
    # - Name and description must not be empty
    # - Price must be a positive number
    if not data.get('name') or not data.get('description'):
        return "Product name and description are required."
    if data.get('price') is None or not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return "Price must be a positive number."
    return None

@app.route('/api/v1/products', methods=['POST'])
def list_product():
    """
    API endpoint to list a product on the Pushd marketplace.
    Request must include 'name', 'description', 'price', and optional 'tags'.
    Returns success message or error.
    """
    try:
        # Parse and validate the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload."}), 400
        
        validation_error = validate_product(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Create a new product entry
        product = {
            "id": str(uuid4()),
            "name": data['name'],
            "description": data['description'],
            "price": data['price'],
            "tags": data.get('tags', []),  # Optional field
        }

        # Add to the in-memory products database
        products.append(product)

        return jsonify({"message": "Product listed successfully!", "product": product}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    """
    API endpoint to retrieve all listed products.
    Returns a list of products.
    """
    return jsonify({"products": products}), 200


# Run the Flask app (For production, use gunicorn or other WSGI servers)
if __name__ == '__main__':
    app.run(debug=True)
```
