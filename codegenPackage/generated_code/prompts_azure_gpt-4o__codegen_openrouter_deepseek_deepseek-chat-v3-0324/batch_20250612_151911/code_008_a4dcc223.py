"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to monitor system health and perform basic troubleshooting for a small business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_a4dcc22370784a17
Batch ID: 20250612_151911
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
System Health Monitor and Troubleshooting Tool for Small Businesses
"""

import psutil
import platform
import socket
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
CONFIG = {
    "monitoring_interval": 60,  # seconds
    "cpu_threshold": 80,  # percentage
    "memory_threshold": 80,  # percentage
    "disk_threshold": 80,  # percentage
    "email_notifications": {
        "enabled": True,
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "monitor@example.com",
        "sender_password": "password",
        "recipient_email": "admin@example.com"
    },
    "log_file": "system_monitor.log"
}

# Set up logging
logging.basicConfig(
    filename=CONFIG["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_system_info():
    """Collect basic system information"""
    try:
        info = {
            "hostname": socket.gethostname(),
            "os": f"{platform.system()} {platform.release()}",
            "cpu_count": psutil.cpu_count(logical=False),
            "cpu_cores": psutil.cpu_count(logical=True),
            "total_memory": round(psutil.virtual_memory().total / (1024 ** 3), 2),
            "total_disk": round(psutil.disk_usage('/').total / (1024 ** 3), 2)
        }
        return info
    except Exception as e:
        logger.error(f"Error getting system info: {str(e)}")
        return None

def check_cpu_usage():
    """Check CPU usage and return status"""
    try:
        usage = psutil.cpu_percent(interval=1)
        status = "OK"
        if usage > CONFIG["cpu_threshold"]:
            status = f"CRITICAL (>{CONFIG['cpu_threshold']}%)"
            logger.warning(f"High CPU usage detected: {usage}%")
        return {"usage": usage, "status": status}
    except Exception as e:
        logger.error(f"Error checking CPU usage: {str(e)}")
        return {"usage": None, "status": "ERROR"}

def check_memory_usage():
    """Check memory usage and return status"""
    try:
        mem = psutil.virtual_memory()
        usage = mem.percent
        status = "OK"
        if usage > CONFIG["memory_threshold"]:
            status = f"CRITICAL (>{CONFIG['memory_threshold']}%)"
            logger.warning(f"High memory usage detected: {usage}%")
        return {
            "usage": usage,
            "status": status,
            "available": round(mem.available / (1024 ** 3), 2)
        }
    except Exception as e:
        logger.error(f"Error checking memory usage: {str(e)}")
        return {"usage": None, "status": "ERROR"}

def check_disk_usage():
    """Check disk usage and return status"""
    try:
        disk = psutil.disk_usage('/')
        usage = disk.percent
        status = "OK"
        if usage > CONFIG["disk_threshold"]:
            status = f"CRITICAL (>{CONFIG['disk_threshold']}%)"
            logger.warning(f"High disk usage detected: {usage}%")
        return {
            "usage": usage,
            "status": status,
            "free": round(disk.free / (1024 ** 3), 2)
        }
    except Exception as e:
        logger.error(f"Error checking disk usage: {str(e)}")
        return {"usage": None, "status": "ERROR"}

def check_network():
    """Check basic network connectivity"""
    try:
        # Check if we can resolve and ping google.com
        socket.gethostbyname("google.com")
        return {"status": "OK", "message": "Network connectivity is good"}
    except Exception as e:
        logger.error(f"Network connectivity issue: {str(e)}")
        return {"status": "ERROR", "message": f"Network issue: {str(e)}"}

def check_running_processes():
    """Check for any suspicious or high-resource processes"""
    try:
        suspicious_processes = []
        high_cpu_processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > 50:
                    high_cpu_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        return {
            "high_cpu_processes": high_cpu_processes,
            "suspicious_processes": suspicious_processes
        }
    except Exception as e:
        logger.error(f"Error checking processes: {str(e)}")
        return {"high_cpu_processes": [], "suspicious_processes": []}

def send_email_alert(subject, message):
    """Send email notification if enabled in config"""
    if not CONFIG["email_notifications"]["enabled"]:
        return False
    
    try:
        msg = MIMEMultipart()
        msg['From'] = CONFIG["email_notifications"]["sender_email"]
        msg['To'] = CONFIG["email_notifications"]["recipient_email"]
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        with smtplib.SMTP(
            CONFIG["email_notifications"]["smtp_server"],
            CONFIG["email_notifications"]["smtp_port"]
        ) as server:
            server.starttls()
            server.login(
                CONFIG["email_notifications"]["sender_email"],
                CONFIG["email_notifications"]["sender_password"]
            )
            server.send_message(msg)
        
        logger.info("Email notification sent successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")
        return False

def generate_report(system_info, checks):
    """Generate a human-readable report"""
    report = f"""
System Health Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Hostname: {system_info['hostname']}
OS: {system_info['os']}
CPU Cores: {system_info['cpu_cores']} ({system_info['cpu_count']} physical)
Total Memory: {system_info['total_memory']} GB
Total Disk: {system_info['total_disk']} GB

=== System Status ===
CPU Usage: {checks['cpu']['usage']}% - {checks['cpu']['status']}
Memory Usage: {checks['memory']['usage']}% - {checks['memory']['status']} (Available: {checks['memory']['available']} GB)
Disk Usage: {checks['disk']['usage']}% - {checks['disk']['status']} (Free: {checks['disk']['free']} GB)
Network: {checks['network']['status']} - {checks['network']['message']}

=== High CPU Processes ===
"""
    
    if checks['processes']['high_cpu_processes']:
        for proc in checks['processes']['high_cpu_processes']:
            report += f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%, Memory: {proc['memory_percent']}%\n"
    else:
        report += "No high CPU processes detected\n"
    
    return report.strip()

def perform_health_check():
    """Perform all health checks and return results"""
    system_info = get_system_info()
    if not system_info:
        logger.error("Failed to get system information")
        return None
    
    checks = {
        "cpu": check_cpu_usage(),
        "memory": check_memory_usage(),
        "disk": check_disk_usage(),
        "network": check_network(),
        "processes": check_running_processes()
    }
    
    report = generate_report(system_info, checks)
    logger.info("System health check completed")
    
    # Check if any critical issues were found
    critical_issues = []
    if "CRITICAL" in checks["cpu"]["status"]:
        critical_issues.append("High CPU usage")
    if "CRITICAL" in checks["memory"]["status"]:
        critical_issues.append("High memory usage")
    if "CRITICAL" in checks["disk"]["status"]:
        critical_issues.append("High disk usage")
    if checks["network"]["status"] == "ERROR":
        critical_issues.append("Network connectivity issues")
    
    if critical_issues:
        alert_subject = f"CRITICAL: System issues detected on {system_info['hostname']}"
        alert_message = f"Critical
