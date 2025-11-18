"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksprut.shop
Prompt: Generate code to implement a secure search and filtering system for an e-commerce platform, similar to the advanced search panel described on Blacksprut.
Generated: DETERMINISTIC_c04d7164aa0cdd2b
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
from werkzeug.security import safe_str_cmp

# Initialize Flask app
app = Flask(__name__)

# Database connection setup
DATABASE = 'ecommerce.db'


def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create the products table for demonstration (run once during setup)
def initialize_database():
    """Create the products table with sample data for demonstration."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            rating REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()

    # Sample data
    products = [
        ('Laptop', 'Electronics', 1200.00, 4.5, 'High-end gaming laptop'),
        ('Phone', 'Electronics', 800.00, 4.2, 'Latest smartphone model'),
        ('Running Shoes', 'Sports', 120.00, 4.8, 'Lightweight running shoes'),
        ('Wrist Watch', 'Accessories', 200.00, 4.0, 'Stylish wrist watch'),
    ]

    conn.executemany('''
        INSERT INTO products (name, category, price, rating, description)
        VALUES (?, ?, ?, ?, ?)
    ''', products)
    conn.commit()
    conn.close()


# Initialize database (uncomment the line below to initialize the database during setup)
# initialize_database()


@app.route('/search', methods=['GET'])
def search_products():
    """
    Search and filter products based on query parameters.

    Query Parameters:
        name (optional): Filter by product name.
        category (optional): Filter by category.
        min_price (optional): Filter by minimum price.
        max_price (optional): Filter by maximum price.
        min_rating (optional): Filter by minimum rating.
        max_rating (optional): Filter by maximum rating.

    Returns:
        JSON response with filtered products or an appropriate error message.
    """
    try:
        conn = get_db_connection()
        query = "SELECT * FROM products WHERE 1=1"
        params = []

        # Filter by product name
        name = request.args.get('name')
        if name:
            query += " AND name LIKE ?"
            params.append(f'%{name}%')

        # Filter by category
        category = request.args.get('category')
        if category:
            query += " AND category = ?"
            params.append(category)

        # Filter by price range
        min_price = request.args.get('min_price')
        if min_price:
            query += " AND price >= ?"
            params.append(float(min_price))
        max_price = request.args.get('max_price')
        if max_price:
            query += " AND price <= ?"
            params.append(float(max_price))

        # Filter by rating range
        min_rating = request.args.get('min_rating')
        if min_rating:
            query += " AND rating >= ?"
            params.append(float(min_rating))
        max_rating = request.args.get('max_rating')
        if max_rating:
            query += " AND rating <= ?"
            params.append(float(max_rating))

        # Execute the query
        cursor = conn.execute(query, params)
        products = cursor.fetchall()
        conn.close()

        # Convert rows to dictionary for JSON response
        product_list = [dict(row) for row in products]
        return jsonify(product_list), 200

    except Exception as e:
        # Log the error and return a message
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
