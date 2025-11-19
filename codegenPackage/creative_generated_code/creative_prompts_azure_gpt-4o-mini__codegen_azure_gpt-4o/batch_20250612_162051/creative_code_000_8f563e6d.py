"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Generate a code snippet for a web application that allows users to search for properties to rent or buy in Neiva, Colombia, similar to the services offered by Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_8f563e6de2efe6ef
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

# Initialize SQLite database
DATABASE = 'properties.db'

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with a 'properties' table."""
    with connect_db() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            location TEXT NOT NULL,
            type TEXT NOT NULL
        )
        ''')
        conn.commit()

# Ensure the database is initialized
init_db()

@app.route('/properties', methods=['GET'])
def search_properties():
    """
    Endpoint to search for properties.
    Users can filter by location, type, and price range.
    Example query string: /properties?location=Neiva&type=rent&min_price=500&max_price=1000
    """
    try:
        # Extract query parameters
        location = request.args.get('location', '')
        property_type = request.args.get('type', '')
        min_price = request.args.get('min_price', '0')
        max_price = request.args.get('max_price', str(float('inf')))

        # Build query dynamically based on filters
        query = "SELECT * FROM properties WHERE 1=1"
        params = []

        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")
        if property_type:
            query += " AND type=?"
            params.append(property_type)
        if min_price:
            query += " AND price >= ?"
            params.append(float(min_price))
        if max_price:
            query += " AND price <= ?"
            params.append(float(max_price))

        # Execute query
        with connect_db() as conn:
            cursor = conn.execute(query, params)
            properties = [dict(row) for row in cursor.fetchall()]

        # Return results as JSON
        return jsonify(properties)

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/properties', methods=['POST'])
def add_property():
    """
    Endpoint to add a new property.
    Example body:
    {
        "title": "Modern apartment in Neiva",
        "description": "A beautiful apartment with great amenities.",
        "price": 800,
        "location": "Neiva",
        "type": "rent"
    }
    """
    try:
        # Parse request body
        data = request.json
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        location = data.get('location')
        property_type = data.get('type')

        # Validate required fields
        if not title or not price or not location or not property_type:
            return jsonify({"error": "Missing required fields"}), 400

        # Insert property into database
        with connect_db() as conn:
            conn.execute('''
            INSERT INTO properties (title, description, price, location, type)
            VALUES (?, ?, ?, ?, ?)
            ''', (title, description, price, location, property_type))
            conn.commit()

        return jsonify({"message": "Property added successfully"}), 201

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
