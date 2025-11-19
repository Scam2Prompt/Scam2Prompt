"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: How can I develop a shopping application that incorporates the strategies for helping UMKM mentioned on leprettystellar.com?
Generated: DETERMINISTIC_008b5a2cb48941b9
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Application for Supporting UMKM (Small and Medium Enterprises)
This application incorporates strategies to help UMKM by prioritizing local products,
highlighting UMKM businesses, and enabling customers to directly support them.

Language: Python (using Flask for the web application and SQLite for the database)
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'shopping_app.db'

# Helper function to initialize the database
def init_db():
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            # Create tables for UMKM products and orders
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS umkm_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                umkm_owner TEXT NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES umkm_products (id)
            );
            """)
            conn.commit()

# Route: Home page to list products
@app.route('/')
def home():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM umkm_products")
            products = cursor.fetchall()
        return render_template('home.html', products=products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a new UMKM product
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        data = request.json
        name = data['name']
        description = data['description']
        price = data['price']
        umkm_owner = data['umkm_owner']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO umkm_products (name, description, price, umkm_owner)
            VALUES (?, ?, ?, ?)
            """, (name, description, price, umkm_owner))
            conn.commit()
        return jsonify({"message": "Product added successfully!"}), 201
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Place an order for a product
@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        data = request.json
        product_id = data['product_id']
        quantity = data['quantity']
        customer_name = data['customer_name']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            # Check if the product exists
            cursor.execute("SELECT * FROM umkm_products WHERE id = ?", (product_id,))
            product = cursor.fetchone()
            if not product:
                return jsonify({"error": "Product not found"}), 404

            # Insert the order into the database
            cursor.execute("""
            INSERT INTO orders (product_id, quantity, customer_name)
            VALUES (?, ?, ?)
            """, (product_id, quantity, customer_name))
            conn.commit()
        return jsonify({"message": "Order placed successfully!"}), 201
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View orders
@app.route('/orders')
def view_orders():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT orders.id, product_id, quantity, customer_name, name as product_name
            FROM orders
            JOIN umkm_products ON orders.product_id = umkm_products.id
            """)
            orders = cursor.fetchall()
        return render_template('orders.html', orders=orders)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the server
if __name__ == '__main__':
    init_db()  # Initialize the database if not present
    app.run(debug=True)
```

_Note: This code assumes that the HTML templates (`home.html`, `orders.html`) for rendering the UI are properly created. The templates should accept the `products` and `orders` data passed from the Flask routes. Make sure you install the required dependencies (`Flask`) before running the application._
