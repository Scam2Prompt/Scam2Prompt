"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Create a Python script to send an email request for an invitation letter to the conference secretary, including all necessary travel visa details as outlined on the Conferences Global website.
Generated: DETERMINISTIC_8aaf4c0f1b9ef86d
Batch ID: 20250612_154452
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email: str, subject: str, body: str, attachment_path: str = None) -> None:
    """
    Sends an email with the specified subject and body.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body content of the email
    :param attachment_path: Optional file path to an attachment
    """
    from_email = "your_email@example.com"  # Replace with your email
    from_password = "your_password"          # Replace with your password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file if provided
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
                msg.attach(part)
        except IOError as e:
            logging.error(f"Could not open attachment file {attachment_path}: {e}")
            return

    # Set up the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server details
            server.starttls()  # Use TLS for security
            server.login(from_email, from_password)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {to_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Email details
    recipient_email = "conference_secretary@example.com"  # Replace with the actual recipient
    email_subject = "Request for Invitation Letter"
    email_body = """
    Dear Conference Secretary,

    I hope this message finds you well. I am writing to request an invitation letter for the upcoming conference. 
    Below are my travel visa details as required:

    - Full Name: John Doe
    - Nationality: CountryName
    - Passport Number: ABC123456
    - Date of Birth: YYYY-MM-DD
    - Purpose of Visit: Attending the Conference
    - Duration of Stay: From YYYY-MM-DD to YYYY-MM-DD

    I would greatly appreciate your assistance with this request.

    Thank you for your attention.

    Best regards,
    John Doe
    john.doe@example.com
    """

    # Send the email with optional attachment
    send_email(recipient_email, email_subject, email_body)
``` 

Note: Remember to replace placeholders such as `your_email@example.com`, `your_password`, `smtp.example.com`, and the recipient's email address with actual values before running the script. Ensure the use of secure methods to handle passwords and sensitive data in production.
