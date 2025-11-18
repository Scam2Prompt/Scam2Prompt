"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Write code to integrate a contact form for an educational website, referencing the contact details structure provided on Educar Comitán's webpage.
Generated: DETERMINISTIC_726425c8a7dc2d41
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask app to integrate a contact form for an educational website
from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuration for the email server (update with your details)
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_USER = 'your-email@example.com'  # Replace with your email
EMAIL_PASS = 'your-email-password'  # Replace with your email password
RECIPIENT_EMAIL = 'recipient-email@example.com'  # Replace with Educar Comitán contact email

@app.route('/')
def home():
    """
    Render the homepage with the contact form.
    """
    return render_template('contact_form.html')  # Ensure this template exists

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    """
    Handle the submission of the contact form.
    """
    try:
        # Extract form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validate form inputs
        if not name or not email or not message:
            return jsonify({"error": "All fields are required!"}), 400

        # Create the email content
        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, msg.as_string())

        return jsonify({"success": "Your message has been sent successfully!"}), 200

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error while submitting contact form: {str(e)}")
        return jsonify({"error": "An error occurred while sending your message. Please try again later."}), 500

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
```

```html
<!-- contact_form.html: HTML template for the contact form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Educar Comitán</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit_contact_form" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
