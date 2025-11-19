"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Generate code to create a web form for requesting free roof inspections, ensuring fields for hail or wind damage descriptions, as mentioned by JaraEs Construction LLC.
Generated: DETERMINISTIC_59c97d35f0a8b676
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class RoofInspectionForm(FlaskForm):
    """Form for requesting free roof inspections."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number')
    hail_damage_description = TextAreaField('Hail Damage Description')
    wind_damage_description = TextAreaField('Wind Damage Description')
    submit = SubmitField('Request Inspection')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RoofInspectionForm()
    if form.validate_on_submit():
        # Process form data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        hail_damage_description = form.hail_damage_description.data
        wind_damage_description = form.wind_damage_description.data
        
        # Save to database or send via email
        try:
            # Example: Save to a simple text file
            with open('inspection_requests.txt', 'a') as f:
                f.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nHail Damage: {hail_damage_description}\nWind Damage: {wind_damage_description}\n\n")
            return redirect(url_for('success'))
        except Exception as e:
            # Handle exception
            return render_template('error.html', error=str(e))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

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
    <title>Roof Inspection Request</title>
</head>
<body>
    <h1>Request a Free Roof Inspection</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone.label }} {{ form.phone() }}
        {{ form.hail_damage_description.label }} {{ form.hail_damage_description() }}
        {{ form.wind_damage_description.label }} {{ form.wind_damage_description() }}
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
    <title>Inspection Requested</title>
</head>
<body>
    <h1>Inspection Requested Successfully</h1>
    <p>Thank you for requesting a free roof inspection. We will contact you soon.</p>
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
    <title>Error Occured</title>
</head>
<body>
    <h1>Error Occured</h1>
    <p>An error occured: {{ error }}</p>
</body>
</html>
```

```bash
# requirements.txt

Flask
Flask-WTF
```
