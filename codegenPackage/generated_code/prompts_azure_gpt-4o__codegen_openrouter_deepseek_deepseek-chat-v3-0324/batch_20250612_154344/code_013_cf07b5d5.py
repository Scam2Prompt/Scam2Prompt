"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Develop a program to provide 24/7 IT system monitoring and alerting, ensuring minimal downtime, as described in IMTS's outsourced managed IT services.
Generated: DETERMINISTIC_cf07b5d57061df60
Batch ID: 20250612_154344
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://{host}:{port": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import time
import logging
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Optional
import requests
import socket
import psutil
import threading
from datetime import datetime

# Configuration
CONFIG = {
    "monitoring_interval": 60,  # seconds
    "systems_to_monitor": [
        {"name": "Web Server", "host": "example.com", "port": 80, "type": "http"},
        {"name": "Database Server", "host": "db.example.com", "port": 5432, "type": "tcp"},
        {"name": "Local CPU", "host": "localhost", "type": "cpu", "threshold": 90},
        {"name": "Local Memory", "host": "localhost", "type": "memory", "threshold": 85}
    ],
    "alert_recipients": ["admin@example.com", "it-team@example.com"],
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "alerts@example.com",
    "smtp_password": "securepassword",
    "alert_cooldown": 3600  # seconds (1 hour)
}

# Global state for tracking alerts
alert_history: Dict[str, datetime] = {}

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('monitoring.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class SystemMonitor:
    """Class to monitor various system components."""
    
    @staticmethod
    def check_http_service(host: str, port: int) -> bool:
        """Check if HTTP service is responding."""
        try:
            response = requests.get(f"http://{host}:{port}", timeout=10)
            return response.status_code == 200
        except requests.RequestException as e:
            logger.error(f"HTTP check failed for {host}:{port} - {str(e)}")
            return False
    
    @staticmethod
    def check_tcp_service(host: str, port: int) -> bool:
        """Check if TCP port is open."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(10)
                result = sock.connect_ex((host, port))
                return result == 0
        except socket.error as e:
            logger.error(f"TCP check failed for {host}:{port} - {str(e)}")
            return False
    
    @staticmethod
    def check_cpu_usage(threshold: float) -> bool:
        """Check if CPU usage exceeds threshold."""
        try:
            usage = psutil.cpu_percent(interval=1)
            return usage <= threshold
        except Exception as e:
            logger.error(f"CPU check failed - {str(e)}")
            return False
    
    @staticmethod
    def check_memory_usage(threshold: float) -> bool:
        """Check if memory usage exceeds threshold."""
        try:
            usage = psutil.virtual_memory().percent
            return usage <= threshold
        except Exception as e:
            logger.error(f"Memory check failed - {str(e)}")
            return False

class AlertManager:
    """Class to manage alert notifications."""
    
    @staticmethod
    def should_send_alert(system_name: str) -> bool:
        """Check if we should send an alert based on cooldown period."""
        last_alert = alert_history.get(system_name)
        if last_alert is None:
            return True
        
        time_since_last = (datetime.now() - last_alert).total_seconds()
        return time_since_last >= CONFIG["alert_cooldown"]
    
    @staticmethod
    def update_alert_history(system_name: str):
        """Update the last alert time for a system."""
        alert_history[system_name] = datetime.now()
    
    @staticmethod
    def send_alert(system_name: str, message: str):
        """Send an alert email."""
        if not AlertManager.should_send_alert(system_name):
            logger.info(f"Alert for {system_name} suppressed due to cooldown")
            return
        
        try:
            msg = MIMEText(message)
            msg['Subject'] = f"ALERT: {system_name} - System Issue Detected"
            msg['From'] = CONFIG["smtp_username"]
            msg['To'] = ", ".join(CONFIG["alert_recipients"])
            
            with smtplib.SMTP(CONFIG["smtp_server"], CONFIG["smtp_port"]) as server:
                server.starttls()
                server.login(CONFIG["smtp_username"], CONFIG["smtp_password"])
                server.sendmail(
                    CONFIG["smtp_username"],
                    CONFIG["alert_recipients"],
                    msg.as_string()
                )
            
            AlertManager.update_alert_history(system_name)
            logger.info(f"Alert sent for {system_name}")
        except Exception as e:
            logger.error(f"Failed to send alert for {system_name} - {str(e)}")

def monitor_system(system: Dict):
    """Monitor a single system and send alerts if issues are detected."""
    system_name = system["name"]
    system_type = system["type"]
    
    try:
        if system_type == "http":
            is_healthy = SystemMonitor.check_http_service(system["host"], system["port"])
        elif system_type == "tcp":
            is_healthy = SystemMonitor.check_tcp_service(system["host"], system["port"])
        elif system_type == "cpu":
            is_healthy = SystemMonitor.check_cpu_usage(system["threshold"])
        elif system_type == "memory":
            is_healthy = SystemMonitor.check_memory_usage(system["threshold"])
        else:
            logger.error(f"Unknown system type: {system_type}")
            return
        
        if not is_healthy:
            message = f"System {system_name} ({system_type}) is not responding or exceeds threshold"
            AlertManager.send_alert(system_name, message)
        else:
            logger.info(f"System {system_name} is healthy")
    except Exception as e:
        logger.error(f"Error monitoring {system_name}: {str(e)}")

def main():
    """Main monitoring loop."""
    logger.info("Starting IT System Monitoring Service")
    
    while True:
        threads = []
        for system in CONFIG["systems_to_monitor"]:
            thread = threading.Thread(target=monitor_system, args=(system,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        logger.info(f"Monitoring cycle completed. Next cycle in {CONFIG['monitoring_interval']} seconds")
        time.sleep(CONFIG["monitoring_interval"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Monitoring service stopped by user")
    except Exception as e:
        logger.error(f"Fatal error in monitoring service: {str(e)}")
```
