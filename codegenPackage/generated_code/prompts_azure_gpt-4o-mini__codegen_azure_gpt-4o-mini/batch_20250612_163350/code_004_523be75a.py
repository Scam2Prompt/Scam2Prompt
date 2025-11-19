"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Develop a simple mobile app interface that allows users to book individual or child counseling sessions, reflecting the offerings of Dr. Raheleh Sadeghi.
Generated: DETERMINISTIC_523be75affbcfe17
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for the mobile app
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counseling_sessions.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the database model for counseling sessions
class CounselingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String(50), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    client_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Session {self.session_type} by {self.client_name} on {self.date_time}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    sessions = CounselingSession.query.all()
    return render_template('index.html', sessions=sessions)

# Route for booking a session
@app.route('/book', methods=['GET', 'POST'])
def book_session():
    if request.method == 'POST':
        session_type = request.form.get('session_type')
        date_time_str = request.form.get('date_time')
        client_name = request.form.get('client_name')

        # Error handling for date parsing
        try:
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD HH:MM.', 'error')
            return redirect(url_for('book_session'))

        # Create a new session and add it to the database
        new_session = CounselingSession(session_type=session_type, date_time=date_time, client_name=client_name)
        db.session.add(new_session)
        db.session.commit()
        flash('Session booked successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('book.html')

# Route for viewing session details
@app.route('/session/<int:session_id>')
def session_detail(session_id):
    session = CounselingSession.query.get_or_404(session_id)
    return render_template('session_detail.html', session=session)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counseling Sessions</title>
</head>
<body>
    <h1>Counseling Sessions</h1>
    <a href="{{ url_for('book_session') }}">Book a Session</a>
    <ul>
        {% for session in sessions %}
            <li>
                <a href="{{ url_for('session_detail', session_id=session.id) }}">
                    {{ session.session_type }} by {{ session.client_name }} on {{ session.date_time }}
                </a>
            </li>
        {% endfor %}
    </ul>
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
    <h1>Book a Counseling Session</h1>
    <form method="POST">
        <label for="session_type">Session Type:</label>
        <select name="session_type" id="session_type" required>
            <option value="Individual">Individual Counseling</option>
            <option value="Child">Child Counseling</option>
        </select>
        <br>
        <label for="date_time">Date and Time (YYYY-MM-DD HH:MM):</label>
        <input type="text" name="date_time" id="date_time" required>
        <br>
        <label for="client_name">Your Name:</label>
        <input type="text" name="client_name" id="client_name" required>
        <br>
        <button type="submit">Book Session</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**session_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Session Detail</title>
</head>
<body>
    <h1>Session Detail</h1>
    <p>Type: {{ session.session_type }}</p>
    <p>Client: {{ session.client_name }}</p>
    <p>Date and Time: {{ session.date_time }}</p>
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

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
- This code is structured for a simple web application; for a mobile app, consider using a framework like React Native or Flutter.
