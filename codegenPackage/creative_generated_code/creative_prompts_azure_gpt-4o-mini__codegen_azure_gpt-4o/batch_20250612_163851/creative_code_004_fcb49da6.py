"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercatura.co.id
Prompt: Suggest a library for building a contact page that reflects the layout and design principles mentioned on Mercatura's website.
Generated: DETERMINISTIC_fcb49da6983307c9
Batch ID: 20250612_163851
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
"""
This script uses Flask to create a contact page that follows modern design principles
inspired by Mercatura's website. The contact page includes a form for users to submit
their name, email, subject, and message. 

The Flask server handles form submissions and provides error handling.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Flask app initialization
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key for production.

# Contact form definition using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=150)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Send Message')

# Route to render the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Process the form data (e.g., send an email or save to a database)
            # For demonstration, we simply flash a success message.
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        else:
            # Flash error messages if validation fails
            flash('Please correct the errors in the form.', 'danger')
    return render_template('contact.html', form=form)

# HTML template (contact.html) should include:
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Contact Us</h1>
        <form method="POST" action="">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label }}<br>
                {{ form.name(class="form-control") }}
                {% for error in form.name.errors %}
                    <small class="text-danger">{{ error }}</small>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.email.label }}<br>
                {{ form.email(class="form-control") }}
                {% for error in form.email.errors %}
                    <small class="text-danger">{{ error }}</small>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.subject.label }}<br>
                {{ form.subject(class="form-control") }}
                {% for error in form.subject.errors %}
                    <small class="text-danger">{{ error }}</small>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.message.label }}<br>
                {{ form.message(class="form-control") }}
                {% for error in form.message.errors %}
                    <small class="text-danger">{{ error }}</small>
                {% endfor %}
            </div>
            <button type="submit" class="btn btn-primary">{{ form.submit.label }}</button>
        </form>
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
"""

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500 - Internal Server Error</h1>", 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production.
```
