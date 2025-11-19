"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-modenetwork.app
Prompt: Generate a code snippet that logs flagged phishing attempts and notifies the website owner, referencing the process mentioned for resolving issues on flagged sites.
Generated: DETERMINISTIC_150801ac1acef048
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://phishing-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='phishing_attempts.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PhishingLogger:
    def __init__(self, owner_email):
        self.owner_email = owner_email

    def log_attempt(self, attempt_details):
        """
        Logs the flagged phishing attempt and notifies the website owner.

        Parameters:
        attempt_details (dict): A dictionary containing details of the phishing attempt.
        """
        try:
            # Log the phishing attempt details
            logging.warning(f"Flagged phishing attempt: {attempt_details}")

            # Notify the website owner
            self.notify_owner(attempt_details)
        except Exception as e:
            logging.error(f"Error logging phishing attempt: {e}")

    def notify_owner(self, attempt_details):
        """
        Sends an email notification to the website owner about the phishing attempt.

        Parameters:
        attempt_details (dict): A dictionary containing details of the phishing attempt.
        """
        subject = "Alert: Flagged Phishing Attempt Detected"
        body = f"Phishing attempt detected with the following details:\n\n{attempt_details}"

        # Create email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'noreply@example.com'
        msg['To'] = self.owner_email

        try:
            # Send email notification
            with smtplib.SMTP('smtp.example.com') as server:
                server.starttls()  # Secure the connection
                server.login('your_email@example.com', 'your_password')  # Use environment variables for sensitive data
                server.send_message(msg)
            logging.info(f"Notification sent to {self.owner_email}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email notification: {e}")

# Example usage
if __name__ == "__main__":
    phishing_logger = PhishingLogger(owner_email='owner@example.com')
    
    # Example phishing attempt details
    attempt_details = {
        'ip_address': '192.0.2.1',
        'url': 'http://phishing-site.com',
        'timestamp': '2023-10-01T12:00:00Z',
        'user_agent': 'Mozilla/5.0'
    }
    
    phishing_logger.log_attempt(attempt_details)
```
