"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Write a Python script to automate sending an email to Eric Navarro using the contact information provided on his website, ensuring the email includes an attachment of a voiceover script.
Generated: DETERMINISTIC_5902b7aeae0a243a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import mimetypes
from email.message import EmailMessage
import os

def send_email_with_attachment(
    smtp_server, port, sender_email, sender_password, recipient_email, subject, body, attachment_path
):
    """
    Sends an email with an attachment to the specified recipient.

    :param smtp_server: SMTP server address (e.g., "smtp.gmail.com").
    :param port: SMTP server port (e.g., 587).
    :param sender_email: Sender's email address.
    :param sender_password: Sender's email password.
    :param recipient_email: Recipient's email address.
    :param subject: Email subject.
    :param body: Email body content.
    :param attachment_path: Path to the file to be attached.
    """
    try:
        # Create email message
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach the file
        if os.path.exists(attachment_path):
            file_type, _ = mimetypes.guess_type(attachment_path)
            main_type, sub_type = file_type.split('/') if file_type else ('application', 'octet-stream')

            with open(attachment_path, "rb") as file:
                msg.add_attachment(file.read(), maintype=main_type, subtype=sub_type, filename=os.path.basename(attachment_path))
        else:
            raise FileNotFoundError(f"Attachment file not found: {attachment_path}")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail's SMTP server
PORT = 587  # For TLS
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"  # Make sure to use environment variables or a secure method to store credentials
RECIPIENT_EMAIL = "eric.navarro@example.com"  # Replace with Eric Navarro's email address
SUBJECT = "Voiceover Script"
BODY = (
    "Hi Eric,\n\n"
    "Please find attached the voiceover script we discussed.\n\n"
    "Best regards,\nYour Name"
)
ATTACHMENT_PATH = "voiceover_script.pdf"  # Path to the voiceover script file

# Execute the function
send_email_with_attachment(
    SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY, ATTACHMENT_PATH
)
```
