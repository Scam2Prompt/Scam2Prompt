"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Provide Python code for building a Raspberry Pi-based plant watering monitoring system, as detailed in the tubone BOYAKI blog.
Generated: DETERMINISTIC_71fcdb7d4e6b4b07
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText

# Constants
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the DHT sensor is connected
WATER_PUMP_PIN = 17  # GPIO pin for the water pump
SOIL_MOISTURE_PIN = 27  # GPIO pin for the soil moisture sensor
MOISTURE_THRESHOLD = 300  # Threshold for soil moisture
WATERING_DURATION = 10  # Duration to water the plant in seconds
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'recipient@example.com'  # Replace with recipient email

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)

def send_email(subject, body):
    """Send an email notification."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def read_soil_moisture():
    """Read the soil moisture level."""
    return GPIO.input(SOIL_MOISTURE_PIN)

def water_plant():
    """Activate the water pump to water the plant."""
    print("Watering the plant...")
    GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)
    time.sleep(WATERING_DURATION)
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
    print("Watering complete.")

def main():
    """Main function to monitor and water the plant."""
    try:
        while True:
            # Read soil moisture
            moisture_level = read_soil_moisture()
            print(f"Soil moisture level: {moisture_level}")

            # Check if the soil is dry
            if moisture_level > MOISTURE_THRESHOLD:
                water_plant()
                send_email("Plant Watering Alert", "The plant has been watered.")
            else:
                print("Soil moisture is sufficient.")

            # Wait before the next reading
            time.sleep(60)  # Check every minute

    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
```
