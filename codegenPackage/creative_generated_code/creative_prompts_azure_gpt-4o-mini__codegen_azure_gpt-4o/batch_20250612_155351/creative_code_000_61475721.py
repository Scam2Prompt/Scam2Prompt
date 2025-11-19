"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://butterfieldtechnology.com
Prompt: Generate code for an ecommerce website that improves customer satisfaction and reduces operational costs, inspired by Butterfield Technology's approach.
Generated: DETERMINISTIC_614757211279b391
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for an ecommerce platform written in Python using the Flask framework. It includes features for improving customer satisfaction and reducing operational costs. It incorporates best practices and is production-ready.

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import sqlite3
import logging

app = Flask(__name__)

# Configure logging for monitoring operational costs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    conn.commit()
    conn.close()

# Utility for database connections
def db_connection():
    """Create and return a database connection."""
    try:
        conn = sqlite3.connect('ecommerce.db')
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        raise

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors gracefully."""
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({'error': e.description}).get_data()
        response.content_type = "application/json"
        return response
    return jsonify({'error': 'An unexpected error occurred'}), 500

# Route: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch and return all available products."""
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()
        return jsonify(products)
    except Exception as e:
        logging.error(f"Error fetching products: {e}")
        return jsonify({'error': 'Unable to fetch products'}), 500

# Route: Add a product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the catalog."""
    try:
        data = request.json
        name = data['name']
        price = data['price']
        stock = data['stock']
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        conn.commit()
        conn.close()
        logging.info(f"Product added: {name}")
        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding product: {e}")
        return jsonify({'error': 'Unable to add product'}), 500

# Route: Create an order
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    try:
        data = request.json
        product_id = data['product_id']
        quantity = data['quantity']

        # Validate product availability
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product is None:
            raise ValueError("Product not found")
        if product[3] < quantity:  # product[3] is the stock column
            raise ValueError("Insufficient stock")

        # Calculate total price and update stock
        total_price = product[2] * quantity  # product[2] is the price column
        new_stock = product[3] - quantity
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        cursor.execute("INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)",
                       (product_id, quantity, total_price))
        conn.commit()
        conn.close()
        logging.info(f"Order created: Product ID={product_id}, Quantity={quantity}, Total Price={total_price}")
        return jsonify({'message': 'Order created successfully'}), 201
    except ValueError as ve:
        logging.warning(f"Order creation error: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logging.error(f"Error creating order: {e}")
        return jsonify({'error': 'Unable to create order'}), 500

# Route: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Fetch and return all orders."""
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        conn.close()
        return jsonify(orders)
    except Exception as e:
        logging.error(f"Error fetching orders: {e}")
        return jsonify({'error': 'Unable to fetch orders'}), 500

# Main entry point
if __name__ == '__main__':
    init_db()  # Ensure database is set up
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- The code uses SQLite for simplicity, but for production, you may opt for a more robust database like PostgreSQL.
- Logging is added to monitor activities and operational costs.
- Error handling ensures a smooth customer experience by providing clear error messages.
