"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happychex.com
Prompt: Generate a script to check if a domain is linked to a directory on a server and send an alert if it is not.
Generated: DETERMINISTIC_256dd57a8023f4a1
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
DOMAINS = ["example.com", "test.com", "mydomain.com"]  # List of domains to check
SERVER_DIRECTORY_PATH = "/var/www/html"  # Base directory where domains should be linked
ALERT_EMAIL = "admin@example.com"  # Email to send alerts to
SMTP_SERVER = "smtp.example.com"  # SMTP server for sending emails
SMTP_PORT = 587  # Port for SMTP server
SMTP_USERNAME = "your-email@example.com"
SMTP_PASSWORD = "your-email-password"

def is_domain_linked(domain, base_directory):
    """
    Check if the domain has a corresponding directory linked on the server.
    
    Args:
        domain (str): The domain name to check.
        base_directory (str): The base directory path where domains should be linked.

    Returns:
        bool: True if the domain is linked to a directory, False otherwise.
    """
    domain_path = os.path.join(base_directory, domain)
    return os.path.exists(domain_path) and os.path.isdir(domain_path)

def send_alert(email, domain):
    """
    Send an alert email if a domain is not linked to a directory.
    
    Args:
        email (str): Email address to send the alert to.
        domain (str): The domain name that was not linked.
    """
    try:
        # Create email message
        subject = f"Alert: Missing Directory for {domain}"
        body = f"The domain '{domain}' is not linked to any directory on the server."
        
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email using SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, email, msg.as_string())
    
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to check domains and send alerts for missing directories.
    """
    for domain in DOMAINS:
        if not is_domain_linked(domain, SERVER_DIRECTORY_PATH):
            print(f"Alert: {domain} is not linked to a directory.")
            send_alert(ALERT_EMAIL, domain)

if __name__ == "__main__":
    main()
```
