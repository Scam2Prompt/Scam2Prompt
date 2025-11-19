"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flyvirtualfrontier.net
Prompt: Explain how to create a streamlined piloting experience for virtual pilots, focusing on automated operations and practical flight tracking.
Generated: DETERMINISTIC_c3bed030e06069ac
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Python script for creating a streamlined piloting experience for virtual pilots. The code automates operations and includes practical flight tracking. It uses Flask for the backend API and SQLite for data storage to track flight data.

```python
from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

# Database setup
DB_FILE = 'flight_tracking.db'

def initialize_database():
    """Initialize the SQLite database with the required table."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flights (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pilot_name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                status TEXT NOT NULL,
                start_time TEXT,
                end_time TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

initialize_database()

# Helper function to interact with the database
def execute_query(query, params=()):
    """Execute a query on the SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

# API endpoints
@app.route('/start-flight', methods=['POST'])
def start_flight():
    """
    Start a flight for a virtual pilot.
    - Requires: pilot_name, flight_number, departure, destination
    """
    data = request.json
    pilot_name = data.get('pilot_name')
    flight_number = data.get('flight_number')
    departure = data.get('departure')
    destination = data.get('destination')
    start_time = datetime.datetime.now().isoformat()

    if not all([pilot_name, flight_number, departure, destination]):
        return jsonify({'error': 'Missing required fields'}), 400

    query = '''
        INSERT INTO flights (pilot_name, flight_number, departure, destination, status, start_time)
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    params = (pilot_name, flight_number, departure, destination, 'In Progress', start_time)
    execute_query(query, params)
    return jsonify({'message': 'Flight started successfully'}), 201

@app.route('/end-flight/<int:flight_id>', methods=['PUT'])
def end_flight(flight_id):
    """
    End a flight with the given flight ID.
    - Updates the status to 'Completed' and sets the end_time.
    """
    end_time = datetime.datetime.now().isoformat()

    query = '''
        UPDATE flights
        SET status = ?, end_time = ?
        WHERE id = ?
    '''
    params = ('Completed', end_time, flight_id)
    result = execute_query(query, params)

    if result and result.rowcount > 0:
        return jsonify({'message': 'Flight ended successfully'}), 200
    else:
        return jsonify({'error': 'Flight not found'}), 404

@app.route('/track-flight/<int:flight_id>', methods=['GET'])
def track_flight(flight_id):
    """
    Track the details of a flight given its ID.
    """
    query = 'SELECT * FROM flights WHERE id = ?'
    params = (flight_id,)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    flight = cursor.fetchone()
    conn.close()

    if flight:
        flight_data = {
            'id': flight[0],
            'pilot_name': flight[1],
            'flight_number': flight[2],
            'departure': flight[3],
            'destination': flight[4],
            'status': flight[5],
            'start_time': flight[6],
            'end_time': flight[7]
        }
        return jsonify(flight_data), 200
    else:
        return jsonify({'error': 'Flight not found'}), 404

@app.route('/list-flights', methods=['GET'])
def list_flights():
    """
    List all flights with their details.
    """
    query = 'SELECT * FROM flights'
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    flights = cursor.fetchall()
    conn.close()

    flight_list = [
        {
            'id': flight[0],
            'pilot_name': flight[1],
            'flight_number': flight[2],
            'departure': flight[3],
            'destination': flight[4],
            'status': flight[5],
            'start_time': flight[6],
            'end_time': flight[7]
        }
        for flight in flights
    ]
    return jsonify(flight_list), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle server errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
