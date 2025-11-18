"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-support-number-pro.blogspot.com
Prompt: Write a Python script to send an email to support@coinbase.com with a predefined message template for reporting a hacked account issue.
Generated: DETERMINISTIC_da4b6fa2386a5f05
Batch ID: 20250612_154131
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email, subject, body):
    """
    Function to send email using SMTP.
    
    Parameters:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    
    Returns:
        None
    """
    try:
        # SMTP server configuration
        smtp_server = 'smtp.example.com'  # Replace with your SMTP server
        smtp_port = 587  # For starttls
        smtp_user = 'your_email@example.com'  # Replace with your email
        smtp_password = 'your_password'  # Replace with your email password

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            logging.info(f'Email sent successfully to {to_email}')

    except Exception as e:
        logging.error(f'Failed to send email: {str(e)}')

def main():
    """
    Main function to execute the email sending process.
    
    Returns:
        None
    """
    to_email = 'support@coinbase.com'
    subject = 'Account Hacked - Immediate Assistance Required'
    body = (
        "Dear Coinbase Support,\n\n"
        "I am writing to report that my account has been hacked. "
        "I noticed unauthorized transactions and I am concerned about the security of my account. "
        "Please assist me in recovering my account and securing it against further unauthorized access.\n\n"
        "Thank you for your prompt attention to this matter.\n\n"
        "Best regards,\n"
        "[Your Name]\n"
        "[Your Email]\n"
        "[Your Phone Number]"
    )

    # Send the email
    send_email(to_email, subject, body)

if __name__ == '__main__':
    main()
```
