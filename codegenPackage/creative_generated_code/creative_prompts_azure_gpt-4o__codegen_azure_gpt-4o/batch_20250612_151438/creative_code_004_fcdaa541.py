"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minecraft-playgo.ru
Prompt: Develop a script to send an email to the support team at support@minecraft-playgo.ru with a technical inquiry, referencing the contact details provided on the site.
Generated: DETERMINISTIC_fcdaa541b721eec4
Batch ID: 20250612_151438
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
import sys

def send_email(to_email, subject, body, from_email, smtp_server, smtp_port, username, password):
    """
    Sends an email using the specified SMTP server.

    :param to_email: Recipient email address
    :param subject: Subject of the email
    :param body: Body of the email
    :param from_email: Sender email address
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param username: SMTP username for authentication
    :param password: SMTP password for authentication
    :return: None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to TLS
            server.login(username, password)
            server.send_message(message)
        
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Configuration for the email (update these with actual values)
TO_EMAIL = "support@minecraft-playgo.ru"
SUBJECT = "Technical Inquiry"
BODY = """
Hello support team,

I am contacting you regarding a technical inquiry. Please provide assistance or further details.

Thank you,
[Your Name]
"""
FROM_EMAIL = "your_email@example.com"  # Replace with your email
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
USERNAME = "your_email@example.com"  # Replace with your email login
PASSWORD = "your_password"  # Replace with your email password

# Send the email
send_email(TO_EMAIL, SUBJECT, BODY, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
```
