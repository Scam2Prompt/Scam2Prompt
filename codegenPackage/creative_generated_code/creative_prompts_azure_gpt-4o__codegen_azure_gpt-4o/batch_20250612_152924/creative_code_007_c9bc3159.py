"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wornholes.com
Prompt: Write code to monitor the availability of Matanga onion links (e.g., matannvya6ym7aki6kuusxyeiz4m24igwcvakcs5sujcny4u5txzs6id.onion) and send alerts when links are down, as discussed on https://wornholes.com.
Generated: DETERMINISTIC_c9bc3159719c8d2d
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://matannvya6ym7aki6kuusxyeiz4m24igwcvakcs5sujcny4u5txzs6id.onion": {
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

# Configuration
ONION_LINKS = [
    "http://matannvya6ym7aki6kuusxyeiz4m24igwcvakcs5sujcny4u5txzs6id.onion",
    # Add more onion links here
]
CHECK_INTERVAL = 300  # Time between checks in seconds
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "alert_receiver@example.com"

def send_email_alert(link):
    """
    Sends an email alert if an onion link is detected as down.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"Onion Link Down Alert: {link}"

        body = f"The following onion link is down: {link}"
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email alert: {e}")

def check_onion_links():
    """
    Checks the availability of onion links and sends an alert if they are down.
    """
    for link in ONION_LINKS:
        try:
            # Use the Tor network proxy to reach .onion links
            proxies = {
                "http": "socks5h://127.0.0.1:9050",
                "https": "socks5h://127.0.0.1:9050"
            }

            response = requests.get(link, proxies=proxies, timeout=10)
            if response.status_code == 200:
                print(f"[INFO] {link} is UP.")
            else:
                print(f"[WARNING] {link} is DOWN. Status Code: {response.status_code}")
                send_email_alert(link)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {link} is DOWN. Exception: {e}")
            send_email_alert(link)

def main():
    """
    Main function to monitor onion links periodically.
    """
    print("Starting Onion Link Monitor...")
    while True:
        check_onion_links()
        print(f"Sleeping for {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```

### Notes for Environment Setup:
1. Install the `requests` library: `pip install requests`.
2. This script assumes the Tor service is running locally on port `9050`.
3. Replace the SMTP configuration with valid email credentials and server details.
4. Be sure to keep sensitive information (e.g., email password) secure. Consider using environment variables or a secret management tool in production environments.
