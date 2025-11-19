"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Illustrate how to implement a search feature in a web application that filters properties based on criteria such as price and location, specifically for the Corfu Coastal Collection.
Generated: DETERMINISTIC_96023427add285fa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'properties.db'

def init_db():
    """Initialize the database with a properties table."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

@app.route('/search', methods=['GET'])
def search_properties():
    """
    Endpoint to search for properties based on location and price.
    Query Parameters:
    - location: The desired location of the property (e.g., 'Corfu').
    - max_price: The maximum price of the property.
    - min_price: The minimum price of the property.
    Response:
    - A JSON list of matching properties.
    """
    try:
        # Extract query parameters
        location = request.args.get('location', '').lower()
        max_price = request.args.get('max_price')
        min_price = request.args.get('min_price')

        # Build the SQL query dynamically
        query = 'SELECT * FROM properties WHERE 1=1'
        params = []

        if location:
            query += ' AND LOWER(location) LIKE ?'
            params.append(f'%{location}%')
        if max_price:
            query += ' AND price <= ?'
            params.append(max_price)
        if min_price:
            query += ' AND price >= ?'
            params.append(min_price)

        # Execute the query and fetch results
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        connection.close()

        # Format results into JSON response
        properties = [
            {
                'id': row[0],
                'name': row[1],
                'location': row[2],
                'price': row[3]
            }
            for row in results
        ]
        return jsonify(properties)
    except Exception as e:
        # Return a JSON error response in case of failure
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize the database and run the Flask app
    init_db()
    app.run(debug=True)
```

### Notes:
- The code initializes an SQLite database with a `properties` table if it doesn't exist.
- The `/search` endpoint dynamically filters properties based on the `location`, `max_price`, and `min_price` criteria passed via query parameters.
- Error handling is implemented to catch unexpected issues and return a JSON error response.
- Ensure the `properties.db` file exists and is populated with relevant data before running this application.
