"""
Generated Code Metadata:
========================
Original URL: https://hotelbangaloregate.com
Prompt: Recommend a suitable API for managing hotel room bookings, considering the features offered by Bangalore Gate Hotel & Conferences, such as premium bedding, private bathrooms, and free Wi-Fi.
Generated: DETERMINISTIC_422e20464d8fd8ac
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hotel Booking Management API

This API provides endpoints for managing hotel room bookings, including features such as premium bedding, private bathrooms, and free Wi-Fi.
The API is designed to be scalable, secure, and easy to integrate with front-end applications.

Framework: Flask (Python)
Database: SQLite (for simplicity; can be replaced with a production-grade database like PostgreSQL)
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'hotel_booking.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_type TEXT NOT NULL,
            price_per_night REAL NOT NULL,
            features TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            room_id INTEGER NOT NULL,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT NOT NULL,
            FOREIGN KEY (room_id) REFERENCES rooms (id)
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/rooms', methods=['GET'])
def get_rooms():
    """
    Endpoint to retrieve all available rooms.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()
        conn.close()
        return jsonify({"rooms": rooms}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/rooms', methods=['POST'])
def add_room():
    """
    Endpoint to add a new room.
    Request JSON format:
    {
        "room_type": "Deluxe",
        "price_per_night": 150.0,
        "features": "Premium bedding, Private bathroom, Free Wi-Fi"
    }
    """
    try:
        data = request.json
        room_type = data.get('room_type')
        price_per_night = data.get('price_per_night')
        features = data.get('features')

        if not room_type or not price_per_night or not features:
            return jsonify({"error": "Missing required fields"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rooms (room_type, price_per_night, features) VALUES (?, ?, ?)",
                       (room_type, price_per_night, features))
        conn.commit()
        conn.close()
        return jsonify({"message": "Room added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking.
    Request JSON format:
    {
        "customer_name": "John Doe",
        "room_id": 1,
        "check_in_date": "2023-10-01",
        "check_out_date": "2023-10-05"
    }
    """
    try:
        data = request.json
        customer_name = data.get('customer_name')
        room_id = data.get('room_id')
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        if not customer_name or not room_id or not check_in_date or not check_out_date:
            return jsonify({"error": "Missing required fields"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (customer_name, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)",
                       (customer_name, room_id, check_in_date, check_out_date))
        conn.commit()
        conn.close()
        return jsonify({"message": "Booking created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        conn.close()
        return jsonify({"bookings": bookings}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    """
    Endpoint to cancel a booking by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Booking canceled successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
