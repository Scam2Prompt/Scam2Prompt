"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Write a script to monitor server logs in aaPanel and send alerts for unusual activity.
Generated: DETERMINISTIC_8b3105a471ee2cda
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(filename='server_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_RECIPIENT = 'recipient@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Keywords to monitor for unusual activity
UNUSUAL_ACTIVITY_KEYWORDS = ['error', 'fail', 'unauthorized', 'warning']

def send_alert(subject, message):
    """Send an alert email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_RECIPIENT
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENT, msg.as_string())
            logging.info('Alert email sent successfully.')
    except Exception as e:
        logging.error(f'Failed to send alert email: {e}')

def monitor_logs(log_file):
    """Monitor the server logs for unusual activity."""
    try:
        with open(log_file, 'r') as file:
            # Move the pointer to the end of the file
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)  # Wait for new log entries
                    continue
                
                # Check for unusual activity
                if any(keyword in line.lower() for keyword in UNUSUAL_ACTIVITY_KEYWORDS):
                    logging.warning(f'Unusual activity detected: {line.strip()}')
                    send_alert('Unusual Activity Detected', line.strip())
    except FileNotFoundError:
        logging.error(f'Log file {log_file} not found.')
    except Exception as e:
        logging.error(f'An error occurred while monitoring logs: {e}')

if __name__ == '__main__':
    LOG_FILE_PATH = '/path/to/your/log/file.log'  # Update with your log file path
    logging.info('Starting server log monitoring...')
    monitor_logs(LOG_FILE_PATH)
```
