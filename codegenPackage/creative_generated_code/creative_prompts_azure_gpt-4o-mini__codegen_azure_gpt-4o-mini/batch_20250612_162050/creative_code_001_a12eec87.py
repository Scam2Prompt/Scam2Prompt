"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Write a Python script that sends an email to a law firm, requesting information about their services in family law and administrative issues.
Generated: DETERMINISTIC_a12eec87be522639
Batch ID: 20250612_162050
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

def send_email(to_email, subject, body, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Send an email using the specified SMTP server.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.
        from_email (str): Sender's email address.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        smtp_user (str): SMTP username.
        smtp_password (str): SMTP password.

    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(smtp_user, smtp_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Email details
    recipient_email = "info@lawfirm.com"  # Law firm's email address
    email_subject = "Inquiry About Family Law and Administrative Services"
    email_body = (
        "Dear Law Firm,\n\n"
        "I hope this message finds you well. I am writing to inquire about your services "
        "regarding family law and administrative issues. I would appreciate any information "
        "you can provide, including consultation availability and fee structures.\n\n"
        "Thank you for your assistance.\n\n"
        "Best regards,\n"
        "[Your Name]\n"
        "[Your Contact Information]"
    )

    # SMTP server configuration
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    smtp_user = "your_email@example.com"  # Replace with your email
    smtp_password = "your_password"  # Replace with your email password

    # Send the email
    send_email(recipient_email, email_subject, email_body, smtp_user, smtp_server, smtp_port, smtp_user, smtp_password)
```
