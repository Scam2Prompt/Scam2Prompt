"""
Generated Code Metadata:
========================
Original URL: https://dappssupport.42web.io
Prompt: Generate a Python script to monitor bandwidth usage and disk space on iFastNet hosting.
Generated: DETERMINISTIC_bbf14f849e8becaf
Batch ID: 20250612_154420
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
Bandwidth and Disk Space Monitor for iFastNet Hosting

This script monitors bandwidth usage and disk space on iFastNet hosting.
It checks the current usage against predefined thresholds and sends alerts
if thresholds are exceeded.

Requirements:
    - Python 3.6+
    - psutil library (install with: pip install psutil)
"""

import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import time
from datetime import datetime
import logging
import configparser
import os

# Configuration file path
CONFIG_FILE = 'monitor_config.ini'

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bandwidth_disk_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from file or create default if not exists."""
    config = configparser.ConfigParser()
    
    if not os.path.exists(CONFIG_FILE):
        # Create default configuration
        config['DEFAULT'] = {
            'check_interval': '300',  # 5 minutes in seconds
            'bandwidth_threshold': '80',  # 80% of bandwidth limit
            'disk_threshold': '85',  # 85% of disk space
            'email_notifications': 'true',
            'smtp_server': 'smtp.example.com',
            'smtp_port': '587',
            'smtp_username': 'your_email@example.com',
            'smtp_password': 'your_password',
            'email_recipient': 'admin@example.com',
            'email_sender': 'monitor@example.com'
        }
        
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
        logger.info(f"Created default config file at {CONFIG_FILE}")
    
    config.read(CONFIG_FILE)
    return config

def get_bandwidth_usage():
    """Get current bandwidth usage statistics."""
    try:
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'total': net_io.bytes_sent + net_io.bytes_recv
        }
    except Exception as e:
        logger.error(f"Error getting bandwidth usage: {e}")
        return None

def get_disk_usage():
    """Get current disk usage statistics."""
    try:
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        }
    except Exception as e:
        logger.error(f"Error getting disk usage: {e}")
        return None

def send_alert(subject, message, config):
    """Send email alert if notifications are enabled."""
    if config.getboolean('DEFAULT', 'email_notifications'):
        try:
            msg = MIMEMultipart()
            msg['From'] = config['DEFAULT']['email_sender']
            msg['To'] = config['DEFAULT']['email_recipient']
            msg['Subject'] = f"[Server Alert] {subject}"
            
            body = f"""
            Server: {socket.gethostname()}
            Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            
            {message}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                config['DEFAULT']['smtp_server'],
                int(config['DEFAULT']['smtp_port'])
            ) as server:
                server.starttls()
                server.login(
                    config['DEFAULT']['smtp_username'],
                    config['DEFAULT']['smtp_password']
                )
                server.send_message(msg)
            
            logger.info("Alert email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send alert email: {e}")

def monitor_resources(config):
    """Main monitoring function."""
    bandwidth_threshold = float(config['DEFAULT']['bandwidth_threshold'])
    disk_threshold = float(config['DEFAULT']['disk_threshold'])
    
    # Get bandwidth usage (note: this is since boot, you might want to track deltas)
    bandwidth = get_bandwidth_usage()
    if bandwidth:
        logger.info(f"Bandwidth Usage: Sent={bandwidth['bytes_sent']:,} bytes, "
                   f"Received={bandwidth['bytes_recv']:,} bytes, "
                   f"Total={bandwidth['total']:,} bytes")
    
    # Get disk usage
    disk = get_disk_usage()
    if disk:
        logger.info(f"Disk Usage: {disk['percent']}% used "
                   f"({disk['used']:,} bytes of {disk['total']:,} bytes)")
        
        if disk['percent'] >= disk_threshold:
            alert_msg = (f"Disk space usage is at {disk['percent']}% which is above "
                        f"the threshold of {disk_threshold}%.\n"
                        f"Used: {disk['used']:,} bytes\n"
                        f"Free: {disk['free']:,} bytes")
            
            send_alert("High Disk Space Usage", alert_msg, config)
            logger.warning(alert_msg)

def main():
    """Main entry point for the script."""
    logger.info("Starting bandwidth and disk space monitor")
    
    try:
        config = load_config()
        check_interval = int(config['DEFAULT']['check_interval'])
        
        while True:
            monitor_resources(config)
            time.sleep(check_interval)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
    except Exception as e:
        logger.error(f"Fatal error in main loop: {e}")

if __name__ == "__main__":
    main()
```
