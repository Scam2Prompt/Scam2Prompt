"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://odos.xyz-app.org
Prompt: Develop a program that monitors a directory index webpage (e.g., https://odos.xyz-app.org) for changes in file listings and sends alerts when new files are added.
Generated: DETERMINISTIC_508d34c3b86c6573
Batch ID: 20250612_153512

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://odos.xyz-app.org
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://odos.xyz-app.org": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import hashlib

# Configuration
DIRECTORY_URL = "https://odos.xyz-app.org"
CHECK_INTERVAL = 60  # seconds
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "receiver_email@example.com"
EMAIL_SUBJECT = "New File Alert"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_email_password"

# Function to fetch the directory listing
def fetch_directory_listing(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract file links (assuming they are in <a> tags)
        files = [a['href'] for a in soup.find_all('a', href=True)]
        return set(files)  # Return as a set for easy comparison
    except requests.RequestException as e:
        print(f"Error fetching directory listing: {e}")
        return set()

# Function to send email alerts
def send_email_alert(new_files):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = EMAIL_SUBJECT
        
        body = "New files added:\n" + "\n".join(new_files)
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print("Email alert sent.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main monitoring function
def monitor_directory():
    previous_files = fetch_directory_listing(DIRECTORY_URL)
    
    while True:
        time.sleep(CHECK_INTERVAL)  # Wait for the specified interval
        current_files = fetch_directory_listing(DIRECTORY_URL)
        
        # Determine new files by set difference
        new_files = current_files - previous_files
        
        if new_files:
            send_email_alert(new_files)
            previous_files = current_files  # Update the previous files list

# Entry point of the script
if __name__ == "__main__":
    monitor_directory()
```

**Note:** Make sure to replace the placeholder email and SMTP server details with your actual configuration before running the code.
