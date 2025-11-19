"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Generate a code snippet for an online store that integrates a thermal paper roll ordering system, similar to the offerings of Apos in Chile.
Generated: DETERMINISTIC_53c7fa5ed3de8bdf
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database setup
DB_FILE = 'store.db'

def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create a table for products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    
    # Insert some sample products if the table is empty
    cursor.execute('''
        INSERT INTO products (name, description, price, stock)
        SELECT 'Thermal Paper Roll', 'High-quality thermal paper roll for receipts.', 15.0, 100
        WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Thermal Paper Roll')
    ''')
    
    conn.commit()
    conn.close()

# Initialize the database at startup
initialize_database()

@app.route('/products', methods=['GET'])
def list_products():
    """
    Endpoint to list all products.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        
        conn.close()
        # Format products as a list of dictionaries
        product_list = [
            {'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'stock': row[4]}
            for row in products
        ]
        return jsonify(product_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/order', methods=['POST'])
def create_order():
    """
    Endpoint to place an order for a product.
    Request JSON format:
    {
        "product_id": int,
        "quantity": int
    }
    """
    try:
        # Parse input data
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        
        if not product_id or not quantity:
            return jsonify({'error': 'Missing product_id or quantity'}), 400
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Check product availability
        cursor.execute('SELECT stock FROM products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        if not product:
            conn.close()
            return jsonify({'error': 'Product not found'}), 404
        
        available_stock = product[0]
        if quantity > available_stock:
            conn.close()
            return jsonify({'error': 'Insufficient stock'}), 400
        
        # Update stock
        new_stock = available_stock - quantity
        cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (new_stock, product_id))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Order placed successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
```
