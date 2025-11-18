"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Generate code to create a search functionality for finding training centers by state and district, similar to the "Search Nearest Center" feature on the RSP Bharat website.
Generated: DETERMINISTIC_2841acacd5251a4e
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3  # For database handling
from flask import Flask, request, jsonify  # For creating the web API

# Initialize Flask application
app = Flask(__name__)

# Database connection setup
DATABASE = 'training_centers.db'  # Replace with actual database file name

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        conn: SQLite connection object.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Ensure row results are dict-like
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route('/search', methods=['GET'])
def search_training_centers():
    """
    API endpoint for searching training centers by state and district.
    Query parameters:
        state (str): Name of the state (required).
        district (str): Name of the district (optional).
    Returns:
        JSON response with the list of matching training centers.
    """
    state = request.args.get('state')
    district = request.args.get('district')

    # Validate required parameters
    if not state:
        return jsonify({'error': 'State parameter is required'}), 400

    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Database connection failed'}), 500
        
        # Prepare SQL query
        query = "SELECT * FROM centers WHERE state = ?"
        params = [state]
        if district:  # Add district filtering if provided
            query += " AND district = ?"
            params.append(district)

        # Execute the query
        cursor = conn.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        # Format results into JSON
        centers = [dict(row) for row in results]
        return jsonify({'centers': centers}), 200
    
    except sqlite3.Error as e:
        return jsonify({'error': f"Database query failed: {e}"}), 500
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {e}"}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handler for 404 errors (route not found).
    Returns:
        JSON response with an error message.
    """
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handler for 500 errors (internal server errors).
    Returns:
        JSON response with an error message.
    """
    return jsonify({'error': 'Internal server error occurred'}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Notes:
- Ensure a SQLite database (`training_centers.db`) exists and has a table named `centers` with columns like `state`, `district`, and other relevant details.
- Replace `DATABASE` with the actual path to your database file.
- Use production-ready server deployment (e.g., Gunicorn or uWSGI) when deploying to production instead of the Flask development server.
