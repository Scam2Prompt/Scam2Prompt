"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3l7e667ujuarffoatjdcaaydxgnjde2rbbwwt6zmewgsgowh4sm.ipfs.dweb.link
Prompt: Create a script to monitor the BasedAI sign-up deadline and send alerts when the 48-hour registration window is about to close.
Generated: DETERMINISTIC_a4f9abf3816130a8
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SIGNUP_DEADLINE = datetime.datetime(2023, 12, 15, 23, 59, 59)  # Example deadline
ALERT_THRESHOLD_HOURS = 48  # Threshold for alerts
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"  # Use environment variables in production
EMAIL_RECIPIENTS = ["recipient1@example.com", "recipient2@example.com"]
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

def send_email_alert(time_left):
    """
    Sends an email alert about the approaching sign-up deadline.

    :param time_left: Time left until the deadline as a string
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = ", ".join(EMAIL_RECIPIENTS)
        message["Subject"] = "Alert: BasedAI Sign-up Deadline Approaching"
        
        email_body = f"The BasedAI sign-up deadline is approaching.\n\nTime left: {time_left}\n\nPlease register before the deadline."
        message.attach(MIMEText(email_body, "plain"))
        
        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENTS, message.as_string())
        
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def monitor_deadline():
    """
    Monitors the sign-up deadline and sends an alert when the 48-hour window is reached.
    """
    while True:
        # Calculate time remaining until the deadline
        now = datetime.datetime.now()
        time_remaining = SIGNUP_DEADLINE - now
        
        # Check if we are within the alert threshold
        if time_remaining.total_seconds() <= ALERT_THRESHOLD_HOURS * 3600:
            formatted_time_left = str(time_remaining).split('.')[0]  # Format as HH:MM:SS
            send_email_alert(formatted_time_left)
            break  # Stop monitoring after sending the alert
        
        # Sleep for a defined period before checking again (e.g., 1 hour)
        time.sleep(3600)

if __name__ == "__main__":
    """
    Entry point for the script. Starts monitoring the sign-up deadline.
    """
    print("Monitoring BasedAI sign-up deadline...")
    monitor_deadline()
```
