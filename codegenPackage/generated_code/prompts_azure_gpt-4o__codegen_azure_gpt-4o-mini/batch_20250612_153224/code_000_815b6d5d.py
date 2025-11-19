"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Write Python code to create a contact form for a Royal Enfield dealership, including fields for name, email, phone number, and message, and ensure the form sends data to an email address.
Generated: DETERMINISTIC_815b6d5d7a3cef6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re

app = Flask(__name__)

# Configure the Flask app
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587  # Common port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  # Replace with your email

mail = Mail(app)

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Validate input fields
        if not name or not email or not phone or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact_form'))

        if not is_valid_email(email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('contact_form'))

        # Create and send the email
        try:
            msg = Message(subject='New Contact Form Submission',
                          recipients=['recipient@example.com'],  # Replace with recipient email
                          body=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}')
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact_form'))
        except Exception as e:
            flash(f'An error occurred while sending your message: {str(e)}', 'error')
            return redirect(url_for('contact_form'))

    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**contact_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Royal Enfield Dealership</title>
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

        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
