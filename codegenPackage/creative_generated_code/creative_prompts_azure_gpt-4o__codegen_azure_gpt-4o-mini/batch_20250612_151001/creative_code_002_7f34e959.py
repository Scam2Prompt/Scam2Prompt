"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Flask to create a web form for booking dumpster rentals, including fields for dumpster size, delivery date, and customer contact information, with backend validation.
Generated: DETERMINISTIC_7f34e9591bc80cb9
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

# Define the form using Flask-WTF
class DumpsterRentalForm(FlaskForm):
    dumpster_size = SelectField(
        'Dumpster Size',
        choices=[('10', '10 Yard'), ('20', '20 Yard'), ('30', '30 Yard')],
        validators=[DataRequired()]
    )
    delivery_date = DateField(
        'Delivery Date',
        format='%Y-%m-%d',
        validators=[DataRequired()]
    )
    contact_name = StringField(
        'Contact Name',
        validators=[DataRequired(), Length(max=50)]
    )
    contact_email = StringField(
        'Contact Email',
        validators=[DataRequired(), Email()]
    )
    submit = SubmitField('Book Rental')

@app.route('/', methods=['GET', 'POST'])
def book_rental():
    form = DumpsterRentalForm()
    
    if form.validate_on_submit():
        # Process the form data
        dumpster_size = form.dumpster_size.data
        delivery_date = form.delivery_date.data
        contact_name = form.contact_name.data
        contact_email = form.contact_email.data

        # Here you would typically save the data to a database
        # For demonstration, we will flash a success message
        flash('Your dumpster rental has been booked successfully!', 'success')
        return redirect(url_for('book_rental'))

    return render_template('booking_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/booking_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Dumpster Rental</title>
</head>
<body>
    <h1>Book Your Dumpster Rental</h1>
    
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul class=flashes>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.dumpster_size.label }}<br>
            {{ form.dumpster_size() }}<br>
            {% for error in form.dumpster_size.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.delivery_date.label }}<br>
            {{ form.delivery_date() }}<br>
            {% for error in form.delivery_date.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.contact_name.label }}<br>
            {{ form.contact_name(size=32) }}<br>
            {% for error in form.contact_name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.contact_email.label }}<br>
            {{ form.contact_email(size=32) }}<br>
            {% for error in form.contact_email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
    </form>
</body>
</html>
```

### Requirements
Make sure to install the necessary packages before running the application:
```bash
pip install Flask Flask-WTF
```
