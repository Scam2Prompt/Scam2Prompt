"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Design a Flask web application that allows users to browse and order Grupo ProBolsa's sustainable promotional products, including reusable bags.
Generated: DETERMINISTIC_bd2ffb531a977a45
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for secure flash messaging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample product data (In production, this would come from a database)
PRODUCTS = [
    {"id": 1, "name": "Reusable Shopping Bag", "price": 10.99, "description": "Eco-friendly reusable shopping bag."},
    {"id": 2, "name": "Promotional Tote Bag", "price": 15.49, "description": "Stylish tote bag made from sustainable materials."},
    {"id": 3, "name": "Drawstring Bag", "price": 8.99, "description": "Durable drawstring bag for everyday use."},
]

# Route: Home page
@app.route('/')
def home():
    """
    Render the home page displaying available products.
    """
    return render_template('index.html', products=PRODUCTS)

# Route: Product details
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Render the individual product details page.
    """
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        flash("Product not found!", "error")
        logging.error(f"Product with ID {product_id} not found.")
        return redirect(url_for('home'))
    return render_template('product_details.html', product=product)

# Route: Order submission
@app.route('/order', methods=['POST'])
def order():
    """
    Handle the order submission.
    """
    try:
        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))
        
        # Get product details
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            flash("Product not found!", "error")
            logging.error(f"Product with ID {product_id} not found during order.")
            return redirect(url_for('home'))
        
        if quantity <= 0:
            flash("Invalid quantity!", "error")
            logging.error(f"Invalid quantity {quantity} submitted.")
            return redirect(url_for('product_details', product_id=product_id))
        
        # Simulate order processing (In production, save order to database)
        total_price = quantity * product["price"]
        flash(f"Order placed successfully for {quantity}x {product['name']}! Total Price: ${total_price:.2f}", "success")
        logging.info(f"Order placed for {quantity}x {product['name']}, Total Price: ${total_price:.2f}")
        return redirect(url_for('home'))
    except ValueError as e:
        flash("Invalid input! Please enter valid data.", "error")
        logging.error(f"Error during order submission: {e}")
        return redirect(url_for('home'))

# Error handling: 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return render_template('404.html'), 404

# Error handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors.
    """
    return render_template('500.html'), 500

# Main execution point
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates (`templates/index.html`, `templates/product_details.html`, `templates/404.html`, `templates/500.html`) will need to be created to render the appropriate pages.
