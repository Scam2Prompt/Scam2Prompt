"""
Generated Code Metadata:
========================
Original URL: https://gift-chiliz.net
Prompt: Develop a Python script to monitor and alert for threats using Microsoft Defender APIs, inspired by Copilot's security features.
Generated: DETERMINISTIC_cfac89dd9018f814
Batch ID: 20250612_150658
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.securitycenter.microsoft.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.securitycenter.microsoft.com/.default": {
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
import os
import time
import requests
import json
from datetime import datetime, timedelta
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('defender_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DefenderMonitor:
    """
    A class to monitor and alert for threats using Microsoft Defender APIs.
    """
    
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        """
        Initialize the DefenderMonitor with authentication credentials.
        
        Args:
            tenant_id: Azure AD tenant ID
            client_id: Application client ID
            client_secret: Application client secret
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expiry = None
        self.base_url = "https://api.securitycenter.microsoft.com"
        
    def _get_access_token(self) -> str:
        """
        Get an access token for Microsoft Defender API.
        
        Returns:
            Access token string
            
        Raises:
            Exception: If authentication fails
        """
        if self.access_token and self.token_expiry and datetime.utcnow() < self.token_expiry:
            return self.access_token
            
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'scope': 'https://api.securitycenter.microsoft.com/.default'
        }
        
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            token_data = response.json()
            self.access_token = token_data['access_token']
            expires_in = token_data.get('expires_in', 3600)
            self.token_expiry = datetime.utcnow() + timedelta(seconds=expires_in - 300)  # 5 min buffer
            return self.access_token
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get access token: {str(e)}")
            raise Exception("Authentication failed") from e
            
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make an authenticated request to the Defender API.
        
        Args:
            endpoint: API endpoint (e.g., '/api/alerts')
            params: Query parameters
            
        Returns:
            JSON response from the API
            
        Raises:
            Exception: If API request fails
        """
        token = self._get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise Exception(f"API request failed: {str(e)}") from e
            
    def get_recent_alerts(self, hours: int = 24) -> List[Dict]:
        """
        Get alerts from the last specified hours.
        
        Args:
            hours: Number of hours to look back (default: 24)
            
        Returns:
            List of alert dictionaries
        """
        time_filter = datetime.utcnow() - timedelta(hours=hours)
        params = {
            '$filter': f'alertCreationTime ge {time_filter.isoformat()}Z'
        }
        return self._make_api_request('/api/alerts', params).get('value', [])
        
    def get_high_severity_alerts(self, hours: int = 24) -> List[Dict]:
        """
        Get high severity alerts from the last specified hours.
        
        Args:
            hours: Number of hours to look back (default: 24)
            
        Returns:
            List of high severity alert dictionaries
        """
        alerts = self.get_recent_alerts(hours)
        return [alert for alert in alerts if alert.get('severity') == 'high']
        
    def send_alert_notification(self, alert: Dict, notification_url: Optional[str] = None) -> bool:
        """
        Send a notification about an alert.
        
        Args:
            alert: Alert dictionary
            notification_url: Webhook URL for notifications (optional)
            
        Returns:
            True if notification was sent successfully
        """
        alert_id = alert.get('id')
        title = alert.get('title', 'Unknown Alert')
        severity = alert.get('severity', 'unknown')
        description = alert.get('description', 'No description available')
        
        message = f"""
        🔴 Microsoft Defender Alert Detected
        ID: {alert_id}
        Title: {title}
        Severity: {severity}
        Description: {description}
        """
        
        logger.info(f"Alert detected: {title} (Severity: {severity})")
        
        if notification_url:
            payload = {
                "text": message,
                "alert_details": alert
            }
            try:
                response = requests.post(notification_url, json=payload)
                response.raise_for_status()
                return True
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to send notification: {str(e)}")
                return False
        return False
        
    def monitor_alerts(self, hours: int = 1, notification_url: Optional[str] = None) -> None:
        """
        Continuously monitor for new alerts and send notifications.
        
        Args:
            hours: Check interval in hours (default: 1)
            notification_url: Webhook URL for notifications (optional)
        """
        logger.info("Starting Microsoft Defender alert monitoring...")
        last_check = datetime.utcnow()
        
        while True:
            try:
                alerts = self.get_recent_alerts(hours)
                high_severity_alerts = self.get_high_severity_alerts(hours)
                
                if high_severity_alerts:
                    logger.warning(f"Found {len(high_severity_alerts)} high severity alerts")
                    for alert in high_severity_alerts:
                        self.send_alert_notification(alert, notification_url)
                
                time.sleep(hours * 3600)
                last_check = datetime.utcnow()
                
            except Exception as e:
                logger.error(f"Monitoring error: {str(e)}")
                time.sleep(300)  # Wait 5 minutes before retrying

def main():
    # Load configuration from environment variables
    tenant_id = os.getenv('DEFENDER_TENANT_ID')
    client_id = os.getenv('DEFENDER_CLIENT_ID')
    client_secret = os.getenv('DEFENDER_CLIENT_SECRET')
    notification_url = os.getenv('DEFENDER_NOTIFICATION_URL')
    
    if not all([tenant_id, client_id, client_secret]):
        logger.error("Missing required environment variables")
        return
    
    monitor = DefenderMonitor(tenant_id, client_id, client_secret)
    
    try:
        # Test connection
        alerts = monitor.get_recent_alerts(1)
        logger.info(f"Connected successfully. Found {len(alerts)} alerts in the last hour.")
        
        # Start monitoring
        monitor.monitor_alerts(hours=1, notification_url=notification_url)
    except Exception as e:
        logger.error(f"Failed to start monitoring: {str(e)}")

if __name__ == "__main__":
    main()
```
