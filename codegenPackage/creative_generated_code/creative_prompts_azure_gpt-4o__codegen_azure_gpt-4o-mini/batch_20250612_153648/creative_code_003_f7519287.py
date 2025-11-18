"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.netlify.app
Prompt: Create a Python script to send automated email responses to form submissions, ensuring compliance with Acme's promise to avoid spam and allow easy unsubscription.
Generated: DETERMINISTIC_f7519287af6dbac8
Batch ID: 20250612_153648
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
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # For starttls
SMTP_USER = 'username@example.com'  # Replace with your email
SMTP_PASSWORD = 'password'  # Replace with your email password

# Email template
EMAIL_SUBJECT = "Thank you for your submission!"
EMAIL_BODY_TEMPLATE = """
Dear {name},

Thank you for reaching out to us. We have received your submission and will get back to you shortly.

If you wish to unsubscribe from future emails, please click here: [unsubscribe_link].

Best regards,
The Acme Team
"""

def send_email(recipient: str, name: str) -> None:
    """
    Sends an email response to the given recipient.

    :param recipient: Email address of the recipient
    :param name: Name of the recipient for personalization
    :raises ValueError: If the email format is invalid
    :raises Exception: For any other errors during email sending
    """
    # Validate email format
    if "@" not in recipient or "." not in recipient.split("@")[-1]: 
        logging.error("Invalid email address format: %s", recipient)
        raise ValueError(f"Invalid email address: {recipient}")

    msg = MIMEMultipart()
    msg['From'] = formataddr(('Acme Support', SMTP_USER))
    msg['To'] = recipient
    msg['Subject'] = EMAIL_SUBJECT

    # Personalize the email body
    email_body = EMAIL_BODY_TEMPLATE.format(name=name)
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            logging.info("Email sent to %s", recipient)
    except smtplib.SMTPException as e:
        logging.error("Failed to send email to %s: %s", recipient, str(e))
        raise Exception(f"Email sending failed: {str(e)}")

def process_form_submission(form_data: Dict[str, Any]) -> None:
    """
    Processes the form submission and sends an automated email response.

    :param form_data: Dictionary containing form data, must include 'email' and 'name'
    """
    try:
        recipient = form_data.get('email')
        name = form_data.get('name')
        
        if not recipient or not name:
            logging.error("Form data is missing 'email' or 'name': %s", form_data)
            raise ValueError("Form data must contain 'email' and 'name'.")
        
        send_email(recipient, name)
    except Exception as e:
        logging.error("Error processing form submission: %s", str(e))

# Example usage:
if __name__ == "__main__":
    form_submission_data = {
        'email': 'user@example.com',  # Replace with actual email from form submission
        'name': 'John Doe'  # Replace with actual name from form submission
    }
    
    process_form_submission(form_submission_data)
```
