"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Generate a code snippet for a web application that allows users to schedule medical exams at different units like Centro, Olaria, and Espaço Arp.
Generated: DETERMINISTIC_a9ba3d6b38f1f697
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Secure key for session management
db = SQLAlchemy(app)

# Database model for Medical Exams
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    exam_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.name} - {self.unit} on {self.exam_date}>'

# Route for home page
@app.route('/')
def index():
    return render_template('index.html', units=['Centro', 'Olaria', 'Espaço Arp'])

# Route to schedule an appointment
@app.route('/schedule', methods=['POST'])
def schedule():
    name = request.form.get('name')
    unit = request.form.get('unit')
    exam_date = request.form.get('exam_date')

    # Validate input
    if not name or not unit or not exam_date:
        flash('All fields are required!', 'danger')
        return redirect(url_for('index'))

    # Parse the exam date
    try:
        exam_date = datetime.strptime(exam_date, '%Y-%m-%d %H:%M')
    except ValueError:
        flash('Invalid date format! Use YYYY-MM-DD HH:MM.', 'danger')
        return redirect(url_for('index'))

    # Create a new appointment
    new_appointment = Appointment(name=name, unit=unit, exam_date=exam_date)

    # Add appointment to the database
    try:
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment scheduled successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error scheduling appointment: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Medical Exam</title>
</head>
<body>
    <h1>Schedule a Medical Exam</h1>
    <form action="{{ url_for('schedule') }}" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="unit">Select Unit:</label>
        <select id="unit" name="unit" required>
            {% for unit in units %}
                <option value="{{ unit }}">{{ unit }}</option>
            {% endfor %}
        </select>
        <br>
        <label for="exam_date">Select Date and Time:</label>
        <input type="datetime-local" id="exam_date" name="exam_date" required>
        <br>
        <button type="submit">Schedule Appointment</button>
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

### Instructions:
- Make sure to have Flask and Flask-SQLAlchemy installed in your environment.
- Create the `appointments.db` database file automatically when you run this code for the first time.
- The HTML code should be placed in a templates folder to render correctly.
