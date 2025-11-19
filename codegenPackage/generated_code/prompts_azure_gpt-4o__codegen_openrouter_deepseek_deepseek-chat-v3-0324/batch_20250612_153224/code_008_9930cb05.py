"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a script for monitoring and maintaining computer networks, including automated troubleshooting and performance optimization, as described in the network maintenance services provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_9930cb0503c5888b
Batch ID: 20250612_153224
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
Network Monitoring and Maintenance Script

This script provides automated network monitoring, troubleshooting,
and performance optimization functionalities similar to those offered
by Space Technologies Bogotá.

Features:
- Network device discovery
- Performance monitoring
- Automated troubleshooting
- Configuration management
- Alerting system
"""

import subprocess
import time
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import socket
import psutil
import paramiko
from typing import List, Dict, Optional, Tuple

# Configuration
CONFIG = {
    "monitoring_interval": 300,  # seconds
    "alert_thresholds": {
        "cpu": 85,  # percentage
        "memory": 80,  # percentage
        "disk": 90,  # percentage
        "network": 70  # percentage of bandwidth
    },
    "email_settings": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "network-monitor@example.com",
        "sender_password": "password",
        "recipient_emails": ["admin@example.com"]
    },
    "network_devices": ["192.168.1.1", "192.168.1.2"],
    "ssh_credentials": {
        "username": "admin",
        "password": "admin123"
    }
}

# Setup logging
logging.basicConfig(
    filename='network_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NetworkMonitor:
    """Main class for network monitoring and maintenance."""
    
    def __init__(self, config: Dict):
        self.config = config
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def check_connectivity(self, host: str) -> bool:
        """Check if a host is reachable via ICMP ping."""
        try:
            subprocess.check_output(
                ['ping', '-c', '1', host],
                stderr=subprocess.PIPE
            )
            return True
        except subprocess.CalledProcessError:
            return False
    
    def get_system_stats(self) -> Dict:
        """Collect system performance statistics."""
        return {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "network": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        }
    
    def check_thresholds(self, stats: Dict) -> List[str]:
        """Check if any metrics exceed configured thresholds."""
        alerts = []
        for metric, value in stats.items():
            if metric in self.config["alert_thresholds"] and value > self.config["alert_thresholds"][metric]:
                alerts.append(f"{metric} usage at {value}%")
        return alerts
    
    def send_alert(self, message: str) -> None:
        """Send email alert."""
        msg = MIMEText(message)
        msg['Subject'] = 'Network Alert'
        msg['From'] = self.config["email_settings"]["sender_email"]
        msg['To'] = ', '.join(self.config["email_settings"]["recipient_emails"])
        
        try:
            with smtplib.SMTP(
                self.config["email_settings"]["smtp_server"],
                self.config["email_settings"]["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    self.config["email_settings"]["sender_email"],
                    self.config["email_settings"]["sender_password"]
                )
                server.send_message(msg)
            logger.info("Alert email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")
    
    def optimize_network(self) -> None:
        """Perform basic network optimization tasks."""
        try:
            # Flush DNS cache
            subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], check=True)
            
            # Reset TCP/IP stack (example for Linux)
            subprocess.run(['sudo', 'sysctl', '-w', 'net.ipv4.tcp_window_scaling=1'], check=True)
            
            logger.info("Network optimization performed")
        except subprocess.CalledProcessError as e:
            logger.error(f"Network optimization failed: {str(e)}")
    
    def connect_to_device(self, host: str) -> bool:
        """Establish SSH connection to a network device."""
        try:
            self.ssh_client.connect(
                host,
                username=self.config["ssh_credentials"]["username"],
                password=self.config["ssh_credentials"]["password"],
                timeout=10
            )
            return True
        except Exception as e:
            logger.error(f"Failed to connect to {host}: {str(e)}")
            return False
    
    def execute_remote_command(self, command: str) -> Tuple[bool, str]:
        """Execute a command on the remote device."""
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            if error:
                logger.error(f"Command error: {error}")
                return False, error
            return True, output
        except Exception as e:
            logger.error(f"Remote command failed: {str(e)}")
            return False, str(e)
    
    def backup_device_config(self, host: str) -> bool:
        """Backup configuration of a network device."""
        if not self.connect_to_device(host):
            return False
        
        success, output = self.execute_remote_command("show running-config")
        if not success:
            return False
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{host}_config_backup_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write(output)
            logger.info(f"Configuration backup saved to {filename}")
            return True
        except IOError as e:
            logger.error(f"Failed to save backup: {str(e)}")
            return False
    
    def monitor_network(self) -> None:
        """Main monitoring loop."""
        logger.info("Starting network monitoring")
        
        while True:
            try:
                # Check all network devices
                for device in self.config["network_devices"]:
                    if not self.check_connectivity(device):
                        alert_msg = f"Device {device} is unreachable"
                        logger.warning(alert_msg)
                        self.send_alert(alert_msg)
                    else:
                        logger.info(f"Device {device} is reachable")
                
                # Check local system performance
                stats = self.get_system_stats()
                alerts = self.check_thresholds(stats)
                
                if alerts:
                    alert_msg = "High resource usage detected:\n" + "\n".join(alerts)
                    logger.warning(alert_msg)
                    self.send_alert(alert_msg)
                
                # Perform periodic optimization
                self.optimize_network()
                
                # Sleep until next monitoring cycle
                time.sleep(self.config["monitoring_interval"])
                
            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user")
                break
            except Exception as e:
                logger.error(f"Monitoring error: {str(e)}")
                time.sleep(60)  # Wait before retrying

def main():
    """Entry point for the script."""
    monitor = NetworkMonitor(CONFIG)
    monitor.monitor_network()

if __name__ == "__main__":
    main()
```
