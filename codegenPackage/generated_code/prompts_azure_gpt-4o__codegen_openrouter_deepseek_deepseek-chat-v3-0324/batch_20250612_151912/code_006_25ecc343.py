"""
Generated Code Metadata:
========================
Original URL: https://web3-wave.com
Prompt: Generate code to monitor server performance and resource usage for LWS's dedicated or VPS hosting solutions.
Generated: DETERMINISTIC_25ecc343565c4f25
Batch ID: 20250612_151912
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
Server Performance Monitor for LWS Hosting Solutions

This script monitors server performance metrics including CPU, memory, disk,
and network usage. It logs the data and can send alerts when thresholds are exceeded.
"""

import psutil
import time
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import json
import argparse
import sys

# Configuration
CONFIG = {
    "monitoring_interval": 60,  # seconds
    "log_file": "/var/log/server_monitor.log",
    "alert_thresholds": {
        "cpu_percent": 90,
        "memory_percent": 85,
        "disk_percent": 90,
        "network_saturation": 80
    },
    "email_alerts": {
        "enabled": False,
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "monitor@example.com",
        "sender_password": "password",
        "recipient_email": "admin@example.com"
    }
}

# Initialize logging
logging.basicConfig(
    filename=CONFIG['log_file'],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ServerMonitor')

def get_system_metrics():
    """Collect system performance metrics."""
    metrics = {
        'timestamp': datetime.now().isoformat(),
        'cpu': {
            'percent': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count()
        },
        'memory': {
            'total': psutil.virtual_memory().total,
            'available': psutil.virtual_memory().available,
            'percent': psutil.virtual_memory().percent,
            'used': psutil.virtual_memory().used
        },
        'disk': {},
        'network': {}
    }

    # Disk metrics
    for partition in psutil.disk_partitions():
        if partition.mountpoint == '/':
            usage = psutil.disk_usage(partition.mountpoint)
            metrics['disk'] = {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            }
            break

    # Network metrics
    net_io = psutil.net_io_counters()
    metrics['network'] = {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

    return metrics

def check_thresholds(metrics):
    """Check if any metrics exceed configured thresholds."""
    alerts = []
    
    if metrics['cpu']['percent'] > CONFIG['alert_thresholds']['cpu_percent']:
        alerts.append(f"High CPU usage: {metrics['cpu']['percent']}%")
    
    if metrics['memory']['percent'] > CONFIG['alert_thresholds']['memory_percent']:
        alerts.append(f"High memory usage: {metrics['memory']['percent']}%")
    
    if 'percent' in metrics['disk'] and metrics['disk']['percent'] > CONFIG['alert_thresholds']['disk_percent']:
        alerts.append(f"High disk usage: {metrics['disk']['percent']}%")
    
    return alerts

def send_email_alert(subject, message):
    """Send email alert if enabled in config."""
    if not CONFIG['email_alerts']['enabled']:
        return
    
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = CONFIG['email_alerts']['sender_email']
        msg['To'] = CONFIG['email_alerts']['recipient_email']
        
        with smtplib.SMTP(
            CONFIG['email_alerts']['smtp_server'],
            CONFIG['email_alerts']['smtp_port']
        ) as server:
            server.starttls()
            server.login(
                CONFIG['email_alerts']['sender_email'],
                CONFIG['email_alerts']['sender_password']
            )
            server.send_message(msg)
    except Exception as e:
        logger.error(f"Failed to send email alert: {str(e)}")

def log_metrics(metrics):
    """Log metrics to file."""
    try:
        logger.info(json.dumps(metrics))
    except Exception as e:
        logger.error(f"Failed to log metrics: {str(e)}")

def load_config(config_file):
    """Load configuration from JSON file."""
    try:
        with open(config_file) as f:
            config = json.load(f)
            CONFIG.update(config)
    except FileNotFoundError:
        logger.warning(f"Config file {config_file} not found, using defaults")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in config file {config_file}")
    except Exception as e:
        logger.error(f"Error loading config: {str(e)}")

def main():
    """Main monitoring loop."""
    parser = argparse.ArgumentParser(description='Server Performance Monitor')
    parser.add_argument('--config', help='Path to config file', default='config.json')
    args = parser.parse_args()
    
    load_config(args.config)
    
    logger.info("Starting server performance monitor")
    
    try:
        while True:
            metrics = get_system_metrics()
            log_metrics(metrics)
            
            alerts = check_thresholds(metrics)
            if alerts:
                alert_message = "\n".join(alerts)
                logger.warning(f"Alert triggered:\n{alert_message}")
                send_email_alert("Server Performance Alert", alert_message)
            
            time.sleep(CONFIG['monitoring_interval'])
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Monitoring failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
