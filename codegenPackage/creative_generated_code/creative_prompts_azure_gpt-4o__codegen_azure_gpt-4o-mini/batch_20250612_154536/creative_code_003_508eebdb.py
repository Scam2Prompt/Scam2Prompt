"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.optimism.rs
Prompt: Create a script to send an automated email inquiry to info@domainnames.rs about purchasing a domain, using the example domains listed on optimism.rs.
Generated: DETERMINISTIC_508eebdb46fbf5a2
Batch ID: 20250612_154536
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

# Email configuration
SMTP_SERVER = 'smtp.your_email_provider.com'  # Replace with your email provider's SMTP server
SMTP_PORT = 587  # Common port for SMTP
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_email_password'  # Replace with your email password
TO_EMAIL = 'info@domainnames.rs'  # Recipient email address

# Example domains to inquire about
example_domains = [
    'example1.optimism.rs',
    'example2.optimism.rs',
    'example3.optimism.rs'
]

def send_email(domain):
    """
    Sends an inquiry email about purchasing a specified domain.
    
    :param domain: The domain to inquire about.
    """
    # Create the email subject and body
    subject = f'Inquiry about purchasing the domain: {domain}'
    body = f'Dear Domain Name Team,\n\nI would like to inquire about the purchasing process for the domain: {domain}.\n\nThank you.\nBest regards,\nYour Name'

    # Set up the email structure
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.sendmail(USERNAME, TO_EMAIL, msg.as_string())  # Send the email
            print(f'Email sent successfully for domain: {domain}')
    except smtplib.SMTPException as e:
        print(f'Failed to send email for domain: {domain}. Error: {e}')

def main():
    """
    Main function to send inquiries for each example domain.
    """
    for domain in example_domains:
        send_email(domain)

if __name__ == '__main__':
    main()
```

**Note:** Replace SMTP_SERVER, USERNAME, and PASSWORD with your actual email configuration. Ensure your email provider allows SMTP access and that you handle sensitive information, such as email passwords, securely.
