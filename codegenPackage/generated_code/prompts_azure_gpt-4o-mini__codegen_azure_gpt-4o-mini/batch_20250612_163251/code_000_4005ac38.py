"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Generate a code snippet for a web application that allows users to order wooden products, specifically focusing on the features of "Maderas Aserradas" and "Cabos" as described on the Maderas Elaboradas website.
Generated: DETERMINISTIC_4005ac386d548f17
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import OrderForm  # Assuming you have a forms.py file with OrderForm defined
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Order {self.product_type} - Quantity: {self.quantity}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

# Route for placing an order
@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()  # Instantiate the order form
    if form.validate_on_submit():
        try:
            # Create a new order
            new_order = Order(product_type=form.product_type.data, quantity=form.quantity.data)
            db.session.add(new_order)
            db.session.commit()
            flash('Order placed successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            logging.error(f'Error placing order: {e}')
            flash('An error occurred while placing your order. Please try again.', 'danger')
    return render_template('order.html', form=form)  # Render the order form

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render a custom 404 page

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### Note:
- Ensure you have a `forms.py` file with a defined `OrderForm` class that includes fields for `product_type` and `quantity`.
- Create the necessary HTML templates (`index.html`, `order.html`, and `404.html`) to render the pages correctly.
- Replace `'your_secret_key'` with a secure key for session management.
- Adjust the database URI as needed for your production environment.
