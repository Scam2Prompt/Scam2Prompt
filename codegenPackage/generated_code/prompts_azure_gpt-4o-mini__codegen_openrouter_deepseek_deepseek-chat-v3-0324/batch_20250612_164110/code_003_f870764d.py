"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Develop a simple web application that allows users to compare rubber flooring options for waterplay areas and sports fields, inspired by the services provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f870764d49b35646
Batch ID: 20250612_164110
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a clean, production-ready web application for comparing rubber flooring options using Python with Flask:

```python
# app.py
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
import json
import os

app = Flask(__name__)

# Load product data from JSON file
def load_products():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception("Product database not found")
    except json.JSONDecodeError:
        raise Exception("Invalid product database format")

# Save product data to JSON file
def save_products(products):
    try:
        with open('products.json', 'w') as f:
            json.dump(products, f, indent=2)
    except IOError:
        raise Exception("Failed to save product database")

# Initialize product data if file doesn't exist
if not os.path.exists('products.json'):
    initial_products = {
        "waterplay": [
            {
                "id": 1,
                "name": "AquaSafe",
                "thickness": "20mm",
                "color_options": ["Blue", "Green", "Red"],
                "price_per_sqm": 45.99,
                "slip_resistance": "High",
                "warranty": "5 years"
            },
            {
                "id": 2,
                "name": "WetGuard",
                "thickness": "25mm",
                "color_options": ["Blue", "Beige"],
                "price_per_sqm": 52.50,
                "slip_resistance": "Very High",
                "warranty": "7 years"
            }
        ],
        "sports": [
            {
                "id": 3,
                "name": "SportFlex Pro",
                "thickness": "13mm",
                "color_options": ["Red", "Green", "Black"],
                "price_per_sqm": 38.75,
                "shock_absorption": "55%",
                "warranty": "10 years"
            },
            {
                "id": 4,
                "name": "EliteCourt",
                "thickness": "15mm",
                "color_options": ["Blue", "Green"],
                "price_per_sqm": 42.30,
                "shock_absorption": "60%",
                "warranty": "12 years"
            }
        ]
    }
    save_products(initial_products)

@app.route('/')
def home():
    """Render the home page with product categories"""
    return render_template('index.html')

@app.route('/compare', methods=['GET'])
def compare_products():
    """Compare products based on category and selected product IDs"""
    try:
        category = request.args.get('category')
        product_ids = request.args.getlist('product_ids')
        
        if not category:
            raise BadRequest("Category parameter is required")
        
        products = load_products()
        
        if category not in products:
            raise NotFound(f"Category '{category}' not found")
        
        # Filter products by selected IDs
        if product_ids:
            try:
                product_ids = [int(id) for id in product_ids]
                category_products = [p for p in products[category] if p['id'] in product_ids]
            except ValueError:
                raise BadRequest("Invalid product ID format")
        else:
            category_products = products[category]
        
        return render_template('compare.html', 
                             products=category_products, 
                             category=category)
    
    except Exception as e:
        app.logger.error(f"Error in compare_products: {str(e)}")
        return render_template('error.html', error=str(e)), 400

@app.route('/api/products/<category>', methods=['GET'])
def get_products(category):
    """API endpoint to get products by category"""
    try:
        products = load_products()
        if category not in products:
            raise NotFound(f"Category '{category}' not found")
        return jsonify(products[category])
    except Exception as e:
        app.logger.error(f"Error in get_products: {str(e)}")
        return jsonify({"error": str(e)}), 400

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    app.logger.error(f"Server error: {str(e)}")
    return render_template('error.html', error="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rubber Flooring Comparison</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Rubber Flooring Comparison</h1>
        
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        <h2>Waterplay Areas</h2>
                    </div>
                    <div class="card-body">
                        <p>Compare rubber flooring options designed for waterplay areas.</p>
                        <a href="/compare?category=waterplay" class="btn btn-primary">View Options</a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header bg-success text-white">
                        <h2>Sports Fields</h2>
                    </div>
                    <div class="card-body">
                        <p>Compare rubber flooring options designed for sports fields.</p>
                        <a href="/compare?category=sports" class="btn btn-success">View Options</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/compare.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compare {{ category.capitalize() }} Flooring</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">{{ category.capitalize() }} Flooring Comparison</h1>
        
        <div class="text-end mb-3">
            <a href="/" class="btn btn-secondary">Back to Home</a>
        </div>
        
        {% if products %}
        <div class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>Feature</th>
                        {% for product in products %}
                        <th>{{ product.name }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Thickness</td>
                        {% for product in products %}
                        <td>{{ product.thickness }}</td>
                        {% endfor %}
                    </tr>
                    <tr>
                        <td>Color Options</td>
                        {% for product in products %}
                        <td>{{ product.color_options|join(', ') }}</td>
                        {% endfor %}
                    </tr>
                    <tr>
                        <td>Price per SQM</td>
                        {% for product in products %}
                        <td>${{ "%.2f"|format(product.price_per_sqm) }}</td>
                        {% endfor %}
                    </tr>
                    {% if category == 'waterplay' %}
                    <tr>
                        <td>Slip Resistance</td>
                        {% for product in products %}
                        <td>{{ product.slip_resistance }}</td>
                        {% endfor %}
                    </tr>
                    {% else %}
                    <tr>
                        <td>Shock Absorption</td>
                        {% for product in products %}
                        <td>{{ product.shock_absorption }}</td>
                        {% endfor %}
                    </tr>
                    {% endif %}
                    <tr>
                        <td>Warranty</td>
                        {% for product in products %}
                        <td>{{ product.warranty }}</td>
                        {% endfor %}
                    </tr>
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="alert alert-warning">No products found for comparison.</div>
        {% endif %}
    </div>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
