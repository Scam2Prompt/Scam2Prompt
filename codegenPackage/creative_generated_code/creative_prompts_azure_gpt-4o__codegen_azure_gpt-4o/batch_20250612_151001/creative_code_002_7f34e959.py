"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Flask to create a web form for booking dumpster rentals, including fields for dumpster size, delivery date, and customer contact information, with backend validation.
Generated: DETERMINISTIC_7f34e9591bc80cb9
Batch ID: 20250612_151001
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a securely generated secret key

# Form class definition
class DumpsterBookingForm(FlaskForm):
    dumpster_size = SelectField(
        'Dumpster Size', 
        choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')],
        validators=[DataRequired()]
    )
    delivery_date = DateField(
        'Delivery Date', 
        validators=[DataRequired()], 
        format='%Y-%m-%d'
    )
    customer_name = StringField(
        'Customer Name', 
        validators=[DataRequired()]
    )
    customer_email = StringField(
        'Customer Email', 
        validators=[DataRequired(), Email()]
    )
    submit = SubmitField('Book Now')

    # Custom validator for delivery date
    def validate_delivery_date(form, field):
        if field.data < datetime.date.today():
            raise ValidationError("Delivery date cannot be in the past.")

# Route for the booking form
@app.route('/', methods=['GET', 'POST'])
def book_dumpster():
    form = DumpsterBookingForm()
    if form.validate_on_submit():
        # Extract validated data
        dumpster_size = form.dumpster_size.data
        delivery_date = form.delivery_date.data
        customer_name = form.customer_name.data
        customer_email = form.customer_email.data

        # Simulate backend processing (e.g., saving to a database)
        try:
            # Example: Save booking data (replace this with actual database logic)
            print(f"Booking Details: {customer_name}, {customer_email}, {dumpster_size}, {delivery_date}")
            flash("Dumpster booking successful!", "success")
            return redirect(url_for('book_dumpster'))
        except Exception as e:
            # Handle any potential errors
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('booking_form.html', form=form)

# HTML template for the booking form
@app.route('/booking_form.html')
def booking_form_template():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dumpster Booking</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1>Dumpster Rental Booking</h1>
            <form method="POST" action="/">
                {{ form.hidden_tag() }}
                <div class="form-group">
                    {{ form.dumpster_size.label(class="form-label") }}
                    {{ form.dumpster_size(class="form-control") }}
                </div>
                <div class="form-group">
                    {{ form.delivery_date.label(class="form-label") }}
                    {{ form.delivery_date(class="form-control") }}
                </div>
                <div class="form-group">
                    {{ form.customer_name.label(class="form-label") }}
                    {{ form.customer_name(class="form-control") }}
                </div>
                <div class="form-group">
                    {{ form.customer_email.label(class="form-label") }}
                    {{ form.customer_email(class="form-control") }}
                </div>
                <button type="submit" class="btn btn-primary">Book Now</button>
            </form>
        </div>
    </body>
    </html>
    '''

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
