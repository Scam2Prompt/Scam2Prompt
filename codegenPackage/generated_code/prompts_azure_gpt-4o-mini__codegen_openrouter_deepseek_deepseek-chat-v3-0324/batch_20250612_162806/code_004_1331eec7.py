"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.network
Prompt: Develop a simple web application that allows users to schedule a consultation for paving services, reflecting the user-friendly approach seen on Bedford Paving's website.
Generated: DETERMINISTIC_1331eec7226c311c
Batch ID: 20250612_162806
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css": {
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
  }
}
"""

# Generated Code:
# ===============

# Consultation Scheduler for Paving Services

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime, date
import logging
from logging.handlers import RotatingFileHandler
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-dev')

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.setLevel(logging.INFO)

# Service options
SERVICE_CHOICES = [
    ('residential', 'Residential Paving'),
    ('commercial', 'Commercial Paving'),
    ('driveway', 'Driveway Installation'),
    ('repair', 'Paving Repair'),
    ('other', 'Other Services')
]

# Time slot options
TIME_SLOTS = [
    ('09:00-11:00', 'Morning (9:00 AM - 11:00 AM)'),
    ('11:00-13:00', 'Late Morning (11:00 AM - 1:00 PM)'),
    ('13:00-15:00', 'Early Afternoon (1:00 PM - 3:00 PM)'),
    ('15:00-17:00', 'Late Afternoon (3:00 PM - 5:00 PM)')
]

class ConsultationForm(FlaskForm):
    """Form for scheduling a paving consultation."""

    # Personal information
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    address = StringField('Property Address', validators=[DataRequired(), Length(min=5, max=100)])

    # Service details
    service_type = SelectField('Service Needed', 
                             choices=SERVICE_CHOICES,
                             validators=[DataRequired()])
    date_preference = DateField('Preferred Date', 
                              format='%Y-%m-%d',
                              validators=[DataRequired()])
    time_preference = SelectField('Preferred Time Slot',
                                choices=TIME_SLOTS,
                                validators=[DataRequired()])
    message = TextAreaField('Additional Information',
                          validators=[Length(max=500)])

    def validate_date_preference(self, field):
        """Ensure date is not in the past."""
        if field.data < date.today():
            raise ValueError("Please select a date in the future.")

@app.route('/', methods=['GET', 'POST'])
def home():
    """Handle the consultation scheduling form."""
    form = ConsultationForm()

    if form.validate_on_submit():
        try:
            # Process the form data (in a real app, this would save to a database)
            data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'address': form.address.data,
                'service_type': form.service_type.data,
                'date_preference': form.date_preference.data.strftime('%Y-%m-%d'),
                'time_preference': form.time_preference.data,
                'message': form.message.data,
                'submission_time': datetime.now().isoformat()
            }

            app.logger.info(f"New consultation request: {data}")

            # In a production environment, you would:
            # 1. Save to database
            # 2. Send confirmation email
            # 3. Notify staff

            # For this example, we'll just flash a success message
            flash('Your consultation request has been submitted successfully! We will contact you shortly.', 'success')
            return redirect(url_for('confirmation'))
        except Exception as e:
            app.logger.error(f"Error processing form: {str(e)}")
            flash('An error occurred while processing your request. Please try again.', 'danger')

    return render_template('home.html', form=form, current_year=datetime.now().year)

@app.route('/confirmation')
def confirmation():
    """Show confirmation page after successful submission."""
    return render_template('confirmation.html', current_year=datetime.now().year)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Bedford Paving Consultation{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
        }
        .navbar {
            background-color: #1a3e72;
        }
        .btn-primary {
            background-color: #1a3e72;
            border-color: #1a3e72;
        }
        .footer {
            background-color: #343a40;
            color: white;
            padding: 20px 0;
            margin-top: 50px;
        }
        .service-card {
            transition: transform 0.3s;
        }
        .service-card:hover {
            transform: translateY(-5px);
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Bedford Paving</a>
        </div>
    </nav>

    <!-- Main content -->
    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}
        {% endblock %}
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container text-center">
            <p>&copy; {{ current_year }} Bedford Paving. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Schedule a Consultation{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow">
            <div class="card-header bg-dark text-white">
                <h3 class="mb-0">Schedule Your Paving Consultation</h3>
                <p class="mb-0">Complete the form below and we'll contact you to confirm your appointment.</p>
            </div>
            <div class="card-body">
                <form method="POST" action="{{ url_for('home') }}">
                    {{ form.hidden_tag() }}
                    
                    <h5 class="card-title">Contact Information</h5>
                    <div class="form-group">
                        {{ form.name.label(class="font-weight-bold") }}
                        {{ form.name(class="form-control", placeholder="Your full name") }}
                        {% if form.name.errors %}
                            <div class="invalid-feedback d-block">
                                {{ form.name.errors[0] }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group col-md-6">
                            {{ form.email.label(class="font-weight-bold") }}
                            {{ form.email(class="form-control", placeholder="your@email.com") }}
                            {% if form
