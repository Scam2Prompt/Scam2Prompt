"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to automate sending an email to Eric Navarro using the contact information provided on his website, ensuring the email includes an attachment of a voiceover script.
Generated: DETERMINISTIC_5902b7aeae0a243a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'eric.navarro@example.com'  # Replace with Eric's email
SUBJECT = 'Voiceover Script Submission'
BODY = 'Dear Eric,\n\nPlease find attached the voiceover script.\n\nBest regards,\nYour Name'

def send_email_with_attachment(recipient, subject, body, attachment_path):
    """Send an email with an attachment."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        if os.path.isfile(attachment_path):
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(part)
        else:
            raise FileNotFoundError(f"The attachment file {attachment_path} does not exist.")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Path to the voiceover script attachment
    attachment_path = 'path/to/voiceover_script.txt'  # Replace with the actual path to the script

    # Send the email
    send_email_with_attachment(RECIPIENT_EMAIL, SUBJECT, BODY, attachment_path)
```
