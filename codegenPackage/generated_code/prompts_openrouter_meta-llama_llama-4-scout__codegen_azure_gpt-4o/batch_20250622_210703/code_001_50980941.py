"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Write a Python script to manage and monitor IT infrastructure remotely, similar to the services offered by Dedicatus-IT to MSPs.
Generated: DETERMINISTIC_50980941fe796c7e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import platform
import psutil
import socket
import json
from datetime import datetime

class ITInfrastructureManager:
    """
    A class to manage and monitor IT infrastructure remotely.
    """

    def __init__(self):
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.os_info = platform.platform()
        self.cpu_info = platform.processor()
        self.memory_info = psutil.virtual_memory()
        self.disk_info = psutil.disk_usage('/')
        self.network_info = psutil.net_if_addrs()

    def get_system_info(self):
        """
        Gather basic system information.
        """
        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "os_info": self.os_info,
            "cpu_info": self.cpu_info,
            "memory_total": self.memory_info.total,
            "memory_used": self.memory_info.used,
            "disk_total": self.disk_info.total,
            "disk_used": self.disk_info.used,
            "network_interfaces": {iface: [addr.address for addr in addrs] for iface, addrs in self.network_info.items()}
        }

    def execute_command(self, command):
        """
        Execute a shell command and return the output.
        """
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            if result.returncode == 0:
                return {"success": True, "output": result.stdout.strip()}
            else:
                return {"success": False, "error": result.stderr.strip()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def monitor_resources(self):
        """
        Monitor system resources such as CPU, memory, and disk usage.
        """
        return {
            "cpu_usage_percent": psutil.cpu_percent(interval=1),
            "memory_usage_percent": self.memory_info.percent,
            "disk_usage_percent": self.disk_info.percent
        }

    def save_report(self, report, filename="system_report.json"):
        """
        Save the system report to a JSON file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            return {"success": True, "message": f"Report saved to {filename}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def run(self):
        """
        Main method to gather system info, monitor resources, and save a report.
        """
        try:
            system_info = self.get_system_info()
            resource_monitoring = self.monitor_resources()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = {
                "timestamp": timestamp,
                "system_info": system_info,
                "resource_monitoring": resource_monitoring
            }

            save_result = self.save_report(report)
            return {"report": report, "save_result": save_result}
        except Exception as e:
            return {"success": False, "error": str(e)}


if __name__ == "__main__":
    # Instantiate the ITInfrastructureManager class
    manager = ITInfrastructureManager()

    # Run the manager to gather system info, monitor resources, and save a report
    result = manager.run()

    # Print the result
    if result.get("success", True):
        print("System report generated successfully.")
        print(json.dumps(result["report"], indent=4))
    else:
        print("An error occurred:", result["error"])
```
