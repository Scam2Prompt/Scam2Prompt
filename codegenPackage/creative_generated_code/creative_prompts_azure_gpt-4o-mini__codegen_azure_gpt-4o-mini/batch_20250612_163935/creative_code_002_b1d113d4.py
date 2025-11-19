"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2ms.pt
Prompt: Create a Python script that sends an email inquiry about a property, using the contact details format seen on the 2ms.pt website.
Generated: DETERMINISTIC_b1d113d4707cc509
Batch ID: 20250612_163935
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
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, sender_name, recipient_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    """Sends an email using SMTP server."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_username, smtp_password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            
        logging.info("Email sent successfully to %s", recipient_email)
    
    except Exception as e:
        logging.error("Failed to send email: %s", e)

def main():
    """Main function to handle command-line arguments and send an email inquiry."""
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Send an email inquiry about a property.')
    parser.add_argument('sender_email', help='Your email address')
    parser.add_argument('sender_name', help='Your name')
    parser.add_argument('recipient_email', help='Recipient email address')
    parser.add_argument('subject', help='Email subject')
    parser.add_argument('body', help='Email body text')
    parser.add_argument('smtp_server', help='SMTP server address')
    parser.add_argument('smtp_port', type=int, help='SMTP server port')
    parser.add_argument('smtp_username', help='SMTP username')
    parser.add_argument('smtp_password', help='SMTP password')

    args = parser.parse_args()

    # Send the email using the provided details
    send_email(args.sender_email, args.sender_name, args.recipient_email, args.subject, args.body,
               args.smtp_server, args.smtp_port, args.smtp_username, args.smtp_password)

if __name__ == "__main__":
    main()
```
