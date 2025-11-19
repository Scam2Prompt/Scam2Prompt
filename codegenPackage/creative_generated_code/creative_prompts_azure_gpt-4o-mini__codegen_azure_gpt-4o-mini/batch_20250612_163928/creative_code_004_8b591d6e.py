"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Create a program that allows parents to book appointments with pediatric dentists in Pune directly through a web interface.
Generated: DETERMINISTIC_8b591d6ec7dfad9c
Batch ID: 20250612_163928
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize the database

# Database model for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each appointment
    parent_name = db.Column(db.String(100), nullable=False)  # Name of the parent
    child_name = db.Column(db.String(100), nullable=False)  # Name of the child
    date_time = db.Column(db.DateTime, nullable=False)  # Date and time of the appointment
    dentist_name = db.Column(db.String(100), nullable=False)  # Dentist's name

    def __repr__(self):
        return f'<Appointment {self.id} - {self.parent_name}>'


# Route for the home page
@app.route('/')
def index():
    # Retrieve all appointments from the database
    appointments = Appointment.query.all()
    return render_template('index.html', appointments=appointments)  # Render the template


# Route to book an appointment
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        try:
            # Get data from the form
            parent_name = request.form['parent_name']
            child_name = request.form['child_name']
            date_time = datetime.strptime(request.form['date_time'], '%Y-%m-%d %H:%M')  # Parse date and time
            dentist_name = request.form['dentist_name']

            # Create a new Appointment instance
            new_appointment = Appointment(
                parent_name=parent_name,
                child_name=child_name,
                date_time=date_time,
                dentist_name=dentist_name
            )

            # Add the appointment to the session and commit to the database
            db.session.add(new_appointment)
            db.session.commit()

            flash('Appointment booked successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))  # Redirect to the home page

        except Exception as e:
            db.session.rollback()  # Rollback if there is an error
            flash(f'Error occurred while booking appointment: {str(e)}', 'danger')  # Flash error message
            return redirect(url_for('book'))  # Redirect back to booking page

    return render_template('book.html')  # Render the booking form


# Route to delete an appointment
@app.route('/delete/<int:id>', methods=['POST'])
def delete_appointment(id):
    # Find the appointment by ID
    appointment = Appointment.query.get_or_404(id)  # Get appointment or 404 if not found
    db.session.delete(appointment)  # Delete the appointment
    db.session.commit()  # Commit the changes
    flash('Appointment deleted successfully!', 'success')  # Flash success message
    return redirect(url_for('index'))  # Redirect to home page


# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if not exist
    app.run(debug=True)  # Run the application in debug mode
```

**HTML Templates (index.html and book.html)**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment List</title>
</head>
<body>
    <h1>Appointment List</h1>
    <a href="{{ url_for('book') }}">Book an Appointment</a>

    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}

    <ul>
        {% for appointment in appointments %}
            <li>
                {{ appointment.parent_name }} - {{ appointment.child_name }} on {{ appointment.date_time }} with {{ appointment.dentist_name }}
                <form action="{{ url_for('delete_appointment', id=appointment.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **book.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book Appointment</h1>
    <form action="{{ url_for('book') }}" method="POST">
        <label for="parent_name">Parent Name:</label>
        <input type="text" name="parent_name" required>

        <label for="child_name">Child Name:</label>
        <input type="text" name="child_name" required>

        <label for="date_time">Date and Time:</label>
        <input type="datetime-local" name="date_time" required>

        <label for="dentist_name">Dentist Name:</label>
        <input type="text" name="dentist_name" required>

        <button type="submit">Book Appointment</button>
    </form>

    <a href="{{ url_for('index') }}">Back to Appointment List</a>
</body>
</html>
```

**Instructions:**
- Install Flask and SQLAlchemy by running `pip install Flask Flask-SQLAlchemy`.
- Save the Python code in a file, e.g., `app.py`.
- Create a folder named `templates` and save the HTML files inside it.
- Run the application using `python app.py`.
