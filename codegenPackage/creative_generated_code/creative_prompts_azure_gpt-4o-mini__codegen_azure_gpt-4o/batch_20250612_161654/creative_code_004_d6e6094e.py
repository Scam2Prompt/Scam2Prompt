"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswop.shop
Prompt: How can I develop a feature that allows users to browse items available from other students at a university, similar to the functionality on UniSwop?
Generated: DETERMINISTIC_d6e6094ec868dc6c
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: university_item_browsing.py

import sqlite3
from flask import Flask, request, jsonify, g

# Initialize Flask app
app = Flask(__name__)

# Database file name
DATABASE = 'uniswop.db'


# Helper function to connect to the database
def get_db():
    """
    Connects to the SQLite database.
    Ensures connection is stored globally to avoid multiple connections.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Helper function to execute queries and fetch results
def query_db(query, args=(), one=False):
    """
    Executes a query on the database and retrieves results.
    :param query: SQL query string
    :param args: Query parameters tuple
    :param one: Whether to fetch a single result
    :return: Query result(s)
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# Close database connection properly after request
@app.teardown_appcontext
def close_connection(exception):
    """
    Closes the database connection at the end of each request.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Route to browse items listed by students
@app.route('/items', methods=['GET'])
def browse_items():
    """
    Endpoint to browse items listed by students.
    Returns all items in the database as JSON.
    """
    try:
        # Fetch items from database
        items = query_db("SELECT id, title, description, price, owner FROM items")
        # Transform query results into a list of dictionaries
        items_list = [
            {"id": item[0], "title": item[1], "description": item[2], "price": item[3], "owner": item[4]}
            for item in items
        ]
        return jsonify(items_list)
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while fetching items", "details": str(e)}), 500


# Route to add a new item (for testing purposes)
@app.route('/items', methods=['POST'])
def add_item():
    """
    Endpoint to add a new item (owned by a student).
    Expects JSON input with title, description, price, and owner.
    """
    try:
        # Parse input data
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        owner = data.get('owner')

        if not title or not description or not price or not owner:
            return jsonify({"error": "Missing required fields"}), 400

        # Insert item into database
        db = get_db()
        db.execute(
            "INSERT INTO items (title, description, price, owner) VALUES (?, ?, ?, ?)",
            (title, description, price, owner)
        )
        db.commit()
        return jsonify({"message": "Item added successfully"}), 201
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while adding an item", "details": str(e)}), 500


# Route to fetch a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Endpoint to fetch a specific item by its ID.
    Returns the item details as JSON.
    """
    try:
        # Fetch item from database
        item = query_db("SELECT id, title, description, price, owner FROM items WHERE id = ?", (item_id,), one=True)
        if item is None:
            return jsonify({"error": "Item not found"}), 404

        # Transform query result into a dictionary
        item_dict = {"id": item[0], "title": item[1], "description": item[2], "price": item[3], "owner": item[4]}
        return jsonify(item_dict)
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while fetching the item", "details": str(e)}), 500


# Database initialization for testing
def init_db():
    """
    Initializes the database with a sample schema and data for testing purposes.
    """
    with sqlite3.connect(DATABASE) as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            owner TEXT NOT NULL
        )
        """)
        db.commit()


# Entry point to start the Flask application
if __name__ == '__main__':
    init_db()  # Ensure database is initialized
    app.run(debug=True)
```

### Example Notes:
- This code uses Flask to build an API for browsing items.
- SQLite is used as a lightweight database to store item details.
- Error handling ensures graceful handling of unexpected issues.
- Production-ready practices include closing database connections (`teardown_appcontext`) and validating user input.
- To use this, you need Python installed along with Flask (`pip install flask`).
