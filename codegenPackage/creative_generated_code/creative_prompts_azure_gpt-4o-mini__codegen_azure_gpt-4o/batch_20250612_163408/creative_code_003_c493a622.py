"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Can you demonstrate how to create a plant watering monitoring system using Raspberry Pi, based on the instructions from tubone BOYAKI?
Generated: DETERMINISTIC_c493a62287bc1fb0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

# GPIO Pin configuration
MOISTURE_SENSOR_PIN = 17  # Pin for the moisture sensor
PUMP_PIN = 27            # Pin for the water pump

# Moisture threshold (adjust based on your sensor and soil type)
MOISTURE_THRESHOLD = 500

# Email notification settings
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "receiver_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Initialize GPIO
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
    GPIO.setup(PUMP_PIN, GPIO.OUT)
    GPIO.output(PUMP_PIN, GPIO.LOW)

# Read moisture sensor value
def read_moisture_sensor():
    # Assuming the sensor outputs a digital signal (0 or 1)
    return GPIO.input(MOISTURE_SENSOR_PIN)

# Trigger water pump
def water_plants():
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    time.sleep(5)  # Run the pump for 5 seconds
    GPIO.output(PUMP_PIN, GPIO.LOW)

# Send email notification
def send_email_notification(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Main monitoring loop
def monitor_plants():
    try:
        setup_gpio()
        print("Plant watering monitoring system started.")

        while True:
            moisture_value = read_moisture_sensor()

            if moisture_value < MOISTURE_THRESHOLD:
                print("Soil is dry. Watering plants...")
                water_plants()
                send_email_notification(
                    "Plant Watering Alert",
                    "The soil was dry and the plants have been watered."
                )
            else:
                print("Soil moisture is sufficient. No need to water plants.")
            
            time.sleep(60)  # Check every 60 seconds

    except KeyboardInterrupt:
        print("Monitoring system stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

# Entry point of the program
if __name__ == "__main__":
    monitor_plants()
```
