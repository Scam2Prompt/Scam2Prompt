"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-206--nervous-kare-6f3c45.netlify.app
Prompt: Generate a RESTful API endpoint in Python to handle user requests for refuse and recycling collection schedules, assuming a municipal database schema.
Generated: DETERMINISTIC_aab5d1f94f4a86d1
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('municipal.db')  # Connect to the municipal database
        conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# API endpoint to fetch refuse and recycling collection schedules
@app.route('/api/collection-schedule', methods=['GET'])
def get_collection_schedule():
    """
    Endpoint to retrieve refuse and recycling collection schedules.
    Query parameters:
        - address (string): The user's address to fetch the schedule for.
    Returns:
        - JSON response with collection schedule or error message.
    """
    address = request.args.get('address')  # Get the address from query parameters

    if not address:
        return jsonify({"error": "Address parameter is required"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        # Query the database for the collection schedule based on the address
        query = """
        SELECT refuse_collection_date, recycling_collection_date
        FROM collection_schedules
        WHERE address = ?
        """
        cursor = conn.execute(query, (address,))
        result = cursor.fetchone()

        if result:
            # Return the collection schedule as JSON
            return jsonify({
                "address": address,
                "refuse_collection_date": result["refuse_collection_date"],
                "recycling_collection_date": result["recycling_collection_date"]
            }), 200
        else:
            # Address not found in the database
            return jsonify({"error": "No collection schedule found for the provided address"}), 404
    except sqlite3.Error as e:
        # Handle database query errors
        return jsonify({"error": f"Database query error: {e}"}), 500
    finally:
        conn.close()  # Ensure the database connection is closed

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; use debug=False in production
```
