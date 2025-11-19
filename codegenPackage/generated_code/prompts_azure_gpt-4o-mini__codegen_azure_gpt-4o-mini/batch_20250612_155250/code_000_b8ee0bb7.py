"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: Generate a code snippet for a web application that displays a list of top fashion brands available at unbeatable prices, similar to the offerings on Brands Outlet.
Generated: DETERMINISTIC_b8ee0bb7855ef92a
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
import requests

# Initialize the Flask application
app = Flask(__name__)

# Sample data for top fashion brands
TOP_BRANDS = [
    {"name": "Nike", "price": "$49.99", "image": "nike_logo.png"},
    {"name": "Adidas", "price": "$39.99", "image": "adidas_logo.png"},
    {"name": "Puma", "price": "$29.99", "image": "puma_logo.png"},
    {"name": "Reebok", "price": "$34.99", "image": "reebok_logo.png"},
    {"name": "Under Armour", "price": "$44.99", "image": "under_armour_logo.png"},
]

@app.route('/')
def index():
    """Render the main page displaying top fashion brands."""
    return render_template('index.html', brands=TOP_BRANDS)

@app.route('/api/brands', methods=['GET'])
def get_brands():
    """API endpoint to retrieve the list of top fashion brands."""
    try:
        return jsonify(TOP_BRANDS), 200
    except Exception as e:
        # Log the error (in a real application, use logging)
        print(f"Error retrieving brands: {e}")
        return jsonify({"error": "Unable to retrieve brands"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Fashion Brands</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Top Fashion Brands at Unbeatable Prices</h1>
    <div id="brands-list">
        {% for brand in brands %}
            <div class="brand-item">
                <img src="{{ brand.image }}" alt="{{ brand.name }} logo">
                <h2>{{ brand.name }}</h2>
                <p>Price: {{ brand.price }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

h1 {
    text-align: center;
}

#brands-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.brand-item {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 20px;
    text-align: center;
    width: 200px;
}

.brand-item img {
    max-width: 100%;
    height: auto;
}
```
