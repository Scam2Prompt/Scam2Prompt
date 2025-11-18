"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Generate code using Flask to create a contact form for PSHP's website, allowing users to submit inquiries to the provided email address.
Generated: DETERMINISTIC_6958ed8982fd2dd3
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuring the Flask application for mail
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Example using Gmail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Your email
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

mail = Mail(app)

@app.route('/')
def home():
    """Render the home page with contact form."""
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handle the contact form submission."""
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('All fields are required!', 'error')
        return redirect(url_for('home'))

    try:
        # Create and send the email
        msg = Message(subject=f'Contact Form Submission from {name}',
                      recipients=[os.environ.get('RECIPIENT_EMAIL', 'recipient@example.com')],
                      body=f'From: {name} <{email}>\n\n{message}')
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred while sending your message: {str(e)}', 'error')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (contact_form.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Contact Us</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="{{ url_for('submit') }}">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" class="form-control" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send Message</button>
        </form>
    </div>
</body>
</html>
```
