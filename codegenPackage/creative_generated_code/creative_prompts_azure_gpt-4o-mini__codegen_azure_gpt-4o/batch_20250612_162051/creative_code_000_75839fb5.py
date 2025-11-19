"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bandadorada.com
Prompt: Generate a code snippet for a web application that allows users to book live music services for weddings and corporate events, similar to the offerings of Orquesta Dorada in Trujillo.
Generated: DETERMINISTIC_75839fb565d54d18
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database setup (SQLite for simplicity)
DB_NAME = 'music_booking.db'

def init_db():
    """
    Initializes the SQLite database with necessary tables.
    Runs only if the database doesn't already exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            event_type TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            message TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/book', methods=['POST'])
def book_event():
    """
    Endpoint to book live music services for weddings or corporate events.
    Expects JSON input with the following fields:
    - name: String, required
    - email: String, required
    - event_type: String (e.g., "Wedding", "Corporate Event"), required
    - date: String (YYYY-MM-DD), required
    - time: String (HH:MM), required
    - message: String, optional
    Returns a confirmation message and booking ID if successful.
    """
    try:
        # Parse request JSON
        data = request.json
        name = data.get('name')
        email = data.get('email')
        event_type = data.get('event_type')
        date = data.get('date')
        time = data.get('time')
        message = data.get('message', '')  # Optional field
        
        # Input validation
        if not name or not email or not event_type or not date or not time:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate date and time format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({"error": "Invalid date or time format"}), 400
        
        # Save booking to database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO bookings (name, email, event_type, date, time, message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, event_type, date, time, message, created_at))
        conn.commit()
        booking_id = cursor.lastrowid
        conn.close()
        
        # Return success response
        return jsonify({"message": "Booking confirmed", "booking_id": booking_id}), 201
    
    except Exception as e:
        # Log error and return response
        return jsonify({"error": "An error occurred while processing your booking", "details": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    Returns a JSON array of all bookings.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bookings')
        rows = cursor.fetchall()
        conn.close()
        
        # Convert rows to dict format
        bookings = [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "event_type": row[3],
                "date": row[4],
                "time": row[5],
                "message": row[6],
                "created_at": row[7]
            }
            for row in rows
        ]
        
        return jsonify(bookings), 200
    
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving bookings", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
