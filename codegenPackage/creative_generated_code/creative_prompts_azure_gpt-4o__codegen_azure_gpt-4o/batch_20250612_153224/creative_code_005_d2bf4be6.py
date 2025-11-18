"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: Write code to display and manage user wishlists, including creating, finding, and viewing lists, as described on Alwan's site.
Generated: DETERMINISTIC_d2bf4be60fdd659e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code to manage user wishlists in Python using a Flask framework with a SQLite database:

```python
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database connection helper function
def get_db_connection():
    try:
        conn = sqlite3.connect('wishlists.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise Exception("Failed to connect to the database")

# Initialize the database
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS wishlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                items TEXT NOT NULL
            )
        ''')
        conn.commit()

# Route to create a new wishlist
@app.route('/wishlists', methods=['POST'])
def create_wishlist():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        name = data.get("name")
        items = data.get("items")
        
        if not user_id or not name or not items:
            return jsonify({"error": "Missing required fields"}), 400
        
        with get_db_connection() as conn:
            conn.execute(
                'INSERT INTO wishlists (user_id, name, items) VALUES (?, ?, ?)',
                (user_id, name, ','.join(items))
            )
            conn.commit()

        return jsonify({"message": "Wishlist created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all wishlists for a specific user
@app.route('/wishlists/<int:user_id>', methods=['GET'])
def get_user_wishlists(user_id):
    try:
        with get_db_connection() as conn:
            wishlists = conn.execute(
                'SELECT * FROM wishlists WHERE user_id = ?', (user_id,)
            ).fetchall()

        if not wishlists:
            return jsonify({"message": "No wishlists found for the user"}), 404
        
        result = [
            {
                "id": wishlist["id"],
                "user_id": wishlist["user_id"],
                "name": wishlist["name"],
                "items": wishlist["items"].split(',')
            } for wishlist in wishlists
        ]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve a specific wishlist by ID
@app.route('/wishlists/view/<int:wishlist_id>', methods=['GET'])
def get_wishlist(wishlist_id):
    try:
        with get_db_connection() as conn:
            wishlist = conn.execute(
                'SELECT * FROM wishlists WHERE id = ?', (wishlist_id,)
            ).fetchone()

        if not wishlist:
            return jsonify({"message": "Wishlist not found"}), 404
        
        result = {
            "id": wishlist["id"],
            "user_id": wishlist["user_id"],
            "name": wishlist["name"],
            "items": wishlist["items"].split(',')
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the initialization if this script is executed directly
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)  # Run the Flask app in debug mode
```

### Notes:
- Make sure you have Flask installed (`pip install flask`) and SQLite available in your setup.
- This code creates a SQLite database (`wishlists.db`) locally and initializes a table for wishlists.
- The routes handle creating, viewing, and retrieving wishlists by user ID and wishlist ID.
- Error handling is implemented to catch issues like missing fields or database connection failures.
