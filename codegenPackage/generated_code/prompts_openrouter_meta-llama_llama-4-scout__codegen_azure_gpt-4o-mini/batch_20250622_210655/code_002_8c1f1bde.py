"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Generate code for a simple alarm system using Python and Raspberry Pi, inspired by the security solutions offered by Space Tecnologies in Bogotá."
Generated: DETERMINISTIC_8c1f1bde911fbd94
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configuration
PIR_PIN = 7  # GPIO pin for PIR motion sensor
ALARM_PIN = 11  # GPIO pin for alarm (buzzer)
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
ALERT_RECIPIENT = 'recipient_email@example.com'  # Replace with recipient email

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)  # Set PIR pin as input
GPIO.setup(ALARM_PIN, GPIO.OUT)  # Set alarm pin as output

def send_alert_email():
    """Send an alert email when motion is detected."""
    try:
        msg = MIMEText("Alert! Motion detected at {}".format(datetime.now()))
        msg['Subject'] = 'Security Alert'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_RECIPIENT

        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def activate_alarm():
    """Activate the alarm (buzzer) for a short duration."""
    try:
        GPIO.output(ALARM_PIN, GPIO.HIGH)  # Turn on the alarm
        time.sleep(5)  # Alarm duration
        GPIO.output(ALARM_PIN, GPIO.LOW)  # Turn off the alarm
    except Exception as e:
        print(f"Failed to activate alarm: {e}")

def main():
    """Main function to run the alarm system."""
    try:
        print("Alarm system is active. Waiting for motion...")
        while True:
            if GPIO.input(PIR_PIN):  # Motion detected
                print("Motion detected!")
                send_alert_email()  # Send alert email
                activate_alarm()  # Activate alarm
                time.sleep(10)  # Wait before checking again to avoid multiple alerts
            time.sleep(0.1)  # Small delay to reduce CPU usage
    except KeyboardInterrupt:
        print("Alarm system stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
```

**Note:** Ensure to replace `your_email@example.com`, `your_password`, and `recipient_email@example.com` with actual email credentials and recipient information. Additionally, you may need to enable "Less secure app access" in your email settings for the SMTP to work.
