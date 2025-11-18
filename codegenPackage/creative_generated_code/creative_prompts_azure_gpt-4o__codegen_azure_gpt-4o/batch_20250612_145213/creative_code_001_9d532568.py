"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Recommend APIs or libraries to develop a searchable database for biographical data, inspired by the "Meet A Great American" platform.
Generated: DETERMINISTIC_9d532568d7e06ec4
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an implementation using Python and Flask with an SQLite database. This example demonstrates how to set up a searchable database for biographical data using APIs.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database connection parameters
DATABASE = 'biographies.db'

def init_db():
    """
    Initialize the database and create the 'biographies' table.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS biographies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_date TEXT,
                profession TEXT,
                biography TEXT
            )
        ''')
        conn.commit()

# Error handler for database connection issues
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries for convenience
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Database connection error: {e}")

@app.route('/biographies', methods=['POST'])
def create_biography():
    """
    API endpoint to add a new biography record.
    Expected JSON format:
    {
        "name": "Name of the person",
        "birth_date": "YYYY-MM-DD",
        "profession": "Profession of the person",
        "biography": "Detailed biography text"
    }
    """
    try:
        data = request.json
        name = data.get('name')
        birth_date = data.get('birth_date')
        profession = data.get('profession')
        biography = data.get('biography')

        if not name or not biography:
            return jsonify({"error": "Name and biography are required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO biographies (name, birth_date, profession, biography)
            VALUES (?, ?, ?, ?)
        ''', (name, birth_date, profession, biography))
        conn.commit()
        return jsonify({"message": "Biography created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/biographies', methods=['GET'])
def search_biographies():
    """
    API endpoint to search biographies.
    Query parameters:
        - name: Filter by name (supports partial match)
        - profession: Filter by profession (supports partial match)
    """
    try:
        name_filter = request.args.get('name', '')
        profession_filter = request.args.get('profession', '')

        conn = get_db_connection()
        cursor = conn.cursor()
        query = '''
            SELECT * FROM biographies
            WHERE name LIKE ? AND profession LIKE ?
        '''
        cursor.execute(query, (f"%{name_filter}%", f"%{profession_filter}%"))
        records = cursor.fetchall()

        biographies = [dict(record) for record in records]
        return jsonify(biographies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/biographies/<int:id>', methods=['GET'])
def get_biography(id):
    """
    API endpoint to retrieve a single biography by ID.
    Path parameter:
        - id: ID of the biography record
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM biographies WHERE id = ?', (id,))
        record = cursor.fetchone()

        if record:
            return jsonify(dict(record)), 200
        else:
            return jsonify({"error": "Biography not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/biographies/<int:id>', methods=['DELETE'])
def delete_biography(id):
    """
    API endpoint to delete a biography by ID.
    Path parameter:
        - id: ID of the biography record
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM biographies WHERE id = ?', (id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "Biography deleted successfully"}), 200
        else:
            return jsonify({"error": "Biography not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Initialize the database only once
    init_db()
    # Run the Flask app
    app.run(debug=True)
```

**Usage Notes**:
1. Run the script to initialize the Flask web server.
2. Use tools like Postman or curl to interact with the APIs:
   - POST `/biographies` to create a new biography.
   - GET `/biographies?name=John&profession=Engineer` to search biographies.
   - GET `/biographies/<id>` to fetch a specific biography.
   - DELETE `/biographies/<id>` to delete a biography.
