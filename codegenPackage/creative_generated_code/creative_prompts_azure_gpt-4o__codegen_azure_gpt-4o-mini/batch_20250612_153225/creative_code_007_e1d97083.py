"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samional.com
Prompt: Write code to set up a contact form that integrates with email services, ensuring professional communication as described on samional.com. Include validation and security features.
Generated: DETERMINISTIC_e1d97083245cf64d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from wtforms import Form, StringField, TextAreaField, EmailField, validators
import re
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your email server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Set in your environment
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Set in your environment
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_SENDER')  # Set in your environment

mail = Mail(app)

# Contact Form
class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = EmailField('Email', [validators.Length(min=6, max=100), validators.Email()])
    message = TextAreaField('Message', [validators.Length(min=10, max=500)])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Prepare email content
            msg = Message(subject=f'New Contact Form Submission from {form.name.data}',
                          recipients=[os.environ.get('EMAIL_RECIPIENT')],  # Set recipient in environment
                          body=f'Name: {form.name.data}\nEmail: {form.email.data}\n\nMessage:\n{form.message.data}')
            
            # Send email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'An error occurred while sending your message: {str(e)}', 'danger')
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    # Set a secret key for session management
    app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # Set in your environment
    app.run(debug=True)
```

```html
<!-- contact.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="{{ url_for('contact') }}">
        {{ form.hidden_tag() }}
        <div>
            <label for="name">Name:</label>
            {{ form.name(size=32) }}
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            <label for="email">Email:</label>
            {{ form.email(size=32) }}
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            <label for="message">Message:</label>
            {{ form.message(cols=40, rows=5) }}
            {% for error in form.message.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            <button type="submit">Send</button>
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
