"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Provide a step-by-step guide to create a laptop diagnostic tool using Python, inspired by the "Laptop Repair: A Comprehensive Guide to Getting Your Device Back in Shape" article on Elon Shiba.
Generated: DETERMINISTIC_d2b02aa217834495
Batch ID: 20250612_152405
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
import subprocess
import json
import os

class LaptopDiagnosticTool:
    def __init__(self):
        """Initialize the diagnostic tool with system information."""
        self.system_info = self.get_system_info()
        self.diagnostics = {}

    def get_system_info(self):
        """Retrieve basic system information."""
        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.architecture(),
            "CPU": platform.processor(),
            "RAM": self.get_ram_info(),
            "Disk": self.get_disk_info()
        }
        return info

    def get_ram_info(self):
        """Get RAM information."""
        ram = psutil.virtual_memory()
        return {
            "Total": ram.total,
            "Available": ram.available,
            "Used": ram.used,
            "Percentage": ram.percent
        }

    def get_disk_info(self):
        """Get disk information."""
        disk = psutil.disk_usage('/')
        return {
            "Total": disk.total,
            "Used": disk.used,
            "Free": disk.free,
            "Percentage": disk.percent
        }

    def run_diagnostics(self):
        """Run various diagnostics and store results."""
        self.diagnostics['CPU Usage'] = self.get_cpu_usage()
        self.diagnostics['Disk Usage'] = self.get_disk_info()
        self.diagnostics['Network Status'] = self.check_network_status()
        self.diagnostics['Battery Status'] = self.get_battery_status()

    def get_cpu_usage(self):
        """Get current CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def check_network_status(self):
        """Check network connectivity."""
        try:
            response = subprocess.check_output(['ping', '-c', '1', '8.8.8.8'])
            return "Connected"
        except subprocess.CalledProcessError:
            return "Not Connected"

    def get_battery_status(self):
        """Get battery status if applicable."""
        battery = psutil.sensors_battery()
        if battery:
            return {
                "Percentage": battery.percent,
                "Plugged In": battery.power_plugged,
                "Time Left": battery.secsleft
            }
        return "No battery information available"

    def save_diagnostics(self, filename='diagnostics_report.json'):
        """Save diagnostics report to a JSON file."""
        report = {
            "System Info": self.system_info,
            "Diagnostics": self.diagnostics
        }
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            print(f"Diagnostics report saved to {filename}")
        except IOError as e:
            print(f"Error saving diagnostics report: {e}")

    def run(self):
        """Run the diagnostic tool."""
        self.run_diagnostics()
        self.save_diagnostics()

if __name__ == "__main__":
    diagnostic_tool = LaptopDiagnosticTool()
    diagnostic_tool.run()
```
