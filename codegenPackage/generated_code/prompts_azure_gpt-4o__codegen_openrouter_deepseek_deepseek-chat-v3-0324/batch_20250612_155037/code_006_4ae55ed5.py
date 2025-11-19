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
  "https://api.qidao.com/api/v1/vaults": {
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
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('vault_monitor.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class VaultConfig:
    vault_id: str
    safe_ratio: float
    critical_ratio: float
    name: str

@dataclass
class VaultStatus:
    vault_id: str
    current_ratio: float
    collateral: float
    debt: float
    last_updated: str

class QiDaoMonitor:
    def __init__(self, config: List[VaultConfig], email_settings: Optional[Dict] = None):
        """
        Initialize the QiDao Monitor with vault configurations and optional email settings.
        
        Args:
            config: List of VaultConfig objects
            email_settings: Dictionary containing email configuration
        """
        self.vault_configs = {v.vault_id: v for v in config}
        self.email_settings = email_settings
        self.api_url = "https://api.qidao.com/api/v1/vaults"
        
    def fetch_vault_data(self) -> Dict[str, VaultStatus]:
        """
        Fetch current vault data from QiDao API.
        
        Returns:
            Dictionary mapping vault IDs to their current status
        """
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            vault_statuses = {}
            for vault in data:
                vault_id = str(vault['id'])
                if vault_id in self.vault_configs:
                    try:
                        ratio = float(vault['collateralizationRatio'])
                        collateral = float(vault['collateral'])
                        debt = float(vault['debt'])
                        last_updated = vault['lastUpdated']
                        
                        vault_statuses[vault_id] = VaultStatus(
                            vault_id=vault_id,
                            current_ratio=ratio,
                            collateral=collateral,
                            debt=debt,
                            last_updated=last_updated
                        )
                    except (KeyError, ValueError) as e:
                        logging.error(f"Error parsing vault {vault_id} data: {e}")
                        
            return vault_statuses
            
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return {}
    
    def check_ratios(self, vault_statuses: Dict[str, VaultStatus]) -> List[Dict]:
        """
        Check vault ratios against configured thresholds.
        
        Args:
            vault_statuses: Current vault statuses from API
            
        Returns:
            List of alerts for vaults approaching unsafe levels
        """
        alerts = []
        for vault_id, status in vault_statuses.items():
            config = self.vault_configs[vault_id]
            
            if status.current_ratio < config.critical_ratio:
                alert_level = "CRITICAL"
            elif status.current_ratio < config.safe_ratio:
                alert_level = "WARNING"
            else:
                continue
                
            alerts.append({
                'vault_id': vault_id,
                'vault_name': config.name,
                'current_ratio': status.current_ratio,
                'safe_ratio': config.safe_ratio,
                'critical_ratio': config.critical_ratio,
                'collateral': status.collateral,
                'debt': status.debt,
                'last_updated': status.last_updated,
                'alert_level': alert_level
            })
            
        return alerts
    
    def send_email_alert(self, alert: Dict) -> bool:
        """
        Send email alert for critical vault status.
        
        Args:
            alert: Alert dictionary containing vault details
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        if not self.email_settings:
            logging.warning("Email settings not configured, skipping email alert")
            return False
            
        try:
            subject = f"[{alert['alert_level']}] QiDao Vault Alert - {alert['vault_name']}"
            
            message = f"""
            QiDao Vault Monitoring Alert:
            
            Vault Name: {alert['vault_name']}
            Vault ID: {alert['vault_id']}
            Current Ratio: {alert['current_ratio']:.2f}%
            Safe Ratio: {alert['safe_ratio']:.2f}%
            Critical Ratio: {alert['critical_ratio']:.2f}%
            
            Collateral: {alert['collateral']:.2f}
            Debt: {alert['debt']:.2f}
            
            Last Updated: {alert['last_updated']}
            
            This is a {alert['alert_level']} level alert. Immediate action may be required.
            """
            
            msg = MIMEText(message.strip())
            msg['Subject'] = subject
            msg['From'] = self.email_settings['sender']
            msg['To'] = self.email_settings['recipient']
            
            with smtplib.SMTP(
                self.email_settings['smtp_server'],
                self.email_settings['smtp_port']
            ) as server:
                if self.email_settings.get('use_tls', True):
                    server.starttls()
                if 'smtp_username' in self.email_settings:
                    server.login(
                        self.email_settings['smtp_username'],
                        self.email_settings['smtp_password']
                    )
                server.send_message(msg)
                
            logging.info(f"Email alert sent for vault {alert['vault_id']}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send email alert: {e}")
            return False
    
    def run_monitoring_cycle(self):
        """
        Run a single monitoring cycle: fetch data, check ratios, send alerts.
        """
        logging.info("Starting monitoring cycle")
        
        vault_statuses = self.fetch_vault_data()
        if not vault_statuses:
            logging.error("No vault data received, skipping cycle")
            return
            
        alerts = self.check_ratios(vault_statuses)
        
        for alert in alerts:
            logging.warning(
                f"{alert['alert_level']} alert for vault {alert['vault_id']}: "
                f"Ratio {alert['current_ratio']:.2f}% (safe: {alert['safe_ratio']:.2f}%)"
            )
            self.send_email_alert(alert)
            
        logging.info(f"Monitoring cycle complete. {len(alerts)} alerts triggered.")

def main():
    # Example configuration - replace with your actual vaults and thresholds
    vault_configs = [
        VaultConfig(
            vault_id="1",
            safe_ratio=150.0,
            critical_ratio=120.0,
            name="ETH-A Vault"
        ),
        VaultConfig(
            vault_id="2",
            safe_ratio=200.0,
            critical_ratio=150.0,
            name="WBTC Vault"
        ),
        # Add more vaults as needed
    ]
    
    # Email configuration - set to None to disable email alerts
    email_settings = {
        'sender': 'alerts@yourdomain.com',
        'recipient': 'admin@yourdomain.com',
        'smtp_server': 'smtp.yourdomain.com',
        'smtp_port': 587,
        'smtp_username': 'your_username',
        'smtp_password': 'your_password',
        'use_tls': True
    }
    
    monitor = QiDaoMonitor(vault_configs, email_settings)
    
    # Run monitoring in a loop with 5 minute intervals
    while True:
        try:
            monitor.run_monitoring_cycle()
            time.sleep(300)  # 5 minutes
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error in monitoring loop: {e}")
            time.sleep(60)  # Wait 1 minute before retrying after error

if __name__ == "__main__":
    main()
```
