"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Develop a web application feature that allows users to choose and order high-quality pebbles directly from Ticino, integrating a contact form for inquiries.
Generated: DETERMINISTIC_d8823f102e35f320
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
import smtplib
from email.mime.text import MIMEText

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key

# Define the contact form using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Inquiry')

    # Custom validation to ensure no spam
    def validate_message(form, field):
        if "spam" in field.data.lower():
            raise ValidationError("Spam detected!")

# Function to send email notifications
def send_email(name, email, message):
    try:
        msg = MIMEText(f'Name: {name}\nEmail: {email}\nMessage: {message}')
        msg['Subject'] = 'New Inquiry from Pebble Ordering Application'
        msg['From'] = 'your_email@example.com'  # Replace with your email
        msg['To'] = 'your_email@example.com'    # Replace with your email

        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')  # Replace with your credentials
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    return True

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage template

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Extract form data
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Send email and provide feedback
        if send_email(name, email, message):
            flash('Your inquiry has been sent successfully!', 'success')
        else:
            flash('There was an error sending your inquiry. Please try again later.', 'danger')

        return redirect(url_for('contact'))  # Redirect to avoid resubmission

    return render_template('contact.html', form=form)  # Render the contact form template

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates (index.html and contact.html)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pebble Ordering</title>
</head>
<body>
    <h1>Welcome to the Pebble Ordering Application</h1>
    <a href="{{ url_for('contact') }}">Contact Us</a>
</body>
</html>
```

**contact.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.message.label }}<br>
            {{ form.message(rows=5, cols=40) }}<br>
            {% for error in form.message.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Note:
- Replace placeholder values in the code, such as email addresses and SMTP server settings, with actual configurations before deploying.
- Make sure to install the necessary packages with `pip install Flask Flask-WTF` before running the code.
