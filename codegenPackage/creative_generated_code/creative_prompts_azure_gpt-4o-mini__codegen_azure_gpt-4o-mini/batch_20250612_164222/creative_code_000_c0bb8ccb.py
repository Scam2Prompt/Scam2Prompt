"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Generate a code snippet for a web application that allows users to schedule a free consultation with Hispanic Services for immigration and tax assistance.
Generated: DETERMINISTIC_c0bb8ccb720077d6
Batch ID: 20250612_164222
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
from wtforms import StringField, EmailField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a form for scheduling consultations
class ConsultationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Schedule Consultation')

# Route for the main scheduling page
@app.route('/', methods=['GET', 'POST'])
def schedule():
    form = ConsultationForm()
    if form.validate_on_submit():
        try:
            # Here you would typically save the data to a database
            # For demonstration, we're just logging the information
            logging.info(f"Consultation scheduled: {form.name.data}, {form.email.data},"
                         f" {form.date.data}, {form.time.data}")
            flash('Your consultation has been scheduled successfully!', 'success')
            return redirect(url_for('schedule'))
        except Exception as e:
            logging.error(f"Error scheduling consultation: {e}")
            flash('An error occurred while scheduling your consultation. Please try again.', 'danger')
    
    return render_template('schedule.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug in a production environment
```

**HTML Template (`schedule.html`):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Schedule Consultation</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h1>Schedule a Free Consultation</h1>
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
            {{ form.date.label(class="form-label") }}
            {{ form.date(class="form-control") }}
        </div>
        <div class="form-group">
            {{ form.time.label(class="form-label") }}
            {{ form.time(class="form-control") }}
        </div>
        {{ form.submit(class="btn btn-primary") }}
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="alert alert-info mt-3">
                {% for message in messages %}
                    {{ message }}
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

**Note**: Ensure to set up a proper web server and database connection for production use, and replace `'your_secret_key'` with a secure key.
