"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Develop a web application to help entrepreneurs open a virtual hardware store without capital, incorporating features mentioned in "Novedoso Paso a Paso para Abrir Virtualmente una Ferretería Sin Capital" from Aula Ferretera.
Generated: DETERMINISTIC_b7f569d9a8afd206
Batch ID: 20250612_153246
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
from werkzeug.exceptions import HTTPException
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For secure session management

# Define database name
DATABASE = 'virtual_hardware_store.db'

# Ensure the database exists
def initialize_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # Create products table
        cursor.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

initialize_db()

# Helper function to interact with the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Route: Home page
@app.route('/')
def home():
    """
    Renders the home page where users can view available products.
    """
    products = query_db("SELECT * FROM products")
    return render_template('home.html', products=products)

# Route: Add a new product
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    """
    Handles adding a new product to the virtual hardware store.
    """
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # Input validation
        if not name or not description or not price:
            flash('All fields are required!', 'error')
            return redirect(url_for('add_product'))

        try:
            price = float(price)
            query_db("INSERT INTO products (name, description, price) VALUES (?, ?, ?)",
                     (name, description, price))
            flash('Product added successfully!', 'success')
            return redirect(url_for('home'))
        except ValueError:
            flash('Invalid price. Please enter a numeric value.', 'error')

    return render_template('add_product.html')

# Route: Delete a product
@app.route('/delete-product/<int:id>', methods=['POST'])
def delete_product(id):
    """
    Handles deleting a product from the virtual hardware store.
    """
    try:
        query_db("DELETE FROM products WHERE id = ?", (id,))
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting product: {str(e)}', 'error')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    return render_template("error.html", error=e), e.code

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates:

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Hardware Store</title>
</head>
<body>
    <h1>Welcome to Your Virtual Hardware Store</h1>
    <a href="/add-product">Add Product</a>
    <h2>Available Products</h2>
    <ul>
        {% for product in products %}
        <li>
            {{ product.name }} - ${{ product.price }} <br>
            Description: {{ product.description }}
            <form action="/delete-product/{{ product.id }}" method="post">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/add_product.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add a New Product</h1>
    <form method="POST">
        <label for="name">Product Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required><br>
        <label for="price">Price:</label>
        <input type="text" id="price" name="price" required><br>
        <button type="submit">Add Product</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error.description }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
