"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corridorweb.com
Prompt: Generate code for building a user-friendly e-commerce interface that matches the scalable and flexible solutions provided by Corridor Web Agency.
Generated: DETERMINISTIC_aa8e253528994125
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings for database and application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route for home page displaying products
@app.route('/')
def home():
    try:
        products = Product.query.all()  # Fetch all products from the database
        return render_template('home.html', products=products)
    except Exception as e:
        flash(f'Error retrieving products: {str(e)}', 'danger')
        return render_template('home.html', products=[])

# Route to view product details
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    try:
        product = Product.query.get_or_404(product_id)  # Fetch product by ID or return 404
        return render_template('product_detail.html', product=product)
    except Exception as e:
        flash(f'Error retrieving product details: {str(e)}', 'danger')
        return redirect(url_for('home'))

# Route for adding a product (Admin functionality)
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        # Validate input data
        if not name or not description or not price or not stock:
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_product'))

        try:
            # Create a new product and add it to the database
            new_product = Product(name=name, description=description, 
                                  price=float(price), stock=int(stock))
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'Error adding product: {str(e)}', 'danger')
            db.session.rollback()

    return render_template('add_product.html')

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
``` 

### Note:
- Ensure you have the required templates (`home.html`, `product_detail.html`, `add_product.html`, `404.html`) set up in the `templates` directory.
- This code uses Flask, SQLAlchemy, and Flask-Migrate. Make sure to install these libraries via pip if you haven't already.
