"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftrealisticevm.com
Prompt: What are the best practices for preventing account suspension in web hosting environments?
Generated: DETERMINISTIC_abeb52f1f3b8babb
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Best Practices to Prevent Account Suspension in Web Hosting Environments

This script provides a framework for monitoring key metrics in web hosting environments
to prevent account suspension due to common issues such as exceeding resource limits,
security violations, or spamming.

Key Features:
- Monitors disk space usage, bandwidth, CPU, and memory consumption.
- Checks for unusual login activity and suspicious file changes.
- Sends alerts when thresholds are exceeded or suspicious activity is detected.
"""

import os
import psutil  # For monitoring system resources
import smtplib  # For sending email alerts
from email.mime.text import MIMEText

# Configuration
ADMIN_EMAIL = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "smtp_user"
SMTP_PASSWORD = "smtp_password"
RESOURCE_THRESHOLDS = {
    "disk_usage_percent": 80,  # Alert if disk usage exceeds 80%
    "cpu_usage_percent": 90,   # Alert if CPU usage exceeds 90%
    "memory_usage_percent": 85 # Alert if memory usage exceeds 85%
}

def send_email_alert(subject, message):
    """
    Sends an email alert to the administrator.
    :param subject: Email subject
    :param message: Email body content
    """
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = SMTP_USERNAME
        msg["To"] = ADMIN_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, ADMIN_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def monitor_disk_usage():
    """
    Monitors disk space usage and sends an alert if the usage exceeds the threshold.
    """
    try:
        disk_usage = psutil.disk_usage('/')
        if disk_usage.percent > RESOURCE_THRESHOLDS["disk_usage_percent"]:
            send_email_alert(
                "Disk Usage Alert",
                f"Warning: Disk usage is at {disk_usage.percent}%. Please take action to free up space."
            )
    except Exception as e:
        print(f"Error monitoring disk usage: {e}")

def monitor_cpu_usage():
    """
    Monitors CPU usage and sends an alert if the usage exceeds the threshold.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > RESOURCE_THRESHOLDS["cpu_usage_percent"]:
            send_email_alert(
                "CPU Usage Alert",
                f"Warning: CPU usage is at {cpu_usage}%. Consider optimizing your processes."
            )
    except Exception as e:
        print(f"Error monitoring CPU usage: {e}")

def monitor_memory_usage():
    """
    Monitors memory usage and sends an alert if the usage exceeds the threshold.
    """
    try:
        memory = psutil.virtual_memory()
        if memory.percent > RESOURCE_THRESHOLDS["memory_usage_percent"]:
            send_email_alert(
                "Memory Usage Alert",
                f"Warning: Memory usage is at {memory.percent}%. Consider reducing memory-intensive tasks."
            )
    except Exception as e:
        print(f"Error monitoring memory usage: {e}")

def monitor_suspicious_file_changes(directory="/var/www/html"):
    """
    Monitors a directory for suspicious file changes (e.g., unexpected new files or modifications).
    Sends an alert if changes are detected.
    :param directory: Path to the directory to monitor
    """
    try:
        # Placeholder implementation: In production, use tools like inotify or file integrity checkers
        suspicious_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # For demonstration, flag all files over a certain size as "suspicious"
                if os.path.getsize(file_path) > 10 * 1024 * 1024:  # 10 MB
                    suspicious_files.append(file_path)
        if suspicious_files:
            send_email_alert(
                "Suspicious File Change Alert",
                f"Warning: The following files are flagged as suspicious: {', '.join(suspicious_files)}"
            )
    except Exception as e:
        print(f"Error monitoring suspicious file changes: {e}")

def main():
    """
    Main function to run all monitoring tasks periodically.
    """
    print("Starting monitoring tasks...")
    try:
        monitor_disk_usage()
        monitor_cpu_usage()
        monitor_memory_usage()
        monitor_suspicious_file_changes()
    except KeyboardInterrupt:
        print("Monitoring tasks stopped by user.")

if __name__ == "__main__":
    main()
```
