"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: Write a code snippet that demonstrates how to set up a contact form for a consulting website focused on polyhedra.
Generated: DETERMINISTIC_a2fd0b5aedb2003e
Batch ID: 20250612_155306
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
from email.mime.text import MIMEText
import smtplib

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # Needed for flash messages

# Route for displaying the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Contact form route. Handles GET (display form) and POST (form submission).
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validation
        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect(url_for('contact'))

        try:
            # Send email (replace with actual email credentials and server settings)
            send_email(name, email, message)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"An error occurred while sending your message: {str(e)}", "error")

        return redirect(url_for('contact'))

    # Render the contact form template for GET requests
    return render_template('contact.html')

def send_email(name, email, message):
    """
    Sends an email with the form data.
    """
    # Email settings (replace with real values)
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'your_email@example.com'
    smtp_password = 'your_email_password'
    recipient_email = 'recipient@example.com'

    # Compose email
    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    email_message = MIMEText(body)
    email_message['From'] = smtp_user
    email_message['To'] = recipient_email
    email_message['Subject'] = subject

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure connection
        server.login(smtp_user, smtp_password)
        server.send_message(email_message)

# Run the Flask application (replace with production-ready server in deployment)
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <!-- Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
        {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
    
    <!-- Contact Form -->
    <form method="POST" action="{{ url_for('contact') }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
