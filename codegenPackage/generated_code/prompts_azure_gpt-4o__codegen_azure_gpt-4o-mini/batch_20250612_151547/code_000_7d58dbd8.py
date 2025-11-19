"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Write Python code to generate a contact form for an NDIS provider, including fields for name, email, phone number, and message, and ensure the form integrates with an email API to send inquiries to "[email protected]".
Generated: DETERMINISTIC_7d58dbd8bc94b2f6
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password
RECIPIENT_EMAIL = 'contact@ndisprovider.com'  # Recipient email address

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not phone or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact_form'))

        # Send email
        try:
            send_email(name, email, phone, message)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact_form'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('contact_form'))

    return render_template('contact_form.html')

def send_email(name, email, phone, message):
    """Send an email with the contact form details."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'New Contact Form Submission'

    # Email body
    body = f"""
    You have received a new message from the contact form.

    Name: {name}
    Email: {email}
    Phone: {phone}
    Message: {message}
    """
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the email server and send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (contact_form.html)**:
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
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>

        <button type="submit">Send</button>
    </form>
</body>
</html>
```

**Note**: Make sure to replace placeholders like `your_email@example.com`, `your_email_password`, and `smtp.example.com` with actual values.
