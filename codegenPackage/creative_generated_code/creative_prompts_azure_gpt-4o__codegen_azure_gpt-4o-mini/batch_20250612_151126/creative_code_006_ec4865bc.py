"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Generate code to implement a contact form with email notifications, referencing the ALPS Foundation's contact us page functionality.
Generated: DETERMINISTIC_ec4865bc06a33466
Batch ID: 20250612_151126
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

# Configure the application secret key and email settings
app.secret_key = os.environ.get('SECRET_KEY', 'your_default_secret_key')
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handles the contact form submission.
    GET request: Renders the contact form.
    POST request: Sends an email notification with the form data.
    """
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('All fields are required.', 'error')
            return redirect(url_for('contact'))

        # Create email content
        msg = Message(subject=f'Contact Form Submission from {name}',
                      recipients=[os.environ.get('RECIPIENT_EMAIL')],
                      body=f'Name: {name}\nEmail: {email}\nMessage: {message}')

        try:
            # Send the email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            # Log the error and notify the user
            app.logger.error(f'Error sending email: {e}')
            flash('An error occurred while sending your message. Please try again later.', 'error')
        
        return redirect(url_for('contact'))

    # Render the contact form
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**contact.html** (Place this file in a `templates` directory)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
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
    <form action="{{ url_for('contact') }}" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <input type="submit" value="Send">
    </form>
</body>
</html>
```

### Instructions
- Replace `smtp.example.com`, `MAIL_USERNAME`, `MAIL_PASSWORD`, and `RECIPIENT_EMAIL` with your actual SMTP server and credentials.
- Ensure Flask and Flask-Mail libraries are installed. You can install them using:
```bash
pip install Flask Flask-Mail
```
- Set the appropriate environment variables for security.
