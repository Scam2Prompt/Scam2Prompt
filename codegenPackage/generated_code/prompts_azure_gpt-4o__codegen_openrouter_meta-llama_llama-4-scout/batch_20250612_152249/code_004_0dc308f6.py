"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Create a Flask application with a contact form for patients to request appointments and send inquiries to Dr. S. Nagendra Boopathy's email ([email protected]).
Generated: DETERMINISTIC_0dc308f6b8fdb2bd
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a Flask application instance
app = Flask(__name__)

# Configuration for email service
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "dr.s.nagendraboopathy@gmail.com"
PASSWORD = "your_password_here"  # Replace with your email password

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Route for the contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        try:
            # Get form data
            name = request.form.get("name")
            email = request.form.get("email")
            phone = request.form.get("phone")
            message = request.form.get("message")

            # Create a message
            msg = MIMEMultipart()
            msg["From"] = FROM_EMAIL
            msg["To"] = FROM_EMAIL
            msg["Subject"] = "Patient Inquiry"

            # Construct the email body
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
            msg.attach(MIMEText(body, "plain"))

            # Send the email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(FROM_EMAIL, PASSWORD)
            text = msg.as_string()
            server.sendmail(FROM_EMAIL, FROM_EMAIL, text)
            server.quit()

            # Redirect to a success page
            return redirect(url_for("success"))
        except Exception as e:
            # Handle exceptions
            print(f"Error: {e}")
            return redirect(url_for("error"))
    return render_template("contact.html")

# Route for the success page
@app.route("/success")
def success():
    return render_template("success.html")

# Route for the error page
@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dr. S. Nagendra Boopathy</title>
</head>
<body>
    <h1>Welcome to Dr. S. Nagendra Boopathy's Website</h1>
    <p><a href="{{ url_for('contact') }}">Contact Us</a></p>
</body>
</html>
```

**templates/contact.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Dr. S. Nagendra Boopathy</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h1>Success!</h1>
    <p>Your message has been sent successfully.</p>
    <p><a href="{{ url_for('index') }}">Back to Home</a></p>
</body>
</html>
```

**templates/error.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Error!</h1>
    <p>An error occurred while sending your message.</p>
    <p><a href="{{ url_for('contact') }}">Try Again</a></p>
</body>
</html>
```
