"""
Generated Code Metadata:
========================
Original URL: https://www.socrates-gm.com
Prompt: How can I design a user-friendly interface for an employee portal that allows easy navigation and access to features like timesheet submission, as seen in the Socrates GM portal?
Generated: DETERMINISTIC_64e47a52a7e7a3b5
Batch ID: 20250612_155327
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    timesheets = db.relationship('Timesheet', backref='employee', lazy=True)

# Define the Timesheet model
class Timesheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for submitting a timesheet
@app.route('/submit_timesheet', methods=['GET', 'POST'])
def submit_timesheet():
    if request.method == 'POST':
        try:
            employee_id = request.form['employee_id']
            hours_worked = float(request.form['hours_worked'])
            new_timesheet = Timesheet(employee_id=employee_id, hours_worked=hours_worked)
            db.session.add(new_timesheet)
            db.session.commit()
            flash('Timesheet submitted successfully!', 'success')
            return redirect(url_for('home'))
        except ValueError:
            flash('Invalid input. Please enter a valid number for hours worked.', 'danger')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
    return render_template('submit_timesheet.html')

# Route for viewing timesheets
@app.route('/view_timesheets/<int:employee_id>')
def view_timesheets(employee_id):
    timesheets = Timesheet.query.filter_by(employee_id=employee_id).all()
    return render_template('view_timesheets.html', timesheets=timesheets)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Portal</title>
</head>
<body>
    <h1>Welcome to the Employee Portal</h1>
    <a href="{{ url_for('submit_timesheet') }}">Submit Timesheet</a>
    <a href="{{ url_for('view_timesheets', employee_id=1) }}">View Timesheets</a> <!-- Replace with dynamic employee ID -->
</body>
</html>
```

**submit_timesheet.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Timesheet</title>
</head>
<body>
    <h1>Submit Timesheet</h1>
    <form method="POST">
        <label for="employee_id">Employee ID:</label>
        <input type="text" name="employee_id" required>
        <label for="hours_worked">Hours Worked:</label>
        <input type="number" step="0.1" name="hours_worked" required>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

**view_timesheets.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Timesheets</title>
</head>
<body>
    <h1>Your Timesheets</h1>
    <ul>
        {% for timesheet in timesheets %}
            <li>{{ timesheet.date_submitted }}: {{ timesheet.hours_worked }} hours</li>
        {% else %}
            <li>No timesheets submitted.</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```
