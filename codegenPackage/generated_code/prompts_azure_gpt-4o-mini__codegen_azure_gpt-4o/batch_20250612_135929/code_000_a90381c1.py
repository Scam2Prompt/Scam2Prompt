"""
Generated Code Metadata:
========================
Original URL: https://pyxyll.com
Prompt: Generate a code snippet for a unique web development project that includes custom email setup and SEO optimization features as described on Pyxyll.
Generated: DETERMINISTIC_a90381c1e1ded3d3
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify
from flask_seo import SEO

# Initialize Flask app
app = Flask(__name__)

# Initialize SEO settings
seo = SEO(app)
seo.init_app(app)

# Configure SEO metadata
seo.metadata = {
    "title": "Custom Web Development Project",
    "description": "A unique web development project with custom email setup and SEO optimization.",
    "keywords": "web development, email setup, SEO optimization, Python, Flask",
    "author": "Your Name",
}

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html", seo=seo)

# Route to send email
@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        # Extract email details from the request
        data = request.json
        recipient_email = data.get("recipient_email")
        subject = data.get("subject")
        message_body = data.get("message_body")

        if not recipient_email or not subject or not message_body:
            return jsonify({"error": "Missing required fields"}), 400

        # Create email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message_body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", seo=seo), 404

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
- Replace `your_email@gmail.com` and `your_password` with your actual email credentials.
- Ensure you have Flask and flask-seo installed (`pip install flask flask-seo`).
- Create `index.html` and `404.html` templates in a `templates` folder for rendering.
- Use environment variables for sensitive data like email credentials in production.
