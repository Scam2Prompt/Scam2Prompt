"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starke-orte.land
Prompt: How can I implement community-driven strategies for activating vacant properties in small towns, as discussed by the Starke Orte Netzwerk?
Generated: DETERMINISTIC_6eb1037914d03676
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code implementation of a simplified system to manage and activate vacant properties in small towns. This will include a web-based interface for property owners, community members, and administrators to collaborate on strategies for utilizing vacant properties. The backend will be implemented in Python using Flask, and the database will use SQLite.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database file path
DB_FILE = 'vacant_properties.db'


# Function to initialize the database
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create properties table
        cursor.execute('''
            CREATE TABLE properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL,
                owner TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('vacant', 'active', 'reserved')),
                description TEXT
            )
        ''')

        # Create community ideas table
        cursor.execute('''
            CREATE TABLE ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                property_id INTEGER NOT NULL,
                contributor TEXT NOT NULL,
                idea TEXT NOT NULL,
                FOREIGN KEY (property_id) REFERENCES properties(id)
            )
        ''')

        conn.commit()
        conn.close()


# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DB_FILE)


# Error handler for database connection issues
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500


# Route to list all vacant properties
@app.route('/properties', methods=['GET'])
def list_properties():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM properties WHERE status="vacant"')
    properties = cursor.fetchall()
    conn.close()

    return jsonify(properties)


# Route to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.json
    if not data or not all(key in data for key in ('address', 'owner', 'status')):
        return jsonify({'error': 'Invalid or missing property data'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO properties (address, owner, status, description)
        VALUES (?, ?, ?, ?)
    ''', (data['address'], data['owner'], data['status'], data.get('description', '')))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Property added successfully'}), 201


# Route to submit an idea for a vacant property
@app.route('/ideas', methods=['POST'])
def submit_idea():
    data = request.json
    if not data or not all(key in data for key in ('property_id', 'contributor', 'idea')):
        return jsonify({'error': 'Invalid or missing idea data'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ideas (property_id, contributor, idea)
        VALUES (?, ?, ?)
    ''', (data['property_id'], data['contributor'], data['idea']))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Idea submitted successfully'}), 201


# Route to list all ideas for a specific property
@app.route('/ideas/<int:property_id>', methods=['GET'])
def list_ideas(property_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ideas WHERE property_id=?', (property_id,))
    ideas = cursor.fetchall()
    conn.close()

    return jsonify(ideas)


if __name__ == '__main__':
    init_db()  # Initialize the database if not present
    app.run(debug=True)  # Run the development server
```

### To Run:
1. Save the code in a file named `app.py`.
2. Install Flask using `pip install flask`.
3. Run the code with `python app.py`.
4. Open a browser or use an API client like Postman to interact with the API.

This code is designed to be expandable and can serve as the foundation for a community-driven system to activate vacant properties in small towns.
