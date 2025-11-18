"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Provide code for setting up a fire alarm system with automated alerts, based on the fire system services described by Inside Safety.
Generated: DETERMINISTIC_1acbffbd35105052
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
import time
import random

class FireAlarmSystem:
    def __init__(self, alert_email, check_interval=5):
        """
        Initializes the FireAlarmSystem with specified parameters.
        
        :param alert_email: Email address to send alerts to
        :param check_interval: Time interval (in seconds) to check the fire sensor
        """
        self.alert_email = alert_email
        self.check_interval = check_interval
        self.is_active = True

    def check_fire_sensor(self):
        """
        Simulates checking the fire sensor. 
        In a real-world application, this method would interface with hardware sensors.
        
        :return: True if fire is detected, False otherwise
        """
        # Simulate a fire detection mechanism (50% chance of detecting fire)
        return random.choice([True, False])

    def send_alert(self, message):
        """
        Sends an alert email with the provided message.
        
        :param message: The content of the email alert
        """
        try:
            # Setup the email server
            smtp_server = 'smtp.example.com'  # Update with your SMTP server
            smtp_port = 587  # Typical port for TLS
            smtp_user = 'your_email@example.com'  # Update with your email
            smtp_password = 'your_password'  # Update with your password
            
            # Create the email content
            msg = MIMEText(message)
            msg['Subject'] = 'Fire Alarm Alert'
            msg['From'] = smtp_user
            msg['To'] = self.alert_email
            
            # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
                
            print("Alert sent successfully.")

        except Exception as e:
            print(f"Error sending alert: {e}")

    def run(self):
        """
        Continuously monitors the fire sensor and sends alerts if fire is detected.
        This should be called in a separate thread or as a main process.
        """
        print("Fire Alarm System is active.")
        while self.is_active:
            if self.check_fire_sensor():
                alert_message = "Attention: Fire detected! Evacuate immediately!"
                self.send_alert(alert_message)
            else:
                print("No fire detected. System is monitoring.")
            time.sleep(self.check_interval)

    def deactivate(self):
        """
        Deactivates the fire alarm system.
        """
        self.is_active = False
        print("Fire Alarm System has been deactivated.")

# Example usage (this code would typically be run in a main block or separate thread)
if __name__ == "__main__":
    # Set up the fire alarm system with an alert email and a check interval of 5 seconds
    fire_alarm_system = FireAlarmSystem(alert_email='recipient@example.com', check_interval=5)
    try:
        fire_alarm_system.run()
    except KeyboardInterrupt:
        # Graceful shutdown on user interrupt
        fire_alarm_system.deactivate()
```

**Note:** Before running the code, you need to replace the SMTP server, email, and password placeholders with actual values relevant to your email service provider.
