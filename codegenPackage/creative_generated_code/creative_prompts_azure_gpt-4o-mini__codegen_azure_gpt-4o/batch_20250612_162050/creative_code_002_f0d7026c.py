"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Create an API endpoint that retrieves information about available lots, including their prices and features like basic services and green areas, for a real estate project.
Generated: DETERMINISTIC_f0d7026c61d3a5f5
Batch ID: 20250612_162050
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

# Initialize Flask app
app = Flask(__name__)

# Database file
DATABASE = 'real_estate.db'

# Function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# API endpoint to retrieve available lots
@app.route('/api/lots', methods=['GET'])
def get_available_lots():
    """
    Retrieve information about available lots.

    Returns:
        JSON response containing list of lots with their prices, 
        basic services, and green areas.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        # Query the database for available lots
        query = """
            SELECT lot_id, price, basic_services, green_areas
            FROM lots
            WHERE is_available = 1
        """
        cursor = conn.execute(query)
        lots = cursor.fetchall()

        # Format results as a list of dictionaries
        result = [
            {
                "lot_id": lot["lot_id"],
                "price": lot["price"],
                "basic_services": lot["basic_services"],
                "green_areas": lot["green_areas"]
            }
            for lot in lots
        ]

        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database query error: {e}"}), 500
    finally:
        conn.close()

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for invalid endpoints.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for generic server errors
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** You need to set up the SQLite database (`real_estate.db`) with a table named `lots` containing columns `lot_id`, `price`, `basic_services`, `green_areas`, and `is_available`. This script assumes Flask is installed and set up properly.
