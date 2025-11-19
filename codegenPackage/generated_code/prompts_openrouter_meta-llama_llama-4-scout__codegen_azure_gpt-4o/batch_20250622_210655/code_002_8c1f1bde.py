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

# Pin configuration
SENSOR_PIN = 18  # GPIO pin connected to the motion sensor
BUZZER_PIN = 23  # GPIO pin connected to the buzzer

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"        # Replace with your email password
ALERT_EMAIL = "alert_recipient@gmail.com"  # Replace with the recipient's email

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set sensor pin as input
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set buzzer pin as output

def send_email_alert():
    """
    Sends an email alert when motion is detected.
    """
    try:
        # Create the email content
        subject = "Security Alert: Motion Detected"
        body = "Motion has been detected by the alarm system. Please check your premises."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ALERT_EMAIL

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, ALERT_EMAIL, msg.as_string())
        server.quit()
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def activate_buzzer(duration=2):
    """
    Activates the buzzer for a specified duration.
    :param duration: Duration in seconds to keep the buzzer active.
    """
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on the buzzer
    time.sleep(duration)  # Keep the buzzer on for the specified duration
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off the buzzer

def main():
    """
    Main function to monitor the motion sensor and trigger alerts.
    """
    print("Alarm system is active. Monitoring for motion...")
    try:
        while True:
            # Check for motion detection
            if GPIO.input(SENSOR_PIN):
                print("Motion detected!")
                activate_buzzer()  # Activate the buzzer
                send_email_alert()  # Send an email alert
                time.sleep(5)  # Wait for 5 seconds before checking again
            else:
                time.sleep(0.1)  # Poll the sensor every 100ms
    except KeyboardInterrupt:
        print("Alarm system shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Reset GPIO settings

if __name__ == "__main__":
    main()
```
