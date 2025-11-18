"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Develop a script to monitor domain status and send alerts if the nameservers are not correctly configured for Hostinger.
Generated: DETERMINISTIC_158baa93feb2115a
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import dns.resolver

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_HOST = 'smtp.example.com'  # SMTP server
EMAIL_PORT = 587  # SMTP port
EMAIL_USER = 'alert@example.com'  # Sender email
EMAIL_PASS = 'your_password'  # Sender email password
ALERT_RECIPIENT = 'recipient@example.com'  # Recipient email for alerts

# Hostinger nameservers
EXPECTED_NAMESERVERS = [
    'ns1.hostinger.com',
    'ns2.hostinger.com',
    'ns3.hostinger.com',
    'ns4.hostinger.com'
]

def send_alert(domain):
    """Send an email alert if nameservers are not correctly configured."""
    subject = f"Domain Alert: Incorrect Nameservers for {domain}"
    body = f"The nameservers for {domain} are not configured correctly. Please check the settings."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = ALERT_RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, ALERT_RECIPIENT, msg.as_string())
            logging.info(f"Alert sent for {domain}.")
    except Exception as e:
        logging.error(f"Failed to send alert for {domain}. Error: {e}")

def check_nameservers(domain):
    """Check the nameservers of a given domain."""
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        nameservers = [str(ns) for ns in answers]
        logging.info(f"Nameservers for {domain}: {nameservers}")

        # Check if expected nameservers are in the response
        if not set(EXPECTED_NAMESERVERS).issubset(set(nameservers)):
            logging.warning(f"Nameservers for {domain} are incorrectly configured.")
            send_alert(domain)
        else:
            logging.info(f"Nameservers for {domain} are configured correctly.")

    except dns.resolver.NoAnswer:
        logging.error(f"No answer for nameserver query for {domain}.")
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
    except Exception as e:
        logging.error(f"Error checking nameservers for {domain}: {e}")

if __name__ == "__main__":
    # Example domain to monitor
    domain_to_monitor = 'yourdomain.com'
    check_nameservers(domain_to_monitor)
```

Make sure to replace placeholders in the email configuration with actual values before running the script.
