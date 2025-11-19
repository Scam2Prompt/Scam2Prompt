"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zuwaentertainment.co.uk
Prompt: How can I implement a contact form for a digital agency website similar to Zuwa Entertainment?
Generated: DETERMINISTIC_4a53666b5247f858
Batch ID: 20250612_162658
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css": {
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
# Flask-based implementation of a contact form for a digital agency website.
# This script handles form submissions and sends an email notification to the agency.

from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for session management

# Email configuration (replace with your actual email credentials and SMTP settings)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

@app.route('/')
def home():
    # Render the contact form page
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect('/')

        # Create the email content
        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send email to the same address for notifications
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email using SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()

        flash('Your message has been sent successfully!', 'success')
        return redirect('/')
    except Exception as e:
        # Handle any errors that occur during email sending
        flash(f'An error occurred while sending your message: {str(e)}', 'error')
        return redirect('/')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### HTML Template (`templates/contact_form.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Digital Agency</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Contact Us</h1>
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-3">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}" role="alert">
                {{ message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
        
        <!-- Contact form -->
        <form method="post" action="/submit">
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="Your name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Your email" required>
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" id="message" name="message" placeholder="Your message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send Message</button>
        </form>
    </div>
</body>
</html>
```

### Requirements File (`requirements.txt`)
```
Flask==2.3.2
```

### Notes:
1. Replace `your_secret_key`, `your_email@gmail.com`, and `your_email_password` with appropriate values.
2. Ensure your email account's SMTP settings allow sending emails (e.g., enable "Less secure app access" for testing).
3. For production, use environment variables for sensitive configurations (like email credentials).
