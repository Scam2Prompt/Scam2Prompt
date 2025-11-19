"""
Generated Code Metadata:
========================
Original URL: https://finflix.me
Prompt: Generate a code snippet that demonstrates how to implement a loan application form for a financial service that offers loans without Schufa checks, similar to the services provided by flix-fin.me.
Generated: DETERMINISTIC_c27f3de503b299d1
Batch ID: 20250612_163826
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
from wtforms import StringField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Define the loan application form using Flask-WTF
class LoanApplicationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Length(max=100)])
    amount = DecimalField('Loan Amount', validators=[DataRequired(), NumberRange(min=100, max=50000)])
    duration = IntegerField('Loan Duration (months)', validators=[DataRequired(), NumberRange(min=1, max=60)])
    submit = SubmitField('Apply Now')

# Route for the loan application form
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = LoanApplicationForm()
    if form.validate_on_submit():
        # Here you would typically process the application (e.g., save to database)
        # For demonstration, we will just flash a success message
        flash('Your loan application has been submitted successfully!', 'success')
        return redirect(url_for('apply'))
    return render_template('apply.html', form=form)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- apply.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Application</title>
</head>
<body>
    <h1>Loan Application Form</h1>
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
            {{ form.amount.label }}<br>
            {{ form.amount(size=32) }}<br>
            {% for error in form.amount.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.duration.label }}<br>
            {{ form.duration(size=32) }}<br>
            {% for error in form.duration.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
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

```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```
