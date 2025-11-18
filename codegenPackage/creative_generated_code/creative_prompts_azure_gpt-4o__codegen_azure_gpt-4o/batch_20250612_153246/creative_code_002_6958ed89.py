"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Generate code using Flask to create a contact form for PSHP's website, allowing users to submit inquiries to the provided email address.
Generated: DETERMINISTIC_6958ed8982fd2dd3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_default_secret_key')  # Secret key for flash messages

# Email settings
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')  # Replace with your SMTP server if different
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # Usually 587 for TLS
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', 'your_email@gmail.com')  # Replace with your email
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_email_password')  # Replace with your email password
TARGET_EMAIL = os.getenv('TARGET_EMAIL', 'target_email@domain.com')  # Replace with the email to receive inquiries


@app.route('/', methods=['GET', 'POST'])
def contact_form():
    """
    Route for the contact form. Handles both displaying the form and processing the submission.
    """
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash("All fields are required. Please fill out the form completely.", "error")
            return redirect(url_for('contact_form'))

        try:
            # Prepare the email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USERNAME
            msg['To'] = TARGET_EMAIL
            msg['Subject'] = f"New Inquiry from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Enable TLS encryption
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.sendmail(EMAIL_USERNAME, TARGET_EMAIL, msg.as_string())

            flash("Your inquiry has been submitted successfully!", "success")
        except Exception as e:
            # Handle email errors gracefully
            flash(f"An error occurred while sending your inquiry. Please try again later. Error: {e}", "error")

        return redirect(url_for('contact_form'))

    return render_template('contact_form.html')


if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/contact_form.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
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
    <form method="POST" action="{{ url_for('contact_form') }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Environment Variables (`.env` file)
```
FLASK_SECRET_KEY=your_secret_key
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
TARGET_EMAIL=target_email@domain.com
```
