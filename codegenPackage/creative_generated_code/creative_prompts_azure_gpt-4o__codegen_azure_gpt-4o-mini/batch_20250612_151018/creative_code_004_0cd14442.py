"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Develop a Raspberry Pi project to monitor plant watering systems, referencing the tutorial from the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_0cd14442de269042
Batch ID: 20250612_151018
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
import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText

# Constants
DHT_PIN = 4  # GPIO pin for DHT sensor
SOIL_MOISTURE_PIN = 17  # GPIO pin for soil moisture sensor
WATER_PUMP_PIN = 27  # GPIO pin for the water pump
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient_email@example.com'

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)

def send_email(subject, body):
    """Send an email notification."""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

def read_soil_moisture():
    """Read soil moisture level from the sensor."""
    return GPIO.input(SOIL_MOISTURE_PIN)

def water_plant():
    """Activate the water pump to water the plant."""
    print("Watering the plant...")
    GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)
    time.sleep(5)  # Water for 5 seconds
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
    print("Plant watered.")

def main():
    """Main function to monitor and manage plant watering."""
    try:
        while True:
            soil_moisture = read_soil_moisture()
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT_PIN)

            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%")
            else:
                print("Failed to retrieve data from humidity sensor.")

            if soil_moisture == GPIO.LOW:  # Soil is dry
                water_plant()
                send_email("Plant Watering Alert", "The plant has been watered.")

            time.sleep(60)  # Check every minute

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings on exit

if __name__ == "__main__":
    main()
```
