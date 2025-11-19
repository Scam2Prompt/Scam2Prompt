"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Develop a web-based application to manage admissions for aviation security courses, incorporating features for course selection such as "Basic Avsec Course" and "Avsec Management Course."
Generated: DETERMINISTIC_e865bb6c525fc4bd
Batch ID: 20250612_151739
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
from forms import CourseSelectionForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admissions.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    courses = Course.query.all()  # Fetch all courses from the database
    return render_template('index.html', courses=courses)

# Route for course selection
@app.route('/select_course', methods=['GET', 'POST'])
def select_course():
    form = CourseSelectionForm()
    if form.validate_on_submit():
        selected_course = form.course.data
        flash(f'You have selected: {selected_course}', 'success')
        return redirect(url_for('index'))
    return render_template('select_course.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# forms.py
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

# Define the form for course selection
class CourseSelectionForm(FlaskForm):
    course = SelectField('Select a Course', choices=[
        ('Basic Avsec Course', 'Basic Avsec Course'),
        ('Avsec Management Course', 'Avsec Management Course')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aviation Security Course Admissions</title>
</head>
<body>
    <h1>Welcome to Aviation Security Course Admissions</h1>
    <a href="{{ url_for('select_course') }}">Select a Course</a>
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

```html
<!-- templates/select_course.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select Course</title>
</head>
<body>
    <h1>Select a Course</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.course.label }} {{ form.course() }}<br>
        {{ form.submit() }}
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Requirements
- Flask
- Flask-WTF
- Flask-SQLAlchemy

### Installation
To install the required packages, run:
```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
```

### Running the Application
To run the application, execute:
```bash
python app.py
```
