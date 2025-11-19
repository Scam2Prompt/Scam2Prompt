"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homemerce.com
Prompt: Generate a code snippet for an e-commerce site that displays a list of best-selling XPS coving cornices with their prices and discounts.
Generated: DETERMINISTIC_9761e2755e0678df
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for best-selling XPS coving cornices
BEST_SELLERS = [
    {"id": 1, "name": "XPS Coving Cornice A", "price": 30.00, "discount": 0.10},  # 10% discount
    {"id": 2, "name": "XPS Coving Cornice B", "price": 25.00, "discount": 0.15},  # 15% discount
    {"id": 3, "name": "XPS Coving Cornice C", "price": 35.00, "discount": 0.05},  # 5% discount
]

@app.route('/')
def index():
    """Renders the main page displaying the best-selling XPS coving cornices."""
    return render_template('index.html', best_sellers=BEST_SELLERS)

@app.route('/api/best-sellers', methods=['GET'])
def get_best_sellers():
    """API endpoint to retrieve the list of best-selling XPS coving cornices."""
    return jsonify(BEST_SELLERS)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handles HTTP exceptions and returns a JSON response."""
    response = {
        "error": {
            "type": e.name,
            "message": e.description
        }
    }
    return jsonify(response), e.code

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best-Selling XPS Coving Cornices</title>
</head>
<body>
    <h1>Best-Selling XPS Coving Cornices</h1>
    <ul>
        {% for cornice in best_sellers %}
            <li>
                <strong>{{ cornice.name }}</strong> - Price: ${{ cornice.price | round(2) }} 
                {% if cornice.discount %}
                    (Discount: {{ (cornice.discount * 100) | round(0) }}%) 
                    <strong>Sale Price: ${{ (cornice.price * (1 - cornice.discount)) | round(2) }}</strong>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
