"""
Generated Code Metadata:
========================
Original URL: https://accessthepooc00in.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for selling sandals and shoes, including product categories for masculine and feminine footwear.
Generated: DETERMINISTIC_0ace875b080a00a7
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Home route to display products
@app.route('/')
def home():
    try:
        products = Product.query.all()  # Fetch all products from the database
        return render_template('home.html', products=products)
    except Exception as e:
        flash('Error fetching products: ' + str(e))
        return render_template('home.html', products=[])

# Route to add a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            price = float(request.form['price'])
            description = request.form['description']

            new_product = Product(name=name, category=category, price=price, description=description)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error adding product: ' + str(e))
            return redirect(url_for('add_product'))

    return render_template('add_product.html')

# Route to filter products by category
@app.route('/category/<category_name>')
def category(category_name):
    try:
        products = Product.query.filter_by(category=category_name).all()
        return render_template('category.html', products=products, category=category_name)
    except Exception as e:
        flash('Error fetching category products: ' + str(e))
        return render_template('category.html', products=[], category=category_name)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - E-commerce</title>
</head>
<body>
    <h1>Welcome to Our E-commerce Store</h1>
    <h2>Products</h2>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - {{ product.price }} - <a href="{{ url_for('category', category_name=product.category) }}">{{ product.category }}</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
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
    <title>Add Product - E-commerce</title>
</head>
<body>
    <h1>Add New Product</h1>
    <form method="POST">
        <label for="name">Product Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="category">Category:</label>
        <select id="category" name="category" required>
            <option value="masculine">Masculine</option>
            <option value="feminine">Feminine</option>
        </select>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" required>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <button type="submit">Add Product</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

**category.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category }} - E-commerce</title>
</head>
<body>
    <h1>{{ category.capitalize() }} Footwear</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - {{ product.price }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production use.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
