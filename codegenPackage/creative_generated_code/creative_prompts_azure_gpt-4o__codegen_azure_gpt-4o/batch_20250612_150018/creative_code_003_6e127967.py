"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write code to automate the generation of contact forms for a packaging manufacturer, including fields for product inquiries about ABS Atlas trays and bakery trays, as described on Isoplas Corporation's website.
Generated: DETERMINISTIC_6e127967ec31037f
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, EmailField, validators

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Define the ContactForm class
class ContactForm(FlaskForm):
    # Define fields for the contact form
    name = StringField('Name', [validators.DataRequired(), validators.Length(max=100)])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    company = StringField('Company Name', [validators.Optional(), validators.Length(max=100)])
    inquiry_type = SelectField(
        'Inquiry Type',
        choices=[
            ('abs_atlas_trays', 'ABS Atlas Trays'),
            ('bakery_trays', 'Bakery Trays')
        ],
        validators=[validators.DataRequired()]
    )
    message = TextAreaField(
        'Message',
        [validators.DataRequired(), validators.Length(max=500)],
        render_kw={"rows": 5}
    )

# Route for the homepage and form display
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    form = ContactForm()  # Initialize the form

    if request.method == 'POST':
        if form.validate_on_submit():
            # Extract form data
            name = form.name.data
            email = form.email.data
            company = form.company.data
            inquiry_type = form.inquiry_type.data
            message = form.message.data

            # Process form data (e.g., save to database or send via email)
            # In production, replace this with suitable logic.
            flash('Thank you for your inquiry! We will get back to you shortly.', 'success')
            
            # For demonstration purposes, redirect to the same page
            return redirect(url_for('contact_form'))
        else:
            # Show validation errors to the user
            flash('Please fix the errors in the form.', 'danger')

    return render_template('contact_form.html', form=form)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the Flask application
if __name__ == '__main__':
    # Use 'flask run' or 'python app.py' to start the server in production
    app.run(debug=True)

```

### Associated HTML Template: `contact_form.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Packaging Manufacturer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Contact Form</h1>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div class="mb-3">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
                {% for error in form.name.errors %}
                <div class="text-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="mb-3">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
                {% for error in form.email.errors %}
                <div class="text-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="mb-3">
                {{ form.company.label(class="form-label") }}
                {{ form.company(class="form-control") }}
            </div>
            <div class="mb-3">
                {{ form.inquiry_type.label(class="form-label") }}
                {{ form.inquiry_type(class="form-select") }}
                {% for error in form.inquiry_type.errors %}
                <div class="text-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="mb-3">
                {{ form.message.label(class="form-label") }}
                {{ form.message(class="form-control") }}
                {% for error in form.message.errors %}
                <div class="text-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-3">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

This Flask app automates the generation of a contact form for product inquiries, complete with error handling and validation. Remember to replace placeholders like `your_secret_key` with appropriate values for production use.
