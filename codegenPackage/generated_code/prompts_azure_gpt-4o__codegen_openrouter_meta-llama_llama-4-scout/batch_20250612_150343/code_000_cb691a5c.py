"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Write a Python script to create a web form for customers to request services like "window and door installation" or "bathroom updating" from Winger R&R, including fields for name, contact information, and service type.
Generated: DETERMINISTIC_cb691a5c23ccd0bb
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define a form class for the service request form
class ServiceRequestForm(FlaskForm):
    """Service Request Form"""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    service_type = SelectField('Service Type', 
                               choices=[
                                   ('window_door_installation', 'Window and Door Installation'),
                                   ('bathroom_updating', 'Bathroom Updating'),
                                   ('other', 'Other (please specify)')
                               ], 
                               validators=[DataRequired()])
    other_service_type = StringField('Other Service Type (if applicable)')
    submit = SubmitField('Submit Request')

# Define a route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    """Index Page"""
    form = ServiceRequestForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        service_type = form.service_type.data
        other_service_type = form.other_service_type.data

        # Save the request to a file or database
        with open('service_requests.txt', 'a') as f:
            f.write(f'Name: {name}\nEmail: {email}\nPhone: {phone}\nService Type: {service_type}\n')
            if other_service_type:
                f.write(f'Other Service Type: {other_service_type}\n')
            f.write('------------------------\n')

        return redirect(url_for('success'))
    return render_template('index.html', form=form)

# Define a route for the success page
@app.route('/success')
def success():
    """Success Page"""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Winger R&R Service Request</title>
</head>
<body>
    <h1>Winger R&R Service Request</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone.label }} {{ form.phone() }}
        {{ form.service_type.label }} {{ form.service_type() }}
        {% if form.other_service_type %}
            {{ form.other_service_type.label }} {{ form.other_service_type() }}
        {% endif %}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Winger R&R Service Request Success</title>
</head>
<body>
    <h1>Service Request Submitted Successfully!</h1>
    <p>Thank you for submitting your service request. We will contact you soon.</p>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-WTF
```
