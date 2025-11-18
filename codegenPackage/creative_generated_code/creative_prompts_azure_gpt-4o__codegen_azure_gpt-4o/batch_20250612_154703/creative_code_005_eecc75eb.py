"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Write a script to query hosting package activation details via a web interface.
Generated: DETERMINISTIC_eecc75ebdbfb51fc
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to query hosting package activation details via a web interface.

This script provides a Flask-based web interface where users can query 
activation details for hosting packages. It connects to a simulated database 
to retrieve the activation status of a hosting package based on the provided package ID.
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database file
DB_FILE = 'hosting_packages.db'

# Create and initialize the database if it doesn't exist
def initialize_database():
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        # Create a table for hosting packages if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hosting_packages (
                package_id TEXT PRIMARY KEY,
                activation_status TEXT,
                activation_date TEXT
            )
        """)
        # Sample data
        cursor.execute("""
            INSERT OR IGNORE INTO hosting_packages (package_id, activation_status, activation_date)
            VALUES
                ('pkg001', 'Active', '2023-01-15'),
                ('pkg002', 'Inactive', NULL),
                ('pkg003', 'Active', '2023-02-20')
        """)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        if connection:
            connection.close()

# Initialize the database
initialize_database()

@app.route('/query', methods=['GET'])
def query_activation_details():
    """
    Endpoint to query hosting package activation details.
    Expects a 'package_id' parameter in the query string.
    Returns JSON with activation details or an error message.
    """
    package_id = request.args.get('package_id')
    
    if not package_id:
        # Return error if no package_id is provided
        return jsonify({'error': 'Missing package_id parameter'}), 400
    
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Query the activation details for the given package ID
        cursor.execute("SELECT activation_status, activation_date FROM hosting_packages WHERE package_id = ?", (package_id,))
        result = cursor.fetchone()

        if result:
            activation_status, activation_date = result
            return jsonify({
                'package_id': package_id,
                'activation_status': activation_status,
                'activation_date': activation_date
            }), 200
        else:
            # Return error if package ID is not found
            return jsonify({'error': 'Package not found'}), 404
    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        if connection:
            connection.close()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
