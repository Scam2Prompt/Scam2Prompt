"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Suggest a design framework for developing a web-based platform to showcase private label cleaning tools, similar to PDC Brush's product offerings.
Generated: DETERMINISTIC_f5c536dd65a506fd
Batch ID: 20250612_150602
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of products."""
    products = Product.query.all()  # Fetch all products from the database
    return render_template('index.html', products=products)

# Route to add a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add a new product to the database."""
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            image_url = request.form['image_url']

            # Create a new product instance
            new_product = Product(name=name, description=description, price=price, image_url=image_url)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error adding product: {str(e)}', 'danger')
    
    return render_template('add_product.html')

# Route to delete a product
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """Delete a product from the database."""
    product = Product.query.get_or_404(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'Error deleting product: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaning Tools Showcase</title>
</head>
<body>
    <h1>Cleaning Tools</h1>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
    <ul>
        {% for product in products %}
            <li>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: ${{ product.price }}</p>
                {% if product.image_url %}
                    <img src="{{ product.image_url }}" alt="{{ product.name }}" style="width:100px;">
                {% endif %}
                <form action="{{ url_for('delete_product', product_id=product.id) }}" method="POST">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_product.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add New Product</h1>
    <form method="POST">
        <label for="name">Product Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" required>
        <br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url">
        <br>
        <button type="submit">Add Product</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure to install Flask and Flask-SQLAlchemy using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Replace `'your_secret_key'` with a secure random key for production use.
- Set `debug=False` in the `app.run()` method for production.
