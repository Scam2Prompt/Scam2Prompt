"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Generate a code snippet for an e-commerce website that showcases a collection of designer lehengas and sarees, similar to the offerings on Vaarabella.
Generated: DETERMINISTIC_2fd258f38281a4f9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application to showcase designer lehengas and sarees
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for lehengas and sarees (would typically come from a database in production)
products = [
    {
        "id": 1,
        "name": "Embroidered Designer Lehenga",
        "category": "Lehenga",
        "price": 15000,
        "image_url": "/static/images/lehengas/embroidered_lehenga.jpg",
        "description": "Beautiful embroidered lehenga perfect for weddings and events."
    },
    {
        "id": 2,
        "name": "Silk Designer Saree",
        "category": "Saree",
        "price": 12000,
        "image_url": "/static/images/sarees/silk_designer_saree.jpg",
        "description": "Elegant silk saree with intricate border designs."
    },
    {
        "id": 3,
        "name": "Mirror Work Lehenga",
        "category": "Lehenga",
        "price": 18000,
        "image_url": "/static/images/lehengas/mirror_work_lehenga.jpg",
        "description": "Handcrafted mirror work lehenga for special occasions."
    },
    {
        "id": 4,
        "name": "Cotton Printed Saree",
        "category": "Saree",
        "price": 8000,
        "image_url": "/static/images/sarees/cotton_printed_saree.jpg",
        "description": "Lightweight cotton saree with beautiful floral prints."
    },
]

@app.route('/')
def home():
    """
    Home page showcasing the collection of designer lehengas and sarees.
    """
    return render_template('index.html', products=products)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    API endpoint to fetch the list of products.
    Returns:
        JSON object of products.
    """
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    API endpoint to fetch details of a specific product by ID.
    Args:
        product_id (int): ID of the product.
    Returns:
        JSON object of the product details or error message if not found.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

@app.errorhandler(404)
def page_not_found(error):
    """
    Custom 404 page handler.
    Args:
        error: The error object.
    Returns:
        Rendered 404 page.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask app in debug mode for development (disable debug in production)
    app.run(debug=True)
```

### Directory structure for the application:
```
/project-folder
    /templates
        - index.html          # Home page template
        - 404.html            # Custom 404 error page
    /static
        /images
            /lehengas
                - embroidered_lehenga.jpg
                - mirror_work_lehenga.jpg
            /sarees
                - silk_designer_saree.jpg
                - cotton_printed_saree.jpg
    app.py                    # Flask application code
```

Ensure you create the corresponding HTML templates (`index.html`, `404.html`) and include static images in the `/static/images` folder as referenced in the `image_url` attributes above.
