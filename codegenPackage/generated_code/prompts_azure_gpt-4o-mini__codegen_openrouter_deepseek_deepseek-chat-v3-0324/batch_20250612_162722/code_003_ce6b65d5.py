"""
Generated Code Metadata:
========================
Original URL: https://claim-paramiabs.app
Prompt: Generate a code snippet that logs phishing attempts and alerts users, inspired by the warning on claim-paramiabs.app.
Generated: DETERMINISTIC_ce6b65d5dd68e597
Batch ID: 20250612_162722
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "http://claim-paramiabs.app": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Generated Code:
# ===============

```python
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from typing import Optional

class PhishingMonitor:
    """
    A class to monitor and log phishing attempts, and alert users via email.
    """

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str, admin_email: str):
        """
        Initialize the PhishingMonitor with SMTP details and admin email.

        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send alerts from
            sender_password: Password for the sender email
            admin_email: Admin email to receive alerts
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.admin_email = admin_email

        # Configure logging
        logging.basicConfig(
            filename='phishing_attempts.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def log_phishing_attempt(self, url: str, ip_address: str, user_agent: Optional[str] = None) -> None:
        """
        Log a phishing attempt and send an alert.

        Args:
            url: The phishing URL that was accessed
            ip_address: IP address of the requester
            user_agent: User agent string of the requester (optional)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Phishing attempt detected - URL: {url}, IP: {ip_address}"
        if user_agent:
            log_message += f", User Agent: {user_agent}"

        # Log the attempt
        self.logger.warning(log_message)

        # Send email alert
        self._send_alert_email(log_message, timestamp)

    def _send_alert_email(self, message: str, timestamp: str) -> None:
        """
        Send an email alert about the phishing attempt.

        Args:
            message: The alert message to send
            timestamp: Timestamp of the attempt
        """
        email_subject = f"Phishing Attempt Alert - {timestamp}"
        email_body = f"""
        Security Alert:
        
        {message}
        
        Timestamp: {timestamp}
        
        This is an automated alert. Please investigate immediately.
        """

        msg = MIMEText(email_body)
        msg['Subject'] = email_subject
        msg['From'] = self.sender_email
        msg['To'] = self.admin_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            self.logger.info("Phishing alert email sent successfully")
        except Exception as e:
            self.logger.error(f"Failed to send phishing alert email: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Configuration (replace with actual values)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "alerts@example.com"
    SENDER_PASSWORD = "securepassword"
    ADMIN_EMAIL = "admin@example.com"

    monitor = PhishingMonitor(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        admin_email=ADMIN_EMAIL
    )

    # Simulate a phishing attempt
    monitor.log_phishing_attempt(
        url="http://claim-paramiabs.app",
        ip_address="192.168.1.100",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )
```
