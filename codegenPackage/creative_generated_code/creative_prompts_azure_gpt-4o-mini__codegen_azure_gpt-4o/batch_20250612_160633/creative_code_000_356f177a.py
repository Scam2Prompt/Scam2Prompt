"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of kitchen accessories, including items like petisqueiras and bandejas, similar to those found on Camicado.
Generated: DETERMINISTIC_356f177af2ef4c1c
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, render_template

# Initialize Flask app
app = Flask(__name__)

# Sample data - List of kitchen accessories
kitchen_accessories = [
    {"id": 1, "name": "Petisqueira Aramado", "price": 49.99, "category": "Serveware"},
    {"id": 2, "name": "Bandeja de Madeira", "price": 89.99, "category": "Serveware"},
    {"id": 3, "name": "Conjunto de Bowls", "price": 35.99, "category": "Dinnerware"},
    {"id": 4, "name": "Jogo de Copos", "price": 79.99, "category": "Glassware"},
    {"id": 5, "name": "Petisqueira de Porcelana", "price": 59.99, "category": "Serveware"},
]

# Route to serve the homepage
@app.route('/')
def home():
    # Render homepage with the list of kitchen accessories
    return render_template('index.html', accessories=kitchen_accessories)

# Route to get kitchen accessories data as JSON
@app.route('/api/accessories', methods=['GET'])
def get_accessories():
    try:
        # Return the accessories as a JSON response
        return jsonify(kitchen_accessories), 200
    except Exception as e:
        # Handle any errors
        error_message = {"error": "Unable to fetch accessories"}
        return jsonify(error_message), 500

# Run the Flask app
if __name__ == '__main__':
    # Use debug mode for development, disable it in production
    app.run(debug=True)

# Below is the accompanying HTML template (index.html)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kitchen Accessories</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 800px; margin: 0 auto; padding: 20px; }
        .item { border-bottom: 1px solid #ddd; padding: 10px 0; }
        .item:last-child { border-bottom: none; }
        .item h3 { margin: 0; }
        .item p { margin: 5px 0; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kitchen Accessories</h1>
        {% for accessory in accessories %}
        <div class="item">
            <h3>{{ accessory.name }}</h3>
            <p>Category: {{ accessory.category }}</p>
            <p>Price: ${{ accessory.price }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''
```
