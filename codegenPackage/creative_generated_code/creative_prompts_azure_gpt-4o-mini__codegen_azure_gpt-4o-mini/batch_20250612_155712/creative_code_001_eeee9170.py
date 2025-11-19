"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: How can I implement a networking opportunity for activity professionals using the guidelines provided by MN Swap?
Generated: DETERMINISTIC_eeee9170bd11b059
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'networking_opportunities.db'

# Create a new SQLite database and table if it doesn't exist
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')
        conn.commit()

# Error handling for database operations
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        app.logger.error(f"Database connection error: {e}")
        abort(500)

# Route to create a new networking opportunity
@app.route('/opportunities', methods=['POST'])
def create_opportunity():
    data = request.get_json()

    if not data or not all(k in data for k in ('title', 'description', 'date', 'location')):
        abort(400, 'Missing required fields: title, description, date, location')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO opportunities (title, description, date, location)
        VALUES (?, ?, ?, ?)
    ''', (data['title'], data['description'], data['date'], data['location']))
    
    conn.commit()
    conn.close()

    return jsonify({'message': 'Opportunity created successfully'}), 201

# Route to get all networking opportunities
@app.route('/opportunities', methods=['GET'])
def get_opportunities():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM opportunities')
    opportunities = cursor.fetchall()

    conn.close()

    return jsonify(opportunities), 200

# Route to delete a networking opportunity by ID
@app.route('/opportunities/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM opportunities WHERE id = ?', (id,))
    if cursor.rowcount == 0:
        conn.close()
        abort(404, 'Opportunity not found')

    conn.commit()
    conn.close()

    return jsonify({'message': 'Opportunity deleted successfully'}), 204

if __name__ == '__main__':
    init_db()  # Initialize the database and table
    app.run(debug=False)  # Run the Flask application
```
