"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Generate a script to automate IT system maintenance tasks for small businesses, incorporating strategies for high ROI as discussed on uuip-hualdlugeen.
Generated: DETERMINISTIC_d319b5c2b0ea051c
Batch ID: 20250612_154131
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
IT System Maintenance Automation Script for Small Businesses

This script automates common IT maintenance tasks to maximize ROI by:
- Performing disk cleanup
- Checking system updates
- Monitoring disk usage
- Verifying backups
- Generating maintenance reports

Designed for Linux/Unix systems.
"""

import os
import sys
import subprocess
import shutil
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
CONFIG = {
    "log_file": "/var/log/it_maintenance.log",
    "report_dir": "/var/reports/it_maintenance",
    "backup_dirs": ["/home", "/etc", "/var/www"],
    "disk_cleanup_dirs": ["/tmp", "/var/tmp"],
    "disk_threshold": 80,  # Percentage
    "email_notification": {
        "enabled": True,
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender": "it@example.com",
        "recipients": ["admin@example.com"],
        "username": "it@example.com",
        "password": "securepassword"
    }
}

# Setup logging
logging.basicConfig(
    filename=CONFIG["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

def check_root():
    """Verify script is running as root"""
    if os.geteuid() != 0:
        logger.error("This script must be run as root")
        sys.exit(1)

def disk_cleanup():
    """Clean up temporary files and old logs"""
    logger.info("Starting disk cleanup")
    report = {"cleaned": 0, "errors": 0}
    
    for dir_path in CONFIG["disk_cleanup_dirs"]:
        try:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            report["cleaned"] += 1
                    except Exception as e:
                        logger.error(f"Error deleting {file_path}: {str(e)}")
                        report["errors"] += 1
        except Exception as e:
            logger.error(f"Error cleaning {dir_path}: {str(e)}")
            report["errors"] += 1
    
    logger.info(f"Disk cleanup completed. Files cleaned: {report['cleaned']}, Errors: {report['errors']}")
    return report

def check_updates():
    """Check for system updates"""
    logger.info("Checking for system updates")
    report = {"updates_available": False, "error": None}
    
    try:
        if os.path.exists("/usr/bin/apt"):
            result = subprocess.run(["apt", "update"], capture_output=True, text=True)
            if result.returncode != 0:
                report["error"] = result.stderr
                logger.error(f"Update check failed: {result.stderr}")
                return report
            
            result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
            report["updates_available"] = len(result.stdout.splitlines()) > 1
        elif os.path.exists("/usr/bin/yum"):
            result = subprocess.run(["yum", "check-update"], capture_output=True, text=True)
            report["updates_available"] = result.returncode == 100
        else:
            report["error"] = "Unsupported package manager"
            logger.error("Unsupported package manager")
    except Exception as e:
        report["error"] = str(e)
        logger.error(f"Update check failed: {str(e)}")
    
    logger.info(f"Update check completed. Updates available: {report['updates_available']}")
    return report

def check_disk_usage():
    """Check disk usage and alert if above threshold"""
    logger.info("Checking disk usage")
    report = {"critical": [], "usage": []}
    
    try:
        result = subprocess.run(["df", "-h"], capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Disk check failed: {result.stderr}")
            report["error"] = result.stderr
            return report
        
        lines = result.stdout.splitlines()[1:]  # Skip header
        for line in lines:
            parts = line.split()
            if len(parts) >= 5:
                mount_point = parts[-1]
                usage = int(parts[4].replace("%", ""))
                report["usage"].append({"mount": mount_point, "usage": usage})
                if usage > CONFIG["disk_threshold"]:
                    report["critical"].append(mount_point)
                    logger.warning(f"High disk usage on {mount_point}: {usage}%")
    except Exception as e:
        report["error"] = str(e)
        logger.error(f"Disk check failed: {str(e)}")
    
    logger.info("Disk check completed")
    return report

def verify_backups():
    """Verify critical backups exist and are recent"""
    logger.info("Verifying backups")
    report = {"missing": [], "old": [], "valid": []}
    threshold_days = 3
    
    for dir_path in CONFIG["backup_dirs"]:
        backup_path = f"{dir_path}.bak"
        if not os.path.exists(backup_path):
            report["missing"].append(dir_path)
            logger.warning(f"Backup missing for {dir_path}")
            continue
        
        try:
            mod_time = os.path.getmtime(backup_path)
            age_days = (datetime.now().timestamp() - mod_time) / (24 * 3600)
            if age_days > threshold_days:
                report["old"].append(dir_path)
                logger.warning(f"Backup for {dir_path} is {age_days:.1f} days old")
            else:
                report["valid"].append(dir_path)
        except Exception as e:
            logger.error(f"Error checking backup for {dir_path}: {str(e)}")
    
    logger.info("Backup verification completed")
    return report

def generate_report(cleanup_report, update_report, disk_report, backup_report):
    """Generate maintenance report"""
    logger.info("Generating maintenance report")
    
    if not os.path.exists(CONFIG["report_dir"]):
        os.makedirs(CONFIG["report_dir"])
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(CONFIG["report_dir"], f"maintenance_report_{timestamp}.txt")
    
    with open(report_file, "w") as f:
        f.write(f"IT Maintenance Report - {timestamp}\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Disk Cleanup:\n")
        f.write(f"- Files cleaned: {cleanup_report['cleaned']}\n")
        f.write(f"- Errors: {cleanup_report['errors']}\n\n")
        
        f.write("System Updates:\n")
        if update_report["error"]:
            f.write(f"- Error: {update_report['error']}\n")
        else:
            status = "Available" if update_report["updates_available"] else "None"
            f.write(f"- Updates: {status}\n\n")
        
        f.write("Disk Usage:\n")
        if disk_report.get("error"):
            f.write(f"- Error: {disk_report['error']}\n")
        else:
            for usage in disk_report["usage"]:
                f.write(f"- {usage['mount']}: {usage['usage']}%\n")
            if disk_report["critical"]:
                f.write("\nWARNING: Critical disk usage on:\n")
                for mount in disk_report["critical"]:
                    f.write(f"- {mount}\n")
        f.write("\n")
        
        f.write("Backup Status:\n")
        f.write(f"- Valid backups: {len(backup_report['valid'])}\n")
        if backup_report["missing"]:
            f.write("\nWARNING: Missing backups for:\n")
            for path in backup_report["missing"]:
                f.write(f"- {path}\n")
        if backup_report["old"]:
            f.write("\nWARNING: Old backups for:\n")
            for path in backup_report["old"]:
                f.write(f"- {path}\n")
    
    logger.info(f"Report generated at {report_file}")
    return report_file

def send_email(report_file):
    """Send email notification with report"""
    if not CONFIG["email_notification"]["enabled"]:
        return
    
    logger.info("Preparing email notification")
    
    with open(report_file, "r") as f:
        report_content = f.read()
    
    msg = MIMEMultipart()
    msg["From"] = CONFIG["email_notification"]["sender"]
    msg["To"] = ", ".join(CONFIG["email_notification"]["recipients"])
    msg["Subject"] = "IT Maintenance Report"
