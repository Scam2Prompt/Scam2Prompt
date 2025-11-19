"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gavasilva.adv.br
Prompt: Generate a code snippet for a web application that allows users to schedule legal consultations with Gava & Silva Advogados, incorporating features for both in-person and online appointments.
Generated: DETERMINISTIC_b487595849c8b6fc
Batch ID: 20250612_162050
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
import re

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    appointment_type = db.Column(db.String(10), nullable=False)  # 'in-person' or 'online'

    def __repr__(self):
        return f'<Appointment {self.name}, {self.date_time}>'

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to schedule an appointment
@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    date_time = request.form.get('date_time')
    appointment_type = request.form.get('appointment_type')

    # Validate input
    if not name or not email or not date_time or appointment_type not in ['in-person', 'online']:
        flash('All fields are required and appointment type must be either "in-person" or "online".')
        return redirect(url_for('index'))

    if not is_valid_email(email):
        flash('Invalid email format.')
        return redirect(url_for('index'))

    try:
        # Convert string to datetime object
        appointment_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        
        # Create a new appointment instance
        new_appointment = Appointment(name=name, email=email, date_time=appointment_date_time, appointment_type=appointment_type)
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment scheduled successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred while scheduling your appointment: {str(e)}')

    return redirect(url_for('index'))

# Route to view scheduled appointments
@app.route('/appointments')
def view_appointments():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule an Appointment</title>
</head>
<body>
    <h1>Schedule a Legal Consultation</h1>
    <form action="{{ url_for('schedule_appointment') }}" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="datetime-local" name="date_time" required>
        <select name="appointment_type" required>
            <option value="">Select Appointment Type</option>
            <option value="in-person">In-Person</option>
            <option value="online">Online</option>
        </select>
        <button type="submit">Schedule</button>
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

#### appointments.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scheduled Appointments</title>
</head>
<body>
    <h1>Scheduled Appointments</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Date and Time</th>
            <th>Appointment Type</th>
        </tr>
        {% for appointment in appointments %}
        <tr>
            <td>{{ appointment.name }}</td>
            <td>{{ appointment.email }}</td>
            <td>{{ appointment.date_time }}</td>
            <td>{{ appointment.appointment_type }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{{ url_for('index') }}">Schedule a new appointment</a>
</body>
</html>
```
