"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Develop a program to provide 24/7 IT system monitoring and alerting, ensuring minimal downtime, as described in IMTS's outsourced managed IT services.
Generated: DETERMINISTIC_cf07b5d57061df60
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import smtplib
import subprocess
import logging
from email.mime.text import MIMEText
from typing import List, Dict

# Configure logging for monitoring events and errors
logging.basicConfig(level=logging.INFO, filename='system_monitor.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USER = 'monitor@example.com'
EMAIL_PASSWORD = 'yourpassword'
ALERT_RECIPIENTS = ['admin@example.com']

# Monitoring configuration
CHECK_INTERVAL = 60  # Check every minute
SYSTEM_COMPONENTS = ['ping -c 1 google.com', 'df -h', 'uptime']  # Example commands to check system health

def send_alert(subject: str, message: str) -> None:
    """
    Sends an alert email to the designated recipients.
    
    :param subject: Subject of the alert email
    :param message: Body message of the alert email
    """
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = ', '.join(ALERT_RECIPIENTS)

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, ALERT_RECIPIENTS, msg.as_string())
        
        logging.info(f'Alert sent: {subject}')
    except Exception as e:
        logging.error(f'Failed to send alert: {e}')

def check_system(component: str) -> Dict[str, str]:
    """
    Executes a system command to check its status and returns the result.
    
    :param component: Command line to execute for checking system status
    :return: A dictionary containing the command and its output
    """
    try:
        output = subprocess.check_output(component, shell=True, stderr=subprocess.STDOUT)
        return {'component': component, 'status': 'OK', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        logging.error(f'Error checking component "{component}": {e.output.decode("utf-8")}')
        return {'component': component, 'status': 'FAIL', 'output': e.output.decode('utf-8')}

def monitor_system() -> None:
    """
    Main monitoring loop that checks the status of system components and sends alerts if necessary.
    """
    while True:
        for component in SYSTEM_COMPONENTS:
            result = check_system(component)
            if result['status'] == 'FAIL':
                alert_subject = f'Alert: {component} check failed'
                alert_message = f'Component: {result["component"]}\nOutput:\n{result["output"]}'
                send_alert(alert_subject, alert_message)
        
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    logging.info('Starting system monitoring...')
    monitor_system()
```

This Python program provides a basic structure for 24/7 IT system monitoring and alerting. It includes error handling, logging, and email notifications. Be sure to update the email configuration and system commands according to your specific needs before deploying the code.
