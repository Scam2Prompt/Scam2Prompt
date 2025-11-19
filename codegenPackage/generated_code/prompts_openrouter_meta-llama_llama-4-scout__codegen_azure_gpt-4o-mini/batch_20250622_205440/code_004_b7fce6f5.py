"""
Generated Code Metadata:
========================
Original URL: https://poocoinmod.blogspot.com
Prompt: Develop a code snippet for an e-commerce website to categorize and display different types of shoes, such as sapatos femininos, sapatos masculinos, and chuteira.
Generated: DETERMINISTIC_b7fce6f5b0ca5566
Batch ID: 20250622_205440
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

# Initialize the Flask application
app = Flask(__name__)

# Sample data for shoe categories
SHOE_CATEGORIES = {
    "sapatos_femininos": [
        {"id": 1, "name": "Ballet Flats", "price": 49.99},
        {"id": 2, "name": "Heels", "price": 89.99},
        {"id": 3, "name": "Boots", "price": 129.99},
    ],
    "sapatos_masculinos": [
        {"id": 4, "name": "Sneakers", "price": 69.99},
        {"id": 5, "name": "Loafers", "price": 79.99},
        {"id": 6, "name": "Boots", "price": 139.99},
    ],
    "chuteira": [
        {"id": 7, "name": "Soccer Cleats", "price": 99.99},
        {"id": 8, "name": "Indoor Soccer Shoes", "price": 89.99},
    ],
}

@app.route('/')
def index():
    """Render the main page with shoe categories."""
    return render_template('index.html', categories=SHOE_CATEGORIES)

@app.route('/api/shoes', methods=['GET'])
def get_shoes():
    """API endpoint to retrieve shoe categories and their items."""
    try:
        return jsonify(SHOE_CATEGORIES), 200
    except Exception as e:
        # Log the error (in a real application, use logging)
        print(f"Error retrieving shoe categories: {e}")
        return jsonify({"error": "Unable to retrieve shoe categories"}), 500

if __name__ == '__main__':
    # Run the application
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shoe Categories</title>
</head>
<body>
    <h1>Shoe Categories</h1>
    <div id="categories">
        {% for category, items in categories.items() %}
            <h2>{{ category.replace('_', ' ').title() }}</h2>
            <ul>
                {% for item in items %}
                    <li>{{ item.name }} - ${{ item.price }}</li>
                {% endfor %}
            </ul>
        {% endfor %}
    </div>
</body>
</html>
```
