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

```python
import sqlite3
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'biography_data.db'

def init_db():
    """Initialize the SQLite database and create the necessary table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS biographies (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                birth_year INTEGER,
                death_year INTEGER,
                bio TEXT
            )
        ''')
        conn.commit()

@app.route('/biographies', methods=['POST'])
def add_biography():
    """Add a new biography to the database."""
    try:
        data = request.get_json()
        name = data.get('name')
        birth_year = data.get('birth_year')
        death_year = data.get('death_year')
        bio = data.get('bio')

        if not name or not bio:
            return jsonify({'error': 'Name and bio are required fields.'}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO biographies (name, birth_year, death_year, bio)
                VALUES (?, ?, ?, ?)
            ''', (name, birth_year, death_year, bio))
            conn.commit()

        return jsonify({'message': 'Biography added successfully!'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/biographies', methods=['GET'])
def search_biographies():
    """Search for biographies by name."""
    try:
        query = request.args.get('query', '')
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM biographies WHERE name LIKE ?
            ''', ('%' + query + '%',))
            results = cursor.fetchall()

        # Format results into a dictionary
        biographies = [
            {'id': row[0], 'name': row[1], 'birth_year': row[2], 'death_year': row[3], 'bio': row[4]}
            for row in results
        ]

        return jsonify(biographies), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run the application
```
