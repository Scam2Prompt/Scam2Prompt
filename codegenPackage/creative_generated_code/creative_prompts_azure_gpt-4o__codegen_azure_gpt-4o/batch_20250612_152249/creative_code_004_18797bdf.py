"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Suggest tools or APIs for managing event registrations and attendee data for multi-location events like those listed on the "Patente d'Impresa" webpage.
Generated: DETERMINISTIC_18797bdf495aa6e8
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to manage event registrations and attendee data 
for multi-location events using Flask (Python web framework) and SQLite as the database.
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'event_registration.db'

def init_db():
    """
    Initializes the SQLite database with tables for locations, events, and attendees.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            location_id INTEGER NOT NULL,
            FOREIGN KEY(location_id) REFERENCES locations(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            event_id INTEGER NOT NULL,
            FOREIGN KEY(event_id) REFERENCES events(id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/locations', methods=['POST'])
def add_location():
    """
    API endpoint to add a new location.
    """
    try:
        data = request.json
        name = data.get('name')
        address = data.get('address')
        
        if not name or not address:
            return jsonify({'error': 'Name and address are required'}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO locations (name, address) VALUES (?, ?)', (name, address))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Location added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/events', methods=['POST'])
def add_event():
    """
    API endpoint to add a new event.
    """
    try:
        data = request.json
        name = data.get('name')
        date = data.get('date')
        location_id = data.get('location_id')
        
        if not name or not date or not location_id:
            return jsonify({'error': 'Name, date, and location_id are required'}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO events (name, date, location_id) VALUES (?, ?, ?)', (name, date, location_id))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Event added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/attendees', methods=['POST'])
def register_attendee():
    """
    API endpoint to register a new attendee for an event.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        event_id = data.get('event_id')
        
        if not name or not email or not event_id:
            return jsonify({'error': 'Name, email, and event_id are required'}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO attendees (name, email, event_id) VALUES (?, ?, ?)', (name, email, event_id))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Attendee registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/events/<int:event_id>/attendees', methods=['GET'])
def get_event_attendees(event_id):
    """
    API endpoint to get all attendees for a specific event.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT name, email FROM attendees WHERE event_id = ?', (event_id,))
        attendees = cursor.fetchall()
        conn.close()
        
        if not attendees:
            return jsonify({'error': 'No attendees found for this event'}), 404
        
        return jsonify({'attendees': [{'name': att[0], 'email': att[1]} for att in attendees]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
