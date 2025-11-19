"""
Generated Code Metadata:
========================
Original URL: https://finishdrop.com
Prompt: Generate a code snippet for setting up an e-commerce website using the tools and methods discussed on FinishDrop, focusing on product integration and optimized site design.
Generated: DETERMINISTIC_f50d8576f52a89f2
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'ecommerce.db'

# Ensure the database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create a table for products
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

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route: Home page
@app.route('/')
def home():
    """
    Render the home page with a list of products.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        conn.close()
        return render_template('index.html', products=products)
    else:
        return "Error connecting to the database.", 500

# Route: Add a new product
@app.route('/add_product', methods=['POST'])
def add_product():
    """
    Add a new product to the database.
    """
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description', '')
        price = data.get('price')
        stock = data.get('stock')

        if not name or not price or not stock:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO products (name, description, price, stock)
                VALUES (?, ?, ?, ?)
            ''', (name, description, price, stock))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Product added successfully'}), 201
        else:
            return jsonify({'error': 'Database connection error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Update product stock
@app.route('/update_stock/<int:product_id>', methods=['PUT'])
def update_stock(product_id):
    """
    Update the stock of a specific product.
    """
    try:
        data = request.json
        new_stock = data.get('stock')

        if new_stock is None:
            return jsonify({'error': 'Missing stock value'}), 400

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE products
                SET stock = ?
                WHERE id = ?
            ''', (new_stock, product_id))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Stock updated successfully'}), 200
        else:
            return jsonify({'error': 'Database connection error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Delete a product
@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product from the database.
    """
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Product deleted successfully'}), 200
        else:
            return jsonify({'error': 'Database connection error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```

### Notes:
- This code sets up a basic e-commerce website backend using Flask and SQLite.
- The database is initialized with a `products` table to store product information.
- Routes are provided for viewing products, adding new products, updating stock, and deleting products.
- Error handling is included for database connection issues and invalid input.
- The frontend (`index.html`) is assumed to exist for rendering the home page.
