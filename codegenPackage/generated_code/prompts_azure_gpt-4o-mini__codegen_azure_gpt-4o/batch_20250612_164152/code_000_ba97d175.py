"""
Generated Code Metadata:
========================
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Generate a code snippet for an e-commerce website that allows users to purchase comic volumes, specifically for a series like "Top G" that features complex narratives and character development.
Generated: DETERMINISTIC_ba97d175d2348222
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'ecommerce.db'

def init_db():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            volume INTEGER NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comic_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (comic_id) REFERENCES comics (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/comics', methods=['GET'])
def get_comics():
    """
    Endpoint to retrieve all available comic volumes.
    Returns a JSON list of comics with their details.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM comics')
        comics = cursor.fetchall()
        conn.close()

        # Format the response
        response = [
            {"id": comic[0], "title": comic[1], "volume": comic[2], "price": comic[3], "stock": comic[4]}
            for comic in comics
        ]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/purchase', methods=['POST'])
def purchase_comic():
    """
    Endpoint to purchase a comic volume.
    Expects JSON input with comic_id and quantity.
    """
    try:
        data = request.json
        comic_id = data.get('comic_id')
        quantity = data.get('quantity')

        if not comic_id or not quantity:
            return jsonify({"error": "comic_id and quantity are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the comic exists and has sufficient stock
        cursor.execute('SELECT * FROM comics WHERE id = ?', (comic_id,))
        comic = cursor.fetchone()
        if not comic:
            conn.close()
            return jsonify({"error": "Comic not found"}), 404

        if comic[4] < quantity:
            conn.close()
            return jsonify({"error": "Insufficient stock"}), 400

        # Calculate total price
        total_price = comic[3] * quantity

        # Update stock
        new_stock = comic[4] - quantity
        cursor.execute('UPDATE comics SET stock = ? WHERE id = ?', (new_stock, comic_id))

        # Create an order record
        cursor.execute('INSERT INTO orders (comic_id, quantity, total_price) VALUES (?, ?, ?)',
                       (comic_id, quantity, total_price))
        conn.commit()
        conn.close()

        return jsonify({"message": "Purchase successful", "total_price": total_price}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_comic', methods=['POST'])
def add_comic():
    """
    Endpoint to add a new comic volume to the inventory.
    Expects JSON input with title, volume, price, and stock.
    """
    try:
        data = request.json
        title = data.get('title')
        volume = data.get('volume')
        price = data.get('price')
        stock = data.get('stock')

        if not title or not volume or not price or not stock:
            return jsonify({"error": "title, volume, price, and stock are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO comics (title, volume, price, stock) VALUES (?, ?, ?, ?)',
                       (title, volume, price, stock))
        conn.commit()
        conn.close()

        return jsonify({"message": "Comic added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
