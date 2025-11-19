"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: Illustrate how to implement a contact form in a web application that sends inquiries to an insurance advisor, similar to the contact methods provided by Yexine Rangel Asesores de Seguros.
Generated: DETERMINISTIC_55d3fe63dc8ae0a1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application to implement a contact form for sending inquiries to an insurance advisor

from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for session management

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

@app.route('/')
def home():
    """
    Render the home page with the contact form.
    """
    return render_template('contact_form.html')

@app.route('/send_inquiry', methods=['POST'])
def send_inquiry():
    """
    Handle the form submission and send the inquiry via email.
    """
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('Name, email, and message are required fields.', 'error')
            return redirect(url_for('home'))

        # Create the email content
        email_subject = f"Inquiry from {name}"
        email_body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send to the advisor's email
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        flash('Your inquiry has been sent successfully!', 'success')
        return redirect(url_for('home'))

    except Exception as e:
        # Handle errors gracefully
        flash(f'An error occurred while sending your inquiry: {str(e)}', 'error')
        return redirect(url_for('home'))

# HTML template for the contact form (contact_form.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Insurance Advisor</h1>
    <form action="/send_inquiry" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>
        
        <button type="submit">Send Inquiry</button>
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
"""

if __name__ == '__main__':
    app.run(debug=True)
```
