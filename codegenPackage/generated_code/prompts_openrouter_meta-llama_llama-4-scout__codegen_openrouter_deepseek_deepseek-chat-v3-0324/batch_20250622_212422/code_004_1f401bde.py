"""
Generated Code Metadata:
========================
Original URL: https://optimism-app.lcfmedia.com
Prompt: Generate a code snippet to monitor LiteSpeed Web Server logs and alert administrators of potential issues.
Generated: DETERMINISTIC_1f401bde3f7adccf
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
LiteSpeed Web Server Log Monitor
Monitors LiteSpeed logs for potential issues and alerts administrators.
"""

import os
import re
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from collections import defaultdict

# Configuration
LOG_FILE = '/usr/local/lsws/logs/error.log'
ALERT_THRESHOLDS = {
    '5xx_errors': 10,  # Number of 5xx errors to trigger alert
    '4xx_errors': 50,  # Number of 4xx errors to trigger alert
    'connection_timeouts': 5,
    'slow_requests': 20  # Requests taking > 5 seconds
}
ALERT_EMAIL = 'admin@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'alert_user@example.com'
SMTP_PASSWORD = 'securepassword'

# Patterns to monitor
PATTERNS = {
    '5xx_errors': re.compile(r'\[error\] .*HTTP (5\d{2})'),
    '4xx_errors': re.compile(r'\[error\] .*HTTP (4\d{2})'),
    'connection_timeouts': re.compile(r'\[error\] .*connection timed out'),
    'slow_requests': re.compile(r'\[info\] .*request time: (\d+\.\d+)s')
}

def read_log_file(log_path):
    """Read log file and return its content."""
    try:
        with open(log_path, 'r') as f:
            return f.readlines()
    except IOError as e:
        raise Exception(f"Error reading log file: {e}")

def analyze_logs(log_lines):
    """Analyze log lines and count occurrences of patterns."""
    counts = defaultdict(int)
    slow_requests = []
    
    for line in log_lines:
        for pattern_name, pattern in PATTERNS.items():
            matches = pattern.search(line)
            if matches:
                counts[pattern_name] += 1
                
                if pattern_name == 'slow_requests':
                    duration = float(matches.group(1))
                    if duration > 5.0:
                        slow_requests.append((line.strip(), duration))
    
    return counts, slow_requests

def check_thresholds(counts):
    """Check if any thresholds have been exceeded."""
    alerts = []
    for key, threshold in ALERT_THRESHOLDS.items():
        if counts.get(key, 0) >= threshold:
            alerts.append(f"{key.replace('_', ' ')} threshold exceeded ({counts[key]} >= {threshold})")
    return alerts

def send_alert(subject, body):
    """Send email alert to administrator."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ALERT_EMAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send alert email: {e}")

def main():
    """Main monitoring function."""
    try:
        # Read and analyze logs
        log_lines = read_log_file(LOG_FILE)
        counts, slow_requests = analyze_logs(log_lines)
        
        # Check for threshold violations
        alerts = check_thresholds(counts)
        
        if alerts or slow_requests:
            # Prepare alert message
            subject = "LiteSpeed Server Alert"
            body = "Potential issues detected:\n\n"
            
            if alerts:
                body += "Threshold violations:\n"
                body += "\n".join(f"- {alert}" for alert in alerts) + "\n\n"
            
            if slow_requests:
                body += "Slow requests (>5s):\n"
                for req, duration in slow_requests[:10]:  # Show top 10 slowest
                    body += f"- {duration:.2f}s: {req}\n"
            
            # Send alert
            send_alert(subject, body)
            print("Alert sent for detected issues.")
        else:
            print("No issues detected.")
            
    except Exception as e:
        print(f"Monitoring failed: {e}")

if __name__ == '__main__':
    main()
```
