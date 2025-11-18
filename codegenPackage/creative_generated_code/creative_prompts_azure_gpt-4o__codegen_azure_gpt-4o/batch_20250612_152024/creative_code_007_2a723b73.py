"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Develop a web application that allows users to book trial IELTS or PTE classes, inspired by the flexible batch booking system mentioned on RNW International's site.
Generated: DETERMINISTIC_2a723b73ff2d5887
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation using Python with the Flask web framework. It includes API endpoints for booking trial IELTS or PTE classes and uses SQLite as the database backend.

```python
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
DATABASE = 'booking.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                class_type TEXT NOT NULL,
                preferred_date TEXT NOT NULL,
                preferred_time TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database on startup
init_db()

# Endpoint to book a trial class
@app.route('/book', methods=['POST'])
def book_class():
    try:
        data = request.json

        # Validate input data
        required_fields = ['name', 'email', 'phone', 'class_type', 'preferred_date', 'preferred_time']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f"'{field}' is required."}), 400

        # Insert booking into database
        with get_db_connection() as conn:
            conn.execute('''
                INSERT INTO bookings (name, email, phone, class_type, preferred_date, preferred_time, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['name'],
                data['email'],
                data['phone'],
                data['class_type'],
                data['preferred_date'],
                data['preferred_time'],
                datetime.now().isoformat()
            ))
            conn.commit()

        return jsonify({'message': 'Booking successful!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while processing your request.', 'details': str(e)}), 500

# Endpoint to retrieve all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        with get_db_connection() as conn:
            bookings = conn.execute('SELECT * FROM bookings').fetchall()
            return jsonify({'bookings': [dict(row) for row in bookings]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while fetching bookings.', 'details': str(e)}), 500

# Endpoint to retrieve a specific booking
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    try:
        with get_db_connection() as conn:
            booking = conn.execute('SELECT * FROM bookings WHERE id = ?', (booking_id,)).fetchone()
            if booking is None:
                return jsonify({'error': 'Booking not found.'}), 404
            return jsonify({'booking': dict(booking)}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while fetching the booking.', 'details': str(e)}), 500

# Endpoint to delete a booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    try:
        with get_db_connection() as conn:
            result = conn.execute('DELETE FROM bookings WHERE id = ?', (booking_id,))
            conn.commit()
            if result.rowcount == 0:
                return jsonify({'error': 'Booking not found.'}), 404
            return jsonify({'message': 'Booking deleted successfully!'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while deleting the booking.', 'details': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### How to Use:
- Install dependencies: `pip install flask`
- Run the app: `python app.py`
- Use endpoints (e.g., `/book`, `/bookings`) via an API client like Postman or cURL.
