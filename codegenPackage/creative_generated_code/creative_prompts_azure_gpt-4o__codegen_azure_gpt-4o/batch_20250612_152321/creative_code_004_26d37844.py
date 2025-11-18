"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Suggest libraries or tools to integrate an online ordering system for hardware products like screws, bolts, and construction materials, as outlined on APN Hardware's website.
Generated: DETERMINISTIC_26d37844c61da299
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# main.py

"""
Integration of an online ordering system for hardware products.
This code leverages Flask for the web framework, SQLAlchemy for database operations,
and Stripe for payment processing.
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware_store.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Stripe API configuration (replace with your actual Stripe keys)
stripe.api_key = 'your_secret_key'

# Database models
class Product(db.Model):
    """Model to store hardware product details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)  # Price per unit
    stock = db.Column(db.Integer, nullable=False)  # Available stock quantity

class Order(db.Model):
    """Model to store customer orders."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Route: Homepage
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')  # Ensure you have an index.html template in the 'templates' folder

# Route: Fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all available products."""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products])

# Route: Place an order
@app.route('/order', methods=['POST'])
def place_order():
    """Place a hardware product order."""
    data = request.json
    try:
        # Validate input
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not all([customer_name, customer_email, product_id, quantity]):
            return jsonify({'error': 'Missing required fields.'}), 400

        # Fetch product details
        product = Product.query.get(product_id)
        if not product or product.stock < quantity:
            return jsonify({'error': 'Product not available or insufficient stock.'}), 400

        # Calculate total price
        total_price = product.price * quantity

        # Create and charge a payment using Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_price * 100),  # Stripe expects amount in cents
            currency='usd',
            description=f"Order for {product.name}",
            receipt_email=customer_email,
        )

        # Reduce stock
        product.stock -= quantity
        db.session.commit()

        # Record the order in the database
        order = Order(
            customer_name=customer_name,
            customer_email=customer_email,
            product_id=product.id,
            quantity=quantity,
            total_price=total_price
        )
        db.session.add(order)
        db.session.commit()

        return jsonify({'message': 'Order placed successfully.', 'payment_intent': payment_intent.id})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Payment success
@app.route('/payment/success', methods=['GET'])
def payment_success():
    """Handle payment success."""
    return render_template('payment_success.html')  # Ensure you have a template for this page

# Route: Payment failure
@app.route('/payment/failure', methods=['GET'])
def payment_failure():
    """Handle payment failure."""
    return render_template('payment_failure.html')  # Ensure you have a template for this page

# Initialize database tables
@app.before_first_request
def create_tables():
    """Create database tables."""
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `your_secret_key` in `stripe.api_key` with your actual Stripe secret key.
2. Create an `index.html`, `payment_success.html`, and `payment_failure.html` in the `templates` folder.
3. Use `sqlite:///hardware_store.db` or configure the database URI to point to your production database (e.g., PostgreSQL, MySQL, etc.).
4. To install dependencies for this code, run:
   ```
   pip install flask flask_sqlalchemy stripe
   ```
