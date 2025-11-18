"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-ido-lake.vercel.app
Prompt: Develop a Python script to monitor and alert users about new IDOs listed on the Memes Pad SOL IDO platform.
Generated: DETERMINISTIC_a64bf11fe630f3dd
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.memespad.sol/idos": {
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
from datetime import datetime
from smtplib import SMTP
from email.message import EmailMessage

# Constants
MEMES_PAD_API_URL = "https://api.memespad.sol/idos"  # Replace with the actual API URL for Memes Pad SOL IDOs
CHECK_INTERVAL = 300  # Time in seconds between checks (5 minutes)
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_SENDER = "your_email@example.com"  # Replace with sender email address
EMAIL_PASSWORD = "your_email_password"  # Replace with sender email password
EMAIL_RECIPIENT = "recipient_email@example.com"  # Replace with recipient email address

# Function to fetch IDOs from Memes Pad API
def fetch_idos():
    try:
        response = requests.get(MEMES_PAD_API_URL, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad response status codes
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Error fetching IDOs: {e}")
        return None

# Function to send email alert
def send_email_alert(new_ido):
    try:
        # Create email message
        msg = EmailMessage()
        msg["Subject"] = f"New IDO Alert: {new_ido['name']}"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECIPIENT
        msg.set_content(
            f"New IDO listed on Memes Pad SOL:\n\n"
            f"Name: {new_ido['name']}\n"
            f"Description: {new_ido.get('description', 'N/A')}\n"
            f"Start Date: {new_ido.get('start_date', 'N/A')}\n"
            f"End Date: {new_ido.get('end_date', 'N/A')}\n"
            f"More Details: {new_ido.get('url', 'N/A')}\n"
        )

        # Send email
        with SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()  # Enable secure connection
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"[{datetime.now()}] Email sent for IDO: {new_ido['name']}")
    except Exception as e:
        print(f"[{datetime.now()}] Error sending email: {e}")

# Main monitoring loop
def monitor_idos():
    print(f"[{datetime.now()}] Starting IDO monitoring...")
    known_idos = set()  # Track already seen IDOs
    while True:
        idos = fetch_idos()
        if idos:
            for ido in idos:
                ido_id = ido.get("id")  # Assuming each IDO has a unique 'id'
                if ido_id and ido_id not in known_idos:
                    known_idos.add(ido_id)
                    send_email_alert(ido)  # Alert for new IDO
        time.sleep(CHECK_INTERVAL)

# Entry point
if __name__ == "__main__":
    try:
        monitor_idos()
    except KeyboardInterrupt:
        print(f"[{datetime.now()}] Monitoring stopped by user.")
    except Exception as e:
        print(f"[{datetime.now()}] Unexpected error: {e}")
```

### Notes:
- Replace the placeholder values (API URL, SMTP server, email credentials, etc.) with appropriate values.
- Ensure the external dependencies (`requests` library) are installed by running `pip install requests`.
- Configure appropriate logging mechanisms for production use instead of using `print` statements.
