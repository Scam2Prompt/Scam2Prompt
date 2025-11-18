"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Write code to design a user-friendly interface for submitting property rental or sale requests, including fields for transaction type, property type, and contact details, similar to the "Consigna tu inmueble" form on Félix Trujillo Falla's website.
Generated: DETERMINISTIC_e56ca8ce6dbb9c36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key

# Define a form class using Flask-WTF
class PropertyRequestForm(FlaskForm):
    transaction_type = SelectField('Transaction Type', choices=[('rent', 'Rent'), ('sale', 'Sale')], validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('apartment', 'Apartment'), ('house', 'House'), ('commercial', 'Commercial')], validators=[DataRequired()])
    contact_name = StringField('Your Name', validators=[DataRequired()])
    contact_email = EmailField('Your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit Request')

# Route to display the form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PropertyRequestForm()
    if form.validate_on_submit():
        # Here you would typically save the data to a database or send an email
        flash('Your request has been submitted successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

# Error handling for the application
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Rental/Sale Request</title>
</head>
<body>
    <h1>Submit Your Property Request</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.transaction_type.label }}: {{ form.transaction_type() }}
        </div>
        <div>
            {{ form.property_type.label }}: {{ form.property_type() }}
        </div>
        <div>
            {{ form.contact_name.label }}: {{ form.contact_name(size=32) }}
        </div>
        <div>
            {{ form.contact_email.label }}: {{ form.contact_email(size=32) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
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
    <p>The page you are looking for does not exist.</p>
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
    <p>Something went wrong. Please try again later.</p>
</body>
</html>
```
