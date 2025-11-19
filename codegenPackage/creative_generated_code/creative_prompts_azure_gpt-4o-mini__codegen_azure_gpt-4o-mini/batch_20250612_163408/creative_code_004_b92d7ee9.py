"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create a Raspberry Pi project that monitors plant watering and sends alerts when moisture levels are low.
Generated: DETERMINISTIC_b92d7ee9f3ecf376
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import RPi.GPIO as GPIO
from gpiozero import LED, Button
import smtplib
from email.mime.text import MIMEText
import Adafruit_DHT

# Configuration for the moisture sensor and email alert
MOISTURE_SENSOR_PIN = 17  # GPIO pin connected to the moisture sensor
DHT_SENSOR_PIN = 4        # GPIO pin connected to the DHT sensor (for temperature/humidity)
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"           # Replace with your email password
ALERT_THRESHOLD = 300  # Threshold value for moisture level (adjust based on your sensor)
CHECK_INTERVAL = 60    # Time in seconds between checks

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

def send_email_alert(moisture_level):
    """Send an email alert when moisture level is low."""
    msg = MIMEText(f"Alert: Moisture level is critically low! Current level: {moisture_level}")
    msg['Subject'] = 'Plant Watering Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Use the appropriate SMTP server
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def read_moisture_level():
    """Read the moisture level from the sensor."""
    return GPIO.input(MOISTURE_SENSOR_PIN)

def read_temperature_humidity():
    """Read temperature and humidity from the DHT sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_SENSOR_PIN)
    return humidity, temperature

def monitor_plant():
    """Monitor the plant moisture level and send alerts if necessary."""
    try:
        while True:
            moisture_level = read_moisture_level()
            humidity, temperature = read_temperature_humidity()

            print(f"Moisture Level: {moisture_level}, Temperature: {temperature}°C, Humidity: {humidity}%")

            if moisture_level > ALERT_THRESHOLD:
                print("Moisture level is low! Sending alert...")
                send_email_alert(moisture_level)

            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings on exit

if __name__ == "__main__":
    monitor_plant()
```
