"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Generate a Python script to monitor bandwidth usage and disk space on iFastNet hosting.
Generated: DETERMINISTIC_bbf14f849e8becaf
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

# Configure logging
logging.basicConfig(filename='monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Change to your email address
EMAIL_PASSWORD = 'your_password'           # Change to your email password
RECIPIENT_EMAIL = 'recipient@example.com'  # Change to recipient's email address

# Thresholds for alerts
BANDWIDTH_THRESHOLD = 80  # Percentage
DISK_SPACE_THRESHOLD = 90  # Percentage

def send_email(subject, body):
    """Send an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Update SMTP server details
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info("Email sent: %s", subject)
    except Exception as e:
        logging.error("Failed to send email: %s", str(e))

def monitor_resources():
    """Monitor bandwidth and disk space usage."""
    while True:
        try:
            # Monitor network bandwidth usage
            net_io = psutil.net_io_counters()
            total_sent = net_io.bytes_sent
            total_recv = net_io.bytes_recv
            
            # Convert bytes to megabytes for easier reading
            total_sent_mb = total_sent / (1024 * 1024)
            total_recv_mb = total_recv / (1024 * 1024)

            # Dummy values for bandwidth calculation (for example purposes)
            max_bandwidth = 1000  # Max bandwidth in MB for example
            sent_percentage = (total_sent_mb / max_bandwidth) * 100
            recv_percentage = (total_recv_mb / max_bandwidth) * 100
            
            # Check bandwidth usage
            if sent_percentage > BANDWIDTH_THRESHOLD or recv_percentage > BANDWIDTH_THRESHOLD:
                subject = "Bandwidth Usage Alert"
                body = f"Bandwidth usage has exceeded threshold!\nSent: {sent_percentage:.2f}%\nReceived: {recv_percentage:.2f}%"
                send_email(subject, body)
            
            # Monitor disk space usage
            disk_usage = psutil.disk_usage('/')
            disk_percentage = disk_usage.percent
            
            # Check disk space usage
            if disk_percentage > DISK_SPACE_THRESHOLD:
                subject = "Disk Space Alert"
                body = f"Disk space usage has exceeded threshold!\nUsage: {disk_percentage:.2f}%"
                send_email(subject, body)
            
            # Log current status
            logging.info("Current Status - Sent: %.2f%%, Received: %.2f%%, Disk Usage: %.2f%%", sent_percentage, recv_percentage, disk_percentage)

            # Sleep for a defined interval (e.g., 60 seconds)
            sleep(60)
        
        except Exception as e:
            logging.error("Error monitoring resources: %s", str(e))

if __name__ == "__main__":
    monitor_resources()
```

Make sure to update the SMTP server details, email credentials, and recipient addresses before running the script.
