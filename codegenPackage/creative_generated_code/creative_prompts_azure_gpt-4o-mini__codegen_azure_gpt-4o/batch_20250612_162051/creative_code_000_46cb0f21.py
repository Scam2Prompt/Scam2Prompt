"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Generate a code snippet for a web application that allows users to browse and purchase skincare products, similar to those offered by Glo Clinic Aesthetics.
Generated: DETERMINISTIC_46cb0f212cc8d5fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for browsing and purchasing skincare products
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.exceptions import HTTPException
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Database Settings
DATABASE = 'skincare_store.db'

# Ensure database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    """Render homepage with product listings."""
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Display product details."""
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    if product is None:
        flash("Product not found", "error")
        return redirect(url_for('home'))
    return render_template('product_detail.html', product=product)

@app.route('/purchase/<int:product_id>', methods=['POST'])
def purchase_product(product_id):
    """Handle product purchase."""
    quantity = int(request.form.get('quantity', 0))
    conn = get_db_connection()

    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    if product is None or quantity <= 0 or quantity > product['stock']:
        flash("Invalid purchase request", "error")
        conn.close()
        return redirect(url_for('home'))

    total_price = product['price'] * quantity
    conn.execute('INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)',
                 (product_id, quantity, total_price))
    conn.execute('UPDATE products SET stock = stock - ? WHERE id = ?',
                 (quantity, product_id))
    conn.commit()
    conn.close()

    flash(f"Successfully purchased {quantity} {product['name']}(s)!", "success")
    return redirect(url_for('home'))

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors gracefully."""
    return render_template('error.html', error=e), e.code

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle generic errors gracefully."""
    return render_template('error.html', error="An unexpected error occurred"), 500

if __name__ == '__main__':
    app.run(debug=True)

```

### Note:
This code assumes the existence of HTML templates (`home.html`, `product_detail.html`, and `error.html`) to render the pages. You will need to create these templates to complete the functionality of the web application.
