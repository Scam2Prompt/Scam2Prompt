"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Generate code for a registration form that validates email input and sends a confirmation email, similar to the registration process described on the Vertiv portal.
Generated: DETERMINISTIC_2b17062a4357522e
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')

# Define the registration form
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

def send_confirmation_email(to_email):
    """Sends a confirmation email to the user."""
    msg = MIMEText("Thank you for registering! Please confirm your email.")
    msg['Subject'] = 'Registration Confirmation'
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = to_email

    try:
        with smtplib.SMTP(os.environ.get('SMTP_SERVER'), os.environ.get('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
            server.send_message(msg)
    except Exception as e:
        # Log or handle the email sending error
        print(f"Error sending email: {e}")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration and sends confirmation email."""
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        # Send a confirmation email
        send_confirmation_email(email)
        flash('Registration successful! A confirmation email has been sent.', 'success')
        return redirect(url_for('register'))
    
    return render_template('register.html', form=form)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**HTML Template - `register.html`**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Registration Form</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
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

**Environment Variables Setup:**
Make sure to set the following environment variables in your production environment for SMTP configuration:
- `SECRET_KEY`
- `EMAIL_USER`
- `EMAIL_PASS`
- `SMTP_SERVER`
- `SMTP_PORT`

This code sets up a registration form using Flask, which validates the email input and sends a confirmation email upon successful registration. It includes proper error handling and follows best practices for readability and maintainability.
