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
# File: plant_monitor.py

import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Pin configuration
MOISTURE_SENSOR_PIN = 17  # GPIO pin connected to the moisture sensor
ALERT_THRESHOLD = 300  # Threshold for low moisture level (adjust based on your sensor)
CHECK_INTERVAL = 60  # Time interval in seconds between checks

# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
ALERT_RECIPIENT = "recipient_email@example.com"  # Replace with recipient's email

# Function to send email alerts
def send_email_alert(moisture_level):
    try:
        # Creating the email message
        subject = "Plant Watering Alert: Low Moisture Detected"
        body = f"The moisture level of the plant is low (Level: {moisture_level}). Please water your plant."
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_RECIPIENT
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Sending the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENT, msg.as_string())
        server.quit()
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to read moisture sensor data
def read_moisture_sensor():
    try:
        # Placeholder mock data; replace with actual sensor reading code
        # Example: Use ADC or analog-to-digital converter to read data from the sensor
        moisture_level = 250  # Replace this with actual sensor reading logic
        return moisture_level
    except Exception as e:
        print(f"Error reading moisture sensor: {e}")
        return None

# Main function
def monitor_plant():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

        print("Starting plant moisture monitoring...")
        while True:
            # Read moisture level
            moisture_level = read_moisture_sensor()
            if moisture_level is None:
                continue

            print(f"Moisture level: {moisture_level}")

            # Check if the moisture level is below the threshold
            if moisture_level < ALERT_THRESHOLD:
                print("Low moisture level detected! Sending alert...")
                send_email_alert(moisture_level)

            # Wait for the next check
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up.")

# Entry point
if __name__ == "__main__":
    monitor_plant()
```

**Note:**  
- Update the `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `ALERT_RECIPIENT` with valid details.  
- Replace the `read_moisture_sensor` function logic with actual code to read from the moisture sensor hardware.
