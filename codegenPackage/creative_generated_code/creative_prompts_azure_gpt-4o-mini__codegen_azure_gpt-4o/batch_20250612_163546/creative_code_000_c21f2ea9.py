"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Generate a code snippet for a web application that allows users to submit their interior design ideas and receive a personalized consultation from Meezan Interior Solutions.
Generated: DETERMINISTIC_c21f2ea9f964a1d4
Batch ID: 20250612_163546
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.0/css/bootstrap.min.css": {
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
# File: app.py
# Description: A Flask web application that allows users to submit their interior design ideas
#              and receive a personalized consultation from Meezan Interior Solutions.

from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Configuration for email (use environment variables in production for security)
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"        # Replace with your email password

@app.route('/')
def home():
    """
    Render the home page where users can submit their design ideas.
    """
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit_design():
    """
    Handle the submission of design ideas.
    """
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        design_idea = request.form.get('design_idea')

        # Validate form data
        if not name or not email or not design_idea:
            flash("All fields are required.", "error")
            return redirect(url_for('home'))

        # Send email with the submitted idea
        send_email(name, email, design_idea)

        flash("Your design idea has been submitted successfully! We will contact you soon.", "success")
        return redirect(url_for('home'))
    except Exception as e:
        # Handle unexpected errors
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('home'))

def send_email(name, email, design_idea):
    """
    Send the submitted design idea to Meezan Interior Solutions email.
    """
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = EMAIL_USERNAME  # Replace with recipient email
        msg['Subject'] = "New Interior Design Consultation Request"
        
        body = f"""
        Name: {name}
        Email: {email}
        Design Idea: {design_idea}
        """
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        raise Exception("Error sending email.") from e

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- File: templates/home.html -->
<!-- Description: HTML template for the home page -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meezan Interior Solutions</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Meezan Interior Solutions</h1>
        <p class="text-center">Submit your interior design ideas and get personalized consultations!</p>

        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            <div>
              {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
              {% endfor %}
            </div>
          {% endif %}
        {% endwith %}

        <!-- Design submission form -->
        <form method="POST" action="/submit">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="design_idea">Your Design Idea</label>
                <textarea class="form-control" id="design_idea" name="design_idea" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```
