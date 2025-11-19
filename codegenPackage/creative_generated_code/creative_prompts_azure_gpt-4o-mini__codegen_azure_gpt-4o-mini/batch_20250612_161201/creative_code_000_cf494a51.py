"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for UPVC window and door systems, similar to the functionality on the DEXODOOR website.
Generated: DETERMINISTIC_cf494a51cfcf3598
Batch ID: 20250612_161201
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# Flask web application to request a quote for UPVC window and door systems

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
import logging

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Configure logging
logging.basicConfig(level=logging.INFO)

# Form class to handle quote request
class QuoteRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15)])
    details = TextAreaField('Details', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Request Quote')

@app.route('/', methods=['GET', 'POST'])
def request_quote():
    """Render the quote request form and handle submission."""
    form = QuoteRequestForm()
    
    if form.validate_on_submit():
        # Process the form data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        details = form.details.data
        
        try:
            # Here you would typically send the details to a database or an email service
            logging.info(f"Quote requested by {name}: Email: {email}, Phone: {phone}, Details: {details}")
            flash('Your quote request has been submitted successfully!', 'success')
            return redirect(url_for('request_quote'))
        except Exception as e:
            logging.error(f"Error processing quote request: {e}")
            flash('There was an issue submitting your quote request. Please try again.', 'error')

    return render_template('request_quote.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode for development
```

`request_quote.html` (HTML Template):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Quote</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Request a Quote for UPVC Window and Door Systems</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="alert alert-dismissible fade show" role="alert">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
        <form method="POST" novalidate>
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.phone.label(class="form-label") }}
                {{ form.phone(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.details.label(class="form-label") }}
                {{ form.details(class="form-control", rows=4) }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```

Make sure to install Flask and Flask-WTF to run this application:

```bash
pip install Flask Flask-WTF
```
