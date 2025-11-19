"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-illuminex.com
Prompt: Write a code snippet to create a digital solution that fosters collaboration between universities and industries, inspired by KAMISLOT's initiatives.
Generated: DETERMINISTIC_cee16d24283b8483
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database initialization function
def init_db():
    # Connect to SQLite database (it will be created if it does not exist)
    conn = sqlite3.connect('collaboration.db')
    cursor = conn.cursor()

    # Create tables for universities, industries, and collaborations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS universities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS industries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sector TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS collaborations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            university_id INTEGER,
            industry_id INTEGER,
            project_name TEXT NOT NULL,
            FOREIGN KEY (university_id) REFERENCES universities (id),
            FOREIGN KEY (industry_id) REFERENCES industries (id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/universities', methods=['POST'])
def add_university():
    """Endpoint to add a new university."""
    data = request.json
    name = data.get('name')
    location = data.get('location')

    if not name or not location:
        return jsonify({'error': 'Name and location are required!'}), 400

    try:
        conn = sqlite3.connect('collaboration.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO universities (name, location) VALUES (?, ?)', (name, location))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

    return jsonify({'message': 'University added successfully!'}), 201


@app.route('/industries', methods=['POST'])
def add_industry():
    """Endpoint to add a new industry."""
    data = request.json
    name = data.get('name')
    sector = data.get('sector')

    if not name or not sector:
        return jsonify({'error': 'Name and sector are required!'}), 400

    try:
        conn = sqlite3.connect('collaboration.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO industries (name, sector) VALUES (?, ?)', (name, sector))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

    return jsonify({'message': 'Industry added successfully!'}), 201


@app.route('/collaborations', methods=['POST'])
def add_collaboration():
    """Endpoint to create a new collaboration between a university and an industry."""
    data = request.json
    university_id = data.get('university_id')
    industry_id = data.get('industry_id')
    project_name = data.get('project_name')

    if not university_id or not industry_id or not project_name:
        return jsonify({'error': 'University ID, Industry ID, and Project Name are required!'}), 400

    try:
        conn = sqlite3.connect('collaboration.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO collaborations (university_id, industry_id, project_name) VALUES (?, ?, ?)', 
                       (university_id, industry_id, project_name))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

    return jsonify({'message': 'Collaboration created successfully!'}), 201


@app.route('/collaborations', methods=['GET'])
def get_collaborations():
    """Endpoint to retrieve all collaborations."""
    try:
        conn = sqlite3.connect('collaboration.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.id, u.name AS university, i.name AS industry, c.project_name 
            FROM collaborations c
            JOIN universities u ON c.university_id = u.id
            JOIN industries i ON c.industry_id = i.id
        ''')
        collaborations = cursor.fetchall()
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

    return jsonify(collaborations), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
