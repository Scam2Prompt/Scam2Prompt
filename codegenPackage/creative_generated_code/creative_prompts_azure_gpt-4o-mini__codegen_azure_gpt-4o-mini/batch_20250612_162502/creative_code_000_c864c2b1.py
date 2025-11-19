"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Generate a code snippet for a web application that allows users to enroll in the "Especialidad en Ortodoncia" program at Instituto de Especialidades Odontológicas, including fields for start date and class schedule.
Generated: DETERMINISTIC_c864c2b13d604534
Batch ID: 20250612_162502
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enrollments.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Enrollment model
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    class_schedule = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Enrollment {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to display the enrollment form
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        try:
            # Get data from the form
            name = request.form['name']
            start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
            class_schedule = request.form['class_schedule']

            # Create a new enrollment instance
            new_enrollment = Enrollment(name=name, start_date=start_date, class_schedule=class_schedule)
            
            # Add to the session and commit to the database
            db.session.add(new_enrollment)
            db.session.commit()

            flash('Enrollment successful!', 'success')
            return redirect(url_for('enroll'))
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            flash(f'Error during enrollment: {str(e)}', 'danger')

    return render_template('enroll.html')

# Route to display all enrollments
@app.route('/enrollments')
def show_enrollments():
    enrollments = Enrollment.query.all()
    return render_template('enrollments.html', enrollments=enrollments)

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template `templates/enroll.html`**
```html
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enroll in Especialidad en Ortodoncia</title>
</head>
<body>
    <h1>Enroll in Especialidad en Ortodoncia</h1>
    <form method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" name="start_date" required>
        
        <label for="class_schedule">Class Schedule:</label>
        <input type="text" id="class_schedule" name="class_schedule" required>
        
        <button type="submit">Enroll</button>
    </form>
</body>
</html>
```

**HTML Template `templates/enrollments.html`**
```html
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enrollments List</title>
</head>
<body>
    <h1>Enrollments List</h1>
    <ul>
        {% for enrollment in enrollments %}
            <li>{{ enrollment.name }} - {{ enrollment.start_date }} - {{ enrollment.class_schedule }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('enroll') }}">Enroll in a new program</a>
</body>
</html>
```

Make sure to install Flask and Flask-SQLAlchemy to run this code:
```bash
pip install Flask Flask-SQLAlchemy
```

This code provides a simple web application that allows users to enroll in a program and view all enrollments.
