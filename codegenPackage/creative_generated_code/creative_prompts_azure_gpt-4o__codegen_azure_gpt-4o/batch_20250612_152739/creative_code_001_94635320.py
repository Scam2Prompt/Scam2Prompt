"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Generate code to create a web form for requesting a callback from Suzuki Capital Motors, including fields for customer name, contact information, and car model.
Generated: DETERMINISTIC_94635320ac501714
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
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
from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, SelectField, validators
import re

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a proper secret key for production

# Define a WTForms form for the callback request
class CallbackRequestForm(Form):
    name = StringField('Customer Name', [
        validators.DataRequired(),
        validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
    ])
    contact = StringField('Contact Information', [
        validators.DataRequired(),
        validators.Regexp(r'^\+?\d{10,15}$', message="Enter a valid contact number (e.g., +1234567890).")
    ])
    car_model = SelectField('Car Model', [
        validators.DataRequired()
    ], choices=[
        ('', 'Select a model'),
        ('Swift', 'Swift'),
        ('Vitara', 'Vitara'),
        ('Ciaz', 'Ciaz'),
        ('Alto', 'Alto'),
        ('Ertiga', 'Ertiga')
    ])

# Route to display the form
@app.route('/', methods=['GET', 'POST'])
def callback_request():
    form = CallbackRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Extract form data
            name = form.name.data
            contact = form.contact.data
            car_model = form.car_model.data

            # Simulate saving to a database or processing the request
            # In production, replace this with actual database logic or API calls
            flash(f"Callback request submitted successfully for {name}.", 'success')
            
            # Redirect to a success page or reload the form
            return redirect(url_for('callback_request'))
        except Exception as e:
            # Handle unexpected errors gracefully
            flash(f"An error occurred: {str(e)}", 'danger')

    # Render the form template
    return render_template('callback_form.html', form=form)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this HTML file as 'templates/callback_form.html' -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Callback Request - Suzuki Capital Motors</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Request a Callback</h1>
        <form method="POST" action="/">
            <!-- Display success/error messages -->
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    <div class="mt-3">
                        {% for category, message in messages %}
                            <div class="alert alert-{{ category }}">{{ message }}</div>
                        {% endfor %}
                    </div>
                {% endif %}
            {% endwith %}

            <!-- Customer Name -->
            <div class="mb-3">
                <label for="name" class="form-label">Customer Name</label>
                <input type="text" name="name" id="name" class="form-control" value="{{ form.name.data }}">
                {% if form.name.errors %}
                    <div class="text-danger mt-1">
                        {{ form.name.errors[0] }}
                    </div>
                {% endif %}
            </div>

            <!-- Contact Information -->
            <div class="mb-3">
                <label for="contact" class="form-label">Contact Information</label>
                <input type="text" name="contact" id="contact" class="form-control" value="{{ form.contact.data }}">
                {% if form.contact.errors %}
                    <div class="text-danger mt-1">
                        {{ form.contact.errors[0] }}
                    </div>
                {% endif %}
            </div>

            <!-- Car Model -->
            <div class="mb-3">
                <label for="car_model" class="form-label">Car Model</label>
                <select name="car_model" id="car_model" class="form-select">
                    {% for value, label in form.car_model.choices %}
                        <option value="{{ value }}" {% if form.car_model.data == value %}selected{% endif %}>{{ label }}</option>
                    {% endfor %}
                </select>
                {% if form.car_model.errors %}
                    <div class="text-danger mt-1">
                        {{ form.car_model.errors[0] }}
                    </div>
                {% endif %}
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```
