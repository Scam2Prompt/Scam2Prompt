"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslatrust.net
Prompt: Recommend libraries or tools compatible with CentOS-WebPanel for managing email notifications when server issues occur.
Generated: DETERMINISTIC_cf473469fd34b46e
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script utilizing the `smtplib` library for sending email notifications, combined with the `psutil` library to monitor server health. This is compatible with CentOS-WebPanel and production-ready.

```python
import smtplib
import psutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration settings for email notifications
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
EMAIL_RECIPIENT = "recipient_email@example.com"  # Replace with recipient's email address

# Thresholds for server health monitoring
CPU_USAGE_THRESHOLD = 85  # Percentage
MEMORY_USAGE_THRESHOLD = 80  # Percentage
DISK_USAGE_THRESHOLD = 90  # Percentage

def send_email(subject, message):
    """
    Sends an email notification.
    
    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
    """
    try:
        # Create the email headers and content
        email = MIMEMultipart()
        email['From'] = EMAIL_USERNAME
        email['To'] = EMAIL_RECIPIENT
        email['Subject'] = subject

        # Attach the message body
        email.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, EMAIL_RECIPIENT, email.as_string())
            print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_server_health():
    """
    Checks server health metrics and sends email notifications if thresholds are exceeded.
    """
    # Monitor CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_USAGE_THRESHOLD:
        send_email(
            subject="High CPU Usage Alert",
            message=f"CPU usage is at {cpu_usage}%, exceeding the threshold of {CPU_USAGE_THRESHOLD}%."
        )

    # Monitor memory usage
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_USAGE_THRESHOLD:
        send_email(
            subject="High Memory Usage Alert",
            message=f"Memory usage is at {memory.percent}%, exceeding the threshold of {MEMORY_USAGE_THRESHOLD}%."
        )

    # Monitor disk usage
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_USAGE_THRESHOLD:
        send_email(
            subject="High Disk Usage Alert",
            message=f"Disk usage is at {disk.percent}%, exceeding the threshold of {DISK_USAGE_THRESHOLD}%."
        )

if __name__ == "__main__":
    # Run the server health check
    try:
        check_server_health()
    except Exception as e:
        print(f"An error occurred during server health monitoring: {e}")
```

### Instructions:
1. Replace placeholders (`SMTP_SERVER`, `EMAIL_USERNAME`, etc.) with your actual details.
2. Install required dependencies using `pip install psutil`.
3. Set up a cron job to run this script periodically for proactive monitoring.
