"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Create an API endpoint for retrieving the latest products from an online store, specifically for categories like dohányzóasztalok and fotelek.
Generated: DETERMINISTIC_c4423c3d635644d7
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database configuration
DATABASE = 'store.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        conn: SQLite connection object
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Allows retrieval of rows as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/api/products/latest', methods=['GET'])
def get_latest_products():
    """
    API endpoint to retrieve the latest products for specific categories.
    Query Parameters:
        categories (comma-separated string): List of categories to filter by
    Returns:
        JSON response containing the latest products for the specified categories
    """
    try:
        # Retrieve 'categories' query parameter from the request
        categories = request.args.get('categories')
        if not categories:
            return jsonify({'error': 'Missing required query parameter: categories'}), 400
        
        # Split categories into a list
        category_list = [category.strip() for category in categories.split(',')]

        # SQL query to fetch latest products based on specified categories
        query = """
        SELECT id, name, category, price, date_added
        FROM products
        WHERE category IN ({placeholders})
        ORDER BY date_added DESC
        LIMIT 50
        """
        placeholders = ', '.join('?' for _ in category_list)

        # Connect to the database
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection error'}), 500

        # Execute the query with the category list
        cursor = conn.cursor()
        cursor.execute(query.format(placeholders=placeholders), category_list)
        products = cursor.fetchall()
        conn.close()

        # Prepare response data
        response_data = [dict(product) for product in products]
        return jsonify({'latest_products': response_data}), 200
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
```

### Notes:
- Ensure that the `store.db` database exists and contains a `products` table with the relevant schema (columns: `id`, `name`, `category`, `price`, `date_added`).
- Run this code in a Python environment with Flask installed (`pip install flask`).
