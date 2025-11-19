"""
Generated Code Metadata:
========================
Original URL: https://onlwallcone.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for a Brazilian distributor of sweets and party supplies, similar to Alyne Distribuidora.
Generated: DETERMINISTIC_eabc3bd9c5e01ab1
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management and flash messages

# Database file path
DATABASE = 'ecommerce.db'

# Ensure the database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create products table
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

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
    products = query_db('SELECT * FROM products')
    return render_template('home.html', products=products)

# Route: Add a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        try:
            query_db('INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)',
                     (name, description, float(price), int(stock)))
            flash('Product added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'Error adding product: {str(e)}', 'danger')
    return render_template('add_product.html')

# Route: Edit a product
@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = query_db('SELECT * FROM products WHERE id = ?', (product_id,), one=True)
    if not product:
        flash('Product not found!', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        try:
            query_db('UPDATE products SET name = ?, description = ?, price = ?, stock = ? WHERE id = ?',
                     (name, description, float(price), int(stock), product_id))
            flash('Product updated successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'Error updating product: {str(e)}', 'danger')
    return render_template('edit_product.html', product=product)

# Route: Delete a product
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    try:
        query_db('DELETE FROM products WHERE id = ?', (product_id,))
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting product: {str(e)}', 'danger')
    return redirect(url_for('home'))

# Route: API to fetch product details
@app.route('/api/products', methods=['GET'])
def api_products():
    products = query_db('SELECT * FROM products')
    return jsonify([dict(product) for product in products])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Create the following HTML templates (`home.html`, `add_product.html`, `edit_product.html`) in a `templates` folder for the app to work properly.
2. Use CSS and JavaScript to enhance the frontend.
3. Set `debug=False` in production and use a proper secret key for security.
