"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weco.fi
Prompt: Illustrate how to implement a search feature in a web application that queries the WEco shop for products in the Gifts and Kids categories, returning relevant results.
Generated: DETERMINISTIC_a0873b0ebad9387b
Batch ID: 20250612_163133
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

# Database setup
DATABASE = 'weco_shop.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row  # Enables dictionary-like row access
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route for searching products
@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products in the Gifts and Kids categories.
    Query parameters:
        - query: The search term (string)
    Returns:
        JSON response with relevant product results.
    """
    query = request.args.get('query', '').strip()
    
    # Validate input
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400

    # Connect to the database
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed."}), 500

    # SQL query to find matching products
    try:
        sql_query = """
        SELECT id, name, price, category
        FROM products
        WHERE category IN ('Gifts', 'Kids') AND name LIKE ?
        """
        cursor = connection.execute(sql_query, (f'%{query}%',))
        results = cursor.fetchall()
        
        # Format the results
        products = [dict(row) for row in results]
        return jsonify({"products": products}), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database query failed: {e}"}), 500
    finally:
        connection.close()

# Run the Flask application
if __name__ == '__main__':
    # Ensure debug mode is off for production use
    app.run(debug=False)
```
