"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: How can I implement an intrusion alarm system similar to those offered by Ray-Z Entreprise for residential security?
Generated: DETERMINISTIC_7dea45b5adf2c967
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

# Define constants
ALARM_LOG_FILE = "alarm_log.txt"
EMAIL_ALERTS_ENABLED = True
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "receiver_email@example.com"

# Simulated intrusion detection function
def detect_intrusion():
    """
    Simulates intrusion detection. Replace this logic with sensor input
    or device integration in a real-world scenario.
    Returns True if an intrusion is detected, False otherwise.
    """
    # Simulate intrusion detection (replace with actual hardware integration)
    return bool(time.time() % 10 < 1)  # Intrusion detected every 10 seconds for simulation

def sound_alarm():
    """
    Simulates sounding an alarm. Replace this with actual alarm activation hardware integration.
    """
    print("ALARM! Intrusion detected!")

def log_intrusion():
    """
    Logs the intrusion event to a file with a timestamp.
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ALARM_LOG_FILE, "a") as log_file:
            log_file.write(f"Intrusion detected at {timestamp}\n")
    except Exception as e:
        print(f"Error logging intrusion: {e}")

def send_email_alert():
    """
    Sends an email alert to the configured receiver about the intrusion.
    """
    try:
        msg = EmailMessage()
        msg.set_content("Intrusion detected! Check your premises immediately.")
        msg["Subject"] = "Intrusion Alert!"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        # Connect to the email server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Error sending email alert: {e}")

def intrusion_alarm_system():
    """
    Main function to monitor for intrusions and trigger the alarm system.
    """
    print("Starting intrusion alarm system...")
    try:
        while True:
            if detect_intrusion():
                sound_alarm()
                log_intrusion()
                if EMAIL_ALERTS_ENABLED:
                    send_email_alert()
            time.sleep(1)  # Adjust according to the sensitivity needed
    except KeyboardInterrupt:
        print("Intrusion alarm system stopped.")
    except Exception as e:
        print(f"Error in alarm system: {e}")

if __name__ == "__main__":
    intrusion_alarm_system()
```

### Notes:
- Replace `detect_intrusion()` logic with actual sensor input or hardware integration for a real production system.
- Update the email credentials (`EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECEIVER`) for your actual email configuration.
- Ensure you have enabled "Less Secure Apps" access or proper OAuth for Gmail, if using Gmail as the SMTP server.
- This is a basic implementation and should be extended with more robust features like secure storage of email credentials, advanced logging systems, and integration with physical alarms or surveillance systems.
