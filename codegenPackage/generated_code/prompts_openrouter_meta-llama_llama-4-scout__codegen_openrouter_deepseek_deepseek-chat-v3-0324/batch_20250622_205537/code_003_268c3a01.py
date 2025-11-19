"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Generate a code snippet for a simple intruder alarm system using a microcontroller and sensors, including features like motion detection and alert notifications.
Generated: DETERMINISTIC_268c3a0144162d77
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Simple Intruder Alarm System
# Uses PIR sensor for motion detection and sends alerts via email

import time
import smtplib
from email.mime.text import MIMEText
import RPi.GPIO as GPIO  # Assuming Raspberry Pi

# Configuration
PIR_PIN = 17             # GPIO pin for PIR sensor
BUZZER_PIN = 18          # GPIO pin for buzzer
LED_PIN = 27             # GPIO pin for status LED

# Email settings
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'alarm@example.com'
EMAIL_PASSWORD = 'password'
RECIPIENT_EMAIL = 'owner@example.com'

# Alarm settings
ALARM_DURATION = 30      # Seconds
DEBOUNCE_TIME = 2        # Seconds

class IntruderAlarm:
    def __init__(self):
        self.alarm_triggered = False
        self.setup_gpio()
        
    def setup_gpio(self):
        """Initialize GPIO pins and sensors"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        
        # Initial state
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.LOW)
        
    def send_alert(self):
        """Send email notification"""
        try:
            msg = MIMEText("Intruder detected at your property!")
            msg['Subject'] = "ALERT: Intruder Detected"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECIPIENT_EMAIL
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                
        except Exception as e:
            print(f"Failed to send alert: {e}")
            
    def trigger_alarm(self):
        """Activate alarm system"""
        self.alarm_triggered = True
        print("ALARM TRIGGERED!")
        
        # Visual and audio indicators
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN, GPIO.HIGH)
        
        # Send alert
        self.send_alert()
        
        # Alarm duration
        time.sleep(ALARM_DURATION)
        self.reset_alarm()
        
    def reset_alarm(self):
        """Reset alarm system"""
        self.alarm_triggered = False
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("Alarm reset")
        
    def monitor(self):
        """Main monitoring loop"""
        print("Alarm system activated - Monitoring for intruders...")
        try:
            while True:
                if GPIO.input(PIR_PIN) and not self.alarm_triggered:
                    print("Motion detected!")
                    self.trigger_alarm()
                    time.sleep(DEBOUNCE_TIME)  # Debounce
                    
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("Alarm system deactivated")
            GPIO.cleanup()
            
if __name__ == "__main__":
    alarm = IntruderAlarm()
    alarm.monitor()
```
