"""
Generated Code Metadata:
========================
Original URL: https://maskatiyasgroup.com
Prompt: Illustrate how to implement a product comparison feature in a web application that highlights the differences between the LCDs offered by Maskatiyas Group, particularly focusing on their AI features and original chipset packs.
Generated: DETERMINISTIC_76f3752a1005e9eb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from functools import wraps
import json

app = Flask(__name__)

# Sample product data (in a real application, this would come from a database)
PRODUCTS = {
    "M1": {
        "name": "Maskatiyas M1",
        "ai_features": ["Smart Brightness", "Color Optimization", "Eye Protection"],
        "chipset": "M-Chip X1",
        "price": 499.99,
        "resolution": "4K UHD"
    },
    "M2": {
        "name": "Maskatiyas M2",
        "ai_features": ["Smart Brightness", "Color Optimization", "Eye Protection", "Adaptive Contrast"],
        "chipset": "M-Chip X2",
        "price": 599.99,
        "resolution": "4K UHD"
    },
    "M3": {
        "name": "Maskatiyas M3",
        "ai_features": ["Smart Brightness Pro", "Color Optimization Pro", "Eye Protection Pro", "Adaptive Contrast", "Motion Enhancement"],
        "chipset": "M-Chip X3",
        "price": 799.99,
        "resolution": "8K UHD"
    }
}

def validate_products(f):
    """Decorator to validate product IDs in the request."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        product_ids = request.args.getlist('products') or request.json.get('products', [])
        for product_id in product_ids:
            if product_id not in PRODUCTS:
                return jsonify({"error": f"Product {product_id} not found"}), 404
        return f(*args, **kwargs)
    return decorated_function

@app.route('/compare', methods=['GET', 'POST'])
@validate_products
def compare_products():
    """Endpoint to compare multiple products."""
    if request.method == 'GET':
        product_ids = request.args.getlist('products')
    else:
        product_ids = request.json.get('products', [])
    
    if len(product_ids) < 2:
        return jsonify({"error": "At least two products are required for comparison"}), 400
    
    # Get the products to compare
    products = [PRODUCTS[pid] for pid in product_ids]
    
    # Prepare comparison data
    comparison = {
        "products": products,
        "differences": {
            "ai_features": find_differences([p["ai_features"] for p in products]),
            "chipset": find_differences([p["chipset"] for p in products]),
            "price": find_differences([p["price"] for p in products]),
            "resolution": find_differences([p["resolution"] for p in products])
        }
    }
    
    return jsonify(comparison)

def find_differences(features_list):
    """Helper function to find differences between product features."""
    if not features_list:
        return []
    
    # For lists (like AI features), find unique and common items
    if isinstance(features_list[0], list):
        all_features = set(features_list[0])
        common_features = set(features_list[0])
        
        for features in features_list[1:]:
            all_features.update(features)
            common_features.intersection_update(features)
        
        differences = []
        for feature in all_features:
            status = "common" if feature in common_features else "unique"
            differences.append({"feature": feature, "status": status})
        
        return differences
    # For single values (like chipset, price), just compare directly
    else:
        if len(set(features_list)) == 1:
            return [{"feature": features_list[0], "status": "common"}]
        else:
            return [{"feature": feature, "status": "unique"} for feature in features_list]

@app.route('/products', methods=['GET'])
def list_products():
    """Endpoint to list all available products."""
    return jsonify({"products": list(PRODUCTS.keys())})

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/comparison.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maskatiyas LCD Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .product-selector {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        select {
            padding: 8px;
            flex-grow: 1;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        .comparison-table th {
            background-color: #f2f2f2;
        }
        .common {
            background-color: #e6ffe6;
        }
        .unique {
            background-color: #ffe6e6;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Maskatiyas LCD Comparison Tool</h1>
        
        <div class="product-selector">
            <select id="product1">
                <option value="">Select Product 1</option>
                {% for product_id in products %}
                <option value="{{ product_id }}">{{ products[product_id].name }}</option>
                {% endfor %}
            </select>
            
            <select id="product2">
                <option value="">Select Product 2</option>
                {% for product_id in products %}
                <option value="{{ product_id }}">{{ products[product_id].name }}</option>
                {% endfor %}
            </select>
            
            <button onclick="compareProducts()">Compare</button>
        </div>
        
        <div id="comparison-result">
            <!-- Comparison results will be displayed here -->
        </div>
    </div>

    <script>
        function compareProducts() {
            const product1 = document.getElementById('product1').value;
            const product2 = document.getElementById('product2').value;
            
            if (!product1 || !product2) {
                alert('Please select two products to compare');
                return;
            }
            
            fetch(`/compare?products=${product1}&products=${product2}`)
                .then(response => response.json())
                .then(data => {
                    displayComparison(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while comparing products');
                });
        }
        
        function displayComparison(data) {
            const resultDiv = document.getElementById('comparison-result');
            
            if (data.error) {
                resultDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
                return;
            }
            
            let html = '<h2>Comparison Results</h2>';
            html += '<table class="comparison-table">';
            
            // Add header row with product names
            html += '<tr><th>Feature</th>';
            data.products.forEach(product => {
                html += `<th>${product.name}</th>`;
            });
            html += '</tr>';
            
            // Add AI features comparison
            html += '<tr><th colspan="' + (data.products.length + 1) + '">AI Features</th></tr>';
            const aiFeatures = {};
            data.products.forEach((product, index) => {
                product.ai_features.forEach(feature => {
                    if (!aiFeatures[feature]) {
                        aiFeatures[feature] = Array(data.products.length).fill(false);
                    }
                    aiFeatures[feature][index] = true;
                });
            });
            
            Object.keys(aiFeatures).forEach(feature => {
                const isCommon = aiFeatures[feature].every(val => val);
                html += `<tr class="${isCommon ? 'common' : 'unique'}"><td>${feature}</td>`;
                aiFeatures[feature].forEach(hasFeature => {
                    html += `<td>${hasFeature ? '✓' : '✗'}</td>`;
                });
                html += '</tr>';
            });
            
            // Add other features
            const features = ['chipset', 'price', 'resolution'];
            features.forEach(feature => {
                html += `<tr><th colspan="${data.products.length + 1}">${feature.charAt(0).toUpperCase() + feature.slice(1)}</th></tr>`;
