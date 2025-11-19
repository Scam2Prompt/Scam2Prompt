"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Generate a code snippet for a travel consultancy website that showcases services like DMCC, MICE & Tourism Safaris, and Study Abroad facilitations.
Generated: DETERMINISTIC_76a0ee0e37ee45c1
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_consultancy.py

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define services offered by the consultancy
SERVICES = {
    'DMCC': 'Dubai Multi Commodities Centre',
    'MICE': 'Meetings, Incentives, Conferences, and Exhibitions',
    'Tourism_Safaris': 'Customized tourism safaris',
    'Study_Abroad': 'Study abroad facilitations'
}

# Define a form for user inquiries
class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    service = StringField('Service of Interest', validators=[DataRequired()])
    message = StringField('Message')
    submit = SubmitField('Submit Inquiry')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)

# Route for service pages
@app.route('/services/<service>')
def service_page(service):
    if service in SERVICES:
        return render_template(f'{service}.html', service=SERVICES[service])
    else:
        return 'Service not found', 404

# Route for inquiries
@app.route('/inquiry', methods=['GET', 'POST'])
def inquiry():
    form = InquiryForm()
    if form.validate_on_submit():
        # Handle form submission (e.g., send an email)
        try:
            # Simulating email sending
            print('Inquiry submitted:')
            print(f'Name: {form.name.data}')
            print(f'Email: {form.email.data}')
            print(f'Service: {form.service.data}')
            print(f'Message: {form.message.data}')
            return 'Inquiry submitted successfully!'
        except Exception as e:
            return 'Error submitting inquiry', 500
    return render_template('inquiry.html', form=form)

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
    <title>Travel Consultancy</title>
</head>
<body>
    <h1>Travel Consultancy Services</h1>
    <ul>
    {% for service, description in services.items() %}
        <li><a href="{{ url_for('service_page', service=service) }}">{{ service }} - {{ description }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('inquiry') }}">Submit an Inquiry</a></p>
</body>
</html>
```

```html
<!-- templates/inquiry.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Inquiry</title>
</head>
<body>
    <h1>Submit an Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.service.label }} {{ form.service() }}
        {{ form.message.label }} {{ form.message() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/DMCC.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DMCC</title>
</head>
<body>
    <h1>{{ service }}</h1>
    <p>Information about DMCC...</p>
</body>
</html>
```

```html
<!-- templates/MICE.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MICE</title>
</head>
<body>
    <h1>{{ service }}</h1>
    <p>Information about MICE...</p>
</body>
</html>
```

```html
<!-- templates/Tourism_Safaris.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tourism Safaris</title>
</head>
<body>
    <h1>{{ service }}</h1>
    <p>Information about Tourism Safaris...</p>
</body>
</html>
```

```html
<!-- templates/Study_Abroad.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Study Abroad</title>
</head>
<body>
    <h1>{{ service }}</h1>
    <p>Information about Study Abroad...</p>
</body>
</html>
```
