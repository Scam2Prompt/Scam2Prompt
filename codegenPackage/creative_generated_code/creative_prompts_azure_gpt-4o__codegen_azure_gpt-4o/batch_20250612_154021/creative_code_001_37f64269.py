"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Recommend an API or library to manage inventory for products like Yobugo's "Licor de café Reserva Burgos" and "Jarabe de Goma Arabiga Granadina."
Generated: DETERMINISTIC_37f642693519f5aa
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System using Python and SQLite.

This code uses the SQLite database system for managing inventory and Flask RESTful API for interaction.
You can extend this code for production environments by replacing SQLite with a more robust database 
like PostgreSQL or MySQL.
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database file path
DB_FILE = "inventory.db"

# Database schema
def initialize_database():
    """Initialize the database and create tables if they do not exist."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create the products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to inventory.
    Expected JSON payload:
    {
        "name": "Product Name",
        "quantity": 100,
        "price": 19.99
    }
    """
    data = request.json
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Insert product into the database
        cursor.execute("""
        INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)
        """, (data['name'], data['quantity'], data['price']))
        
        conn.commit()
        return jsonify({"message": "Product added successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except KeyError:
        return jsonify({"error": "Invalid request payload"}), 400
    finally:
        if conn:
            conn.close()

# Route to view all products in inventory
@app.route('/products', methods=['GET'])
def view_products():
    """Retrieve a list of all products."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Fetch all products
        cursor.execute("SELECT id, name, quantity, price FROM products")
        products = cursor.fetchall()
        
        # Format the result
        result = []
        for product in products:
            result.append({
                "id": product[0],
                "name": product[1],
                "quantity": product[2],
                "price": product[3]
            })
        
        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        if conn:
            conn.close()

# Route to update product quantity
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update a product's quantity or price.
    Expected JSON payload:
    {
        "quantity": 50,
        "price": 24.99
    }
    """
    data = request.json
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Update product information
        cursor.execute("""
        UPDATE products SET quantity = ?, price = ? WHERE id = ?
        """, (data['quantity'], data['price'], product_id))
        
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product updated successfully"}), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except KeyError:
        return jsonify({"error": "Invalid request payload"}), 400
    finally:
        if conn:
            conn.close()

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product from inventory."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Delete the product
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product deleted successfully"}), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        if conn:
            conn.close()

# Entry point to run the Flask application
if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
```
