"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonshiba.org
Prompt: Provide a step-by-step guide to create a laptop diagnostic tool using Python, inspired by the "Laptop Repair: A Comprehensive Guide to Getting Your Device Back in Shape" article on Elon Shiba.
Generated: DETERMINISTIC_d2b02aa217834495
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import psutil
import socket
import subprocess


class LaptopDiagnostics:
    """
    A class to gather and display diagnostic information about the laptop.
    """

    def __init__(self):
        """
        Initializes the LaptopDiagnostics class.
        """
        self.system_info = {}
        self.memory_info = {}
        self.cpu_info = {}
        self.disk_info = {}
        self.network_info = {}

    def collect_system_info(self):
        """ Collects basic system information. """
        self.system_info['OS'] = platform.system()
        self.system_info['OS Version'] = platform.version()
        self.system_info['Architecture'] = platform.architecture()
        self.system_info['Hostname'] = socket.gethostname()
        self.system_info['IP Address'] = self.get_ip_address()

    def collect_memory_info(self):
        """ Collects memory usage information. """
        mem = psutil.virtual_memory()
        self.memory_info['Total Memory'] = mem.total
        self.memory_info['Available Memory'] = mem.available
        self.memory_info['Used Memory'] = mem.used
        self.memory_info['Memory Usage (%)'] = mem.percent

    def collect_cpu_info(self):
        """ Collects CPU usage information. """
        self.cpu_info['CPU Cores'] = psutil.cpu_count(logical=False)
        self.cpu_info['Logical CPUs'] = psutil.cpu_count(logical=True)
        self.cpu_info['CPU Frequency (MHz)'] = psutil.cpu_freq().current
        self.cpu_info['CPU Usage (%)'] = psutil.cpu_percent(interval=1)

    def collect_disk_info(self):
        """ Collects disk usage information. """
        disk = psutil.disk_usage('/')
        self.disk_info['Total Disk Space'] = disk.total
        self.disk_info['Used Disk Space'] = disk.used
        self.disk_info['Free Disk Space'] = disk.free
        self.disk_info['Disk Usage (%)'] = disk.percent

    def get_ip_address(self):
        """ Returns the IP address of the laptop. """
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except Exception as e:
            return str(e)

    def display_diagnostics(self):
        """ Displays the collected diagnostic information. """
        print("System Information:")
        for key, value in self.system_info.items():
            print(f"{key}: {value}")

        print("\nMemory Information:")
        for key, value in self.memory_info.items():
            print(f"{key}: {value / (1024 ** 2):.2f} MB" if 'Memory' in key else f"{key}: {value}")

        print("\nCPU Information:")
        for key, value in self.cpu_info.items():
            print(f"{key}: {value}")

        print("\nDisk Information:")
        for key, value in self.disk_info.items():
            print(f"{key}: {value / (1024 ** 3):.2f} GB" if 'Disk' in key else f"{key}: {value}")

    def run_diagnostics(self):
        """ Runs all diagnostic collections and displays the results. """
        try:
            self.collect_system_info()
            self.collect_memory_info()
            self.collect_cpu_info()
            self.collect_disk_info()
            self.display_diagnostics()
        except Exception as e:
            print(f"An error occurred while running diagnostics: {e}")


if __name__ == "__main__":
    diagnostics_tool = LaptopDiagnostics()
    diagnostics_tool.run_diagnostics()
```

This Python code defines a `LaptopDiagnostics` class that collects various diagnostic information about the laptop, including system, memory, CPU, and disk information, and displays it in a user-friendly format. The code includes error handling to manage any issues that may arise during the collection process.
