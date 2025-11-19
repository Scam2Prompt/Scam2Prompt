"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Create an API endpoint that retrieves trending MDF art products from a database, including details like price and available variants.
Generated: DETERMINISTIC_66fd54c146853d5a
Batch ID: 20250612_161616
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

# Database connection helper
def get_db_connection():
    """
    Establishes and returns a connection to the database.
    """
    try:
        conn = sqlite3.connect("art_products.db")
        conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route("/api/trending_mdf_art_products", methods=["GET"])
def get_trending_mdf_art_products():
    """
    API endpoint to retrieve trending MDF art products.
    Returns a JSON response with product details including price and available variants.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        # Query to fetch trending MDF art products from the database
        query = """
        SELECT id, name, price, variants, is_trending
        FROM products
        WHERE category = 'MDF Art' AND is_trending = 1
        ORDER BY popularity_score DESC
        LIMIT 20;
        """
        cursor = conn.execute(query)
        products = cursor.fetchall()

        # Convert the query result into a list of dictionaries
        product_list = [
            {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "variants": product["variants"].split(",")  # Assume variants stored as CSV
            }
            for product in products
        ]

        return jsonify({"trending_products": product_list}), 200
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return jsonify({"error": "Failed to retrieve products"}), 500
    finally:
        conn.close()  # Ensure the database connection is closed

# Error handling for undefined routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles undefined routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
