"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate a code snippet for a web application that allows users to book a real estate photography session, incorporating features like scheduling and client testimonials.
Generated: DETERMINISTIC_b5cab19b0f2578fe
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'photography_booking.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS testimonials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/book-session', methods=['POST'])
def book_session():
    """
    Endpoint to book a real estate photography session.
    Expects JSON payload with name, email, phone, date, and time.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not all([name, email, phone, date, time]):
            return jsonify({'error': 'All fields are required'}), 400

        # Check if date and time are valid
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date or time format'}), 400

        # Save booking to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (name, email, phone, date, time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, date, time))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Booking successful'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """
    Endpoint to add a client testimonial.
    Expects JSON payload with name and message.
    """
    try:
        data = request.json
        name = data.get('name')
        message = data.get('message')

        # Validate input
        if not all([name, message]):
            return jsonify({'error': 'Name and message are required'}), 400

        # Save testimonial to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO testimonials (name, message, created_at)
            VALUES (?, ?, ?)
        ''', (name, message, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Testimonial added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint to retrieve all client testimonials.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT name, message, created_at FROM testimonials ORDER BY created_at DESC')
        testimonials = cursor.fetchall()
        conn.close()

        # Format testimonials for response
        response = [
            {'name': name, 'message': message, 'created_at': created_at}
            for name, message, created_at in testimonials
        ]

        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
