"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Create a Python function that simulates automated alerts for temperature deviations in healthcare facilities, leveraging OpSense's monitoring capabilities.
Generated: DETERMINISTIC_488b4114f865de22
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemperatureAlertSystem:
    def __init__(self, threshold: float, email_recipients: List[str], smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initialize the TemperatureAlertSystem with the specified parameters.

        :param threshold: The temperature threshold for alerts.
        :param email_recipients: List of email addresses to notify.
        :param smtp_server: SMTP server address for sending emails.
        :param smtp_port: SMTP server port.
        :param smtp_user: SMTP username for authentication.
        :param smtp_password: SMTP password for authentication.
        """
        self.threshold = threshold
        self.email_recipients = email_recipients
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_alert(self, temperature: float):
        """
        Send an alert email when the temperature exceeds the threshold.

        :param temperature: The temperature that triggered the alert.
        """
        subject = "Temperature Alert"
        body = f"Alert! The temperature has deviated from the normal range. Current temperature: {temperature}°C"
        
        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = ', '.join(self.email_recipients)

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, self.email_recipients, msg.as_string())
                logging.info("Alert email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send alert email: {e}")

    def monitor_temperature(self, temperature_data: Dict[str, float]):
        """
        Monitor temperature readings and trigger alerts for deviations.

        :param temperature_data: A dictionary with facility names as keys and their corresponding temperatures as values.
        """
        for facility, temperature in temperature_data.items():
            logging.info(f"Monitoring {facility}: Current temperature is {temperature}°C")
            if temperature > self.threshold:
                logging.warning(f"Temperature deviation detected at {facility}: {temperature}°C exceeds threshold of {self.threshold}°C")
                self.send_alert(temperature)

# Example usage
if __name__ == "__main__":
    # Configuration for the alert system
    THRESHOLD = 25.0  # Example threshold in degrees Celsius
    EMAIL_RECIPIENTS = ["admin@example.com"]
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "user@example.com"
    SMTP_PASSWORD = "securepassword"

    # Create an instance of the alert system
    alert_system = TemperatureAlertSystem(THRESHOLD, EMAIL_RECIPIENTS, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Simulated temperature data for monitoring
    simulated_temperature_data = {
        "Facility A": 24.5,
        "Facility B": 26.7,  # This should trigger an alert
        "Facility C": 23.0
    }

    # Start monitoring temperatures
    alert_system.monitor_temperature(simulated_temperature_data)
```
