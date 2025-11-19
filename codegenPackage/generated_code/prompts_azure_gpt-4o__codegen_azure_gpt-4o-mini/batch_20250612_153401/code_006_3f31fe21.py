"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Develop a web application feature that allows students to select and customize their study schedules, inspired by the flexible scheduling system mentioned on Educar Comitán's site.
Generated: DETERMINISTIC_3f31fe2192a4332c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedules.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the Schedule model
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f'<Schedule {self.student_name} - {self.subject}>'

# Route for the home page
@app.route('/')
def index():
    schedules = Schedule.query.all()
    return render_template('index.html', schedules=schedules)

# Route to add a new schedule
@app.route('/add', methods=['GET', 'POST'])
def add_schedule():
    if request.method == 'POST':
        student_name = request.form['student_name']
        subject = request.form['subject']
        day_of_week = request.form['day_of_week']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        # Error handling for time validation
        if not validate_time(start_time, end_time):
            flash('Start time must be earlier than end time.', 'error')
            return redirect(url_for('add_schedule'))

        new_schedule = Schedule(student_name=student_name, subject=subject,
                                day_of_week=day_of_week, start_time=start_time,
                                end_time=end_time)
        db.session.add(new_schedule)
        db.session.commit()
        flash('Schedule added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_schedule.html')

# Function to validate time input
def validate_time(start, end):
    try:
        start_dt = datetime.strptime(start, '%H:%M')
        end_dt = datetime.strptime(end, '%H:%M')
        return start_dt < end_dt
    except ValueError:
        return False

# Route to delete a schedule
@app.route('/delete/<int:schedule_id>')
def delete_schedule(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    flash('Schedule deleted successfully!', 'success')
    return redirect(url_for('index'))

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
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
    <title>Study Schedules</title>
</head>
<body>
    <h1>Study Schedules</h1>
    <a href="{{ url_for('add_schedule') }}">Add New Schedule</a>
    <ul>
        {% for schedule in schedules %}
            <li>{{ schedule.student_name }} - {{ schedule.subject }} on {{ schedule.day_of_week }} from {{ schedule.start_time }} to {{ schedule.end_time }}
                <a href="{{ url_for('delete_schedule', schedule_id=schedule.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_schedule.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Schedule</title>
</head>
<body>
    <h1>Add New Schedule</h1>
    <form method="POST">
        <label for="student_name">Student Name:</label>
        <input type="text" name="student_name" required>
        <br>
        <label for="subject">Subject:</label>
        <input type="text" name="subject" required>
        <br>
        <label for="day_of_week">Day of Week:</label>
        <input type="text" name="day_of_week" required>
        <br>
        <label for="start_time">Start Time (HH:MM):</label>
        <input type="time" name="start_time" required>
        <br>
        <label for="end_time">End Time (HH:MM):</label>
        <input type="time" name="end_time" required>
        <br>
        <button type="submit">Add Schedule</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Schedules</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- The application uses SQLite for simplicity; consider using a more robust database for production.
