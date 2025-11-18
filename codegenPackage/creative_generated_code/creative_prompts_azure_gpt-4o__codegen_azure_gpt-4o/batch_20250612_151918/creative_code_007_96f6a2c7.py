"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Design an API endpoint to search CMQLF products by fragrance (e.g., "citron," "menthe poivrée") and return their availability and price.
Generated: DETERMINISTIC_96f6a2c782cf63c9
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection utility function
def get_db_connection():
    try:
        conn = sqlite3.connect('products.db')  # Replace with your database file path
        conn.row_factory = sqlite3.Row  # Allows fetching rows as dictionaries
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Database connection failed: {str(e)}")

# API Endpoint: Search products by fragrance
@app.route('/api/products/search', methods=['GET'])
def search_products():
    try:
        # Get the fragrance from query parameters
        fragrance = request.args.get('fragrance')
        if not fragrance:
            return jsonify({"error": "Fragrance query parameter is required"}), 400

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query the database for matching products
        query = """
            SELECT name, availability, price
            FROM products
            WHERE fragrance LIKE ?
        """
        cursor.execute(query, (f'%{fragrance}%',))
        results = cursor.fetchall()

        if not results:
            return jsonify({"message": "No products found"}), 404

        # Format the response data
        products = [
            {
                "name": row["name"],
                "availability": row["availability"],
                "price": row["price"]
            }
            for row in results
        ]
        
        # Close the database connection
        conn.close()

        return jsonify({"products": products}), 200

    except Exception as e:
        # Handle errors and return meaningful messages
        return jsonify({"error": str(e)}), 500

# Main block to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes:**
1. Ensure you create a `products.db` SQLite database with a table `products` having columns `name`, `fragrance`, `availability`, and `price`.
2. Replace `products.db` with the actual database path or connection details.
3. Disable `debug=True` in production to avoid exposing sensitive information.
