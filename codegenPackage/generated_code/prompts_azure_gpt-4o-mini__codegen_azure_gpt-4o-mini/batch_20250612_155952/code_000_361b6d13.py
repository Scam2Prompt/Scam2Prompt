"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Generate a code snippet for a registration form that allows users to sign up for basketball leagues at Courtside Fitness, incorporating fields for name, email, skill level, and preferred league.
Generated: DETERMINISTIC_361b6d13918c8406
Batch ID: 20250612_155952
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
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Define the registration form using Flask-WTF
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    skill_level = SelectField('Skill Level', choices=[('beginner', 'Beginner'), 
                                                       ('intermediate', 'Intermediate'), 
                                                       ('advanced', 'Advanced')],
                               validators=[DataRequired()])
    preferred_league = SelectField('Preferred League', choices=[('league1', 'League 1'), 
                                                                 ('league2', 'League 2'), 
                                                                 ('league3', 'League 3')],
                                    validators=[DataRequired()])
    submit = SubmitField('Register')

# Route for the registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here you would typically save the data to a database
        # For demonstration, we will just flash a success message
        flash(f'Registration successful for {form.name.data}!', 'success')
        return redirect(url_for('register'))  # Redirect to the same page after submission
    return render_template('register.html', form=form)

# Error handling for unexpected issues
@app.errorhandler(500)
def internal_error(error):
    return "An unexpected error occurred. Please try again later.", 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body>
    <h1>Register for Basketball Leagues at Courtside Fitness</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.skill_level.label }}<br>
            {{ form.skill_level() }}<br>
            {% for error in form.skill_level.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.preferred_league.label }}<br>
            {{ form.preferred_league() }}<br>
            {% for error in form.preferred_league.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
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
