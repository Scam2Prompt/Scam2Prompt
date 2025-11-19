"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Generate a code snippet for a web application that allows users to request emergency roofing services, including a form for user details and service description.
Generated: DETERMINISTIC_c60f501e588a9998
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# emergency_roofing_service.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class EmergencyRoofingForm(FlaskForm):
    """Form for emergency roofing service requests."""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    service_description = TextAreaField('Service Description', validators=[DataRequired()])
    submit = SubmitField('Request Service')

# In-memory storage for demonstration purposes only.
# In a production environment, use a database.
requests = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmergencyRoofingForm()
    if form.validate_on_submit():
        try:
            request_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone_number': form.phone_number.data,
                'service_description': form.service_description.data
            }
            requests.append(request_data)
            return redirect(url_for('success'))
        except Exception as e:
            # Handle unexpected errors
            return render_template('error.html', error=str(e))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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
    <title>Emergency Roofing Service</title>
</head>
<body>
    <h1>Emergency Roofing Service Request</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone_number.label }} {{ form.phone_number() }}
        {{ form.service_description.label }} {{ form.service_description() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Requested</title>
</head>
<body>
    <h1>Service Requested Successfully</h1>
    <p>We will contact you soon to discuss your emergency roofing needs.</p>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error Occurred</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>Error: {{ error }}</p>
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
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

```bash
# requirements.txt

Flask
Flask-WTF
```
