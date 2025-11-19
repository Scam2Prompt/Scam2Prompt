"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Provide code for setting up a fire alarm system with automated alerts, based on the fire system services described by Inside Safety.
Generated: DETERMINISTIC_1acbffbd35105052
Batch ID: 20250612_153224
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
from email.mime.multipart import MIMEMultipart
import time
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fire_alarm.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FireAlarmSystem:
    """
    A fire alarm system with automated alerts based on sensor inputs.
    """
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        admin_emails: List[str],
        sensor_poll_interval: int = 30
    ):
        """
        Initialize the fire alarm system with email configuration.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send alerts from
            sender_password: Password for sender email
            admin_emails: List of admin email addresses to notify
            sensor_poll_interval: Interval in seconds to check sensors
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.admin_emails = admin_emails
        self.sensor_poll_interval = sensor_poll_interval
        self.is_active = False
        
    def start_monitoring(self) -> None:
        """Start monitoring fire sensors and sending alerts when triggered."""
        self.is_active = True
        logger.info("Fire alarm system started monitoring")
        
        try:
            while self.is_active:
                # Simulate checking fire sensors (replace with actual sensor reading)
                fire_detected = self._check_fire_sensors()
                
                if fire_detected:
                    self._trigger_alarm()
                
                time.sleep(self.sensor_poll_interval)
        except KeyboardInterrupt:
            self.stop_monitoring()
        except Exception as e:
            logger.error(f"Monitoring error: {str(e)}")
            self.stop_monitoring()
    
    def stop_monitoring(self) -> None:
        """Stop the monitoring process."""
        self.is_active = False
        logger.info("Fire alarm system stopped monitoring")
    
    def _check_fire_sensors(self) -> bool:
        """
        Check fire sensors for any signs of fire.
        
        Returns:
            bool: True if fire is detected, False otherwise
        """
        # In a real implementation, this would interface with actual sensors
        # For demo purposes, we simulate occasional fire detection
        import random
        return random.random() < 0.05  # 5% chance of fire for demo
    
    def _trigger_alarm(self) -> None:
        """Trigger the fire alarm and send notifications."""
        logger.warning("FIRE DETECTED! Triggering alarm and sending alerts")
        
        # Sound local alarm (simulated)
        self._sound_local_alarm()
        
        # Send email alerts
        self._send_email_alerts()
        
        # Additional actions could be added here (e.g., call emergency services)
    
    def _sound_local_alarm(self) -> None:
        """Sound the local alarm system."""
        logger.info("Sounding local alarm")
        # In a real implementation, this would activate physical alarms
    
    def _send_email_alerts(self) -> None:
        """Send email alerts to all configured admin emails."""
        subject = "URGENT: Fire Detected in Building"
        body = """
        WARNING: The fire alarm system has detected a potential fire.
        
        Location: Main Building
        Time: {time}
        
        Please evacuate immediately and contact emergency services.
        """
        
        formatted_body = body.format(time=time.strftime("%Y-%m-%d %H:%M:%S"))
        
        for recipient in self.admin_emails:
            try:
                message = MIMEMultipart()
                message['From'] = self.sender_email
                message['To'] = recipient
                message['Subject'] = subject
                
                message.attach(MIMEText(formatted_body, 'plain'))
                
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.sender_email, self.sender_password)
                    server.send_message(message)
                
                logger.info(f"Alert email sent to {recipient}")
            except Exception as e:
                logger.error(f"Failed to send email to {recipient}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Configuration (should be moved to config file in production)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "alerts@example.com"
    SENDER_PASSWORD = "securepassword"
    ADMIN_EMAILS = ["admin1@example.com", "admin2@example.com"]
    
    # Initialize and start the system
    fire_alarm = FireAlarmSystem(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        admin_emails=ADMIN_EMAILS,
        sensor_poll_interval=10  # Check every 10 seconds for demo
    )
    
    try:
        fire_alarm.start_monitoring()
    except Exception as e:
        logger.error(f"System error: {str(e)}")
```
