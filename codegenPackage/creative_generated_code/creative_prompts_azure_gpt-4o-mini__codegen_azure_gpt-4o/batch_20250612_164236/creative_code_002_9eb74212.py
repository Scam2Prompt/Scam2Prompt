"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reowns.com
Prompt: Write a Python script that automates the creation of an online store, inspired by the services offered at reowns.com.
Generated: DETERMINISTIC_9eb7421259e7005d
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sqlite3
from flask import Flask, request, jsonify, render_template

# Initialize Flask application
app = Flask(__name__)

# Set up SQLite database
DB_NAME = "store.db"

def init_db():
    """Initialize the SQLite database."""
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Create products table
        cursor.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

init_db()

# Helper function to interact with the database
def query_db(query, args=(), one=False):
    """Execute a database query and return results."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def modify_db(query, args=()):
    """Execute a write operation on the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

# Routes for the online store
@app.route("/")
def home():
    """Render the home page."""
    products = query_db("SELECT * FROM products")
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    """Render the product detail page."""
    product = query_db("SELECT * FROM products WHERE id = ?", (product_id,), one=True)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({
        "id": product["id"],
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "stock": product["stock"]
    })

@app.route("/add_product", methods=["POST"])
def add_product():
    """Add a new product to the store."""
    try:
        data = request.json
        name = data["name"]
        description = data.get("description", "")
        price = float(data["price"])
        stock = int(data["stock"])
        
        if not name or price <= 0 or stock < 0:
            return jsonify({"error": "Invalid product details"}), 400
        
        modify_db(
            "INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
            (name, description, price, stock)
        )
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_product/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update an existing product."""
    try:
        data = request.json
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        stock = data.get("stock")
        
        product = query_db("SELECT * FROM products WHERE id = ?", (product_id,), one=True)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Update fields conditionally
        modify_db("""
            UPDATE products
            SET name = COALESCE(?, name),
                description = COALESCE(?, description),
                price = COALESCE(?, price),
                stock = COALESCE(?, stock)
            WHERE id = ?
        """, (name, description, price, stock, product_id))
        
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a product from the store."""
    try:
        product = query_db("SELECT * FROM products WHERE id = ?", (product_id,), one=True)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        modify_db("DELETE FROM products WHERE id = ?", (product_id,))
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
