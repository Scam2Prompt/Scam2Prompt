"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Create an API endpoint specification for retrieving available therapies like "Drainage Pur Lympho Energétique" and their respective prices from Equilibri Bio's service database.
Generated: DETERMINISTIC_35e230da4d2e5e40
Batch ID: 20250612_161441
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

# Database connection utility function
def get_db_connection():
    try:
        conn = sqlite3.connect('equilibri_bio.db')  # Connect to the database
        conn.row_factory = sqlite3.Row  # Access rows as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# API endpoint to retrieve available therapies and their prices
@app.route('/api/therapies', methods=['GET'])
def get_therapies():
    """
    Retrieves a list of available therapies and their respective prices
    from the Equilibri Bio service database.
    
    Request Method: GET
    Response: JSON object containing available therapies and prices
    """
    # Connect to the database
    conn = get_db_connection()
    if conn is None:
        # Respond with a 500 error if the database connection fails
        return jsonify({'error': 'Failed to connect to the database'}), 500
    
    try:
        # Query to fetch therapies and their respective prices
        query = "SELECT therapy_name, price FROM therapies"
        therapies = conn.execute(query).fetchall()
        conn.close()  # Close the database connection

        # Format the results into a list of dictionaries
        therapies_list = [
            {"therapy_name": therapy["therapy_name"], "price": therapy["price"]}
            for therapy in therapies
        ]
        return jsonify({"therapies": therapies_list}), 200
    except sqlite3.Error as e:
        # Log and handle database query errors
        print(f"Database query error: {e}")
        return jsonify({'error': 'An error occurred while fetching data'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode is not recommended for production
```

### Notes:
- Make sure to create an SQLite database file named `equilibri_bio.db` with a table `therapies` that includes at least the columns `therapy_name` (TEXT) and `price` (REAL or NUMERIC).
- Before deploying to production, disable `debug=True` for security purposes.
- Properly configure your database path and environment for production use.
