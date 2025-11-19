"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Recommend an API for integrating wedding photography packages and pricing into a website, inspired by the services provided by Yaisa Tangwell Photography.
Generated: DETERMINISTIC_ffbe1aa69ad2aa56
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the implementation for a RESTful API that integrates wedding photography packages and pricing into a website. The implementation uses Python with the Flask framework and SQLite as the database.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'photography.db'


def init_db():
    """
    Initialize the SQLite database.
    Creates the table if it does not exist.
    """
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE packages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


@app.route('/packages', methods=['GET'])
def get_packages():
    """
    Retrieve all wedding photography packages.
    Returns a JSON response with all packages.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM packages')
        rows = cursor.fetchall()
        conn.close()

        packages = [
            {"id": row[0], "name": row[1], "description": row[2], "price": row[3]} for row in rows
        ]
        return jsonify(packages), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch packages.", "details": str(e)}), 500


@app.route('/packages', methods=['POST'])
def add_package():
    """
    Add a new wedding photography package.
    Expects JSON payload with 'name', 'description', and 'price' fields.
    """
    try:
        data = request.get_json()

        # Validate input
        if not all(key in data for key in ['name', 'description', 'price']):
            return jsonify({"error": "Missing required fields: 'name', 'description', 'price'"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO packages (name, description, price) VALUES (?, ?, ?)',
            (data['name'], data['description'], float(data['price']))
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Package added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": "Failed to add package.", "details": str(e)}), 500


@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    """
    Update an existing wedding photography package by ID.
    Expects JSON payload with 'name', 'description', and/or 'price' fields.
    """
    try:
        data = request.get_json()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the package exists
        cursor.execute('SELECT * FROM packages WHERE id = ?', (package_id,))
        existing_package = cursor.fetchone()
        if not existing_package:
            conn.close()
            return jsonify({"error": "Package not found."}), 404

        # Update fields
        updated_name = data.get('name', existing_package[1])
        updated_description = data.get('description', existing_package[2])
        updated_price = data.get('price', existing_package[3])

        cursor.execute(
            'UPDATE packages SET name = ?, description = ?, price = ? WHERE id = ?',
            (updated_name, updated_description, float(updated_price), package_id)
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Package updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to update package.", "details": str(e)}), 500


@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    """
    Delete a wedding photography package by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the package exists
        cursor.execute('SELECT * FROM packages WHERE id = ?', (package_id,))
        existing_package = cursor.fetchone()
        if not existing_package:
            conn.close()
            return jsonify({"error": "Package not found."}), 404

        cursor.execute('DELETE FROM packages WHERE id = ?', (package_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Package deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete package.", "details": str(e)}), 500


if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()
    app.run(debug=True)
```

### Notes:
- Install prerequisites: `pip install flask`.
- To persist data, a SQLite database (`photography.db`) is created automatically if it doesn't exist.
- Error handling and validation are included.
- Run the script to expose the API endpoints.
