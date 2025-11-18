"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Develop a web application using Flask that showcases the product range of metallic stickers, including Nickel Metal Stickers and 3D Metal Nickel Stickers, with customization options as described on jttlogos.com.
Generated: DETERMINISTIC_3c21209888e31d5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock data for metallic stickers
products = [
    {
        "id": 1,
        "name": "Nickel Metal Stickers",
        "description": "Durable and shiny stickers made from nickel metal.",
        "customization_options": [
            "Color options (silver, gold, black)",
            "Size options",
            "Text customization"
        ]
    },
    {
        "id": 2,
        "name": "3D Metal Nickel Stickers",
        "description": "Stylish 3D stickers with nickel finish for premium branding.",
        "customization_options": [
            "3D design options",
            "Color options",
            "Custom shapes and logos"
        ]
    }
]

# Home route
@app.route('/')
def home():
    """
    Render the homepage with a list of metallic stickers.
    """
    return render_template('index.html', products=products)

# Product details route
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Render the product details page for a specific product.

    Args:
        product_id (int): ID of the product.

    Returns:
        Rendered HTML page for product details.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return render_template('404.html'), 404

# Customization route
@app.route('/customize/<int:product_id>', methods=['POST'])
def customize_product(product_id):
    """
    Handle customization requests for a product.

    Args:
        product_id (int): ID of the product.

    Returns:
        JSON response indicating success or failure of customization.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    try:
        # Extract customization details from the request
        customization_details = request.json
        # For simplicity, just return the submitted customization details
        return jsonify({
            "message": "Customization submitted successfully",
            "product_id": product_id,
            "customization_details": customization_details
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.

    Args:
        e: Exception object.

    Returns:
        Rendered HTML page for 404 error.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the application in debug mode (disable debug for production!)
    app.run(debug=True)
```

### Templates Directory Structure
Place the following HTML templates in a `templates` directory within the project.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metallic Stickers</title>
</head>
<body>
    <h1>Welcome to Metallic Stickers!</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="/product/{{ product.id }}">{{ product.name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `product_details.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <h2>Customization Options:</h2>
    <ul>
        {% for option in product.customization_options %}
            <li>{{ option }}</li>
        {% endfor %}
    </ul>
    <form action="/customize/{{ product.id }}" method="post">
        <button type="submit">Customize</button>
    </form>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
