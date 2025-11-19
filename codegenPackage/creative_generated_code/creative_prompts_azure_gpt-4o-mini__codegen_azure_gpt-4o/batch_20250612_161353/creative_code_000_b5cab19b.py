"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate a code snippet for a web application that allows users to book a real estate photography session, incorporating features like scheduling and client testimonials.
Generated: DETERMINISTIC_b5cab19b0f2578fe
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Python-based web application using the Flask framework:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Secret key for session management

DATABASE = 'database.db'

# Utility function to interact with the database
def query_db(query, args=(), one=False):
    """Query the database and return results."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Route: Home Page
@app.route('/')
def home():
    """Render the home page with testimonials."""
    testimonials = query_db("SELECT * FROM testimonials ORDER BY created_at DESC")
    return render_template('home.html', testimonials=testimonials)

# Route: Booking Page
@app.route('/book', methods=['GET', 'POST'])
def book_session():
    """Allow users to book a photography session."""
    if request.method == 'POST':
        client_name = request.form.get('name')
        client_email = request.form.get('email')
        session_date = request.form.get('date')

        # Simple validation
        if not client_name or not client_email or not session_date:
            flash('All fields are required!', 'error')
            return redirect(url_for('book_session'))

        try:
            # Validate date format
            session_date_obj = datetime.strptime(session_date, '%Y-%m-%d')

            # Save booking to the database
            query_db(
                "INSERT INTO bookings (name, email, session_date) VALUES (?, ?, ?)",
                (client_name, client_email, session_date_obj)
            )
            flash('Your session has been successfully booked!', 'success')
            return redirect(url_for('home'))
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('book_session'))

    return render_template('book.html')

# Route: Submit Testimonials
@app.route('/testimonial', methods=['GET', 'POST'])
def testimonial():
    """Allow users to submit testimonials."""
    if request.method == 'POST':
        client_name = request.form.get('name')
        testimonial_text = request.form.get('testimonial')

        # Simple validation
        if not client_name or not testimonial_text:
            flash('Both fields are required!', 'error')
            return redirect(url_for('testimonial'))

        # Save testimonial to the database
        query_db(
            "INSERT INTO testimonials (name, testimonial, created_at) VALUES (?, ?, ?)",
            (client_name, testimonial_text, datetime.now())
        )

        flash('Thank you for submitting your testimonial!', 'success')
        return redirect(url_for('home'))

    return render_template('testimonial.html')

# Initialize the database
@app.before_first_request
def setup_database():
    """Create necessary tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            session_date DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS testimonials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            testimonial TEXT NOT NULL,
            created_at DATETIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Required HTML Templates:
1. **home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home - Real Estate Photography</title>
</head>
<body>
    <h1>Welcome to Real Estate Photography Booking</h1>
    <a href="/book">Book a Session</a> | <a href="/testimonial">Submit a Testimonial</a>

    <h2>Client Testimonials</h2>
    {% for testimonial in testimonials %}
        <p><strong>{{ testimonial['name'] }}</strong>: {{ testimonial['testimonial'] }} ({{ testimonial['created_at'] }})</p>
    {% endfor %}
</body>
</html>
```

2. **book.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Book a Session</title>
</head>
<body>
    <h1>Book a Photography Session</h1>
    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>
        <label for="date">Session Date (YYYY-MM-DD):</label><br>
        <input type="text" id="date" name="date"><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

3. **testimonial.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Submit a Testimonial</title>
</head>
<body>
    <h1>Submit a Testimonial</h1>
    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <label for="testimonial">Testimonial:</label><br>
        <textarea id="testimonial" name="testimonial"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
