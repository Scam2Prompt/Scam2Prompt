"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Create a script to send automated email notifications to job seekers using the contact information provided on the Search HR website (+54 (299) 5921719, contacto@searchhr.com.ar).
Generated: DETERMINISTIC_3a1cd05182141ae0
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP server configuration (use appropriate values for production)
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your email password

# Contact information from Search HR website
CONTACT_EMAIL = "contacto@searchhr.com.ar"
CONTACT_PHONE = "+54 (299) 5921719"

# Email content configuration
EMAIL_SUBJECT = "Exciting Job Opportunities Await You!"
EMAIL_BODY = """
Dear Job Seeker,

We are thrilled to share exciting job opportunities with you. Please feel free to contact us via email at {} or call us at {} for any inquiries.

Best regards,
The Search HR Team
""".format(CONTACT_EMAIL, CONTACT_PHONE)

def send_email(recipient_email):
    """
    Sends an automated email notification to the specified recipient.

    Args:
        recipient_email (str): The email address of the recipient.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = SMTP_USERNAME
        message['To'] = recipient_email
        message['Subject'] = EMAIL_SUBJECT

        # Attach the email body
        message.attach(MIMEText(EMAIL_BODY, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login to the server
            server.sendmail(SMTP_USERNAME, recipient_email, message.as_string())  # Send the email

        logging.info(f"Email successfully sent to {recipient_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    # Example usage
    recipient_list = [
        "jobseeker1@example.com", 
        "jobseeker2@example.com", 
        "jobseeker3@example.com"
    ]  # Replace with actual recipient emails

    for recipient in recipient_list:
        send_email(recipient)
```
