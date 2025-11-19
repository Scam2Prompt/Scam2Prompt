"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Flask to create a web form for booking dumpster rentals, including fields for dumpster size, delivery date, and customer contact information, with backend validation.
Generated: DETERMINISTIC_7f34e9591bc80cb9
Batch ID: 20250612_151001
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/dumpster_rental`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, validators
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class DumpsterRentalForm(FlaskForm):
    """Form for booking dumpster rentals."""
    
    # Dumpster size options
    dumpster_sizes = [
        ('10', '10 Yard Dumpster'),
        ('20', '20 Yard Dumpster'),
        ('30', '30 Yard Dumpster'),
        ('40', '40 Yard Dumpster')
    ]

    # Form fields
    dumpster_size = SelectField('Dumpster Size', choices=dumpster_sizes, validators=[DataRequired()])
    delivery_date = DateField('Delivery Date', validators=[DataRequired()])
    customer_name = StringField('Customer Name', validators=[DataRequired(), Length(min=2, max=50)])
    customer_email = StringField('Customer Email', validators=[DataRequired(), Email()])
    customer_phone = StringField('Customer Phone', validators=[DataRequired(), Length(min=10, max=15)])

@app.route('/dumpster_rental', methods=['GET', 'POST'])
def dumpster_rental():
    """Handle dumpster rental form submission."""
    
    form = DumpsterRentalForm()
    
    if form.validate_on_submit():
        # Get form data
        dumpster_size = form.dumpster_size.data
        delivery_date = form.delivery_date.data
        customer_name = form.customer_name.data
        customer_email = form.customer_email.data
        customer_phone = form.customer_phone.data
        
        # Save data to database or send confirmation email (example)
        try:
            # Example: Save to database
            print("Dumpster Rental Request:")
            print(f"Size: {dumpster_size}")
            print(f"Delivery Date: {delivery_date}")
            print(f"Customer Name: {customer_name}")
            print(f"Customer Email: {customer_email}")
            print(f"Customer Phone: {customer_phone}")
            
            # Redirect to success page
            return redirect(url_for('success'))
        except Exception as e:
            # Handle database or email errors
            form.dumpster_size.errors.append('Error processing request. Please try again.')
    
    return render_template('dumpster_rental.html', form=form)

@app.route('/success')
def success():
    """Render success page."""
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/dumpster_rental.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dumpster Rental Form</title>
</head>
<body>
    <h1>Dumpster Rental Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.dumpster_size.label }} {{ form.dumpster_size() }}
        {{ form.delivery_date.label }} {{ form.delivery_date() }}
        {{ form.customer_name.label }} {{ form.customer_name() }}
        {{ form.customer_email.label }} {{ form.customer_email() }}
        {{ form.customer_phone.label }} {{ form.customer_phone() }}
        <input type="submit" value="Submit">
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
    <title>Dumpster Rental Success</title>
</head>
<body>
    <h1>Dumpster Rental Request Successful!</h1>
    <p>Thank you for submitting your dumpster rental request. We will contact you soon.</p>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-WTF
WTForms
```

To run the application:

1. Install dependencies: `pip install -r requirements.txt`
2. Create a new file named `app.py` and paste the provided Python code.
3. Create a new directory named `templates` and add `dumpster_rental.html` and `success.html` files with the provided HTML code.
4. Run the application: `python app.py`
5. Open a web browser and navigate to `http://localhost:5000/dumpster_rental` to access the dumpster rental form.
