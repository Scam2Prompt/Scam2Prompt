"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Recommend a library or API to integrate a contact form for Balaji Tours & Travels that sends inquiries to their email address (balajitravelsch56@gmail.com) and validates inputs like name, mobile number, and email.
Generated: DETERMINISTIC_234f40f3e6d9fd3f
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using Flask and Flask-Mail to integrate a contact form for Balaji Tours & Travels. Make sure to install the required libraries (`flask`, `flask-mail`) before running the code.

```python
# Import required libraries and modules
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import re

# Initialize Flask application
app = Flask(__name__)

# Secret key for flashing messages
app.secret_key = 'supersecretkey'

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'   # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # Replace with your email

# Initialize Flask-Mail
mail = Mail(app)

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Mobile number validation regex
MOBILE_REGEX = r'^\d{10}$'

# Route for the contact form
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        message = request.form.get('message')

        # Validate inputs
        if not name or len(name.strip()) == 0:
            flash('Name is required', 'error')
            return render_template('contact_form.html')

        if not email or not re.match(EMAIL_REGEX, email):
            flash('Invalid email address', 'error')
            return render_template('contact_form.html')

        if not mobile or not re.match(MOBILE_REGEX, mobile):
            flash('Invalid mobile number (must be 10 digits)', 'error')
            return render_template('contact_form.html')

        if not message or len(message.strip()) == 0:
            flash('Message is required', 'error')
            return render_template('contact_form.html')

        # Prepare email
        try:
            msg = Message(
                subject=f"Inquiry from {name}",
                recipients=['balajitravelsch56@gmail.com'],  # The destination email
                body=f"""
                Inquiry Details:
                Name: {name}
                Email: {email}
                Mobile: {mobile}
                Message: {message}
                """
            )
            mail.send(msg)
            flash('Your inquiry has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send inquiry: {str(e)}', 'error')

    return render_template('contact_form.html')

# Template for contact form (HTML)
@app.route('/contact_form.html')
def contact_form_template():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Form</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 30px; }
            form { max-width: 400px; margin: auto; }
            .form-group { margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <h1>Contact Us - Balaji Tours & Travels</h1>
        <form method="POST" action="/">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="mobile">Mobile Number:</label>
                <input type="text" id="mobile" name="mobile" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>
            <button type="submit">Send Inquiry</button>
        </form>
    </body>
    </html>
    """

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes:**
- Replace `your-email@gmail.com` and `your-email-password` in the configuration with valid credentials to send emails.
- Ensure that "Allow less secure apps" is enabled for the email account (if using Gmail). Alternatively, use a service-specific password or an API key for better security.
- Use HTTPS in production for secure input handling.
- The HTML contact form is embedded as a string for simplicity but can be moved to a separate HTML template file in a production environment.
