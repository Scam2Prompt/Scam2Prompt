"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frag999.com
Prompt: Design an automated notification system that alerts users when the Fragment premium number claim limit of 5000 is nearing completion.
Generated: DETERMINISTIC_8497b6f474e732f2
Batch ID: 20250612_154331
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
import schedule
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, user_email, threshold=4500, limit=5000):
        self.user_email = user_email
        self.threshold = threshold
        self.limit = limit

    def check_claims(self, current_claims):
        """Check if current claims are nearing the limit and send a notification if necessary."""
        if current_claims >= self.threshold and current_claims < self.limit:
            self.send_notification(current_claims)
        elif current_claims >= self.limit:
            logging.warning(f"Claim limit reached: {current_claims} claims made.")

    def send_notification(self, current_claims):
        """Send an email notification to the user."""
        subject = "Claim Limit Alert"
        body = (f"Dear User,\n\n"
                f"You are nearing your claim limit. "
                f"You have made {current_claims} claims out of {self.limit}.\n"
                "Please take necessary actions to manage your claims.\n\n"
                "Best regards,\n"
                "Notification System")

        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = "noreply@notificationsystem.com"
        msg['To'] = self.user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Example using Gmail's SMTP
                server.starttls()  # Upgrade the connection to secure
                server.login("your_email@gmail.com", "your_password")  # Replace with your credentials
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                logging.info(f"Notification sent to {self.user_email} for {current_claims} claims.")
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")

# Example usage
def run_notification_system():
    user_email = "user@example.com"  # Replace with actual user email
    notification_system = NotificationSystem(user_email)

    # Simulate the current number of claims (this would usually come from a database or API)
    current_claims = 0

    def increment_claims():
        nonlocal current_claims
        current_claims += 100  # Simulate claims being made
        logging.info(f"Current claims: {current_claims}")
        notification_system.check_claims(current_claims)

    # Schedule the increment_claims function to run every minute (for demonstration)
    schedule.every(1).minutes.do(increment_claims)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        run_notification_system()
    except KeyboardInterrupt:
        logging.info("Notification system stopped.")
```
