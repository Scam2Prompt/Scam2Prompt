"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Generate code for a web application that allows users to request free estimates for architectural design and historical building preservation projects. Include form validation and email notification functionality.
Generated: DETERMINISTIC_3a8c90107e3bd0ce
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A simple Flask web application for requesting free estimates for architectural design and historical building preservation
# This application includes form validation and email notification functionality.

from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management and flash messaging

# Configuration for email notifications
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587                 # Replace with your SMTP server's port
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your-email-password'    # Replace with your email password
ADMIN_EMAIL = 'admin@example.com'         # Replace with the admin's email address

@app.route('/')
def index():
    """Render the home page with the form."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_estimate_request():
    """Handle form submission and send email notifications."""
    try:
        # Extract form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        project_type = request.form.get('project_type', '').strip()
        message = request.form.get('message', '').strip()

        # Validate form data
        if not name or not email or not project_type:
            flash('Please fill out all required fields.', 'error')
            return redirect(url_for('index'))

        # Additional email validation
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('index'))

        # Prepare email content
        subject = 'New Estimate Request'
        body = f"Name: {name}\nEmail: {email}\nProject Type: {project_type}\nMessage: {message}"

        # Send email notification
        send_email_notification(ADMIN_EMAIL, subject, body)

        flash('Your request has been submitted successfully! We will get back to you soon.', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        # Handle unexpected errors
        flash(f"An error occurred while processing your request: {str(e)}", 'error')
        return redirect(url_for('index'))

def send_email_notification(to_email, subject, body):
    """
    Send an email notification to the admin.
    :param to_email: Recipient email address
    :param subject: Email subject
    :param body: Email body content
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach email body
        msg.attach(MIMEText(body, 'plain'))

        # Send email via SMTP
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        # Log errors (in production, use proper logging mechanisms)
        print(f"Failed to send email notification: {str(e)}")

# HTML template for the form
@app.route('/index.html')
def serve_template():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Request Free Estimate</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .form-container { max-width: 500px; margin: auto; }
            .form-group { margin-bottom: 15px; }
            label { display: block; font-weight: bold; }
            input, textarea { width: 100%; padding: 8px; margin-top: 5px; }
            .form-actions { text-align: right; }
            button { padding: 10px 15px; background-color: #007BFF; color: #FFF; border: none; cursor: pointer; }
            .flash-message { padding: 10px; border: 1px solid #CCC; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Request Free Estimate</h1>
            {% with messages = get_flashed_messages(with_categories=True) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="flash-message {{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
            <form method="POST" action="/submit">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="project_type">Project Type:</label>
                    <input type="text" id="project_type" name="project_type" required>
                </div>
                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" rows="5"></textarea>
                </div>
                <div class="form-actions">
                    <button type="submit">Submit</button>
                </div>
            </form>
        </div>
    </body>
    </html>
    """

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
