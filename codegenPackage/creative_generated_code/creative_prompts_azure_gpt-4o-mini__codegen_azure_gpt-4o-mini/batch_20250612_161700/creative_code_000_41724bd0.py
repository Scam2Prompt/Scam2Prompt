"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pavingblockcirebon.com
Prompt: Generate a code snippet for a web application that displays a catalog of paving block products, including specifications and pricing, similar to the offerings of Komando Block Cirebon.
Generated: DETERMINISTIC_41724bd05f55c6dc
Batch ID: 20250612_161700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample catalog data
catalog = [
    {
        "id": 1,
        "name": "Standard Paving Block",
        "specifications": {
            "size": "200x100x60 mm",
            "weight": "4.5 kg",
            "material": "Concrete",
            "color": "Gray"
        },
        "price": 2.50
    },
    {
        "id": 2,
        "name": "Decorative Paving Block",
        "specifications": {
            "size": "300x300x80 mm",
            "weight": "10 kg",
            "material": "Concrete",
            "color": "Red"
        },
        "price": 3.75
    },
    {
        "id": 3,
        "name": "Permeable Paving Block",
        "specifications": {
            "size": "400x400x100 mm",
            "weight": "15 kg",
            "material": "Concrete",
            "color": "Beige"
        },
        "price": 5.00
    }
]

@app.route('/')
def index():
    """Render the main catalog page."""
    return render_template('index.html', products=catalog)

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to get the list of paving block products."""
    try:
        return jsonify(catalog), 200
    except Exception as e:
        logging.error("Error fetching products: %s", e)
        return jsonify({"error": "Unable to fetch products"}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```

### HTML Template (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paving Block Catalog</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Paving Block Products</h1>
        <div class="row">
            {% for product in products %}
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">
                            <strong>Specifications:</strong><br>
                            Size: {{ product.specifications.size }}<br>
                            Weight: {{ product.specifications.weight }}<br>
                            Material: {{ product.specifications.material }}<br>
                            Color: {{ product.specifications.color }}<br>
                        </p>
                        <p class="card-text"><strong>Price: ${{ product.price }}</strong></p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Instructions for Setting Up the Web Application
1. Make sure you have Flask installed. You can do this with the following command:
   ```
   pip install Flask
   ```

2. Create a folder for your project and create two files: `app.py` for the Python code and `templates/index.html` for the HTML template.

3. Copy the provided code into the respective files.

4. Run the application using:
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to view the catalog.
