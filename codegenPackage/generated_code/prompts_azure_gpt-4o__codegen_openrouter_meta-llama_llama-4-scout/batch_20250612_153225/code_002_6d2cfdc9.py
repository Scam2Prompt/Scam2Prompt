"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Generate code to create a web form for scheduling a polygraph test appointment, including fields for selecting test types like fidelity tests, fraud investigations, or legal cases, as mentioned on the Euro Poligraf Center website.
Generated: DETERMINISTIC_6d2cfdc93e535d25
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
from wtforms import StringField, SelectField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class PolygraphTestForm(FlaskForm):
    """Form for scheduling a polygraph test appointment"""
    test_types = [
        ('fidelity_test', 'Fidelity Test'),
        ('fraud_investigation', 'Fraud Investigation'),
        ('legal_case', 'Legal Case'),
        ('pre_employment_screening', 'Pre-Employment Screening'),
        ('other', 'Other (please specify)')
    ]

    test_type = SelectField('Test Type', choices=test_types, validators=[DataRequired()])
    test_date = DateField('Test Date', validators=[DataRequired()])
    test_time = TimeField('Test Time', validators=[DataRequired()])
    client_name = StringField('Client Name', validators=[DataRequired()])
    client_email = StringField('Client Email', validators=[DataRequired()])
    additional_info = StringField('Additional Information')
    submit = SubmitField('Schedule Appointment')

@app.route('/schedule_test', methods=['GET', 'POST'])
def schedule_test():
    form = PolygraphTestForm()
    if form.validate_on_submit():
        test_type = form.test_type.data
        test_date = form.test_date.data
        test_time = form.test_time.data
        client_name = form.client_name.data
        client_email = form.client_email.data
        additional_info = form.additional_info.data

        # Save the appointment to the database or send a confirmation email
        try:
            # For demonstration purposes, just print the appointment details
            print("Appointment Scheduled:")
            print(f"Test Type: {test_type}")
            print(f"Test Date: {test_date}")
            print(f"Test Time: {test_time}")
            print(f"Client Name: {client_name}")
            print(f"Client Email: {client_email}")
            print(f"Additional Info: {additional_info}")

            return redirect(url_for('appointment_scheduled'))
        except Exception as e:
            # Handle any errors that occur during appointment scheduling
            form.test_type.errors.append('Error scheduling appointment: ' + str(e))

    return render_template('schedule_test.html', form=form)

@app.route('/appointment_scheduled')
def appointment_scheduled():
    return render_template('appointment_scheduled.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/schedule_test.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Polygraph Test Appointment</title>
</head>
<body>
    <h1>Schedule Polygraph Test Appointment</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.test_type.label }} {{ form.test_type() }}
        {{ form.test_date.label }} {{ form.test_date() }}
        {{ form.test_time.label }} {{ form.test_time() }}
        {{ form.client_name.label }} {{ form.client_name() }}
        {{ form.client_email.label }} {{ form.client_email() }}
        {{ form.additional_info.label }} {{ form.additional_info() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/appointment_scheduled.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Scheduled</title>
</head>
<body>
    <h1>Appointment Scheduled</h1>
    <p>Your polygraph test appointment has been scheduled successfully.</p>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-WTF
```
