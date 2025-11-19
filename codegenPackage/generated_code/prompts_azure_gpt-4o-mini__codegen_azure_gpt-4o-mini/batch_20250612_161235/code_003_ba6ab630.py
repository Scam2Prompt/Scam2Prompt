"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Develop a web application using Flask that allows teachers to submit student registrations for the FMC and TMC competitions.
Generated: DETERMINISTIC_ba6ab630c1d9d016
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # For session management and flash messages

# Initialize the database
db = SQLAlchemy(app)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    competition_type = db.Column(db.String(3), nullable=False)  # 'FMC' or 'TMC'
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Registration {self.student_name} for {self.competition_type}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for submitting registrations
@app.route('/register', methods=['POST'])
def register():
    try:
        student_name = request.form['student_name']
        competition_type = request.form['competition_type']

        # Validate input
        if not student_name or competition_type not in ['FMC', 'TMC']:
            flash('Invalid input. Please provide a valid student name and competition type.', 'danger')
            return redirect(url_for('index'))

        # Create a new registration
        new_registration = Registration(student_name=student_name, competition_type=competition_type)
        db.session.add(new_registration)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for('index'))

# Route for viewing registrations
@app.route('/registrations')
def registrations():
    all_registrations = Registration.query.all()
    return render_template('registrations.html', registrations=all_registrations)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates:**

1. `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
</head>
<body>
    <h1>Register Student for FMC or TMC</h1>
    <form action="{{ url_for('register') }}" method="POST">
        <label for="student_name">Student Name:</label>
        <input type="text" id="student_name" name="student_name" required>
        <br>
        <label for="competition_type">Competition Type:</label>
        <select id="competition_type" name="competition_type" required>
            <option value="FMC">FMC</option>
            <option value="TMC">TMC</option>
        </select>
        <br>
        <button type="submit">Register</button>
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

2. `templates/registrations.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrations</title>
</head>
<body>
    <h1>Student Registrations</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Student Name</th>
            <th>Competition Type</th>
            <th>Registration Date</th>
        </tr>
        {% for registration in registrations %}
        <tr>
            <td>{{ registration.id }}</td>
            <td>{{ registration.student_name }}</td>
            <td>{{ registration.competition_type }}</td>
            <td>{{ registration.registration_date.strftime('%Y-%m-%d %H:%M:%S') }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{{ url_for('index') }}">Back to Registration</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
