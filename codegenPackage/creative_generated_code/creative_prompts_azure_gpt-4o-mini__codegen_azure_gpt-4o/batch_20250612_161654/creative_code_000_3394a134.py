"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: How can I create a contact form similar to the one on The Prepper Codex website for customer inquiries?
Generated: DETERMINISTIC_3394a1346397e1cb
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a production-ready contact form implementation in Python using the Flask framework:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key for production

# Route for the home page (renders the contact form)
@app.route('/')
def index():
    return render_template('contact_form.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Collect form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        # Send an email (configure SMTP settings for your email provider)
        send_email(name, email, message)

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash('An error occurred while submitting the form. Please try again later.', 'error')
        return redirect(url_for('index'))

def send_email(name, email, message):
    """
    Sends an email containing the contact form data.
    Configure the SMTP server and sender credentials before using.
    """
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Typical port for TLS
    smtp_user = 'your_email@example.com'  # Replace with your email
    smtp_password = 'your_email_password'  # Replace with your email password
    recipient_email = 'your_email@example.com'  # Replace with the email to receive inquiries

    # Craft the email message
    subject = f"Customer Inquiry from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = recipient_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, recipient_email, msg.as_string())

# HTML Template for the contact form (save as 'templates/contact_form.html')
"""
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
    <form method="POST" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Steps Before Running:**
1. Replace placeholders (`smtp.example.com`, `your_email@example.com`, `your_email_password`) with actual SMTP and email credentials.
2. Save the HTML template in a `templates` folder.
3. Install Flask (`pip install flask`) and run this script.
