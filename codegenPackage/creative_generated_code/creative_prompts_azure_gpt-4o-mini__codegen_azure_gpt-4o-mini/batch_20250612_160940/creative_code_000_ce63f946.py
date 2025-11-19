"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apipoocoin-tk.blogspot.com
Prompt: Generate a reservation form for a vacation rental at Toca do Caranguejo, including details about the Casa Guaiamum and its amenities.
Generated: DETERMINISTIC_ce63f946d8542f3a
Batch ID: 20250612_160940
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
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key

class ReservationForm(FlaskForm):
    """Form for booking a reservation."""
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email Address', validators=[DataRequired(), Length(max=100)])
    check_in = DateField('Check-in Date', format='%Y-%m-%d', validators=[DataRequired()])
    check_out = DateField('Check-out Date', format='%Y-%m-%d', validators=[DataRequired()])
    guests = IntegerField('Number of Guests', validators=[DataRequired(), NumberRange(min=1, max=10)])
    amenities = SelectField('Select Amenities', choices=[('wifi', 'Wi-Fi'), ('pool', 'Swimming Pool'), ('parking', 'Parking')],
                            validators=[DataRequired()])
    submit = SubmitField('Book Now')

@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the reservation form and handle form submission."""
    form = ReservationForm()
    if form.validate_on_submit():
        # Log the reservation details
        logging.info(f'Reservation made for {form.name.data} from {form.check_in.data} to {form.check_out.data}.')
        flash('Reservation successfully submitted!', 'success')
        return redirect(url_for('home'))

    return render_template('reservation_form.html', form=form)

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Enable debug mode for development
    except Exception as e:
        logging.error(f'Error starting the application: {e}')
```

**HTML Template (reservation_form.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reservation Form - Toca do Caranguejo</title>
</head>
<body>
    <h1>Reservation Form for Casa Guaiamum</h1>
    <p>Welcome to Toca do Caranguejo! Please fill out the form below to reserve your stay at Casa Guaiamum.</p>
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
            {{ form.check_in.label }}<br>
            {{ form.check_in() }}<br>
            {% for error in form.check_in.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.check_out.label }}<br>
            {{ form.check_out() }}<br>
            {% for error in form.check_out.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.guests.label }}<br>
            {{ form.guests(size=2) }}<br>
            {% for error in form.guests.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.amenities.label }}<br>
            {{ form.amenities() }}<br>
            {% for error in form.amenities.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
</body>
</html>
```
