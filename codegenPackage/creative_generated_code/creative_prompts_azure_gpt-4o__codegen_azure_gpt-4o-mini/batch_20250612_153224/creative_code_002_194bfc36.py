"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Generate code for a web application that allows parents to book therapy sessions for their children, incorporating features for psychology, logopedia, and occupational therapy, inspired by the services offered at Centro Abakadabra.
Generated: DETERMINISTIC_194bfc3623a65a24
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Model representing therapy sessions
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_name = db.Column(db.String(100), nullable=False)
    therapy_type = db.Column(db.String(50), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Session {self.id} for {self.child_name}>'

# Route for the home page
@app.route('/')
def index():
    sessions = Session.query.all()  # Fetch all sessions
    return render_template('index.html', sessions=sessions)

# Route for booking a new therapy session
@app.route('/book', methods=['GET', 'POST'])
def book_session():
    if request.method == 'POST':
        child_name = request.form['child_name']
        therapy_type = request.form['therapy_type']
        session_date = request.form['session_date']

        # Input validation
        if not child_name or not therapy_type or not session_date:
            flash('All fields are required!', 'error')
            return redirect(url_for('book_session'))

        try:
            session_date = datetime.strptime(session_date, '%Y-%m-%d %H:%M')  # Ensure correct date format
            new_session = Session(child_name=child_name, therapy_type=therapy_type, session_date=session_date)

            db.session.add(new_session)  # Add new session to the session list
            db.session.commit()  # Commit the session to the database
            flash('Session booked successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error occurred: {e}', 'error')
            return redirect(url_for('book_session'))

    return render_template('book.html')

# Initialize database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Therapy Session Booking</title>
</head>
<body>
    <h1>Booked Therapy Sessions</h1>
    <ul>
        {% for session in sessions %}
            <li>{{ session.child_name }} - {{ session.therapy_type }} on {{ session.session_date.strftime('%Y-%m-%d %H:%M') }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('book_session') }}">Book a New Session</a>
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
    <title>Book Therapy Session</title>
</head>
<body>
    <h1>Book a Therapy Session</h1>
    <form action="{{ url_for('book_session') }}" method="POST">
        <label for="child_name">Child's Name:</label>
        <input type="text" id="child_name" name="child_name" required>
        <br>
        <label for="therapy_type">Therapy Type:</label>
        <select id="therapy_type" name="therapy_type" required>
            <option value="psychology">Psychology</option>
            <option value="logopedia">Logopedia</option>
            <option value="occupational_therapy">Occupational Therapy</option>
        </select>
        <br>
        <label for="session_date">Session Date:</label>
        <input type="datetime-local" id="session_date" name="session_date" required>
        <br>
        <button type="submit">Book Session</button>
    </form>
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
    <p>We're sorry, but the page you were looking for doesn't exist.</p>
    <a href="{{ url_for('index') }}">Return Home</a>
</body>
</html>
```

### Instructions to Run the Application:
1. Ensure you have Python and Flask installed.
2. Create a virtual environment and activate it.
3. Install Flask and Flask-SQLAlchemy:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
4. Save the Python code in `app.py` and the HTML templates in a `templates` folder.
5. Run the application:
   ```bash
   python app.py
   ```
6. Visit `http://127.0.0.1:5000/` in your web browser to interact with the application.
