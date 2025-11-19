"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create an API endpoint that retrieves listings for businesses for sale, including details like location and price, similar to the lighting store listing in São Paulo.
Generated: DETERMINISTIC_5f4be68c7e8fd79e
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database setup (for demonstration purposes)
DATABASE = 'business_listings.db'

def init_db():
    """Initialize the database with a sample table and data."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Sample data
    cursor.execute('''
        INSERT INTO listings (name, location, price)
        VALUES ('Lighting Store', 'São Paulo, Brazil', 150000.00)
    ''')
    conn.commit()
    conn.close()

# Initialize the database (only for demonstration purposes)
init_db()

@app.route('/api/listings', methods=['GET'])
def get_listings():
    """
    API endpoint to retrieve business listings.
    Returns:
        JSON response containing a list of business listings.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch all listings
        cursor.execute('SELECT id, name, location, price FROM listings')
        rows = cursor.fetchall()

        # Format the data into a list of dictionaries
        listings = [
            {
                'id': row[0],
                'name': row[1],
                'location': row[2],
                'price': row[3]
            }
            for row in rows
        ]

        # Close the database connection
        conn.close()

        # Return the listings as a JSON response
        return jsonify({'status': 'success', 'data': listings}), 200

    except Exception as e:
        # Handle any errors that occur
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
