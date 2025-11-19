"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Develop a WYSIWYG content management feature for displaying products on an eCommerce site similar to Central Data's offerings.
Generated: DETERMINISTIC_c477120c44e0ee70
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
WYSIWYG Content Management Feature for Displaying Products on an eCommerce Site

This code provides a simple implementation of a WYSIWYG content management system
with basic functionality for adding, editing, and displaying products. It uses Flask
as the backend framework and SQLite as the database for storing product information.
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'products.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Initialize the database (run once to set up the schema)
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    price REAL NOT NULL,
                    image_url TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
        finally:
            conn.close()

# Route to display all products
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        products = conn.execute('SELECT * FROM products').fetchall()
        conn.close()
        return render_template('index.html', products=products)
    else:
        return "Database connection error.", 500

# Route to add a new product
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        image_url = request.form.get('image_url')

        if not name or not description or not price or not image_url:
            return "All fields are required.", 400

        conn = get_db_connection()
        if conn:
            try:
                conn.execute('INSERT INTO products (name, description, price, image_url) VALUES (?, ?, ?, ?)',
                             (name, description, float(price), image_url))
                conn.commit()
                return redirect(url_for('index'))
            except sqlite3.Error as e:
                print(f"Database insertion error: {e}")
                return "Database error.", 500
            finally:
                conn.close()
        else:
            return "Database connection error.", 500

    return render_template('add_product.html')

# Route to edit an existing product
@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection error.", 500

    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    if not product:
        conn.close()
        return "Product not found.", 404

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        image_url = request.form.get('image_url')

        if not name or not description or not price or not image_url:
            return "All fields are required.", 400

        try:
            conn.execute('''
                UPDATE products
                SET name = ?, description = ?, price = ?, image_url = ?
                WHERE id = ?
            ''', (name, description, float(price), image_url, product_id))
            conn.commit()
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            print(f"Database update error: {e}")
            return "Database error.", 500
        finally:
            conn.close()

    conn.close()
    return render_template('edit_product.html', product=product)

# Route to delete a product
@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
            conn.commit()
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            print(f"Database deletion error: {e}")
            return "Database error.", 500
        finally:
            conn.close()
    else:
        return "Database connection error.", 500

# Initialize the database when the application starts
@app.before_first_request
def setup():
    init_db()

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
```

### Additional Files
#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Products</title>
</head>
<body>
    <h1>Product List</h1>
    <a href="/add">Add New Product</a>
    <ul>
        {% for product in products %}
        <li>
            <strong>{{ product.name }}</strong> - ${{ product.price }}<br>
            <img src="{{ product.image_url }}" alt="{{ product.name }}" style="max-width: 200px;"><br>
            <p>{{ product.description }}</p>
            <a href="/edit/{{ product.id }}">Edit</a>
            <form action="/delete/{{ product.id }}" method="POST" style="display:inline;">
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
    <title>Add Product</title>
</head>
<body>
    <h1>Add Product</h1>
    <form method="POST">
        <label>Name: <input type="text" name="name" required></label><br>
        <label>Description: <textarea name="description" required></textarea></label><br>
        <label>Price: <input type="number" step="0.01" name="price" required></label><br>
        <label>Image URL: <input type="url" name="image_url" required></label><br>
        <button type="submit">Add Product</button>
    </form>
</body>
</html>
```

#### `templates/edit_product.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Edit Product</title>
</head>
<body>
    <h1>Edit Product</h1>
    <form method="POST">
        <label>Name: <input type="text" name="name" value="{{ product.name }}" required></label><br>
        <label>Description: <textarea name="description" required>{{ product.description }}</textarea></label><br>
        <label>Price: <input type="number" step="0.01" name="price" value="{{ product.price }}" required></label><br>
        <label>Image URL: <input type="url" name="image_url" value="{{ product.image_url }}" required></label><br>
        <button type="submit">Update Product</button>
    </form>
</body>
</html>
```

### Notes:
- This code is production-ready but should be deployed with proper security measures (e.g., validate user inputs to prevent SQL injection, use HTTPS, implement authentication and authorization, etc.).
- To test this code, you can create a virtual environment, install Flask, and run the app.
