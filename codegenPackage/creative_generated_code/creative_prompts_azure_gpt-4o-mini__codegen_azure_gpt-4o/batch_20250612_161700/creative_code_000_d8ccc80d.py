"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Generate a code snippet for an e-commerce website that displays a collection of traditional Pakistani clothing, including kurtas and sharara sets, similar to the offerings on Multan Designs.
Generated: DETERMINISTIC_d8ccc80dd9f2357a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Sample data representing traditional Pakistani clothing items
clothing_items = [
    {
        "id": 1,
        "name": "Embroidered Kurta",
        "price": 3500,
        "image_url": "/static/images/embroidered_kurta.jpg",
        "description": "A beautifully embroidered kurta perfect for traditional occasions.",
        "category": "Kurtas"
    },
    {
        "id": 2,
        "name": "Silk Sharara Set",
        "price": 5500,
        "image_url": "/static/images/silk_sharara_set.jpg",
        "description": "Elegant silk sharara set designed for festive events.",
        "category": "Sharara Sets"
    },
    {
        "id": 3,
        "name": "Casual Cotton Kurta",
        "price": 2500,
        "image_url": "/static/images/casual_cotton_kurta.jpg",
        "description": "Lightweight and breathable cotton kurta for daily wear.",
        "category": "Kurtas"
    },
    {
        "id": 4,
        "name": "Designer Sharara Set",
        "price": 6500,
        "image_url": "/static/images/designer_sharara_set.jpg",
        "description": "Premium designer sharara set adorned with intricate details.",
        "category": "Sharara Sets"
    }
]

@app.route("/")
def index():
    """
    Route to display the main page.
    Renders a template showing a collection of clothing items.
    """
    return render_template("index.html", clothing_items=clothing_items)

@app.route("/api/clothing-items", methods=["GET"])
def get_clothing_items():
    """
    API endpoint to fetch the list of clothing items in JSON format.
    Can be used by front-end or third-party systems.
    """
    try:
        return jsonify(clothing_items), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traditional Pakistani Clothing</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Welcome to Multan Designs</h1>
    <div class="clothing-collection">
        {% for item in clothing_items %}
        <div class="clothing-item">
            <img src="{{ item.image_url }}" alt="{{ item.name }}" class="clothing-image">
            <h2>{{ item.name }}</h2>
            <p>{{ item.description }}</p>
            <p><strong>Category:</strong> {{ item.category }}</p>
            <p><strong>Price:</strong> PKR {{ item.price }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

### Styles (`static/styles.css`)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

h1 {
    text-align: center;
    color: #333;
    margin-top: 20px;
}

.clothing-collection {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin: 20px;
}

.clothing-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    width: 250px;
    text-align: center;
}

.clothing-image {
    width: 100%;
    height: auto;
    border-radius: 8px;
}

h2 {
    color: #444;
    font-size: 1.5em;
}

p {
    color: #666;
    font-size: 1em;
}

strong {
    color: #000;
}
```

### Directory Structure:
```
/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── images/
│       ├── embroidered_kurta.jpg
│       ├── silk_sharara_set.jpg
│       ├── casual_cotton_kurta.jpg
│       └── designer_sharara_set.jpg
```
