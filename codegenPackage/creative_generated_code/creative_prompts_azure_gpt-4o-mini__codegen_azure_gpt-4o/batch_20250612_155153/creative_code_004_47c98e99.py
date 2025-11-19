"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Illustrate how to use a library to send automated emails to parents for school announcements, similar to those from the Colegio Panamericano e Instituto Libertadores.
Generated: DETERMINISTIC_47c98e99f5f49cd3
Batch ID: 20250612_155153
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
from email.utils import formataddr

# Configuration for the email server and sender details
SMTP_SERVER = "smtp.gmail.com"  # Use your SMTP server (This example uses Gmail)
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"  # Replace with your email
SENDER_NAME = "School Announcements"
SENDER_PASSWORD = "your_password"  # Replace with your email password (use environment variables in production)

def send_email(recipient_email, recipient_name, subject, message_body):
    """
    Sends an email to the specified recipient with the provided subject and message body.

    Args:
        recipient_email (str): The email address of the recipient.
        recipient_name (str): The name of the recipient.
        subject (str): The subject of the email.
        message_body (str): The body of the email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = formataddr((recipient_name, recipient_email))
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            # Start TLS for security
            server.starttls()
            # Login to the server
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            # Send the email
            server.send_message(msg)
            return True

    except Exception as e:
        # Log the error (you may want to use a logging library in production)
        print(f"Error sending email to {recipient_email}: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # List of recipients (replace with actual data)
    recipients = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"}
    ]

    # Subject and message body
    email_subject = "Important School Announcement"
    email_body = (
        "Dear Parent,\n\nWe wanted to inform you about an upcoming event at our school.\n"
        "Please check the school portal for more details.\n\nBest Regards,\nSchool Administration"
    )

    # Send emails to each recipient
    for recipient in recipients:
        success = send_email(
            recipient_email=recipient["email"],
            recipient_name=recipient["name"],
            subject=email_subject,
            message_body=email_body
        )
        if success:
            print(f"Email successfully sent to {recipient['name']} ({recipient['email']})")
        else:
            print(f"Failed to send email to {recipient['name']} ({recipient['email']})")
```

**Note:** 
- Replace `your_email@example.com` and `your_password` with valid credentials. Use environment variables or secure credential management for passwords in production environments.
- Ensure the SMTP server and port match your email provider's configuration.
