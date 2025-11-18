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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Configuration for SMTP server
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_USERNAME = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
TO_EMAIL = "dealership_email@example.com"  # Replace with the dealership email address

@app.route('/')
def contact_form():
    """
    Render the contact form HTML page.
    """
    return render_template("contact_form.html")  # Ensure the contact_form.html exists in the templates folder

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle the submission of the contact form, validate data, and send an email.
    """
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate required fields
        if not name or not email or not phone or not message:
            return jsonify({"error": "All fields are required"}), 400

        # Compose the email
        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = TO_EMAIL
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email via SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Authenticate
            server.send_message(msg)  # Send the email

        return jsonify({"message": "Form submitted successfully!"}), 200

    except Exception as e:
        # Handle exceptions and provide meaningful error messages
        return jsonify({"error": "Failed to process your request", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

### Notes for Deployment:
- Replace placeholder values (e.g., `your_email@gmail.com`, `your_email_password`, and `dealership_email@example.com`) with actual values.
- Ensure that the SMTP credentials are properly secured (e.g., use environment variables or a secrets manager).
- Create an HTML file `contact_form.html` in the `templates` folder for the form UI.

### HTML (`contact_form.html` Sample):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Royal Enfield Dealership</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone Number:</label><br>
        <input type="tel" id="phone" name="phone" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
