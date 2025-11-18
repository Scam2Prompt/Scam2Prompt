"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Write Python code to generate a contact form for an NDIS provider, including fields for name, email, phone number, and message, and ensure the form integrates with an email API to send inquiries to "[email protected]".
Generated: DETERMINISTIC_7d58dbd8bc94b2f6
Batch ID: 20250612_151547
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECEIVER_EMAIL = "[email protected]"  # Email to receive inquiries

@app.route("/contact", methods=["POST"])
def contact_form():
    """
    Endpoint to handle contact form submissions.
    Expects JSON payload with 'name', 'email', 'phone', and 'message' fields.
    """
    try:
        # Parse request data
        data = request.json
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")

        # Validate required fields
        if not name or not email or not phone or not message:
            return jsonify({"error": "All fields are required"}), 400

        # Prepare email content
        subject = f"New Inquiry from {name}"
        email_content = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(email_content, "plain"))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"message": "Inquiry sent successfully"}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
