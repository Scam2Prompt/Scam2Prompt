"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Create a script that displays the latest products in a home improvement store, similar to the 'Últimas Unidades' section on Jurunense Home Center."
Generated: DETERMINISTIC_1250f84785c02eac
Batch ID: 20250612_155250
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/mower.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/drill.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/sprayer.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data for demonstration purposes
# In a real application, this data would be fetched from a database or an external API
LATEST_PRODUCTS = [
    {
        "id": 1,
        "name": "Cordless Drill",
        "price": 99.99,
        "image_url": "https://example.com/images/drill.jpg",
        "description": "A powerful cordless drill for all your home improvement needs."
    },
    {
        "id": 2,
        "name": "Paint Sprayer",
        "price": 149.99,
        "image_url": "https://example.com/images/sprayer.jpg",
        "description": "Achieve a smooth finish with our easy-to-use paint sprayer."
    },
    {
        "id": 3,
        "name": "Lawn Mower",
        "price": 299.99,
        "image_url": "https://example.com/images/mower.jpg",
        "description": "Keep your lawn pristine with our efficient lawn mower."
    }
]

@app.route('/')
def index():
    """Render the main page displaying the latest products."""
    return render_template('index.html', products=LATEST_PRODUCTS)

@app.route('/api/latest-products', methods=['GET'])
def get_latest_products():
    """API endpoint to retrieve the latest products in JSON format."""
    try:
        return jsonify(LATEST_PRODUCTS), 200
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error retrieving latest products: {e}")
        return jsonify({"error": "Unable to retrieve products"}), 500

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Products</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Últimas Unidades</h1>
        <div class="row">
            {% for product in products %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <img src="{{ product.image_url }}" class="card-img-top" alt="{{ product.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <p class="card-text">{{ product.description }}</p>
                            <p class="card-text"><strong>${{ product.price }}</strong></p>
                            <a href="#" class="btn btn-primary">View Product</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
