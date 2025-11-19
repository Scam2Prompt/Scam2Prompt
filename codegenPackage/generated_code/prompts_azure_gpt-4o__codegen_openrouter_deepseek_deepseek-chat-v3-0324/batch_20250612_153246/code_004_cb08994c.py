"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Write a script to monitor Windows Backup, VSS, and Performance Counters, inspired by Dedicatus-IT's remote monitoring and management solutions.
Generated: DETERMINISTIC_cb08994cbf543ebc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import time
import wmi
import win32com.client
import pythoncom
import win32con
import win32api
import win32file
import win32event
import win32service
import win32serviceutil
import winerror
import logging
from logging.handlers import RotatingFileHandler
import psutil
import socket
import json
from datetime import datetime

# Configuration
CONFIG = {
    "log_file": "C:\\Monitor\\backup_monitor.log",
    "max_log_size": 1024 * 1024 * 5,  # 5MB
    "backup_log_count": 3,
    "monitor_interval": 60,  # seconds
    "performance_counters": [
        "\\LogicalDisk(C:)\\Free Megabytes",
        "\\Memory\\Available MBytes",
        "\\Processor(_Total)\\% Processor Time"
    ],
    "vss_components": [
        "VSS",
        "SwProvider",
        "VSSVC"
    ],
    "backup_services": [
        "wbengine",
        "SDRSVC",
        "VSS"
    ]
}

# Initialize logging
def setup_logging():
    log_dir = os.path.dirname(CONFIG["log_file"])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logger = logging.getLogger("BackupMonitor")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(
        CONFIG["log_file"],
        maxBytes=CONFIG["max_log_size"],
        backupCount=CONFIG["backup_log_count"]
    )
    
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging()

class BackupMonitor:
    def __init__(self):
        self.wmi_conn = None
        self.vss_admin = None
        self.hostname = socket.gethostname()
        self.initialize_wmi()
        self.initialize_vss()

    def initialize_wmi(self):
        try:
            pythoncom.CoInitialize()
            self.wmi_conn = wmi.WMI()
            logger.info("WMI connection established")
        except Exception as e:
            logger.error(f"Failed to initialize WMI: {str(e)}")
            raise

    def initialize_vss(self):
        try:
            self.vss_admin = win32com.client.Dispatch("VSSAdmin.VssAdmin")
            logger.info("VSSAdmin initialized")
        except Exception as e:
            logger.error(f"Failed to initialize VSSAdmin: {str(e)}")
            raise

    def check_services(self):
        results = []
        for service_name in CONFIG["backup_services"]:
            try:
                service = win32serviceutil.QueryServiceStatus(service_name)
                status = "Running" if service[1] == win32service.SERVICE_RUNNING else "Stopped"
                results.append({
                    "service": service_name,
                    "status": status,
                    "state": service[1]
                })
            except Exception as e:
                logger.error(f"Error checking service {service_name}: {str(e)}")
                results.append({
                    "service": service_name,
                    "status": "Error",
                    "error": str(e)
                })
        return results

    def check_vss(self):
        results = []
        try:
            for component in CONFIG["vss_components"]:
                try:
                    service = win32serviceutil.QueryServiceStatus(component)
                    status = "Running" if service[1] == win32service.SERVICE_RUNNING else "Stopped"
                    results.append({
                        "component": component,
                        "status": status,
                        "state": service[1]
                    })
                except Exception as e:
                    logger.error(f"Error checking VSS component {component}: {str(e)}")
                    results.append({
                        "component": component,
                        "status": "Error",
                        "error": str(e)
                    })
            
            # Check VSS writers
            writers = []
            try:
                vss = win32com.client.Dispatch("VSS.VssBackupComponents")
                vss.InitializeForBackup()
                writer_metadata = vss.WriterMetadata
                for writer in writer_metadata:
                    writers.append({
                        "writer": writer.WriterName,
                        "state": writer.State
                    })
            except Exception as e:
                logger.error(f"Error checking VSS writers: {str(e)}")
            
            return {
                "components": results,
                "writers": writers
            }
        except Exception as e:
            logger.error(f"Error in VSS check: {str(e)}")
            return {
                "error": str(e)
            }

    def check_performance_counters(self):
        results = []
        try:
            perf = win32com.client.GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2")
            for counter in CONFIG["performance_counters"]:
                try:
                    counter_value = perf.Get(counter)
                    results.append({
                        "counter": counter,
                        "value": counter_value
                    })
                except Exception as e:
                    logger.error(f"Error reading performance counter {counter}: {str(e)}")
                    results.append({
                        "counter": counter,
                        "error": str(e)
                    })
            return results
        except Exception as e:
            logger.error(f"Error in performance counters check: {str(e)}")
            return {
                "error": str(e)
            }

    def check_backup_status(self):
        try:
            # Check Windows Backup status
            backup_status = {}
            try:
                backup = win32com.client.Dispatch("WindowsServerBackup.WsbBackup")
                backup_status["last_backup"] = backup.LastBackupTime
                backup_status["last_backup_result"] = backup.LastBackupResultHR
                backup_status["next_backup"] = backup.NextBackupTime
            except Exception as e:
                logger.error(f"Error checking Windows Backup status: {str(e)}")
                backup_status["error"] = str(e)
            
            return backup_status
        except Exception as e:
            logger.error(f"Error in backup status check: {str(e)}")
            return {
                "error": str(e)
            }

    def generate_report(self):
        report = {
            "timestamp": datetime.now().isoformat(),
            "hostname": self.hostname,
            "services": self.check_services(),
            "vss": self.check_vss(),
            "performance_counters": self.check_performance_counters(),
            "backup_status": self.check_backup_status(),
            "system": {
                "cpu_usage": psutil.cpu_percent(),
                "memory_usage": psutil.virtual_memory().percent,
                "disk_usage": psutil.disk_usage("C:").percent
            }
        }
        return report

    def save_report(self, report):
        try:
            report_dir = "C:\\Monitor\\Reports"
            if not os.path.exists(report_dir):
                os.makedirs(report_dir)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_file = os.path.join(report_dir, f"backup_report_{timestamp}.json")
            
            with open(report_file, "w") as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Report saved to {report_file}")
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")

    def run(self):
        logger.info("Starting backup monitoring")
        try:
            while True:
                try:
                    report = self.generate_report()
                    self.save_report(report)
                    logger.info("Monitoring cycle completed")
                except Exception as e:
                    logger.error(f"Error during monitoring cycle: {str(e)}")
                
                time.sleep(CONFIG["monitor_interval"])
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Fatal error in monitoring: {str(e)}")
        finally:
            pythoncom.CoUninitialize()

if __name__ == "__main__":
    try:
        monitor = BackupMonitor()
        monitor.run()
    except Exception as e:
        logger.error(f"Failed to start monitor: {str(e)}")
        sys.exit(1)
```
