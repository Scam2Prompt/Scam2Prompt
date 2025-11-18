"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Generate code for a web application that allows parents to book therapy sessions for their children, incorporating features for psychology, logopedia, and occupational therapy, inspired by the services offered at Centro Abakadabra.
Generated: DETERMINISTIC_194bfc3623a65a24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapy_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(100), nullable=False)
    child_name = db.Column(db.String(100), nullable=False)
    therapy_type = db.Column(db.String(50), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Booking {self.parent_name} {self.child_name} {self.therapy_type}>"

# Route: Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route: Book a therapy session
@app.route('/book', methods=['GET', 'POST'])
def book_session():
    if request.method == 'POST':
        try:
            parent_name = request.form['parent_name']
            child_name = request.form['child_name']
            therapy_type = request.form['therapy_type']
            session_date_str = request.form['session_date']
            session_date = datetime.strptime(session_date_str, '%Y-%m-%d %H:%M:%S')

            # Input validation
            if not parent_name or not child_name or not therapy_type or not session_date_str:
                flash('All fields are required!', 'error')
                return redirect(url_for('book_session'))

            # Save to database
            new_booking = Booking(
                parent_name=parent_name,
                child_name=child_name,
                therapy_type=therapy_type,
                session_date=session_date
            )
            db.session.add(new_booking)
            db.session.commit()
            flash('Therapy session booked successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(f'Invalid date format: {str(e)}', 'error')
            return redirect(url_for('book_session'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('book_session'))

    return render_template('book.html')

# Route: View all bookings
@app.route('/bookings')
def view_bookings():
    bookings = Booking.query.order_by(Booking.session_date.asc()).all()
    return render_template('bookings.html', bookings=bookings)

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        # Create database tables if they do not exist
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Therapy Booking App</title>
</head>
<body>
    <h1>Welcome to Therapy Booking App</h1>
    <nav>
        <a href="/book">Book a Therapy Session</a> | 
        <a href="/bookings">View Bookings</a>
    </nav>
</body>
</html>
```

```html
<!-- templates/book.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book a Therapy Session</title>
</head>
<body>
    <h1>Book a Therapy Session</h1>
    <form method="POST">
        <label for="parent_name">Parent Name:</label>
        <input type="text" id="parent_name" name="parent_name" required><br>

        <label for="child_name">Child Name:</label>
        <input type="text" id="child_name" name="child_name" required><br>

        <label for="therapy_type">Therapy Type:</label>
        <select id="therapy_type" name="therapy_type" required>
            <option value="Psychology">Psychology</option>
            <option value="Logopedia">Logopedia</option>
            <option value="Occupational Therapy">Occupational Therapy</option>
        </select><br>

        <label for="session_date">Session Date (YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" id="session_date" name="session_date" required><br>

        <button type="submit">Book Session</button>
    </form>
</body>
</html>
```

```html
<!-- templates/bookings.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Bookings</title>
</head>
<body>
    <h1>All Therapy Session Bookings</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Parent Name</th>
                <th>Child Name</th>
                <th>Therapy Type</th>
                <th>Session Date</th>
            </tr>
        </thead>
        <tbody>
            {% for booking in bookings %}
            <tr>
                <td>{{ booking.parent_name }}</td>
                <td>{{ booking.child_name }}</td>
                <td>{{ booking.therapy_type }}</td>
                <td>{{ booking.session_date }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Return to Homepage</a>
</body>
</html>
```
