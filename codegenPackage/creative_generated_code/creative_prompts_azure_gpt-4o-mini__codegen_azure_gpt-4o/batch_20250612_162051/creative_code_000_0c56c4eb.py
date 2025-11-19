"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bepretty.hamburg
Prompt: Generate a code snippet for a web application that allows users to book professional hair and makeup services, similar to the offerings at bePretty Hamburg.
Generated: DETERMINISTIC_0c56c4eb513cb600
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application for booking professional hair and makeup services
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'bookings.db'

def init_db():
    """Initialize the database and create necessary tables if not exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            service TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        """)
        conn.commit()

# Initialize the database before starting the application
init_db()


@app.route('/book', methods=['POST'])
def book_service():
    """
    Endpoint to book a professional hair and makeup service.
    Expects JSON input with name, email, service, date, and time.
    """
    try:
        # Extract data from request
        data = request.json
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        service = data.get('service', '').strip()
        date = data.get('date', '').strip()
        time = data.get('time', '').strip()

        # Validate the input
        if not name or not email or not service or not date or not time:
            return jsonify({"error": "All fields are required."}), 400

        # Ensure date and time are valid
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."}), 400

        # Save booking to the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO bookings (name, email, service, date, time)
            VALUES (?, ?, ?, ?, ?)
            """, (name, email, service, date, time))
            conn.commit()

        return jsonify({"message": "Booking successful!"}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


@app.route('/bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to list all bookings.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, service, date, time FROM bookings")
            bookings = cursor.fetchall()

        # Format the response
        formatted_bookings = [
            {"id": b[0], "name": b[1], "email": b[2], "service": b[3], "date": b[4], "time": b[5]}
            for b in bookings
        ]

        return jsonify({"bookings": formatted_bookings}), 200

    except Exception as e:
        return jsonify({"error": "Unable to retrieve bookings.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
