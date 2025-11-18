"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Create a web application that allows users to compare safety shoe features like "Kevlar midsole" and "metal-free design" across different Gladiator Shoes products.
Generated: DETERMINISTIC_a9123191b225d21c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to compare Gladiator Shoes safety features

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample product data: In a real-world application, this would come from a database
PRODUCTS = [
    {"id": 1, "name": "Gladiator Pro", "features": ["Kevlar midsole", "metal-free design", "anti-slip sole"]},
    {"id": 2, "name": "Gladiator Ultra", "features": ["Kevlar midsole", "steel toe cap", "waterproof"]},
    {"id": 3, "name": "Gladiator Lite", "features": ["metal-free design", "lightweight", "breathable"]},
]

@app.route('/')
def index():
    """
    Home route displaying the product comparison interface.
    """
    return render_template('index.html', products=PRODUCTS)

@app.route('/compare', methods=['POST'])
def compare_features():
    """
    Endpoint for comparing features of selected products.
    """
    try:
        # Parse the selected product IDs from the request
        selected_ids = request.json.get('product_ids', [])
        if not selected_ids:
            return jsonify({"error": "No products selected"}), 400

        # Filter the products based on selected IDs
        selected_products = [product for product in PRODUCTS if product['id'] in selected_ids]

        # Gather and compare features across selected products
        comparison_result = {}
        for product in selected_products:
            comparison_result[product['name']] = product['features']

        return jsonify({"comparison": comparison_result})

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing the request", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safety Shoe Comparison</title>
    <script>
        async function compareProducts() {
            // Get selected product IDs from the checkboxes
            const selectedProducts = Array.from(document.querySelectorAll('input[name="product"]:checked'))
                .map(input => parseInt(input.value));

            if (selectedProducts.length === 0) {
                alert('Please select at least one product to compare.');
                return;
            }

            // Send a POST request to compare endpoint
            const response = await fetch('/compare', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ product_ids: selectedProducts }),
            });

            const data = await response.json();

            // Display comparison results
            const resultContainer = document.getElementById('comparison-result');
            if (response.ok) {
                resultContainer.innerHTML = '<h3>Comparison Result:</h3>';
                Object.entries(data.comparison).forEach(([productName, features]) => {
                    const featureList = features.map(feature => `<li>${feature}</li>`).join('');
                    resultContainer.innerHTML += `<h4>${productName}</h4><ul>${featureList}</ul>`;
                });
            } else {
                resultContainer.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        }
    </script>
</head>
<body>
    <h1>Gladiator Shoes Feature Comparison</h1>
    <form>
        <h3>Select products to compare:</h3>
        {% for product in products %}
            <label>
                <input type="checkbox" name="product" value="{{ product.id }}">
                {{ product.name }}
            </label><br>
        {% endfor %}
    </form>
    <button type="button" onclick="compareProducts()">Compare</button>
    <div id="comparison-result"></div>
</body>
</html>
```
