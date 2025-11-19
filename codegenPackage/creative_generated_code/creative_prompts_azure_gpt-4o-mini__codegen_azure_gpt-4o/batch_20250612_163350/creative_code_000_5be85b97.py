"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate a code snippet for a web application that allows users to book dumpster rentals online, similar to the system used by Junk in The Box ATL.
Generated: DETERMINISTIC_5be85b97a57238b3
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py - Flask application for dumpster rental booking

from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup function
def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect('dumpster_rental.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            dumpster_size TEXT NOT NULL,
            rental_date TEXT NOT NULL,
            address TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_dumpster():
    """
    Handle dumpster rental booking requests.
    Expects JSON payload with name, email, phone, dumpster_size, rental_date, and address.
    """
    try:
        # Parse the JSON payload
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        dumpster_size = data.get('dumpster_size')
        rental_date = data.get('rental_date')
        address = data.get('address')

        # Validate input
        if not all([name, email, phone, dumpster_size, rental_date, address]):
            return jsonify({'error': 'All fields are required.'}), 400

        # Convert rental_date to proper format and validate
        try:
            rental_date = datetime.strptime(rental_date, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Save to database
        conn = sqlite3.connect('dumpster_rental.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (name, email, phone, dumpster_size, rental_date, address, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, dumpster_size, rental_date, address, datetime.now()))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({'message': 'Booking successful!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/bookings', methods=['GET'])
def list_bookings():
    """Retrieve a list of all bookings."""
    try:
        conn = sqlite3.connect('dumpster_rental.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bookings')
        rows = cursor.fetchall()
        conn.close()

        # Convert rows to a list of dictionaries
        bookings = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'dumpster_size': row[4],
                'rental_date': row[5],
                'address': row[6],
                'created_at': row[7]
            }
            for row in rows
        ]

        return jsonify(bookings), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html - Homepage template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dumpster Rental Booking</title>
</head>
<body>
    <h1>Welcome to Dumpster Rental Booking</h1>
    <form id="bookingForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="dumpster_size">Dumpster Size:</label>
        <select id="dumpster_size" name="dumpster_size" required>
            <option value="10-yard">10-yard</option>
            <option value="20-yard">20-yard</option>
            <option value="30-yard">30-yard</option>
        </select><br><br>

        <label for="rental_date">Rental Date:</label>
        <input type="date" id="rental_date" name="rental_date" required><br><br>

        <label for="address">Address:</label>
        <textarea id="address" name="address" required></textarea><br><br>

        <button type="submit">Book Dumpster</button>
    </form>

    <script>
        // JavaScript to handle form submission
        document.getElementById('bookingForm').addEventListener('submit', async function (e) {
            e.preventDefault();

            const data = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                dumpster_size: document.getElementById('dumpster_size').value,
                rental_date: document.getElementById('rental_date').value,
                address: document.getElementById('address').value
            };

            try {
                const response = await fetch('/book', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                if (response.ok) {
                    alert(result.message);
                } else {
                    alert(`Error: ${result.error}`);
                }
            } catch (error) {
                alert(`Error: ${error.message}`);
            }
        });
    </script>
</body>
</html>
```
