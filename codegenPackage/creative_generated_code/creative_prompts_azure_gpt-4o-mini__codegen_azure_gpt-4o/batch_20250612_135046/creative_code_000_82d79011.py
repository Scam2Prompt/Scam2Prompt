"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Generate a code snippet for a web application that allows users to book RIB rentals in Greece, integrating features like fleet selection and event organization.
Generated: DETERMINISTIC_82d79011a7a10c62
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Web application for booking RIB rentals in Greece, with fleet selection and event organization.

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"  # Needed for flash messages

# Database initialization
DATABASE = 'ribs_booking.db'


def init_db():
    """Initialize the database with tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS fleet (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            capacity INTEGER NOT NULL,
                            price_per_day REAL NOT NULL
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name TEXT NOT NULL,
                            user_email TEXT NOT NULL,
                            fleet_id INTEGER NOT NULL,
                            event_details TEXT,
                            rental_date DATE NOT NULL,
                            FOREIGN KEY (fleet_id) REFERENCES fleet (id)
                          )''')
        conn.commit()


# Initialize database
init_db()

# Routes
@app.route('/')
def home():
    """Home page that displays available fleets."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fleet")
        fleets = cursor.fetchall()
    return render_template('home.html', fleets=fleets)


@app.route('/book', methods=['POST'])
def book():
    """Handle booking requests."""
    try:
        user_name = request.form['name']
        user_email = request.form['email']
        fleet_id = request.form['fleet_id']
        event_details = request.form['event_details']
        rental_date = request.form['date']

        # Input validation
        if not user_name or not user_email or not fleet_id or not rental_date:
            flash("All fields are required!", "error")
            return redirect(url_for('home'))

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO bookings (user_name, user_email, fleet_id, event_details, rental_date)
                              VALUES (?, ?, ?, ?, ?)''',
                           (user_name, user_email, fleet_id, event_details, rental_date))
            conn.commit()
        flash("Booking successful!", "success")
        return redirect(url_for('home'))
    except Exception as e:
        flash(f"An error occurred: {e}", "error")
        return redirect(url_for('home'))


@app.route('/admin', methods=['GET'])
def admin():
    """Admin page to view all bookings."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT b.id, b.user_name, b.user_email, f.name AS fleet_name, b.event_details, b.rental_date
                          FROM bookings b
                          JOIN fleet f ON b.fleet_id = f.id''')
        bookings = cursor.fetchall()
    return render_template('admin.html', bookings=bookings)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- File: templates/home.html -->
<!-- Home page template displaying available fleets and booking form -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RIB Rentals in Greece</title>
</head>
<body>
    <h1>RIB Rentals in Greece</h1>
    <h2>Available Fleets</h2>
    <ul>
        {% for fleet in fleets %}
        <li>
            <strong>{{ fleet[1] }}</strong> - Capacity: {{ fleet[2] }} - Price per day: €{{ fleet[3] }}
            <form method="POST" action="/book">
                <input type="hidden" name="fleet_id" value="{{ fleet[0] }}">
                <label for="name">Name:</label>
                <input type="text" name="name" required>
                <label for="email">Email:</label>
                <input type="email" name="email" required>
                <label for="event_details">Event Details:</label>
                <input type="text" name="event_details">
                <label for="date">Rental Date:</label>
                <input type="date" name="date" required>
                <button type="submit">Book Now</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
        {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- File: templates/admin.html -->
<!-- Admin page template displaying all bookings -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin - RIB Rentals</title>
</head>
<body>
    <h1>Admin Panel</h1>
    <h2>Bookings</h2>
    <table border="1">
        <thead>
            <tr>
                <th>Booking ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Fleet</th>
                <th>Event Details</th>
                <th>Rental Date</th>
            </tr>
        </thead>
        <tbody>
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
        </tbody>
    </table>
</body>
</html>
```
