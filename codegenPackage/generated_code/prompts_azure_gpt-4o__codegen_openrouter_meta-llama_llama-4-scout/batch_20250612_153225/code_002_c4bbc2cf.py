"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Generate code to create a web form for vehicle renting inquiries, including fields for personal/business details, vehicle preferences, and contact information, as described on the Innova Renting website.
Generated: DETERMINISTIC_c4bbc2cf3f0a64f2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class VehicleInquiryForm(FlaskForm):
    """Form for vehicle renting inquiries."""
    
    # Personal/ Business Details
    title = SelectField('Title', choices=['Mr', 'Ms', 'Mrs', 'Dr', 'Other'], validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    company_name = StringField('Company Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])

    # Vehicle Preferences
    vehicle_type = SelectField('Vehicle Type', choices=['Sedan', 'SUV', 'Truck', 'Van', 'Other'], validators=[DataRequired()])
    pickup_location = StringField('Pickup Location', validators=[DataRequired()])
    pickup_date = DateField('Pickup Date', validators=[DataRequired()])
    return_date = DateField('Return Date', validators=[DataRequired()])
    driver_age = IntegerField('Driver Age', validators=[DataRequired()])

    # Additional Information
    additional_info = StringField('Additional Information')

    submit = SubmitField('Submit Inquiry')

@app.route('/inquiry', methods=['GET', 'POST'])
def vehicle_inquiry():
    form = VehicleInquiryForm()
    if form.validate_on_submit():
        # Process form data
        title = form.title.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        company_name = form.company_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        vehicle_type = form.vehicle_type.data
        pickup_location = form.pickup_location.data
        pickup_date = form.pickup_date.data
        return_date = form.return_date.data
        driver_age = form.driver_age.data
        additional_info = form.additional_info.data
        
        # Save to database or send email
        # For demonstration purposes, just print the data
        print("Inquiry Details:")
        print(f"Title: {title}")
        print(f"Name: {first_name} {last_name}")
        print(f"Company: {company_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone_number}")
        print(f"Vehicle Type: {vehicle_type}")
        print(f"Pickup Location: {pickup_location}")
        print(f"Pickup Date: {pickup_date}")
        print(f"Return Date: {return_date}")
        print(f"Driver Age: {driver_age}")
        print(f"Additional Info: {additional_info}")
        
        return redirect(url_for('success'))
    return render_template('inquiry.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/inquiry.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Renting Inquiry</title>
</head>
<body>
    <h1>Vehicle Renting Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        
        <p>
            {{ form.title.label }}<br>
            {{ form.title() }}
        </p>
        <p>
            {{ form.first_name.label }}<br>
            {{ form.first_name() }}
        </p>
        <p>
            {{ form.last_name.label }}<br>
            {{ form.last_name() }}
        </p>
        <p>
            {{ form.company_name.label }}<br>
            {{ form.company_name() }}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email() }}
        </p>
        <p>
            {{ form.phone_number.label }}<br>
            {{ form.phone_number() }}
        </p>
        
        <p>
            {{ form.vehicle_type.label }}<br>
            {{ form.vehicle_type() }}
        </p>
        <p>
            {{ form.pickup_location.label }}<br>
            {{ form.pickup_location() }}
        </p>
        <p>
            {{ form.pickup_date.label }}<br>
            {{ form.pickup_date() }}
        </p>
        <p>
            {{ form.return_date.label }}<br>
            {{ form.return_date() }}
        </p>
        <p>
            {{ form.driver_age.label }}<br>
            {{ form.driver_age() }}
        </p>
        
        <p>
            {{ form.additional_info.label }}<br>
            {{ form.additional_info() }}
        </p>
        
        <p>{{ form.submit() }}</p>
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
    <title>Inquiry Submitted</title>
</head>
<body>
    <h1>Inquiry Submitted Successfully</h1>
    <p>Thank you for submitting your inquiry. We will contact you soon.</p>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-WTF
WTForms
```
