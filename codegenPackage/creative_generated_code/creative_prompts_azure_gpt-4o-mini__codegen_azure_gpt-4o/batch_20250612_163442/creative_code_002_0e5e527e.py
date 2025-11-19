"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zepeapp.com
Prompt: Create a REST API endpoint that retrieves meal package details, including pricing and dietary information, similar to the offerings on the Zepe platform.
Generated: DETERMINISTIC_0e5e527ebf9cf6f4
Batch ID: 20250612_163442
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

# Database setup (for simplicity, using SQLite)
DATABASE = 'meal_packages.db'

def init_db():
    """Initialize the database with sample data (for demonstration purposes)."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meal_packages (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            dietary_info TEXT NOT NULL
        )
    ''')
    # Insert some sample data
    cursor.executemany('''
        INSERT INTO meal_packages (name, price, dietary_info)
        VALUES (?, ?, ?)
    ''', [
        ("Vegan Delight", 15.99, "Vegan, Gluten-Free"),
        ("Protein Power", 12.99, "High-Protein, Low-Carb"),
        ("Classic Comfort", 10.99, "Vegetarian"),
    ])
    conn.commit()
    conn.close()

# Call database initialization (only for demonstration purposes)
init_db()


@app.route('/api/meal-packages', methods=['GET'])
def get_meal_packages():
    """
    REST API endpoint to retrieve all meal package details.
    Returns:
        JSON object with meal package details including name, price, and dietary information.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, price, dietary_info FROM meal_packages')
        rows = cursor.fetchall()

        # Transform rows into a list of dictionaries
        meal_packages = [
            {
                'id': row[0],
                'name': row[1],
                'price': row[2],
                'dietary_info': row[3]
            }
            for row in rows
        ]

        conn.close()
        return jsonify({"success": True, "data": meal_packages}), 200
    except Exception as e:
        # Log the error (in production, use a logger instead of print)
        print(f"Error retrieving meal packages: {e}")
        return jsonify({"success": False, "error": "An error occurred while retrieving meal packages."}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"success": False, "error": "Endpoint not found."}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server-side issues.
    """
    return jsonify({"success": False, "error": "Internal server error."}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
