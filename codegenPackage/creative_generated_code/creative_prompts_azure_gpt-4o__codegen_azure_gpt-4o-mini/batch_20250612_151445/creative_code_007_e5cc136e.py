"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockbook.btc-2.zelcore.io
Prompt: Generate a Python program that monitors the "Last Mempool Update" time from the Blockbook API and sends an alert if the update exceeds a specified threshold.
Generated: DETERMINISTIC_e5cc136e23c6e589
Batch ID: 20250612_151445
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blockbook.api.example.com/api/v2/status": {
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
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
BLOCKBOOK_API_URL = "https://blockbook.api.example.com/api/v2/status"  # Replace with actual Blockbook API URL
ALERT_THRESHOLD = 300  # seconds, e.g., 5 minutes
CHECK_INTERVAL = 60  # seconds, how often to check the API
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
ALERT_RECIPIENT = "recipient_email@example.com"  # Replace with the alert recipient's email

def send_alert_email(last_update_time):
    """Send an alert email when the last update exceeds the threshold."""
    subject = "Alert: Last Mempool Update Exceeded Threshold"
    body = f"The last mempool update time is {last_update_time}, which exceeds the threshold of {ALERT_THRESHOLD} seconds."
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with SMTP server details
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Alert email sent to {ALERT_RECIPIENT}.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def check_last_mempool_update():
    """Check the last mempool update time from the Blockbook API."""
    try:
        response = requests.get(BLOCKBOOK_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Assuming the API response contains a 'lastMempoolUpdate' field in ISO 8601 format
        last_update_time_str = data.get('lastMempoolUpdate')
        if last_update_time_str:
            last_update_time = datetime.fromisoformat(last_update_time_str.replace("Z", "+00:00"))
            return last_update_time
        else:
            print("Error: 'lastMempoolUpdate' field not found in API response.")
            return None
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return None

def monitor_mempool_update():
    """Monitor the last mempool update and send alerts if it exceeds the threshold."""
    while True:
        last_update_time = check_last_mempool_update()
        if last_update_time:
            current_time = datetime.utcnow()
            time_since_update = (current_time - last_update_time).total_seconds()
            
            if time_since_update > ALERT_THRESHOLD:
                send_alert_email(last_update_time)
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_mempool_update()
```
