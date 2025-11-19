"""
Generated Code Metadata:
========================
Original URL: https://rabbi-apps.teachable.com
Prompt: Write code to display a "No products found" message dynamically when a course platform has no available products.
Generated: DETERMINISTIC_d56481f4f7ceacea
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing available products
available_products = []  # This list can be populated with product data

@app.route('/')
def index():
    """
    Render the main page displaying products or a 'No products found' message.
    """
    # Check if there are available products
    if not available_products:
        message = "No products found"
    else:
        message = None  # Reset message if products are available

    # Render the template with the products and message
    return render_template('index.html', products=available_products, message=message)

if __name__ == '__main__':
    try:
        # Run the application
        app.run(debug=True)
    except Exception as e:
        # Handle any exceptions that occur during application startup
        print(f"An error occurred while starting the application: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Platform</title>
</head>
<body>
    <h1>Available Products</h1>
    
    {% if message %}
        <p>{{ message }}</p>
    {% else %}
        <ul>
            {% for product in products %}
                <li>{{ product }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```
