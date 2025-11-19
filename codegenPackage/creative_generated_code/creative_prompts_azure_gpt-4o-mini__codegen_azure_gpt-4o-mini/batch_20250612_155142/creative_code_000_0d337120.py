"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Generate a code snippet for a web application that allows users to register for gliding courses at the AAVE club, including fields for personal information and course selection.
Generated: DETERMINISTIC_0d337120df47efb4
Batch ID: 20250612_155142
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
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gliding_courses.db'
db = SQLAlchemy(app)

# Define the model for registered users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    course = db.Column(db.String(100), nullable=False)

# Create the registration form
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    course = SelectField('Course', choices=[
        ('beginner', 'Beginner Course'),
        ('intermediate', 'Intermediate Course'),
        ('advanced', 'Advanced Course')
    ], validators=[DataRequired()])
    submit = SubmitField('Register')

# Route for the registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user entry
        new_user = User(name=form.name.data, email=form.email.data, course=form.course.data)
        try:
            db.session.add(new_user)  # Add new user to the session
            db.session.commit()  # Commit the session to the database
            flash('Registration successful!', 'success')  # Flash success message
            return redirect(url_for('register'))  # Redirect to the register page
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error occurred: {e}', 'danger')  # Flash error message
    return render_template('register.html', form=form)  # Render the registration template

# Create the database and tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

```html
<!-- register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gliding Course Registration</title>
</head>
<body>
    <h1>Register for Gliding Courses</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.course.label }}<br>
            {{ form.course() }}<br>
            {% for error in form.course.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
      {% if messages %}
        {% for category, message in messages %}
          <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}
</body>
</html>
```
