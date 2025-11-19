"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Generate a code snippet for an e-commerce website that showcases iPhone cases with stylish designs, similar to the offerings on Glisten's site.
Generated: DETERMINISTIC_1097d9db418839ce
Batch ID: 20250612_163400
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
import json

app = Flask(__name__)

# Mock data for iPhone cases (similar to what might be on Glisten's site)
cases = [
    {
        "id": 1,
        "name": "Minimalist Marble Case",
        "price": 19.99,
        "image_url": "/static/images/marble_case.jpg",
        "description": "Sleek and stylish marble design for your iPhone."
    },
    {
        "id": 2,
        "name": "Floral Elegance Case",
        "price": 24.99,
        "image_url": "/static/images/floral_case.jpg",
        "description": "Beautiful floral patterns, perfect for spring vibes."
    },
    {
        "id": 3,
        "name": "Abstract Art Case",
        "price": 22.99,
        "image_url": "/static/images/abstract_case.jpg",
        "description": "Unique abstract designs for art lovers."
    }
]

# Route for the homepage
@app.route('/')
def homepage():
    """
    Render the homepage showcasing iPhone cases.
    """
    return render_template('homepage.html', cases=cases)

# API endpoint to fetch case data
@app.route('/api/cases', methods=['GET'])
def get_cases():
    """
    Return JSON data for available iPhone cases.
    """
    try:
        return jsonify(cases)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully with a custom message.
    """
    return jsonify({"error": "Page Not Found"}), 404

# Error handling for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully with a custom message.
    """
    return jsonify({"error": "Internal Server Error"}), 500

# Main execution
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`homepage.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stylish iPhone Cases</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .case {
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
            padding: 15px;
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        .case img {
            max-width: 100px;
            margin-right: 20px;
        }
        .case-info {
            flex-grow: 1;
        }
        .case-info h2 {
            margin: 0;
            font-size: 1.2em;
        }
        .case-info p {
            margin: 5px 0;
            color: #555;
        }
        .case-info .price {
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Stylish iPhone Cases</h1>
        {% for case in cases %}
        <div class="case">
            <img src="{{ case.image_url }}" alt="{{ case.name }}">
            <div class="case-info">
                <h2>{{ case.name }}</h2>
                <p>{{ case.description }}</p>
                <p class="price">${{ case.price }}</p>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```
