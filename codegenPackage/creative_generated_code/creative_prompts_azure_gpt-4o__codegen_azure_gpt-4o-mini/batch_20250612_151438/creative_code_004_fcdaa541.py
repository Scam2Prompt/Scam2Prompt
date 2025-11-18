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
from email.utils import formataddr
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, sender_email, sender_name, recipient_email):
    """
    Sends an email to the specified recipient.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    sender_email (str): The email address of the sender.
    sender_name (str): The name of the sender.
    recipient_email (str): The email address of the recipient.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        smtp_server = 'smtp.example.com'  # Replace with your SMTP server
        smtp_port = 587                    # Commonly used port for TLS
        smtp_username = 'your_username'    # Replace with your SMTP username
        smtp_password = 'your_password'    # Replace with your SMTP password

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_username, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {recipient_email} successfully.')

    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    # Define the email details
    subject = 'Technical Inquiry'
    body = '''
    Dear Support Team,

    I am writing to inquire about the technical issues I have been experiencing.
    Please let me know if you require further details.

    Best regards,
    [Your Name]
    [Your Contact Details]
    '''
    sender_email = 'your_email@example.com'  # Replace with your email address
    sender_name = 'Your Name'                  # Replace with your name
    recipient_email = 'support@minecraft-playgo.ru'  # Support team email

    # Call the function to send the email
    send_email(subject, body, sender_email, sender_name, recipient_email)
```
**Note:** Replace placeholders (like 'smtp.example.com', 'your_username', 'your_password', etc.) with actual values before running the script.
