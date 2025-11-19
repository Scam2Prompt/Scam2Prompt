"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Create a configuration plan for an intrusion alarm system with motion detection and remote monitoring capabilities for a residential client."
Generated: DETERMINISTIC_1a357c9bf598012b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Intrusion Alarm System Configuration Plan
This script sets up a configuration plan for an intrusion alarm system with motion detection
and remote monitoring capabilities for a residential client. It includes motion sensor setup,
alarm triggering, and remote monitoring via email notifications.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Configuration for the alarm system
class AlarmSystemConfig:
    def __init__(self):
        # Motion detection settings
        self.motion_sensitivity = 0.8  # Sensitivity level (0.0 to 1.0)
        self.motion_detection_enabled = True
        
        # Alarm settings
        self.alarm_duration = 30  # Duration in seconds
        self.alarm_enabled = True
        
        # Remote monitoring settings
        self.email_notifications_enabled = True
        self.email_server = "smtp.gmail.com"
        self.email_port = 587
        self.email_sender = "your_email@gmail.com"
        self.email_password = "your_password"  # Use environment variables in production
        self.email_recipient = "recipient_email@gmail.com"

# Motion detection simulation
def detect_motion(sensitivity):
    """
    Simulates motion detection. Returns True if motion is detected based on sensitivity.
    """
    import random
    return random.random() < sensitivity

# Trigger alarm
def trigger_alarm(duration):
    """
    Simulates triggering the alarm for the specified duration.
    """
    print("ALARM TRIGGERED! Sounding alarm...")
    time.sleep(duration)
    print("Alarm stopped.")

# Send email notification
def send_email_notification(config):
    """
    Sends an email notification to the recipient.
    """
    try:
        # Create email message
        message = MIMEMultipart()
        message["From"] = config.email_sender
        message["To"] = config.email_recipient
        message["Subject"] = "Intrusion Alert: Motion Detected"
        body = "Motion has been detected in your residence. Please check immediately."
        message.attach(MIMEText(body, "plain"))
        
        # Connect to email server and send email
        server = smtplib.SMTP(config.email_server, config.email_port)
        server.starttls()
        server.login(config.email_sender, config.email_password)
        server.sendmail(config.email_sender, config.email_recipient, message.as_string())
        server.quit()
        
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

# Main function to simulate the alarm system
def main():
    # Load configuration
    config = AlarmSystemConfig()
    
    print("Intrusion Alarm System Initialized.")
    print("Monitoring for motion...")
    
    try:
        while True:
            # Check for motion
            if config.motion_detection_enabled and detect_motion(config.motion_sensitivity):
                print("Motion detected!")
                
                # Trigger alarm
                if config.alarm_enabled:
                    trigger_alarm(config.alarm_duration)
                
                # Send email notification
                if config.email_notifications_enabled:
                    send_email_notification(config)
                
                # Break after handling one intrusion for simulation purposes
                break
            
            # Wait before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("System monitoring stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
