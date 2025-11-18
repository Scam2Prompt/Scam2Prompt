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
# Laptop Diagnostic Tool
# This tool provides basic diagnostics for checking laptop health, including CPU usage, memory usage, disk usage, and battery status.

import psutil
import platform
import shutil
from datetime import datetime


def get_system_info():
    """
    Retrieves basic system information like OS, processor, and system architecture.
    """
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "System Architecture": platform.architecture()[0],
    }
    return system_info


def check_cpu_usage():
    """
    Retrieves the current CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)  # Interval of 1 second


def check_memory_usage():
    """
    Retrieves memory usage statistics.
    """
    memory = psutil.virtual_memory()
    memory_info = {
        "Total": memory.total,
        "Available": memory.available,
        "Used": memory.used,
        "Percentage": memory.percent,
    }
    return memory_info


def check_disk_usage():
    """
    Retrieves disk usage statistics.
    """
    disk = shutil.disk_usage("/")
    disk_info = {
        "Total": disk.total,
        "Used": disk.used,
        "Free": disk.free,
        "Percentage Used": (disk.used / disk.total) * 100,
    }
    return disk_info


def check_battery_status():
    """
    Retrieves the battery status if available.
    """
    battery = psutil.sensors_battery()
    if battery:
        battery_info = {
            "Percentage": battery.percent,
            "Plugged In": battery.power_plugged,
            "Time Left (minutes)": battery.secsleft // 60 if battery.secsleft >= 0 else "Charging",
        }
        return battery_info
    else:
        return None  # Battery information not available


def generate_diagnostics_report():
    """
    Generates a diagnostics report by collecting all system statistics.
    """
    report = {}
    report["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report["System Info"] = get_system_info()
    report["CPU Usage (%)"] = check_cpu_usage()
    report["Memory Usage"] = check_memory_usage()
    report["Disk Usage"] = check_disk_usage()
    report["Battery Status"] = check_battery_status()
    return report


def display_report(report):
    """
    Displays the diagnostics report in a readable format.
    """
    print("=== Laptop Diagnostics Report ===")
    print(f"Timestamp: {report['Timestamp']}")
    print("\n--- System Information ---")
    for key, value in report["System Info"].items():
        print(f"{key}: {value}")

    print("\n--- CPU Usage ---")
    print(f"CPU Usage: {report['CPU Usage (%)']}%")

    print("\n--- Memory Usage ---")
    for key, value in report["Memory Usage"].items():
        print(f"{key}: {value / (1024 ** 3):.2f} GB" if key != "Percentage" else f"{key}: {value}%")

    print("\n--- Disk Usage ---")
    for key, value in report["Disk Usage"].items():
        print(f"{key}: {value / (1024 ** 3):.2f} GB" if key != "Percentage Used" else f"{key}: {value:.2f}%")

    print("\n--- Battery Status ---")
    battery_status = report["Battery Status"]
    if battery_status:
        for key, value in battery_status.items():
            print(f"{key}: {value}")
    else:
        print("Battery information not available.")
    print("\n===============================")


def main():
    """
    Main function to run the laptop diagnostic tool.
    """
    try:
        diagnostics_report = generate_diagnostics_report()
        display_report(diagnostics_report)
    except Exception as e:
        print(f"An error occurred while running the diagnostics tool: {e}")


if __name__ == "__main__":
    main()
```
