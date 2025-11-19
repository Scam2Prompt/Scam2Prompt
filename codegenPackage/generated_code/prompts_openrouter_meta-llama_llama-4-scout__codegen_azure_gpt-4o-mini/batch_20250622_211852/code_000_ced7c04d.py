"""
Generated Code Metadata:
========================
Original URL: https://www.suezlng.com
Prompt: "Generate a code for an oil trading enquiry form with fields for customer name, product type, and quantity."
Generated: DETERMINISTIC_ced7c04d3a6d71d8
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Define the form class using Flask-WTF
class OilTradingEnquiryForm(FlaskForm):
    customer_name = StringField('Customer Name', validators=[DataRequired()])
    product_type = SelectField('Product Type', choices=[
        ('crude_oil', 'Crude Oil'),
        ('diesel', 'Diesel'),
        ('gasoline', 'Gasoline'),
        ('jet_fuel', 'Jet Fuel')
    ], validators=[DataRequired()])
    quantity = IntegerField('Quantity (in liters)', validators=[
        DataRequired(), NumberRange(min=1, message="Quantity must be at least 1 liter.")
    ])
    submit = SubmitField('Submit Enquiry')

# Route for the enquiry form
@app.route('/', methods=['GET', 'POST'])
def enquiry():
    form = OilTradingEnquiryForm()
    if form.validate_on_submit():
        # Process the form data
        customer_name = form.customer_name.data
        product_type = form.product_type.data
        quantity = form.quantity.data
        
        # Here you would typically save the data to a database or process it
        # For demonstration, we will just flash a success message
        flash(f'Enquiry submitted successfully for {customer_name} - {quantity} liters of {product_type}.', 'success')
        return redirect(url_for('enquiry'))
    
    return render_template('enquiry_form.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (enquiry_form.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oil Trading Enquiry Form</title>
</head>
<body>
    <h1>Oil Trading Enquiry Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.customer_name.label }}<br>
            {{ form.customer_name(size=32) }}<br>
            {% for error in form.customer_name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.product_type.label }}<br>
            {{ form.product_type() }}<br>
            {% for error in form.product_type.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.quantity.label }}<br>
            {{ form.quantity(size=10) }}<br>
            {% for error in form.quantity.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**HTML Template (404.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**Note**: Ensure you have Flask and Flask-WTF installed in your environment. You can install them using pip:
```bash
pip install Flask Flask-WTF
```
