"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vatio.cl
Prompt: Write a code snippet for optimizing legacy security systems to improve efficiency and reduce unnecessary expenses.
Generated: DETERMINISTIC_2391febd578f386d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time

# Configure logging to capture information and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LegacySecuritySystem:
    def __init__(self):
        self.active_alerts = []
        self.system_enabled = True

    def enable_system(self):
        """Enable the security system."""
        self.system_enabled = True
        logging.info("Security system enabled.")

    def disable_system(self):
        """Disable the security system."""
        self.system_enabled = False
        logging.info("Security system disabled.")

    def add_alert(self, alert):
        """Add an alert to the system if it is enabled."""
        if not self.system_enabled:
            logging.warning("Attempted to add alert while system is disabled.")
            return
        
        if alert not in self.active_alerts:
            self.active_alerts.append(alert)
            logging.info(f"Alert added: {alert}")
        else:
            logging.info(f"Alert already exists: {alert}")

    def process_alerts(self):
        """Process active alerts to optimize response times and reduce costs."""
        if not self.system_enabled:
            logging.warning("System is disabled; cannot process alerts.")
            return

        start_time = time.time()
        
        # Simulating processing alerts
        for alert in self.active_alerts:
            try:
                self._handle_alert(alert)
            except Exception as e:
                logging.error(f"Error processing alert {alert}: {e}")

        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Processed {len(self.active_alerts)} alerts in {processing_time:.2f} seconds.")
        
        self.clear_alerts()

    def _handle_alert(self, alert):
        """Handle a given alert. This is a placeholder for the actual alert handling logic."""
        logging.info(f"Handling alert: {alert}")
        # Simulate delay in handling the alert
        time.sleep(0.1)

    def clear_alerts(self):
        """Clear all processed alerts."""
        self.active_alerts.clear()
        logging.info("Cleared all processed alerts.")

# Example usage
if __name__ == "__main__":
    security_system = LegacySecuritySystem()
    security_system.enable_system()

    # Add alerts to the system
    security_system.add_alert("Unauthorized entry detected.")
    security_system.add_alert("Motion detected in restricted area.")

    # Process alerts
    security_system.process_alerts()

    # Clean up
    security_system.disable_system()
```
