"""
Generated Code Metadata:
========================
Original URL: https://beefy-v2.vercel.app
Prompt: Generate a script to monitor and alert when the APY of a specific Beefy Finance vault changes significantly.
Generated: DETERMINISTIC_a4ab8d9ee9b956d8
Batch ID: 20250612_145933
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.beefy.finance": {
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
from email.mime.multipart import MIMEMultipart
import logging
from typing import Optional, Dict, Any

# Configuration
CONFIG = {
    "VAULT_ID": "your-vault-id",  # Replace with actual Beefy vault ID
    "BEEFY_API_URL": "https://api.beefy.finance",
    "CHECK_INTERVAL": 300,  # 5 minutes in seconds
    "APY_CHANGE_THRESHOLD": 0.5,  # 0.5% change threshold
    "SMTP_SERVER": "smtp.example.com",
    "SMTP_PORT": 587,
    "SMTP_USERNAME": "your-email@example.com",
    "SMTP_PASSWORD": "your-password",
    "ALERT_EMAILS": ["recipient@example.com"],
    "FROM_EMAIL": "your-email@example.com"
}

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('beefy_apy_monitor.log'),
        logging.StreamHandler()
    ]
)

class BeefyAPYMonitor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.last_apy: Optional[float] = None

    def fetch_vault_data(self) -> Optional[Dict[str, Any]]:
        """Fetch vault data from Beefy API."""
        try:
            url = f"{self.config['BEEFY_API_URL']}/vaults/{self.config['VAULT_ID']}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching vault data: {e}")
            return None

    def get_current_apy(self) -> Optional[float]:
        """Extract current APY from vault data."""
        vault_data = self.fetch_vault_data()
        if vault_data and 'apy' in vault_data:
            return float(vault_data['apy'])
        return None

    def calculate_apy_change(self, current_apy: float) -> float:
        """Calculate percentage change from last APY."""
        if self.last_apy is None:
            return 0.0
        return abs((current_apy - self.last_apy) / self.last_apy * 100)

    def send_alert(self, current_apy: float, change_percent: float) -> None:
        """Send email alert about significant APY change."""
        subject = f"ALERT: Significant APY Change in Beefy Vault {self.config['VAULT_ID']}"
        body = (
            f"Beefy Finance Vault {self.config['VAULT_ID']} APY has changed significantly.\n\n"
            f"Previous APY: {self.last_apy:.2f}%\n"
            f"Current APY: {current_apy:.2f}%\n"
            f"Change: {change_percent:.2f}%"
        )

        msg = MIMEMultipart()
        msg['From'] = self.config['FROM_EMAIL']
        msg['To'] = ", ".join(self.config['ALERT_EMAILS'])
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.config['SMTP_SERVER'], self.config['SMTP_PORT']) as server:
                server.starttls()
                server.login(self.config['SMTP_USERNAME'], self.config['SMTP_PASSWORD'])
                server.send_message(msg)
            logging.info("Alert email sent successfully")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send alert email: {e}")

    def run(self) -> None:
        """Main monitoring loop."""
        logging.info("Starting Beefy APY Monitor")
        while True:
            try:
                current_apy = self.get_current_apy()
                if current_apy is not None:
                    logging.info(f"Current APY: {current_apy:.2f}%")
                    
                    if self.last_apy is not None:
                        change_percent = self.calculate_apy_change(current_apy)
                        if change_percent >= self.config['APY_CHANGE_THRESHOLD']:
                            logging.warning(
                                f"Significant APY change detected: {change_percent:.2f}%"
                            )
                            self.send_alert(current_apy, change_percent)
                    
                    self.last_apy = current_apy
                else:
                    logging.warning("Failed to get current APY")

                time.sleep(self.config['CHECK_INTERVAL'])
            except Exception as e:
                logging.error(f"Unexpected error in monitoring loop: {e}")
                time.sleep(60)  # Wait before retrying after error

if __name__ == "__main__":
    monitor = BeefyAPYMonitor(CONFIG)
    monitor.run()
```
