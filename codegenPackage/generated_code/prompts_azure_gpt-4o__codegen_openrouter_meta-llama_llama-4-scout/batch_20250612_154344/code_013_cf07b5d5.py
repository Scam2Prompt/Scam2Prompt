"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Develop a program to provide 24/7 IT system monitoring and alerting, ensuring minimal downtime, as described in IMTS's outsourced managed IT services.
Generated: DETERMINISTIC_cf07b5d57061df60
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# it_monitoring_system.py

import logging
import os
import psutil
import schedule
import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up logging configuration
logging.basicConfig(filename='it_monitoring_system.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants for email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your-email@gmail.com'
PASSWORD = 'your-password'

# Define constants for system thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 90  # in percentage
DISK_THRESHOLD = 90  # in percentage

def send_email(subject, message, to_email):
    """
    Send an email using SMTP server.

    Args:
        subject (str): Email subject.
        message (str): Email body.
        to_email (str): Recipient's email address.
    """
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, to_email, text)
    server.quit()

def check_system_resources():
    """
    Check system resources (CPU, memory, disk usage) and send alerts if thresholds are exceeded.
    """
    try:
        # Get current system resource usage
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Check if thresholds are exceeded
        if cpu_usage > CPU_THRESHOLD:
            send_email('High CPU Usage', f'CPU usage is {cpu_usage}%', 'recipient-email@example.com')
            logging.warning(f'High CPU usage: {cpu_usage}%')

        if memory_usage > MEMORY_THRESHOLD:
            send_email('High Memory Usage', f'Memory usage is {memory_usage}%', 'recipient-email@example.com')
            logging.warning(f'High memory usage: {memory_usage}%')

        if disk_usage > DISK_THRESHOLD:
            send_email('High Disk Usage', f'Disk usage is {disk_usage}%', 'recipient-email@example.com')
            logging.warning(f'High disk usage: {disk_usage}%')

    except Exception as e:
        logging.error(f'Error checking system resources: {str(e)}')

def check_service_status(service_name):
    """
    Check if a service is running.

    Args:
        service_name (str): Name of the service to check.
    """
    try:
        # Check if service is running
        if not psutil.find_process_by_name(service_name):
            send_email(f'{service_name} Service Down', f'{service_name} service is not running.', 'recipient-email@example.com')
            logging.error(f'{service_name} service is not running.')
    except Exception as e:
        logging.error(f'Error checking {service_name} service status: {str(e)}')

def main():
    # Schedule tasks to run every 5 minutes
    schedule.every(5).minutes.do(check_system_resources)

    # Schedule tasks to run every 1 minute
    schedule.every(1).minutes.do(check_service_status, 'nginx')

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            logging.error(f'Error in main loop: {str(e)}')

if __name__ == '__main__':
    main()
```
