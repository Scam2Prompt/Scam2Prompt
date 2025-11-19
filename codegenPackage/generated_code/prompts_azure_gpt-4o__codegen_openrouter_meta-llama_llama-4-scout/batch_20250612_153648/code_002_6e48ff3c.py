"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate code to create a web-based form for business inquiries, ensuring fields for project details, client contact information, and service selection, as described on the Remas Engineering Consultants website.
Generated: DETERMINISTIC_6e48ff3c92a098dc
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class BusinessInquiryForm(FlaskForm):
    """Form for business inquiries."""
    
    # Project details
    project_name = StringField('Project Name', validators=[DataRequired()])
    project_description = TextAreaField('Project Description', validators=[DataRequired()])
    
    # Client contact information
    client_name = StringField('Client Name', validators=[DataRequired()])
    client_email = StringField('Client Email', validators=[DataRequired(), Email()])
    client_phone = StringField('Client Phone', validators=[DataRequired()])
    
    # Service selection
    services = SelectField('Services Required', choices=[
        ('structural_engineering', 'Structural Engineering'),
        ('geotechnical_engineering', 'Geotechnical Engineering'),
        ('environmental_consulting', 'Environmental Consulting'),
        ('other', 'Other (please specify)')
    ])
    other_services = StringField('Other Services (if selected)')
    
    submit = SubmitField('Submit Inquiry')

@app.route('/inquiry', methods=['GET', 'POST'])
def inquiry():
    form = BusinessInquiryForm()
    
    if form.validate_on_submit():
        project_name = form.project_name.data
        project_description = form.project_description.data
        client_name = form.client_name.data
        client_email = form.client_email.data
        client_phone = form.client_phone.data
        services = form.services.data
        other_services = form.other_services.data
        
        # Here you would typically send an email or store the inquiry in a database
        # For demonstration purposes, we'll just print the data
        print("Inquiry Received:")
        print(f"Project Name: {project_name}")
        print(f"Project Description: {project_description}")
        print(f"Client Name: {client_name}")
        print(f"Client Email: {client_email}")
        print(f"Client Phone: {client_phone}")
        print(f"Services: {services}")
        if services == 'other':
            print(f"Other Services: {other_services}")
        
        return redirect(url_for('inquiry_success'))
    
    return render_template('inquiry.html', form=form)

@app.route('/inquiry_success')
def inquiry_success():
    return render_template('inquiry_success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/inquiry.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Inquiry</title>
</head>
<body>
    <h1>Business Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        
        <p>
            {{ form.project_name.label }}<br>
            {{ form.project_name(size=64) }}
        </p>
        <p>
            {{ form.project_description.label }}<br>
            {{ form.project_description(rows=10, cols=40) }}
        </p>
        <p>
            {{ form.client_name.label }}<br>
            {{ form.client_name(size=64) }}
        </p>
        <p>
            {{ form.client_email.label }}<br>
            {{ form.client_email(size=64) }}
        </p>
        <p>
            {{ form.client_phone.label }}<br>
            {{ form.client_phone(size=64) }}
        </p>
        <p>
            {{ form.services.label }}<br>
            {{ form.services }}
        </p>
        <p id="other-services" style="display: none;">
            {{ form.other_services.label }}<br>
            {{ form.other_services(size=64) }}
        </p>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const servicesSelect = document.querySelector('#services');
                const otherServicesInput = document.querySelector('#other-services');
                
                servicesSelect.addEventListener('change', function() {
                    if (servicesSelect.value === 'other') {
                        otherServicesInput.style.display = 'block';
                    } else {
                        otherServicesInput.style.display = 'none';
                    }
                });
            });
        </script>
        <p>
            {{ form.submit() }}
        </p>
    </form>
</body>
</html>
```

```html
<!-- templates/inquiry_success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Submitted</title>
</head>
<body>
    <h1>Thank you for your inquiry!</h1>
    <p>We will be in touch with you soon.</p>
</body>
</html>
```

```html
<!-- templates/base.html (optional) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remas Engineering Consultants</title>
</head>
<body>
    <nav>
        <!-- navigation menu -->
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/inquiry.html (using base.html) -->

{% extends "base.html" %}

{% block content %}
    <h1>Business Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        
        <p>
            {{ form.project_name.label }}<br>
            {{ form.project_name(size=64) }}
        </p>
        <p>
            {{ form.project_description.label }}<br>
            {{ form.project_description(rows=10, cols=40) }}
        </p>
        <p>
            {{ form.client_name.label }}<br>
            {{ form.client_name(size=64) }}
        </p>
        <p>
            {{ form.client_email.label }}<br>
            {{ form.client_email(size=64) }}
        </p>
        <p>
            {{ form.client_phone.label }}<br>
            {{ form.client_phone(size=64) }}
        </p>
        <p>
            {{ form.services.label }}<br>
            {{ form.services }}
        </p>
        <p id="other-services" style="display: none;">
            {{ form.other_services.label }}<br>
            {{ form.other_services(size=64) }}
        </p>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const servicesSelect = document.querySelector('#services');
                const otherServicesInput = document.querySelector('#other-services');
                
                servicesSelect.addEventListener('change', function() {
                    if (servicesSelect.value === 'other') {
                        otherServicesInput.style.display = 'block';
                    } else {
                        otherServicesInput.style.display = 'none';
                    }
                });
            });
        </script>
        <p>
            {{ form.submit() }}
        </p>
    </form>
{% endblock %}
```
