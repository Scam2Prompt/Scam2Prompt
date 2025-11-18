"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-defenderbot.app
Prompt: Create a script that uses Cloudflare's Trust & Safety API to log flagged phishing sites and send automated alerts to administrators.
Generated: DETERMINISTIC_99cc98619f5c6ba9
Batch ID: 20250612_153709
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/": {
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
import requests
import logging
import smtplib
from email.mime.text import MIMEText
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cloudflare API configuration
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4/"
API_TOKEN = "your_api_token_here"  # Replace with your Cloudflare API token
ADMIN_EMAIL = "admin@example.com"  # Replace with your administrator email

# Function to log flagged phishing sites
def log_flagged_sites():
    try:
        response = requests.get(
            f"{CLOUDFLARE_API_URL}trustsafety/phishing",
            headers={"Authorization": f"Bearer {API_TOKEN}"}
        )

        # Check for successful response
        response.raise_for_status()  # Raise an error for bad responses
        flagged_sites = response.json().get('result', [])

        if flagged_sites:
            logging.info("Flagged phishing sites retrieved successfully.")
            for site in flagged_sites:
                logging.info(f"Flagged site: {site['url']}")
                send_alert(site['url'])
        else:
            logging.info("No flagged phishing sites found.")

    except RequestException as e:
        logging.error(f"Error fetching flagged sites: {e}")

# Function to send alert to administrators
def send_alert(site_url):
    try:
        subject = "Alert: Flagged Phishing Site Detected"
        body = f"A phishing site has been flagged: {site_url}"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "noreply@example.com"  # Replace with a valid sender email
        msg["To"] = ADMIN_EMAIL

        # Send email using SMTP
        with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login("your_smtp_username", "your_smtp_password")  # Replace with your SMTP credentials
            server.sendmail(msg["From"], [ADMIN_EMAIL], msg.as_string())

        logging.info(f"Alert sent to {ADMIN_EMAIL} for flagged site: {site_url}")

    except Exception as e:
        logging.error(f"Error sending alert email: {e}")

if __name__ == "__main__":
    log_flagged_sites()
```

**Note:** Make sure to replace placeholders like `your_api_token_here`, `admin@example.com`, `smtp.example.com`, and SMTP credentials with actual values before running the script.
