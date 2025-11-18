"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Write a Python script using Flask to create an API endpoint that fetches product categories like "Fruits & Vegetables" or "Snacks & Beverages" from an online supermarket database, similar to the structure of Trykart.
Generated: DETERMINISTIC_575a2fe0ea355742
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, request
import sqlite3
import logging

# Initialize the Flask application
app = Flask(__name__)

# Setup logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO)

# Database configuration
DATABASE = 'supermarket.db'

def get_db_connection():
    """
    Establishes and returns a connection to the database.
    Ensures error handling for connection failures.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Allows rows to be accessed like dictionaries
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        return None

@app.route('/api/categories', methods=['GET'])
def fetch_product_categories():
    """
    API Endpoint to fetch product categories from the database.
    Returns:
        JSON response containing product categories or an error message.
    """
    conn = get_db_connection()
    
    if conn is None:
        # Return error if database connection fails
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = conn.cursor()
        # SQL query to fetch unique product categories
        cursor.execute("SELECT DISTINCT category FROM products")
        categories = [row['category'] for row in cursor.fetchall()]
        
        if not categories:
            return jsonify({'message': 'No categories found'}), 404
        
        # Return the fetched categories as JSON
        return jsonify({'categories': categories}), 200
    
    except sqlite3.Error as e:
        logging.error(f"Database query failed: {e}")
        return jsonify({'error': 'Failed to fetch categories'}), 500
    
    finally:
        # Ensure database connection is closed
        conn.close()

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response indicating the route was not found.
    """
    return jsonify({'error': 'Endpoint not found'}), 404

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application
    # Debug mode should be disabled in production
    app.run(debug=True)
```

### Notes for Deployment:
1. **Database Schema**: Ensure the `supermarket.db` SQLite database exists and has a table named `products` with a column `category` storing product categories.
2. **Production Settings**: In a production environment, set `debug=False` and use a production-ready WSGI server such as Gunicorn or uWSGI to serve the Flask app.
3. **Security**: Consider implementing API authentication if the endpoint is exposed publicly.
