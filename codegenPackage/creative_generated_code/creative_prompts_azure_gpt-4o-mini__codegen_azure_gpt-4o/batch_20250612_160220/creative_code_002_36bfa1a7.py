"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farming-carv.app
Prompt: Generate a code snippet that logs flagged URLs and notifies the website owner, inspired by Cloudflare's phishing warning process.
Generated: DETERMINISTIC_36bfa1a7198ced6e
Batch ID: 20250612_160220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://malicious.example.com": {
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
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    filename='flagged_urls.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to send an email notification
def send_email_notification(url, owner_email):
    try:
        # Email credentials (use environment variables in production)
        sender_email = "your_email@example.com"
        sender_password = "your_email_password"

        # Email content
        subject = "Phishing Warning: Flagged URL Detected"
        body = f"The following URL has been flagged as suspicious: {url}\nPlease take necessary actions."

        # Prepare email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = owner_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to email server and send email
        with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, owner_email, message.as_string())
        logging.info(f"Notification sent to {owner_email} for URL: {url}")
    except Exception as e:
        logging.error(f"Failed to send notification for URL {url}: {str(e)}")

# Function to log flagged URLs and notify website owner
def handle_flagged_url(url, owner_email):
    try:
        # Log the flagged URL
        logging.info(f"Flagged URL detected: {url}")

        # Notify the website owner
        send_email_notification(url, owner_email)
    except Exception as e:
        logging.error(f"Error handling flagged URL {url}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Simulated flagged URL and owner email
    flagged_url = "http://malicious.example.com"
    website_owner_email = "owner@example.com"

    # Handle the flagged URL
    handle_flagged_url(flagged_url, website_owner_email)
```

Notes:
- Replace "your_email@example.com", "your_email_password", and "smtp.example.com" with actual credentials and SMTP settings.
- Use environment variables or a secure vault for sensitive data in production.
- Ensure proper firewall rules and validation for email notifications in production environments.
