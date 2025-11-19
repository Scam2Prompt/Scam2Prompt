"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lgtc.edu.pk
Prompt: Develop a web application that allows students to view and register for the technical programs offered by Lahore Group of Technical, focusing on DAE and Pharmacy Technician courses.
Generated: DETERMINISTIC_529ca3d0cd27c695
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programs.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # For session management
db = SQLAlchemy(app)

# Model for Technical Programs
class TechnicalProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Program {self.name}>'

# Home route to display available programs
@app.route('/')
def index():
    programs = TechnicalProgram.query.all()  # Fetch all programs from the database
    return render_template('index.html', programs=programs)

# Registration route for a specific program
@app.route('/register/<int:program_id>', methods=['GET', 'POST'])
def register(program_id):
    program = TechnicalProgram.query.get_or_404(program_id)  # Get program or 404
    form = RegistrationForm()

    if form.validate_on_submit():  # Check if form is submitted and valid
        flash(f'Successfully registered for {program.name}!', 'success')
        return redirect(url_for('index'))  # Redirect to home page

    return render_template('register.html', form=form, program=program)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Create the database and the database table
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development use only

# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Registration form for students
class RegistrationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    submit = SubmitField('Register')

# templates/index.html
'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programs - Lahore Group of Technical</title>
</head>
<body>
    <h1>Available Technical Programs</h1>
    <ul>
        {% for program in programs %}
            <li>{{ program.name }} - <a href="{{ url_for('register', program_id=program.id) }}">Register</a></li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# templates/register.html
'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - {{ program.name }}</title>
</head>
<body>
    <h1>Register for {{ program.name }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name(size=32) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
'''

# templates/404.html
'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Go Back Home</a>
</body>
</html>
'''
```
Make sure to install Flask and Flask-WTF via pip, and create an SQLite database before running the application.
