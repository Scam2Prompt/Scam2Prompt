"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Recommend an API to integrate a free consultation booking system on a website, similar to the "Free Consultation" feature offered by Meezan Interior Solutions.
Generated: DETERMINISTIC_42f1c2329b30cddb
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'consultation_bookings.db'

def init_db():
    """Initializes the database and creates the necessary table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/book_consultation', methods=['POST'])
def book_consultation():
    """
    Endpoint to book a free consultation.
    Expects JSON payload with name, email, phone, date, and time.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input data
        required_fields = ['name', 'email', 'phone', 'date', 'time']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Extract data
        name = data['name']
        email = data['email']
        phone = data['phone']
        date = data['date']
        time = data['time']

        # Insert booking into the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO bookings (name, email, phone, date, time)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, phone, date, time))
            conn.commit()

        return jsonify({'message': 'Consultation booked successfully!'}), 201

    except sqlite3.Error as e:
        # Handle database error
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle general error
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/view_bookings', methods=['GET'])
def view_bookings():
    """Endpoint to retrieve all booked consultations."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM bookings')
            bookings = cursor.fetchall()

        # Format the bookings for response
        booking_list = [{
            'id': booking[0],
            'name': booking[1],
            'email': booking[2],
            'phone': booking[3],
            'date': booking[4],
            'time': booking[5]
        } for booking in bookings]

        return jsonify({'bookings': booking_list}), 200

    except sqlite3.Error as e:
        # Handle database error
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle general error
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)  # Set debug=False for production
```
