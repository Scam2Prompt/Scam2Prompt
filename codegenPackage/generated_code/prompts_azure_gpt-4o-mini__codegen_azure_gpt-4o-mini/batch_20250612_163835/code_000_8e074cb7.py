"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Generate a code snippet that implements an interactive warning system for mobile devices, focusing on product-specific alerts and safety notifications.
Generated: DETERMINISTIC_8e074cb7d5bb3ecc
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Alert:
    """Class to represent a product-specific alert."""
    
    def __init__(self, product_id: str, message: str, severity: str):
        self.product_id = product_id
        self.message = message
        self.severity = severity

    def to_dict(self) -> Dict[str, str]:
        """Convert the alert to a dictionary format for JSON serialization."""
        return {
            "product_id": self.product_id,
            "message": self.message,
            "severity": self.severity
        }

class AlertSystem:
    """Class to manage and send alerts to mobile devices."""
    
    def __init__(self):
        self.alerts: List[Alert] = []

    def add_alert(self, alert: Alert):
        """Add a new alert to the system."""
        self.alerts.append(alert)
        logging.info(f"Alert added: {alert.to_dict()}")

    def send_alerts(self):
        """Send all alerts to the mobile device."""
        for alert in self.alerts:
            try:
                self._send_alert_to_device(alert)
            except Exception as e:
                logging.error(f"Failed to send alert for product {alert.product_id}: {e}")

    def _send_alert_to_device(self, alert: Alert):
        """Simulate sending an alert to a mobile device."""
        # Here you would implement the actual sending logic (e.g., push notifications)
        logging.info(f"Sending alert to device: {json.dumps(alert.to_dict())}")

    def clear_alerts(self):
        """Clear all alerts from the system."""
        self.alerts.clear()
        logging.info("All alerts cleared.")

# Example usage
if __name__ == "__main__":
    alert_system = AlertSystem()
    
    # Create some sample alerts
    alert1 = Alert(product_id="12345", message="Battery overheating!", severity="high")
    alert2 = Alert(product_id="67890", message="Firmware update available.", severity="medium")
    
    # Add alerts to the system
    alert_system.add_alert(alert1)
    alert_system.add_alert(alert2)
    
    # Send alerts to mobile devices
    alert_system.send_alerts()
    
    # Clear alerts after sending
    alert_system.clear_alerts()
```
