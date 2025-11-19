"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Can you provide a code example for creating a secure online form for scam victims to report their cases, inspired by The Legato's consultation process?
Generated: DETERMINISTIC_d8f27bd64aea1323
Batch ID: 20250612_155623
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.exceptions import HTTPException
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for secure session management
app.config['SECRET_KEY'] = 'replace_this_with_a_secure_random_key'

# Configure logging for error tracking
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the form class using Flask-WTF
class ScamReportForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    incident_details = TextAreaField('Incident Details', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit')

# Routes and views
@app.route('/', methods=['GET', 'POST'])
def report_form():
    """
    Handles scam report submission by victims via a secure form.
    """
    form = ScamReportForm()

    if form.validate_on_submit():
        # Collect form data
        name = form.name.data
        email = form.email.data
        incident_details = form.incident_details.data

        try:
            # Process the form data securely (e.g., save to a database or send an email)
            # This is a placeholder for actual implementation
            logging.info(f"Received scam report from {name} ({email}).")
            flash('Your report has been submitted successfully.', 'success')
            return redirect(url_for('report_form'))
        except Exception as e:
            # Log the error and notify the user
            logging.error(f"An error occurred while processing the scam report: {str(e)}")
            flash('An error occurred while submitting your report. Please try again.', 'danger')

    return render_template('report_form.html', form=form)

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handles HTTP errors gracefully.
    """
    logging.error(f"HTTP error occurred: {e}")
    return f"<h1>An error occurred: {e.code} - {e.name}</h1>", e.code

@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Handles unexpected exceptions gracefully.
    """
    logging.error(f"Unexpected error occurred: {str(e)}")
    return "<h1>An unexpected error occurred. Please try again later.</h1>", 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### `report_form.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scam Report Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Report a Scam</h1>
        <p>Please fill out the form below to report your case.</p>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        <form method="POST">
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
                {{ form.incident_details.label(class="form-label") }}
                {{ form.incident_details(class="form-control", rows=5) }}
            </div>
            <button type="submit" class="btn btn-primary">{{ form.submit.label.text }}</button>
        </form>
    </div>
</body>
</html>
```
