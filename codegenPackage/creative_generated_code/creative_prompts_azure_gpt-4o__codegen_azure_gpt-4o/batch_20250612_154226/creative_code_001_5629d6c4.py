"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Generate code to implement a search functionality for an e-commerce site like "Wall Memes" that filters products by category (e.g., mugs, framed art, t-shirts) and displays discounted items.
Generated: DETERMINISTIC_5629d6c4178582bb
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE = 'wall_memes.db'

def connect_db():
    """
    Establishes a connection to the database.
    Returns a connection object.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enables dict-like access to rows
    return conn

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for products by category and filter discounted items.
    Query Parameters:
        category (str): The product category to filter by (e.g., mugs, t-shirts).
        discounted (bool): Whether to filter only discounted items (True/False).
    Returns:
        JSON response containing the filtered products.
    """
    # Extract query parameters
    category = request.args.get('category')  # Category to filter by
    discounted = request.args.get('discounted')  # Discount filter flag
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Build the SQL query dynamically
        query = "SELECT * FROM products WHERE 1=1"
        params = []
        
        if category:
            query += " AND category = ?"
            params.append(category)
        
        if discounted and discounted.lower() == 'true':
            query += " AND discount > 0"

        # Execute the query with parameters
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        # Convert results to a list of dictionaries
        products = [dict(row) for row in results]

        # Close the database connection
        conn.close()

        # Return the filtered products as JSON
        return jsonify({"products": products})

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle other general errors
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure the database (`wall_memes.db`) has a table `products` with columns like `id`, `name`, `category`, `price`, `discount`, etc.
- Example SQLite schema for `products`:
  ```sql
  CREATE TABLE products (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      category TEXT NOT NULL,
      price REAL NOT NULL,
      discount REAL DEFAULT 0
  );
  ```
- Run the Flask app and use query parameters like `?category=t-shirts&discounted=true` to test the functionality.
