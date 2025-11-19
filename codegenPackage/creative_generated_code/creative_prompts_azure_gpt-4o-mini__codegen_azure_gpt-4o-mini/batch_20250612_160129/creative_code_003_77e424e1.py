"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dtstradings.com
Prompt: Can you provide a sample email template to inquire about a suspended hosting account?
Generated: DETERMINISTIC_77e424e1f531bffd
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_suspension_inquiry(smtp_server, port, username, password, recipient_email):
    """
    Sends an email to inquire about a suspended hosting account.

    Args:
        smtp_server (str): The SMTP server address.
        port (int): The port number to use for the SMTP server.
        username (str): The email username for authentication.
        password (str): The email password for authentication.
        recipient_email (str): The recipient's email address.

    Raises:
        Exception: If unable to send the email.
    """

    # Create the email content
    subject = "Inquiry About Suspended Hosting Account"
    body = """
    Dear Support Team,

    I hope this message finds you well. I am writing to inquire about the status of my hosting account, which has been suspended. 

    Account details:
    - Username: [Your_Username]
    - Domain: [Your_Domain]

    I would appreciate your assistance in understanding the reason for the suspension and what steps I can take to resolve any issues.

    Thank you for your prompt attention to this matter.

    Best regards,
    [Your_Name]
    [Your_Contact_Information]
    """

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Log in to the email server
            server.send_message(message)  # Send the email
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        # Handle any SMTP exceptions
        print(f"Error sending email: {e}")
        raise

# Example usage
if __name__ == "__main__":
    send_email_suspension_inquiry(
        smtp_server="smtp.example.com",
        port=587,
        username="your_email@example.com",
        password="your_password",
        recipient_email="support@example.com"
    )
```
