"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Write Python code to create a contact form for a Royal Enfield dealership, including fields for name, email, phone number, and message, and ensure the form sends data to an email address.
Generated: DETERMINISTIC_815b6d5d7a3cef6b
Batch ID: 20250612_153224
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
from flask_mail import Mail, Message
import os

# Initialize Flask application
app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change to your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Set your email user
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Set your email password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')  # Default sender
app.secret_key = os.environ.get('SECRET_KEY') or 'mysecret'  # Secret key for sessions

# Initialize mail
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    """Contact form route."""
    if request.method == 'POST':
        # Retrieve data from form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Basic validation
        if not name or not email or not phone or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact'))

        # Create email message
        msg = Message('Contact Form Submission',
                      recipients=[os.environ.get('RECIPIENT_EMAIL')])  # Recipient email
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

        try:
            # Send email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('contact'))

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Royal Enfield Dealership</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="/">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Message</button>
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

### Environment Variables
Make sure to set the following environment variables for the application to work:
- `EMAIL_USER`: Your email address used for sending the email.
- `EMAIL_PASS`: The password for your email account.
- `RECIPIENT_EMAIL`: The email address that will receive the contact form submissions.
- `SECRET_KEY`: A secret key for your Flask application.

### Dependencies
To run this code, you will need to install the Flask and Flask-Mail libraries:
```bash
pip install Flask Flask-Mail
```
