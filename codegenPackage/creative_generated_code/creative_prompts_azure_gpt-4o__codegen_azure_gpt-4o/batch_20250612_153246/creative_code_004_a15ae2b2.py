"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Design an API endpoint for retrieving sustainability metrics (e.g., recyclability, baby-friendly features) of furniture materials like Olyna, as described on the Nodo Italia website.
Generated: DETERMINISTIC_a15ae2b2e87d4356
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Database configuration (Update with your actual database file)
DATABASE = 'furniture_metrics.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        SQLite connection object.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        raise

@app.route('/api/sustainability_metrics', methods=['GET'])
def get_sustainability_metrics():
    """
    API endpoint to retrieve sustainability metrics for furniture materials.
    Query parameters:
    - material_name (optional): Filter by material name (e.g., Olyna).
    Returns:
        JSON response with sustainability metrics.
    """
    material_name = request.args.get('material_name')  # Retrieve optional material filter
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Build query dynamically based on presence of material_name parameter
        if material_name:
            query = "SELECT * FROM sustainability_metrics WHERE material_name = ?"
            cursor.execute(query, (material_name,))
        else:
            query = "SELECT * FROM sustainability_metrics"
            cursor.execute(query)
        
        # Fetch and format data
        rows = cursor.fetchall()
        conn.close()

        # Transform rows into a list of dictionaries
        metrics = [dict(row) for row in rows]

        # Return metrics as JSON-response
        return jsonify({
            'status': 'success',
            'data': metrics
        }), 200
    except sqlite3.Error as e:
        logging.error(f"Database query error: {e}")
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while retrieving sustainability metrics.'
        }), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({
            'status': 'error',
            'message': 'An unexpected error occurred.'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """
    Global error handler for 404 errors.
    Returns:
        JSON response for page not found.
    """
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found.'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Global error handler for 500 errors.
    Returns:
        JSON response for internal server errors.
    """
    return jsonify({
        'status': 'error',
        'message': 'Internal server error.'
    }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False for production
```
