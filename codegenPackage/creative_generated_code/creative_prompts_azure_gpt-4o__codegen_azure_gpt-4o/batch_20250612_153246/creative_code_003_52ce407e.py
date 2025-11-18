"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Create a web application that allows users to book professional home services like furniture assembly and kitchen installation, similar to شركة الاحترافية's offerings.
Generated: DETERMINISTIC_52ce407e8f72c816
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a simple web application in Python using the Flask framework. This application allows users to browse, book professional home services, and view their bookings. It includes basic functionality and adheres to the request requirements.

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session security

# Database setup
DATABASE = 'services.db'

def init_db():
    """Initialize the database table structure."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Create table for services
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Create table for bookings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_id INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            FOREIGN KEY (service_id) REFERENCES services (id)
        )
    ''')

    connection.commit()
    connection.close()

# Initialize the database when the application starts
init_db()

# Routes

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/services')
def list_services():
    """Display the list of available services."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM services')
    services = cursor.fetchall()
    connection.close()
    return render_template('services.html', services=services)

@app.route('/book/<int:service_id>', methods=['GET', 'POST'])
def book_service(service_id):
    """Allow users to book a service."""
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        booking_date = request.form['booking_date']

        # Input validation
        if not customer_name or not customer_email or not booking_date:
            flash('All fields are required', 'error')
            return redirect(url_for('book_service', service_id=service_id))

        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO bookings (service_id, customer_name, customer_email, booking_date) '
                'VALUES (?, ?, ?, ?)', (service_id, customer_name, customer_email, booking_date)
            )
            connection.commit()
            connection.close()
            flash('Booking successful!', 'success')
            return redirect(url_for('list_services'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('list_services'))

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM services WHERE id = ?', (service_id,))
    service = cursor.fetchone()
    connection.close()
    return render_template('book.html', service=service)

@app.route('/bookings')
def view_bookings():
    """Display all bookings."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        SELECT bookings.id, services.name, bookings.customer_name, bookings.customer_email, bookings.booking_date
        FROM bookings
        INNER JOIN services ON bookings.service_id = services.id
    ''')
    bookings = cursor.fetchall()
    connection.close()
    return render_template('bookings.html', bookings=bookings)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates:
You need to create the following HTML files in a `templates` folder:

#### `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home Services</title>
</head>
<body>
    <h1>Welcome to Professional Home Services</h1>
    <a href="/services">Browse Services</a>
</body>
</html>
```

#### `services.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Available Services</title>
</head>
<body>
    <h1>Available Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <h2>{{ service[1] }}</h2>
                <p>{{ service[2] }}</p>
                <p>Price: ${{ service[3] }}</p>
                <a href="/book/{{ service[0] }}">Book Now</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `book.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Book Service</title>
</head>
<body>
    <h1>Book Service: {{ service[1] }}</h1>
    <form method="POST">
        <label for="customer_name">Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>
        <br>
        <label for="customer_email">Email:</label>
        <input type="email" id="customer_email" name="customer_email" required>
        <br>
        <label for="booking_date">Booking Date:</label>
        <input type="date" id="booking_date" name="booking_date" required>
        <br>
        <button type="submit">Confirm Booking</button>
    </form>
</body>
</html>
```

#### `bookings.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Bookings</title>
</head>
<body>
    <h1>All Bookings</h1>
    <ul>
        {% for booking in bookings %}
            <li>
                <h2>Service: {{ booking[1] }}</h2>
                <p>Name: {{ booking[2] }}</p>
                <p>Email: {{ booking[3] }}</p>
                <p>Date: {{ booking[4] }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
1. Run the application with `python app.py`.
2. Ensure Flask is installed using `pip install flask`.
3. Set up the SQLite database before running the app using the `init_db()` function.
