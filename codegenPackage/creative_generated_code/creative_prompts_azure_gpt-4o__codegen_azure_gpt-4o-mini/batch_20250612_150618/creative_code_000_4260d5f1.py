"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write code to create a product listing page for an online marketplace like "Mass Compras," including categories such as "Electrodomésticos," "Belleza / Spa," and "Marketing / Publicidad."
Generated: DETERMINISTIC_4260d5f132d57848
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define a Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name} - {self.category}>'

# Route for the homepage displaying the product listing
@app.route('/')
def index():
    try:
        products = Product.query.all()  # Retrieve all products from the database
        return render_template('index.html', products=products)  # Render the template with the products
    except Exception as e:
        flash('Error loading products: ' + str(e))  # Handle database access errors
        return render_template('index.html', products=[])

# Route to add a new product
@app.route('/add', methods=['POST'])
def add_product():
    try:
        name = request.form['name']
        category = request.form['category']
        price = float(request.form['price'])
        
        if not name or not category or price < 0:
            flash('Invalid input. Please check the product details.')  # Validate inputs
            return redirect(url_for('index'))

        new_product = Product(name=name, category=category, price=price)
        db.session.add(new_product)  # Add product to the session
        db.session.commit()  # Commit the session to save the product
        flash('Product added successfully!')  # Success message
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash('Error adding product: ' + str(e))  # Handle errors during addition
    return redirect(url_for('index'))

# Route to delete a product
@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)  # Retrieve the product or return 404
        db.session.delete(product)  # Delete the product
        db.session.commit()  # Commit the deletion
        flash('Product deleted successfully!')  # Success message
    except Exception as e:
        db.session.rollback()  # Rollback on error
        flash('Error deleting product: ' + str(e))  # Handle errors during deletion
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application in debug mode
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Listing - Mass Compras</title>
</head>
<body>
    <h1>Product Listing</h1>
    
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for msg in messages %}
                <li>{{ msg }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <!-- Form to add a new product -->
    <form action="{{ url_for('add_product') }}" method="post">
        <input type="text" name="name" placeholder="Product Name" required>
        <input type="text" name="category" placeholder="Category" required>
        <input type="number" step="0.01" name="price" placeholder="Price" required>
        <button type="submit">Add Product</button>
    </form>

    <!-- Product listing -->
    <h2>Available Products</h2>
    <ul>
        {% for product in products %}
            <li>
                {{ product.name }} - {{ product.category }} - ${{ product.price }}
                <a href="{{ url_for('delete_product', product_id=product.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Requirements
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using:
```bash
pip install Flask Flask-SQLAlchemy
```

### Database Initialization
- Ensure to run the script once to create the `products.db` SQLite database. This will create the required schema for the application.
