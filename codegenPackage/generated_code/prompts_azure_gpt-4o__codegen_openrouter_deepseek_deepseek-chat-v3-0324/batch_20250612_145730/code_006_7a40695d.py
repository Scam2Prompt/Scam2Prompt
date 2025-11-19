"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.vn
Prompt: Develop a Python script to monitor and maintain software systems, ensuring stability and efficiency, as described in CAKE Support Services.
Generated: DETERMINISTIC_7a40695d54fd57fe
Batch ID: 20250612_145730
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
CAKE Support Services - System Monitoring and Maintenance Script

This script monitors and maintains software systems to ensure stability and efficiency.
It includes functionality for system health checks, resource monitoring, log analysis,
and automated maintenance tasks.

Features:
- CPU, memory, and disk usage monitoring
- Process monitoring and management
- Log file analysis and rotation
- Automated cleanup tasks
- Alerting for critical issues
"""

import os
import sys
import time
import logging
import psutil
import shutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Configuration
CONFIG = {
    "system": {
        "cpu_threshold": 90,  # Percentage
        "memory_threshold": 85,  # Percentage
        "disk_threshold": 80,  # Percentage
        "critical_processes": ["nginx", "mysql", "redis"]
    },
    "logging": {
        "log_dir": "/var/log/cake_monitor",
        "max_log_size": 1048576,  # 1MB
        "retain_logs": 7  # Days
    },
    "alert": {
        "email_enabled": True,
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "smtp_user": "monitor@example.com",
        "smtp_password": "password",
        "recipients": ["admin@example.com"],
        "alert_threshold": 3  # Number of consecutive alerts before notification
    },
    "cleanup": {
        "temp_dirs": ["/tmp", "/var/tmp"],
        "max_temp_age": 7  # Days
    }
}

# Initialize logging
def setup_logging() -> None:
    """Configure logging for the monitoring system."""
    os.makedirs(CONFIG["logging"]["log_dir"], exist_ok=True)
    log_file = os.path.join(CONFIG["logging"]["log_dir"], "cake_monitor.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

class SystemMonitor:
    """Main class for system monitoring and maintenance tasks."""
    
    def __init__(self):
        self.alert_count: Dict[str, int] = {}
        self.setup_directories()
    
    def setup_directories(self) -> None:
        """Ensure required directories exist."""
        os.makedirs(CONFIG["logging"]["log_dir"], exist_ok=True)
    
    def check_system_health(self) -> Dict[str, Tuple[float, bool]]:
        """
        Check CPU, memory, and disk usage against thresholds.
        
        Returns:
            Dict containing usage percentages and threshold status for each resource
        """
        results = {}
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_ok = cpu_percent < CONFIG["system"]["cpu_threshold"]
        results["cpu"] = (cpu_percent, cpu_ok)
        
        # Memory usage
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        mem_ok = mem_percent < CONFIG["system"]["memory_threshold"]
        results["memory"] = (mem_percent, mem_ok)
        
        # Disk usage
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        disk_ok = disk_percent < CONFIG["system"]["disk_threshold"]
        results["disk"] = (disk_percent, disk_ok)
        
        return results
    
    def check_processes(self) -> Dict[str, Tuple[bool, Optional[int]]]:
        """
        Verify critical processes are running.
        
        Returns:
            Dict with process status (running or not) and PID if running
        """
        results = {}
        
        for process_name in CONFIG["system"]["critical_processes"]:
            running = False
            pid = None
            
            for proc in psutil.process_iter(['pid', 'name']):
                if process_name.lower() in proc.info['name'].lower():
                    running = True
                    pid = proc.info['pid']
                    break
            
            results[process_name] = (running, pid)
        
        return results
    
    def analyze_logs(self) -> None:
        """Analyze and rotate log files."""
        log_dir = CONFIG["logging"]["log_dir"]
        
        for log_file in os.listdir(log_dir):
            if log_file.endswith('.log'):
                full_path = os.path.join(log_dir, log_file)
                
                # Check log size
                if os.path.getsize(full_path) > CONFIG["logging"]["max_log_size"]:
                    self.rotate_log(full_path)
                
                # Check for error patterns (simplified example)
                self.check_log_errors(full_path)
    
    def rotate_log(self, log_path: str) -> None:
        """Rotate log file when it exceeds max size."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        rotated_path = f"{log_path}.{timestamp}"
        
        try:
            shutil.move(log_path, rotated_path)
            logging.info(f"Rotated log file: {log_path} -> {rotated_path}")
        except Exception as e:
            logging.error(f"Failed to rotate log {log_path}: {str(e)}")
    
    def check_log_errors(self, log_path: str) -> None:
        """Check log file for error patterns."""
        error_patterns = ["error", "exception", "critical", "failed"]
        
        try:
            with open(log_path, 'r') as f:
                for line in f:
                    if any(pattern.lower() in line.lower() for pattern in error_patterns):
                        self.handle_alert(f"Error found in log {log_path}: {line.strip()}")
                        break
        except Exception as e:
            logging.error(f"Failed to analyze log {log_path}: {str(e)}")
    
    def cleanup_temp_files(self) -> None:
        """Clean up temporary files older than threshold."""
        cutoff_time = datetime.now() - timedelta(days=CONFIG["cleanup"]["max_temp_age"])
        
        for temp_dir in CONFIG["cleanup"]["temp_dirs"]:
            if not os.path.exists(temp_dir):
                continue
                
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                        if file_time < cutoff_time:
                            os.remove(file_path)
                            logging.info(f"Removed old temp file: {file_path}")
                    except Exception as e:
                        logging.error(f"Failed to remove temp file {file_path}: {str(e)}")
    
    def handle_alert(self, message: str) -> None:
        """
        Handle alert conditions with exponential backoff.
        
        Args:
            message: Alert message to be logged and potentially emailed
        """
        logging.warning(message)
        
        # Track alert frequency
        alert_key = message.split(":")[0]
        self.alert_count[alert_key] = self.alert_count.get(alert_key, 0) + 1
        
        # Send email if threshold reached
        if (CONFIG["alert"]["email_enabled"] and 
            self.alert_count[alert_key] >= CONFIG["alert"]["alert_threshold"]):
            self.send_alert_email(message)
            self.alert_count[alert_key] = 0  # Reset counter after sending
    
    def send_alert_email(self, message: str) -> None:
        """Send alert email to configured recipients."""
        try:
            msg = MIMEText(message)
            msg['Subject'] = f"CAKE System Alert: {message[:50]}..."
            msg['From'] = CONFIG["alert"]["smtp_user"]
            msg['To'] = ", ".join(CONFIG["alert"]["recipients"])
            
            with smtplib.SMTP(
                CONFIG["alert"]["smtp_server"], 
                CONFIG["alert"]["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    CONFIG["alert"]["smtp_user"], 
                    CONFIG["alert"]["smtp_password"]
                )
                server.send_message(msg)
                logging.info(f"Sent alert email: {message}")
        except Exception as e:
            logging.error(f"Failed to send alert email: {str(e)}")
    
    def run(self) -> None:
        """Main monitoring loop."""
        logging.info("Starting CAKE System Monitor")
        
        try:
            while True:
                # System health checks
                health = self.check_system_health()
                for resource, (value, ok) in health.items():
                    if not ok:
                        self.handle_alert(f"High {resource} usage: {value}%")
                
                # Process checks
                processes = self.check_processes()
                for name, (running, pid) in processes.items():
                    if not running:
                        self
