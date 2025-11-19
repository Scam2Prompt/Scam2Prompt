"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Generate a code snippet for a simple web application that allows users to book laser procedures like ZWAVE and ZTONE online."
Generated: DETERMINISTIC_a4c69f05c1c24188
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A simple web application for booking laser procedures like ZWAVE and ZTONE online.

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flash messages

# Database setup
DATABASE = 'laser_booking.db'

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            procedure TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    """Handle booking requests."""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            email = request.form['email']
            procedure = request.form['procedure']
            date = request.form['date']
            time = request.form['time']

            # Validate input
            if not name or not email or not procedure or not date or not time:
                flash('All fields are required!', 'error')
                return redirect(url_for('book'))

            # Save booking to the database
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO bookings (name, email, procedure, date, time)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, procedure, date, time))
            conn.commit()
            conn.close()

            flash('Booking successful!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('book'))
    return render_template('book.html')

@app.route('/admin/bookings')
def admin_bookings():
    """Display all bookings (admin view)."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bookings')
        bookings = cursor.fetchall()
        conn.close()
        return render_template('admin_bookings.html', bookings=bookings)
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# templates/index.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Laser Procedure Booking</title>
</head>
<body>
    <h1>Welcome to Laser Procedure Booking</h1>
    <a href="/book">Book a Procedure</a>
    <a href="/admin/bookings">Admin View</a>
</body>
</html>
"""

# templates/book.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Book a Procedure</title>
</head>
<body>
    <h1>Book a Laser Procedure</h1>
    <form method="POST" action="/book">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="procedure">Procedure:</label>
        <select id="procedure" name="procedure" required>
            <option value="ZWAVE">ZWAVE</option>
            <option value="ZTONE">ZTONE</option>
        </select><br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required><br>
        <label for="time">Time:</label>
        <input type="time" id="time" name="time" required><br>
        <button type="submit">Book</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
"""

# templates/admin_bookings.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Admin - Bookings</title>
</head>
<body>
    <h1>All Bookings</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Procedure</th>
            <th>Date</th>
            <th>Time</th>
        </tr>
        {% for booking in bookings %}
        <tr>
            <td>{{ booking[0] }}</td>
            <td>{{ booking[1] }}</td>
            <td>{{ booking[2] }}</td>
            <td>{{ booking[3] }}</td>
            <td>{{ booking[4] }}</td>
            <td>{{ booking[5] }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
"""
```
