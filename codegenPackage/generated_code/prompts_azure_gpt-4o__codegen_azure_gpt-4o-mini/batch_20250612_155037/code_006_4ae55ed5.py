"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Develop a Python-based tool to monitor the collateralization ratio of MAI stablecoins in QiDao vaults and send alerts if the ratio approaches unsafe levels.
Generated: DETERMINISTIC_4ae55ed5be67fd27
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.qidao.finance/vaults": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import time
import smtplib
from email.mime.text import MIMEText
from decimal import Decimal

# Constants
QI_DAO_VAULT_API_URL = "https://api.qidao.finance/vaults"  # Replace with the actual API endpoint
ALERT_THRESHOLD = Decimal('1.5')  # Set the collateralization ratio threshold
CHECK_INTERVAL = 300  # Time in seconds between checks
EMAIL_SENDER = "your_email@example.com"  # Replace with your email
EMAIL_RECEIVER = "alert_receiver@example.com"  # Replace with the receiver's email
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
SMTP_USERNAME = "your_email@example.com"  # Replace with your SMTP username
SMTP_PASSWORD = "your_email_password"  # Replace with your SMTP password

def fetch_vault_data():
    """Fetch the vault data from the QiDao API."""
    try:
        response = requests.get(QI_DAO_VAULT_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching vault data: {e}")
        return None

def calculate_collateralization_ratio(vault):
    """Calculate the collateralization ratio for a given vault."""
    try:
        collateral = Decimal(vault['collateral'])  # Replace with actual key
        debt = Decimal(vault['debt'])  # Replace with actual key
        return collateral / debt if debt > 0 else Decimal('0')
    except (KeyError, ValueError, ZeroDivisionError) as e:
        print(f"Error calculating collateralization ratio: {e}")
        return None

def send_alert(vault_name, ratio):
    """Send an alert email if the collateralization ratio is unsafe."""
    subject = f"Alert: Unsafe Collateralization Ratio for {vault_name}"
    body = f"The collateralization ratio for vault '{vault_name}' is {ratio:.2f}, which is below the safe threshold."
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Alert sent for vault '{vault_name}' with ratio {ratio:.2f}.")
    except Exception as e:
        print(f"Error sending alert email: {e}")

def monitor_vaults():
    """Monitor the collateralization ratios of all vaults and send alerts if necessary."""
    while True:
        vaults_data = fetch_vault_data()
        if vaults_data is None:
            time.sleep(CHECK_INTERVAL)
            continue

        for vault in vaults_data:
            vault_name = vault['name']  # Replace with actual key
            ratio = calculate_collateralization_ratio(vault)
            if ratio is not None and ratio < ALERT_THRESHOLD:
                send_alert(vault_name, ratio)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_vaults()
```
