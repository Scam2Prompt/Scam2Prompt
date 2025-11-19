"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniapt.space
Prompt: How do I contact the server administrator for a 500 Internal Server Error issue, as mentioned for uniapt.space?
Generated: DETERMINISTIC_87585a5bc631e4a2
Batch ID: 20250612_161427
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

def send_error_report(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Send an email to the server administrator about a 500 Internal Server Error.

    Parameters:
    subject (str): The subject of the email.
    message (str): The body of the email containing error details.
    from_email (str): The sender's email address.
    to_email (str): The recipient's email address (server administrator).
    smtp_server (str): The SMTP server address.
    smtp_port (int): The port to use for the SMTP server.
    smtp_user (str): The SMTP username.
    smtp_password (str): The SMTP password.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Set up the server connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable security
            server.login(smtp_user, smtp_password)  # Log in to the server
            server.sendmail(from_email, to_email, msg.as_string())  # Send the email

        print("Error report sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send error report: {e}")

if __name__ == "__main__":
    # Example usage
    subject = "500 Internal Server Error on uniapt.space"
    message = "There was a 500 Internal Server Error when accessing the website uniapt.space. Please investigate the issue."
    from_email = "your_email@example.com"
    to_email = "admin@uniapt.space"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    send_error_report(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password)
```
