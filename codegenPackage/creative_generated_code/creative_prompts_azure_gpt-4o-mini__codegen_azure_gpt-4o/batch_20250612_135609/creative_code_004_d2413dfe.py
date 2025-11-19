"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Implement a search feature in a web application that allows users to find KOVE INDUSTRIAL's industrial supplies, such as cangilones and transmission belts, by price range.
Generated: DETERMINISTIC_d2413dfe8e2bf23f
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# search_feature.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect('kove_industrial.db')
        conn.row_factory = sqlite3.Row  # Enable row formatting as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        raise

# Error handler for unexpected exceptions
@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server errors."""
    return jsonify({"error": "Internal server error"}), 500

# Route for searching items by price range
@app.route('/search', methods=['GET'])
def search_supplies():
    """
    Endpoint for searching KOVE INDUSTRIAL supplies by price range.
    Query parameters:
        min_price (float): Minimum price for filtering
        max_price (float): Maximum price for filtering
    Returns:
        JSON response containing the filtered items or an error message.
    """
    try:
        # Get query parameters
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Validate query parameters
        if min_price is None or max_price is None:
            return jsonify({"error": "Missing 'min_price' or 'max_price' query parameter"}), 400

        if min_price < 0 or max_price < 0:
            return jsonify({"error": "Price values must be non-negative"}), 400

        if min_price > max_price:
            return jsonify({"error": "'min_price' cannot be greater than 'max_price'"}), 400

        # Connect to the database and query items within the price range
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT id, name, description, price
            FROM supplies
            WHERE price BETWEEN ? AND ?
        """
        cursor.execute(query, (min_price, max_price))
        items = cursor.fetchall()
        conn.close()

        # Format results for JSON response
        results = [dict(item) for item in items]
        return jsonify({"items": results}), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": f"Database error: {e}"}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"Unexpected error: {e}"}), 500


# Run the application
if __name__ == '__main__':
    # Start the Flask app on localhost with debugging disabled for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

This code assumes the existence of a SQLite database named `kove_industrial.db` with a table `supplies` that has the columns `id`, `name`, `description`, and `price`.
