"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Write Python code to generate a contact form for an NDIS provider, including fields for name, email, phone number, and message, and ensure the form integrates with an email API to send inquiries to "[email protected]".
Generated: DETERMINISTIC_7d58dbd8bc94b2f6
Batch ID: 20250612_151547
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
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Configure Flask-Mail with SMTP settings
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587  # Typically 587 for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Use environment variable for security
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Use environment variable for security
app.config['MAIL_DEFAULT_SENDER'] = 'ndisprovider@example.com'  # Your sender email

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not phone or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact'))

        # Create email message
        msg = Message("New Contact Inquiry", recipients=["ndisprovider@example.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        try:
            # Send email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred while sending your message: {str(e)}', 'error')
        
        return redirect(url_for('contact'))

    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**HTML Template (contact_form.html):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>

        <button type="submit">Send</button>
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
