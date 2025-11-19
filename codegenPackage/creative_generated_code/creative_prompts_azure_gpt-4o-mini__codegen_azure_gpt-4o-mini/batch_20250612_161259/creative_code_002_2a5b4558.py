"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaleeji.com
Prompt: Create an API request to send an email inquiry to Owner@Khaleeji.com regarding the sale of KHALEEJI.COM.
Generated: DETERMINISTIC_2a5b45583fd9bcf7
Batch ID: 20250612_161259
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

def send_email(subject, body, to_email):
    """
    Sends an email using SMTP.

    Args:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        to_email (str): The recipient's email address.

    Raises:
        Exception: If there's an error sending the email.
    """
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # For TLS
    sender_email = 'your_email@example.com'  # Replace with your sender email
    sender_password = 'your_password'  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the email server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Login to the email server
            server.send_message(msg)  # Send the email
            print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

if __name__ == "__main__":
    # Prepare the email details
    subject = "Inquiry Regarding the Sale of KHALEEJI.COM"
    body = "Dear Owner,\n\nI am interested in inquiring about the sale of KHALEEJI.COM. Please provide further details.\n\nBest regards,\nYour Name"
    to_email = "Owner@Khaleeji.com"

    # Send the email
    send_email(subject, body, to_email)
```
