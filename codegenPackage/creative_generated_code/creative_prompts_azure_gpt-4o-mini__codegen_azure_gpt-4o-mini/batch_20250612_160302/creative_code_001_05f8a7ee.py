"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.xyz
Prompt: What are the best practices for setting up a domain inquiry form similar to the one on Idex.xyz?
Generated: DETERMINISTIC_05f8a7ee421f41e2
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# domain_inquiry_form.py

import flask
from flask import request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Set to False in production
app.config["MAIL_SERVER"] = 'smtp.example.com'  # Update with your SMTP server
app.config["MAIL_PORT"] = 587  # Update with your SMTP port
app.config["MAIL_USERNAME"] = 'your_email@example.com'  # Update with your email
app.config["MAIL_PASSWORD"] = 'your_password'  # Update with your email password
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

def send_email(subject, body, recipient):
    """Send an email to the specified recipient."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = app.config["MAIL_USERNAME"]
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))
        
        # Setup SMTP server and send the email
        with smtplib.SMTP(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]) as server:
            server.starttls()  # Start TLS for security
            server.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")  # Log error for debugging

@app.route('/')
def home():
    """Render the domain inquiry form."""
    return render_template('inquiry_form.html')

@app.route('/submit', methods=['POST'])
def submit_inquiry():
    """Handle the form submission and send an inquiry email."""
    try:
        # Retrieve form data
        domain_name = request.form['domain_name']
        user_email = request.form['email']
        message = request.form['message']
        
        # Validate input data
        if not domain_name or not user_email or not message:
            return jsonify({'error': 'All fields are required!'}), 400
        
        # Prepare and send email
        subject = f"Domain Inquiry for {domain_name}"
        body = f"User Email: {user_email}\nMessage: {message}"
        send_email(subject, body, app.config["MAIL_USERNAME"])
        
        return jsonify({'success': 'Inquiry submitted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run()
```

```html
<!-- templates/inquiry_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Inquiry Form</title>
</head>
<body>
    <h1>Domain Inquiry</h1>
    <form action="/submit" method="POST">
        <label for="domain_name">Domain Name:</label><br>
        <input type="text" id="domain_name" name="domain_name" required><br><br>
        <label for="email">Your Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <input type="submit" value="Submit Inquiry">
    </form>
</body>
</html>
```

### Note:
- Replace SMTP server settings with your actual email server details before deploying.
- Ensure that you have Flask installed and the appropriate dependencies in your environment.
