"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Develop a Python-based tool to monitor the collateralization ratio of MAI stablecoins in QiDao vaults and send alerts if the ratio approaches unsafe levels.
Generated: DETERMINISTIC_4ae55ed5be67fd27
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.qidao.org/vaults": {
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
from decimal import Decimal

# Configuration variables
QI_DAO_API_URL = "https://api.qidao.org/vaults"  # Placeholder URL; please replace with actual API endpoint
COLLATERALIZATION_THRESHOLD = Decimal("1.5")  # Example threshold for safe collateralization
CHECK_INTERVAL = 60  # Check every 60 seconds

# Email configuration for alerts
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASSWORD = "your_email_password"
ALERT_EMAIL = "alert_recipient@example.com"

def send_alert(message):
    """Send an alert email when collateralization ratio is unsafe."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'Collateralization Ratio Alert'
        msg['From'] = SMTP_USER
        msg['To'] = ALERT_EMAIL
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending alert email: {e}")

def get_vaults_data():
    """Fetch the vaults data from QiDao API."""
    try:
        response = requests.get(QI_DAO_API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Assuming the response is in JSON format
    except requests.RequestException as e:
        print(f"Error fetching vaults data: {e}")
        return None

def monitor_collateralization():
    """Monitor the collateralization ratio of MAI stablecoins in QiDao vaults."""
    while True:
        vaults_data = get_vaults_data()
        if vaults_data is None:
            time.sleep(CHECK_INTERVAL)  # Wait before retrying
            continue
        
        for vault in vaults_data:
            try:
                collateral_amount = Decimal(vault['collateralAmount'])
                debt_amount = Decimal(vault['debtAmount'])
                if debt_amount == 0:
                    continue  # Avoid division by zero

                collateralization_ratio = collateral_amount / debt_amount
                
                # Check if the collateralization ratio is approaching unsafe levels
                if collateralization_ratio < COLLATERALIZATION_THRESHOLD:
                    alert_message = (
                        f"Alert: Vault {vault['id']} has a low "
                        f"collateralization ratio of {collateralization_ratio:.2f}."
                    )
                    print(alert_message)  # Log to console
                    send_alert(alert_message)  # Send alert email
            except (KeyError, ValueError) as e:
                print(f"Error processing vault data: {e}")
        
        time.sleep(CHECK_INTERVAL)  # Wait before the next check

if __name__ == "__main__":
    monitor_collateralization()
```

Make sure to replace the placeholder SMTP server and email configurations with your actual email service details. Additionally, ensure that the QiDao API URL is correct as per your requirements.
