"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolpalplatform.com
Prompt: Create a real-time notification system that alerts operators about critical pool updates, such as chemical imbalances or equipment failures, referencing PoolPal™ SCMC's alarm features.
Generated: DETERMINISTIC_9f8ba3518939a091
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import threading
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration for the notification system
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'alerts@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_RECIPIENTS = ['operator1@example.com', 'operator2@example.com']

# Define critical thresholds for pool conditions
CHEMICAL_THRESHOLD = {
    'pH': (7.2, 7.8),  # Acceptable pH range
    'Chlorine': (1.0, 3.0)  # Acceptable Chlorine range in ppm
}

# Simulated pool state
pool_state = {
    'pH': 7.4,
    'Chlorine': 2.0,
    'equipment_status': 'Operational'
}

class NotificationSystem:
    """A class that monitors pool conditions and sends alerts for critical updates."""
    
    def __init__(self):
        self.running = True

    def monitor_pool(self):
        """Continuously monitor the pool state in real-time."""
        while self.running:
            # Simulate updates to pool state
            self.update_pool_state()
            self.check_conditions()
            time.sleep(5)  # Check every 5 seconds

    def update_pool_state(self):
        """Simulate changes in pool conditions."""
        pool_state['pH'] = random.uniform(6.5, 8.5)  # Simulate pH change
        pool_state['Chlorine'] = random.uniform(0.5, 5.0)  # Simulate Chlorine change
        # Randomly simulate equipment failure
        if random.random() < 0.1:  # 10% chance of failure
            pool_state['equipment_status'] = 'Failure'
        else:
            pool_state['equipment_status'] = 'Operational'

    def check_conditions(self):
        """Check for critical pool conditions and send alerts if necessary."""
        if not self.is_within_threshold('pH', pool_state['pH']):
            self.send_alert(f'Critical Alert: pH level out of range: {pool_state["pH"]:.2f}')
        if not self.is_within_threshold('Chlorine', pool_state['Chlorine']):
            self.send_alert(f'Critical Alert: Chlorine level out of range: {pool_state["Chlorine"]:.2f}')
        if pool_state['equipment_status'] == 'Failure':
            self.send_alert('Critical Alert: Equipment failure detected!')

    def is_within_threshold(self, chemical, value):
        """Check if a given chemical value is within acceptable thresholds."""
        lower, upper = CHEMICAL_THRESHOLD[chemical]
        return lower <= value <= upper

    def send_alert(self, message):
        """Send an alert email to the specified recipients."""
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'PoolPal™ SCMC Alert'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = ', '.join(ALERT_RECIPIENTS)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENTS, msg.as_string())
            print(f'Alert sent: {message}')
        except Exception as e:
            print(f'Error sending alert: {e}')

    def stop_monitoring(self):
        """Stop the monitoring process."""
        self.running = False

if __name__ == "__main__":
    # Initialize and start the notification system
    notification_system = NotificationSystem()
    monitoring_thread = threading.Thread(target=notification_system.monitor_pool)
    
    try:
        monitoring_thread.start()
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        notification_system.stop_monitoring()
        monitoring_thread.join()
        print("Monitoring stopped.")
```
