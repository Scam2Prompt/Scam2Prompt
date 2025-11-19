"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Develop a simple web application that allows users to schedule a consultation for paving services, reflecting the user-friendly approach seen on Bedford Paving's website.
Generated: DETERMINISTIC_1331eec7226c311c
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize the database
db = SQLAlchemy(app)

# Model for consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.name} on {self.date_time}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to schedule a consultation
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date_time_str = request.form.get('date_time')

        # Validate the date and time format
        try:
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date and time format. Please use YYYY-MM-DD HH:MM.', 'error')
            return redirect(url_for('schedule'))

        # Create a new consultation entry
        new_consultation = Consultation(name=name, email=email, phone=phone, date_time=date_time)

        # Add to the database
        try:
            db.session.add(new_consultation)
            db.session.commit()
            flash('Consultation scheduled successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error scheduling consultation: {str(e)}', 'error')

        return redirect(url_for('home'))

    return render_template('schedule.html')

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database and tables
    app.run(debug=True)  # Run in debug mode for development
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bedford Paving Consultation</title>
</head>
<body>
    <h1>Welcome to Bedford Paving</h1>
    <a href="{{ url_for('schedule') }}">Schedule a Consultation</a>
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

**schedule.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Consultation</title>
</head>
<body>
    <h1>Schedule a Consultation</h1>
    <form action="{{ url_for('schedule') }}" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        <label for="date_time">Date and Time:</label>
        <input type="datetime-local" id="date_time" name="date_time" required>
        <br>
        <input type="submit" value="Schedule">
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Instructions
1. Ensure you have Flask and SQLAlchemy installed in your Python environment.
2. Create a folder structure to hold the Flask app and HTML templates as shown.
3. Run the application. The consultations will be stored in a SQLite database file named `consultations.db`.
