"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-etherfinance.app
Prompt: Generate a code snippet that logs phishing site alerts and notifies the website owner, referencing Cloudflare's Trust & Safety guidelines.
Generated: DETERMINISTIC_77aae7dc751d4002
Batch ID: 20250612_162601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://trust.cloudflare.com/api/v1/phishing-alerts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import logging
import smtplib
from email.mime.text import MIMEText
import requests
from requests.exceptions import HTTPError

# Configure logging
logging.basicConfig(
    filename='phishing_site_alerts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Cloudflare Trust & Safety API endpoint
CLOUDFLARE_API_URL = "https://trust.cloudflare.com/api/v1/phishing-alerts"

# Email notification settings
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_SENDER = "alerts@example.com"  # Replace with your sender email
EMAIL_PASSWORD = "yourpassword"  # Replace with your sender email password
EMAIL_RECIPIENT = "owner@example.com"  # Replace with the recipient email

def log_phishing_alert(domain: str):
    """
    Logs phishing site alerts and notifies the website owner via email.
    
    Args:
        domain (str): The domain of the suspected phishing site.
    """
    try:
        # Step 1: Log phishing site alert
        logging.info(f"Detected potential phishing site: {domain}")
        
        # Step 2: Submit the phishing site to Cloudflare Trust & Safety
        response = requests.post(
            CLOUDFLARE_API_URL,
            json={"domain": domain},
            timeout=10
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        
        # Step 3: Notify the website owner via email
        email_body = (
            f"Dear Website Owner,\n\n"
            f"We have detected a potential phishing site: {domain}\n"
            f"The report has been submitted to Cloudflare Trust & Safety.\n"
            f"Please take appropriate actions to safeguard your users.\n\n"
            f"Best regards,\nYour Security Monitoring Team"
        )
        msg = MIMEText(email_body)
        msg['Subject'] = f"Phishing Alert: {domain}"
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIPIENT

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        
        logging.info(f"Notification email sent to {EMAIL_RECIPIENT} regarding domain {domain}")

    except HTTPError as http_err:
        logging.error(f"HTTP error occurred while reporting to Cloudflare: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    # Replace 'example-phishing-site.com' with the suspicious domain
    suspicious_domain = "example-phishing-site.com"
    log_phishing_alert(suspicious_domain)
```
