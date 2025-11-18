"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opsense.com
Prompt: Create a Python function that simulates automated alerts for temperature deviations in healthcare facilities, leveraging OpSense's monitoring capabilities.
Generated: DETERMINISTIC_488b4114f865de22
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemperatureAlert:
    def __init__(self, threshold_high, threshold_low, email_config):
        """
        Initializes the TemperatureAlert with specified thresholds and email configuration.
        
        :param threshold_high: The maximum acceptable temperature.
        :param threshold_low: The minimum acceptable temperature.
        :param email_config: A dictionary containing email settings (sender, recipient, subject, smtp_server, port)
        """
        self.threshold_high = threshold_high
        self.threshold_low = threshold_low
        self.email_config = email_config

    def send_alert(self, current_temperature):
        """
        Sends an alert email when temperature is outside the acceptable range.
        
        :param current_temperature: The current temperature reading.
        """
        logging.info(f"Sending alert for temperature: {current_temperature}")
        
        # Create the email content
        sender_email = self.email_config['sender']
        recipient_email = self.email_config['recipient']
        subject = self.email_config['subject']
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        body = f"Alert: Temperature deviation detected! Current temperature: {current_temperature}°C"
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Setup SMTP server and send the email
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['port']) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(sender_email, self.email_config['password'])
                server.send_message(msg)
                logging.info("Alert email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send alert email: {e}")

    def monitor_temperature(self):
        """
        Continuously monitors temperature and sends alerts on deviation.
        Simulated temperature readings are generated randomly.
        """
        logging.info("Starting temperature monitoring...")
        while True:
            # Simulate temperature reading (for demo purposes)
            current_temperature = random.uniform(-10, 50)
            logging.info(f"Current temperature reading: {current_temperature}°C")
            
            # Check for temperature deviations
            if current_temperature > self.threshold_high or current_temperature < self.threshold_low:
                self.send_alert(current_temperature)

            # Sleep for a specified duration before the next reading
            time.sleep(5)  # Adjust this value as needed for real-world use

if __name__ == "__main__":
    # Define thresholds and email configuration
    threshold_high = 25.0  # Set high threshold (example)
    threshold_low = 15.0   # Set low threshold (example)
    
    email_configuration = {
        'sender': 'your_email@example.com',
        'recipient': 'recipient_email@example.com',
        'subject': 'Temperature Alert',
        'smtp_server': 'smtp.example.com',
        'port': 587,
        'password': 'your_email_password'  # Use environment variable or secure vault in production
    }
    
    # Create an instance of TemperatureAlert
    temperature_alert_system = TemperatureAlert(threshold_high, threshold_low, email_configuration)
    
    # Start monitoring temperature
    try:
        temperature_alert_system.monitor_temperature()
    except KeyboardInterrupt:
        logging.info("Temperature monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred during monitoring: {e}")
```
