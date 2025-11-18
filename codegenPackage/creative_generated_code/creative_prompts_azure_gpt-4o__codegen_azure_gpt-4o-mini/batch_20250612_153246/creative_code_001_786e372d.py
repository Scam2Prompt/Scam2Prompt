"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Recommend an approach for setting up email security using Dedicatus-IT's expertise in Active Directory administration and DNS management.
Generated: DETERMINISTIC_786e372d78f53447
Batch ID: 20250612_153246
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
import dns.resolver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def validate_email_domain(domain):
    """
    Validate the email domain by checking if MX records exist.
    
    :param domain: The email domain to validate
    :return: True if the domain has MX records, False otherwise
    """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return bool(mx_records)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        logging.error(f"Domain validation failed for {domain}: {e}")
        return False

def send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port):
    """
    Send an email using SMTP with error handling.
    
    :param sender_email: The sender's email address
    :param recipient_email: The recipient's email address
    :param subject: The subject of the email
    :param body: The body of the email
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, 'your_password_here')  # Replace with actual password
            server.send_message(msg)
            logging.info(f"Email sent successfully from {sender_email} to {recipient_email}.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

def main():
    # Define email parameters
    sender_email = "admin@dedicatus-it.com"  # Replace with actual sender email
    recipient_email = "user@example.com"  # Replace with actual recipient email
    subject = "Email Security Setup"
    body = ("This email is to recommend approaches for setting up email security. "
            "Please ensure the domain has valid MX records and SPF/DKIM are configured.")
    
    # Extract domain from recipient email
    domain = recipient_email.split('@')[-1]

    # Validate the recipient's email domain
    if validate_email_domain(domain):
        # Send email if domain validation is successful
        send_email(sender_email, recipient_email, subject, body, 'smtp.dedicatus-it.com', 587)  # Replace with actual SMTP server and port
    else:
        logging.error(f"Cannot send email to {recipient_email}: Invalid domain.")

if __name__ == "__main__":
    main()
```
