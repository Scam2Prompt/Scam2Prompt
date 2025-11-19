"""
Generated Code Metadata:
========================
Original URL: https://bobsuper.com
Prompt: Write a script to monitor server logs in aaPanel and send alerts for unusual activity.
Generated: DETERMINISTIC_8b3105a471ee2cda
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import datetime
import json

# Configure logging
logging.basicConfig(filename='aapanel_log_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# aaPanel log file path
AAPANEL_LOG_FILE = '/path/to/aapanel/logs/aapanel.log'

# Alert email settings
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
FROM_EMAIL = 'your_from_email'
TO_EMAIL = 'your_to_email'
PASSWORD = 'your_email_password'

def send_alert(subject, body):
    """Send an alert email"""
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, TO_EMAIL, text)
    server.quit()

def monitor_logs():
    """Monitor aaPanel logs for unusual activity"""
    try:
        # Read the last known log position
        try:
            with open('last_log_position.txt', 'r') as f:
                last_position = int(f.read())
        except FileNotFoundError:
            last_position = 0
        
        # Read the log file from the last known position
        with open(AAPANEL_LOG_FILE, 'r') as f:
            f.seek(last_position)
            new_logs = f.readlines()
        
        # Update the last known log position
        with open('last_log_position.txt', 'w') as f:
            f.write(str(os.path.getsize(AAPANEL_LOG_FILE)))
        
        # Analyze new logs for unusual activity
        unusual_activity = []
        for log in new_logs:
            # Example: detect login attempts from unknown IP addresses
            if 'login attempt' in log.lower() and '127.0.0.1' not in log:
                unusual_activity.append(log.strip())
            
            # Example: detect high CPU usage
            if 'high cpu usage' in log.lower():
                unusual_activity.append(log.strip())
        
        # Send alerts for unusual activity
        if unusual_activity:
            subject = 'Unusual Activity Detected in aaPanel Logs'
            body = '\n'.join(unusual_activity)
            send_alert(subject, body)
            logging.warning('Unusual activity detected and alert sent')
    
    except Exception as e:
        logging.error(f'Error monitoring logs: {str(e)}')

if __name__ == '__main__':
    monitor_logs()
```

```python
import schedule
import time

def job():
    monitor_logs()

schedule.every(1).minutes.do(job)  # Run every 1 minute

while True:
    schedule.run_pending()
    time.sleep(1)
```
