"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: "Create a code snippet for an e-commerce website that showcases handmade, second-hand, and reusable products, such as braided trivets, coasters, and tote bags, with a focus on upcycling and sustainability."
Generated: DETERMINISTIC_5c3b4ab55d075af9
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, render_template, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample product data showcasing handmade, second-hand, and reusable products
PRODUCTS = [
    {
        "id": 1,
        "name": "Braided Trivet",
        "description": "Handmade braided trivet made from upcycled fabric scraps.",
        "price": 15.99,
        "category": "Handmade",
        "image_url": "/static/images/braided_trivet.jpg"
    },
    {
        "id": 2,
        "name": "Coasters Set",
        "description": "Set of 4 coasters crafted from reclaimed wood.",
        "price": 12.99,
        "category": "Second-hand",
        "image_url": "/static/images/coasters_set.jpg"
    },
    {
        "id": 3,
        "name": "Reusable Tote Bag",
        "description": "Eco-friendly tote bag made from recycled materials.",
        "price": 9.99,
        "category": "Reusable",
        "image_url": "/static/images/reusable_tote_bag.jpg"
    }
]

# Route to display the homepage
@app.route('/')
def homepage():
    """
    Render the homepage with a list of products.
    """
    return render_template('index.html', products=PRODUCTS)

# Route to fetch product details by ID
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch and return product details by ID.
    """
    try:
        # Find the product by ID
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product)
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Route to add a new product (for admin use)
@app.route('/product', methods=['POST'])
def add_product():
    """
    Add a new product to the catalog.
    """
    try:
        # Parse the incoming JSON data
        data = request.json
        if not data or not all(key in data for key in ("name", "description", "price", "category", "image_url")):
            return jsonify({"error": "Invalid product data"}), 400

        # Create a new product entry
        new_product = {
            "id": max(p["id"] for p in PRODUCTS) + 1,
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "category": data["category"],
            "image_url": data["image_url"]
        }
        PRODUCTS.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```

### Notes:
- This code uses Flask, a lightweight Python web framework, to create an e-commerce website.
- The `index.html` template should be created separately to render the homepage with product details.
- Static images should be stored in a `/static/images/` directory.
- Error handling is included for invalid product data and unexpected server errors.
- The `add_product` route is intended for admin use to add new products to the catalog.
