"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinburstfire.blogspot.com
Prompt: Develop a small web application using a library that showcases various types of footwear, such as formal shoes and colorful sandals, as described in the content from Amanda Sapatos.
Generated: DETERMINISTIC_64ea8cf1aa21eb73
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
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for footwear items
footwear_items = [
    {
        "id": 1,
        "name": "Formal Shoes",
        "description": "Elegant formal shoes suitable for business and formal occasions.",
        "image": "images/formal_shoes.jpg",
        "category": "Formal"
    },
    {
        "id": 2,
        "name": "Colorful Sandals",
        "description": "Bright and colorful sandals perfect for casual outings.",
        "image": "images/colorful_sandals.jpg",
        "category": "Casual"
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "description": "Comfortable running shoes for all your athletic needs.",
        "image": "images/running_shoes.jpg",
        "category": "Sport"
    }
]

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html', footwear=footwear_items)

@app.route('/api/footwear', methods=['GET'])
def get_footwear():
    """API endpoint to return all footwear items in JSON format."""
    return jsonify(footwear_items)

@app.route('/api/footwear/<int:footwear_id>', methods=['GET'])
def get_footwear_by_id(footwear_id):
    """API endpoint to return a specific footwear item by its ID."""
    item = next((item for item in footwear_items if item['id'] == footwear_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Footwear not found"}), 404

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)

```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Footwear Showcase</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>Footwear Showcase</h1>
    <div class="footwear-container">
        <!-- Display each footwear item -->
        {% for item in footwear %}
        <div class="footwear-item">
            <img src="{{ item.image }}" alt="{{ item.name }}">
            <h2>{{ item.name }}</h2>
            <p>{{ item.description }}</p>
            <p>Category: {{ item.category }}</p>
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

.footwear-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.footwear-item {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 15px;
    padding: 20px;
    width: 250px;
    text-align: center;
}

.footwear-item img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}
```
