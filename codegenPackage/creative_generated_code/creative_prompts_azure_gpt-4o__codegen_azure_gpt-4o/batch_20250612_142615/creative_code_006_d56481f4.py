"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Write code to display a "No products found" message dynamically when a course platform has no available products.
Generated: DETERMINISTIC_d56481f4f7ceacea
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Mock data: List of products (empty list to simulate no products available)
products = []

@app.route('/')
def home():
    """
    Home route that checks if there are any products available.
    Renders a message if no products are found.
    """
    try:
        if not products:
            # If the products list is empty, display the "No products found" message
            return render_template('no_products.html', message="No products found")
        return render_template('products.html', products=products)
    except Exception as e:
        # Handle any unexpected errors gracefully
        return render_template('error.html', error_message=f"An error occurred: {str(e)}")

# Create HTML templates dynamically to be used
@app.route('/generate_templates')
def generate_templates():
    """
    Dynamically creates simple HTML templates for the demonstration.
    """
    try:
        with open('templates/no_products.html', 'w') as no_products:
            no_products.write("""
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>No Products</title>
            </head>
            <body>
                <h1>{{ message }}</h1>
            </body>
            </html>
            """)

        with open('templates/products.html', 'w') as products_page:
            products_page.write("""
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Products</title>
            </head>
            <body>
                <h1>Available Products:</h1>
                <ul>
                    {% for product in products %}
                        <li>{{ product }}</li>
                    {% endfor %}
                </ul>
            </body>
            </html>
            """)

        with open('templates/error.html', 'w') as error_page:
            error_page.write("""
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Error</title>
            </head>
            <body>
                <h1>{{ error_message }}</h1>
            </body>
            </html>
            """)
            
        return "Templates generated successfully!"
    except Exception as e:
        return f"Error generating templates: {str(e)}"

if __name__ == '__main__':
    # Ensure necessary directories exist
    import os
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Run the Flask application
    app.run(debug=True)
```
