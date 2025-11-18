"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Create a script that automates alerts for crypto scams using a unique notification system, inspired by the scam detection features mentioned on the Champs Only website.
Generated: DETERMINISTIC_557111cbf6d18a13
Batch ID: 20250612_145228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/scam-reports": {
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
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for the notification system
CRYPTO_SCAM_URL = "https://example.com/scam-reports"  # Replace with the actual URL
CHECK_INTERVAL = 300  # Time in seconds between checks
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECIPIENT_EMAIL = "recipient@example.com"  # Recipient email for alerts

def fetch_scam_reports():
    """Fetches the latest crypto scam reports from the specified URL."""
    try:
        response = requests.get(CRYPTO_SCAM_URL)
        response.raise_for_status()  # Raise an error for bad responses
        logging.info("Successfully fetched scam reports.")
        return parse_scam_reports(response.text)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching scam reports: {e}")
        return []

def parse_scam_reports(html_content):
    """Parses the HTML content to extract scam reports."""
    soup = BeautifulSoup(html_content, 'html.parser')
    scams = []
    for scam in soup.find_all('div', class_='scam-report'):  # Adjust based on actual HTML structure
        scam_title = scam.find('h2').get_text(strip=True)
        scam_link = scam.find('a')['href']
        scams.append({'title': scam_title, 'link': scam_link})
    return scams

def send_email_alert(scam):
    """Sends an email alert for a detected scam."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Alert: New Crypto Scam Detected - {scam['title']}"

        body = f"A new scam has been reported: {scam['title']}\nDetails: {scam['link']}"
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()  # Use TLS for security
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f"Email alert sent for scam: {scam['title']}")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

def monitor_scams(known_scams):
    """Continuously monitors for new scams and sends alerts."""
    while True:
        current_scams = fetch_scam_reports()
        new_scams = [scam for scam in current_scams if scam not in known_scams]

        for scam in new_scams:
            send_email_alert(scam)

        known_scams.update(current_scams)  # Update known scams to include newly detected ones
        time.sleep(CHECK_INTERVAL)

def main():
    """Main entry point of the script."""
    logging.info("Starting crypto scam alert system.")
    known_scams = set()  # Initialize an empty set to store known scams
    monitor_scams(known_scams)

if __name__ == "__main__":
    main()
```
