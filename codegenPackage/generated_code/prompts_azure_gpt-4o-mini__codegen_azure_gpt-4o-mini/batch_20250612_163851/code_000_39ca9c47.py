"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions, incorporating features for individual therapy and webinars as described on Melika Taheri's website.
Generated: DETERMINISTIC_39ca9c47f8aa7d52
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapy_sessions.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management
db = SQLAlchemy(app)

# Database model for therapy sessions
class TherapySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String(50), nullable=False)  # 'individual' or 'webinar'
    date_time = db.Column(db.DateTime, nullable=False)
    user_email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Session {self.session_type} on {self.date_time}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for booking a therapy session
@app.route('/book', methods=['GET', 'POST'])
def book_session():
    if request.method == 'POST':
        session_type = request.form.get('session_type')
        date_time_str = request.form.get('date_time')
        user_email = request.form.get('user_email')

        # Validate input
        if not session_type or not date_time_str or not user_email:
            flash('All fields are required!', 'danger')
            return redirect(url_for('book_session'))

        try:
            # Parse the date and time
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
            new_session = TherapySession(session_type=session_type, date_time=date_time, user_email=user_email)

            # Add the session to the database
            db.session.add(new_session)
            db.session.commit()
            flash('Session booked successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('book_session'))

    return render_template('book.html')

# Route for viewing booked sessions
@app.route('/sessions')
def view_sessions():
    sessions = TherapySession.query.all()
    return render_template('sessions.html', sessions=sessions)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Therapy Booking</title>
</head>
<body>
    <h1>Welcome to Online Therapy Booking</h1>
    <a href="{{ url_for('book_session') }}">Book a Session</a>
    <a href="{{ url_for('view_sessions') }}">View Booked Sessions</a>
</body>
</html>
```

**book.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book a Session</title>
</head>
<body>
    <h1>Book a Therapy Session</h1>
    <form method="POST">
        <label for="session_type">Session Type:</label>
        <select name="session_type" required>
            <option value="individual">Individual Therapy</option>
            <option value="webinar">Webinar</option>
        </select>
        <br>
        <label for="date_time">Date and Time (YYYY-MM-DD HH:MM):</label>
        <input type="text" name="date_time" required>
        <br>
        <label for="user_email">Your Email:</label>
        <input type="email" name="user_email" required>
        <br>
        <button type="submit">Book Session</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**sessions.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booked Sessions</title>
</head>
<body>
    <h1>Booked Therapy Sessions</h1>
    <ul>
        {% for session in sessions %}
            <li>{{ session.session_type }} on {{ session.date_time }} - {{ session.user_email }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
``` 

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- This code is a basic implementation and can be extended with additional features such as user authentication, email notifications, and more robust error handling as needed.
