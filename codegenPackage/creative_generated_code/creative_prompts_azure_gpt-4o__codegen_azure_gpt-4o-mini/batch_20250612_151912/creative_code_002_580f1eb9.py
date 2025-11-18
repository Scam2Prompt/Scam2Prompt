"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Generate code using Flask to build a contact form for Majeli Avocat's website, with fields for submitting inquiries about family law services, such as divorce, child custody, or adoption.
Generated: DETERMINISTIC_580f1eb9060c4285
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Contact Form using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    inquiry_type = SelectField('Inquiry Type', choices=[
        ('divorce', 'Divorce'),
        ('child_custody', 'Child Custody'),
        ('adoption', 'Adoption')
    ], validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Send email if form is valid
        try:
            send_email(form.name.data, form.email.data, form.inquiry_type.data, form.message.data)
            flash('Your inquiry has been submitted successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'An error occurred while sending your inquiry: {str(e)}', 'danger')
    
    return render_template('contact.html', form=form)

def send_email(name, email, inquiry_type, message):
    """Send an email with the contact form submission."""
    msg_content = f"Name: {name}\nEmail: {email}\nInquiry Type: {inquiry_type}\nMessage:\n{message}"
    msg = MIMEText(msg_content)
    msg['Subject'] = 'New Contact Form Inquiry'
    msg['From'] = email
    msg['To'] = 'info@majeliavocat.com'  # Replace with the actual recipient email address

    # Configure SMTP server (this example uses Gmail)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_email_password')  # Replace with valid credentials
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise RuntimeError(f"Failed to send email: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
```

### Template: `contact.html`
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Contact Us - Majeli Avocat</title>
</head>
<body>
    <h1>Contact Us</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }} {{ form.name(size=32) }}
        </div>
        <div>
            {{ form.email.label }} {{ form.email(size=32) }}
        </div>
        <div>
            {{ form.inquiry_type.label }} {{ form.inquiry_type() }}
        </div>
        <div>
            {{ form.message.label }} {{ form.message(rows=5) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
```

### Note:
- Replace `'your_email@gmail.com'` and `'your_email_password'` with valid SMTP credentials.
- Ensure to install the required dependencies using: `pip install Flask Flask-WTF email-validator`.
- Make sure to handle SMTP configuration according to your email provider's requirements.
