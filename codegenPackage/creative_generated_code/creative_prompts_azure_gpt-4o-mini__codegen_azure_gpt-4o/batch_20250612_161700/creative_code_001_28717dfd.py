"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africafoodiesindustries.com
Prompt: Write a Python script that checks the expiration date of a website's domain and sends an alert if it is nearing suspension.
Generated: DETERMINISTIC_28717dfde94b1590
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import whois
import smtplib
from datetime import datetime, timedelta

# Configuration
ALERT_DAYS_THRESHOLD = 30  # Number of days before expiration to send an alert
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "alert@example.com"
EMAIL_PASSWORD = "your_password"  # Use environment variables or a secrets manager for production systems
EMAIL_RECIPIENT = "admin@example.com"
DOMAIN_TO_CHECK = "example.com"

def send_alert(domain, expiration_date):
    """
    Sends an email alert about a domain nearing expiration.
    Arguments:
        domain (str): The domain name.
        expiration_date (datetime): The expiration date of the domain.
    """
    subject = f"Alert: Domain {domain} Expiration Notice"
    body = f"The domain '{domain}' is nearing expiration on {expiration_date.strftime('%Y-%m-%d')}. Please take action to renew it."
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, message)
        print(f"Alert sent successfully for domain: {domain}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def check_domain_expiration(domain):
    """
    Checks the expiration date of a domain and sends an alert if it is nearing expiration.
    Arguments:
        domain (str): The domain name to check.
    """
    try:
        # Fetch domain information using the `whois` module
        domain_info = whois.whois(domain)
        expiration_date = domain_info.expiration_date
        
        # Handle cases where expiration_date is a list (some WHOIS services may return multiple dates)
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        
        # Ensure expiration_date is valid
        if not isinstance(expiration_date, datetime):
            print(f"Unable to determine expiration date for domain: {domain}")
            return
        
        # Calculate days until expiration
        days_until_expiration = (expiration_date - datetime.now()).days
        print(f"Domain: {domain}, Expiration Date: {expiration_date}, Days Until Expiration: {days_until_expiration}")
        
        # Send alert if the expiration date is within the threshold
        if days_until_expiration <= ALERT_DAYS_THRESHOLD:
            send_alert(domain, expiration_date)
        else:
            print("Domain is not nearing expiration.")
    except Exception as e:
        print(f"Error checking domain expiration: {e}")

# Main Execution
if __name__ == "__main__":
    check_domain_expiration(DOMAIN_TO_CHECK)
```
