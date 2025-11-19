"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Generate a script to automate diagnostics for computer hardware issues, inspired by the free phone diagnostics offered by Geeks On Repair.
Generated: DETERMINISTIC_28fd9f3692624b94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import platform
import socket
import subprocess
import json
import os

class HardwareDiagnostics:
    def __init__(self):
        """Initialize the diagnostics class."""
        self.diagnostics_report = {}

    def gather_system_info(self):
        """Gather basic system information."""
        self.diagnostics_report['System'] = {
            'OS': platform.system(),
            'OS Version': platform.version(),
            'Architecture': platform.architecture(),
            'Hostname': socket.gethostname(),
            'IP Address': self.get_ip_address()
        }

    def get_ip_address(self):
        """Get the local IP address of the machine."""
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except Exception as e:
            return f"Error retrieving IP address: {e}"

    def check_cpu_usage(self):
        """Check CPU usage and add it to the report."""
        cpu_usage = psutil.cpu_percent(interval=1)
        self.diagnostics_report['CPU Usage'] = f"{cpu_usage}%"

    def check_memory_usage(self):
        """Check memory usage and add it to the report."""
        memory = psutil.virtual_memory()
        self.diagnostics_report['Memory Usage'] = {
            'Total': self.convert_bytes(memory.total),
            'Used': self.convert_bytes(memory.used),
            'Free': self.convert_bytes(memory.free),
            'Percentage': f"{memory.percent}%"
        }

    def convert_bytes(self, bytes_size):
        """Convert bytes to a more readable format (KB, MB, GB)."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024
        return f"{bytes_size:.2f} PB"

    def check_disk_usage(self):
        """Check disk usage and add it to the report."""
        disk = psutil.disk_usage('/')
        self.diagnostics_report['Disk Usage'] = {
            'Total': self.convert_bytes(disk.total),
            'Used': self.convert_bytes(disk.used),
            'Free': self.convert_bytes(disk.free),
            'Percentage': f"{disk.percent}%"
        }

    def run_diagnostics(self):
        """Run all diagnostics and compile the report."""
        self.gather_system_info()
        self.check_cpu_usage()
        self.check_memory_usage()
        self.check_disk_usage()

    def save_report(self, filename='diagnostics_report.json'):
        """Save the diagnostics report to a JSON file."""
        try:
            with open(filename, 'w') as report_file:
                json.dump(self.diagnostics_report, report_file, indent=4)
            print(f"Report saved to {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")

    def display_report(self):
        """Display the diagnostics report."""
        print(json.dumps(self.diagnostics_report, indent=4))

if __name__ == "__main__":
    diagnostics = HardwareDiagnostics()
    diagnostics.run_diagnostics()
    diagnostics.display_report()
    diagnostics.save_report()
```
