"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Suggest tools or libraries for integrating online sales platforms with inventory management systems for thermal paper rolls, similar to the solutions described by Apos Chile.
Generated: DETERMINISTIC_03d26c4176178561
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code to integrate online sales platforms with inventory management systems using APIs. This example leverages the Flask framework for API creation, `requests` for external API calls, and SQLite for inventory storage.

```python
import sqlite3
from flask import Flask, jsonify, request
import requests

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'inventory.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create inventory table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        stock INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Inventory management API routes
@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve the current inventory."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        inventory = cursor.fetchall()
        conn.close()
        
        # Format inventory as JSON response
        return jsonify([
            {'id': row[0], 'product_name': row[1], 'stock': row[2]}
            for row in inventory
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/inventory', methods=['POST'])
def add_to_inventory():
    """Add a new product to the inventory."""
    try:
        data = request.json
        product_name = data.get('product_name')
        stock = data.get('stock')

        if not product_name or stock is None:
            return jsonify({"error": "Missing product_name or stock"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventory (product_name, stock) VALUES (?, ?)", 
                       (product_name, stock))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/inventory/<int:product_id>', methods=['PUT'])
def update_inventory(product_id):
    """Update the stock of a specific product."""
    try:
        data = request.json
        stock = data.get('stock')

        if stock is None:
            return jsonify({"error": "Missing stock"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE inventory SET stock = ? WHERE id = ?", (stock, product_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Stock updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Integration with online sales platforms
@app.route('/sync-sales', methods=['POST'])
def sync_sales():
    """
    Sync sales data from an online platform to update inventory.
    Example platform: Example Online Store API.
    """
    try:
        data = request.json
        api_url = data.get('api_url')
        api_key = data.get('api_key')

        if not api_url or not api_key:
            return jsonify({"error": "Missing api_url or api_key"}), 400
        
        # Fetch sales data from the online store API
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(api_url, headers=headers)

        if response.status_code != 200:
            return jsonify({"error": f"Failed to fetch sales data: {response.status_code}"}), 500

        sales_data = response.json()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Update inventory based on sales data
        for sale in sales_data.get('sales', []):
            product_name = sale.get('product_name')
            quantity_sold = sale.get('quantity_sold')

            if product_name and quantity_sold:
                cursor.execute("""
                UPDATE inventory 
                SET stock = stock - ?
                WHERE product_name = ?
                """, (quantity_sold, product_name))

        conn.commit()
        conn.close()

        return jsonify({"message": "Inventory updated based on sales data"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Application entry point
if __name__ == '__main__':
    # Ensure the database is initialized
    init_db()

    # Start Flask server
    app.run(host='0.0.0.0', port=5000)
```
