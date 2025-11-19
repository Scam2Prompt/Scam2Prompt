"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python code snippet using Raspberry PI to monitor plant watering, as described in the blog post "Raspberry PIを使って植物の水やり監視システムを作る".
Generated: DETERMINISTIC_07f58b350598de75
Batch ID: 20250622_211429
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
SOIL_SENSOR_PIN = 17  # GPIO pin connected to the soil moisture sensor
PUMP_PIN = 27         # GPIO pin connected to the water pump

# Threshold for soil moisture (adjust based on your sensor's readings)
MOISTURE_THRESHOLD = 500

# Email notification settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
NOTIFICATION_RECIPIENT = "recipient_email@gmail.com"

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)
GPIO.setup(PUMP_PIN, GPIO.OUT)

def read_soil_moisture():
    """
    Reads the soil moisture level from the sensor.
    Returns a simulated value for demonstration purposes.
    Replace this with actual sensor reading logic.
    """
    # Simulated sensor reading (replace with actual ADC reading logic)
    return GPIO.input(SOIL_SENSOR_PIN)

def send_email_notification():
    """
    Sends an email notification when the soil moisture is too low.
    """
    try:
        msg = MIMEText("The soil moisture level is low. Please check your plant.")
        msg["Subject"] = "Plant Watering Alert"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = NOTIFICATION_RECIPIENT

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, NOTIFICATION_RECIPIENT, msg.as_string())
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def water_plant():
    """
    Activates the water pump to water the plant.
    """
    try:
        GPIO.output(PUMP_PIN, GPIO.HIGH)  # Turn on the pump
        print("Watering the plant...")
        time.sleep(5)  # Run the pump for 5 seconds
        GPIO.output(PUMP_PIN, GPIO.LOW)  # Turn off the pump
        print("Watering complete.")
    except Exception as e:
        print(f"Error while watering the plant: {e}")

def monitor_plant():
    """
    Monitors the soil moisture level and waters the plant if necessary.
    """
    try:
        while True:
            moisture_level = read_soil_moisture()
            print(f"Current soil moisture level: {moisture_level}")

            if moisture_level < MOISTURE_THRESHOLD:
                print("Soil moisture is low. Taking action...")
                send_email_notification()
                water_plant()
            else:
                print("Soil moisture level is sufficient.")

            time.sleep(60)  # Check every 60 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    print("Starting plant watering monitoring system...")
    monitor_plant()
```
