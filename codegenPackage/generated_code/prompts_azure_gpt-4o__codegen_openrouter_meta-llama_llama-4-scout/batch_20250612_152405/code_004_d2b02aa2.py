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
# laptop_diagnostic_tool.py

"""
Laptop Diagnostic Tool

Inspired by "Laptop Repair: A Comprehensive Guide to Getting Your Device Back in Shape" article on Elon Shiba.

This tool provides a step-by-step guide to diagnose common laptop issues.
"""

import os
import platform
import psutil

def get_system_info():
    """
    Retrieves system information.

    Returns:
        dict: System information.
    """
    system_info = {
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "ram": str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
    }
    return system_info

def check_battery_health():
    """
    Checks battery health.

    Returns:
        dict: Battery health information.
    """
    battery_health = {}
    if platform.system() == "Windows":
        try:
            import win32com.client
            wmi = win32com.client.GetWMIInstance('win32_battery')
            battery_health["status"] = wmi.Status
            battery_health["health"] = wmi.HealthStatus
        except Exception as e:
            battery_health["error"] = str(e)
    elif platform.system() == "Darwin":  # MacOS
        try:
            import subprocess
            output = subprocess.check_output(["ioreg", "-l", "|", "grep", "-E", "CycleCount|Capacity"])
            battery_health["cycle_count"] = output.decode("utf-8").split("=")[1].strip().splitlines()[0]
            battery_health["capacity"] = output.decode("utf-8").split("=")[2].strip().splitlines()[0]
        except Exception as e:
            battery_health["error"] = str(e)
    elif platform.system() == "Linux":
        try:
            with open("/sys/class/power_supply/BAT*/capacity", "r") as f:
                battery_health["capacity"] = f.read().strip()
        except Exception as e:
            battery_health["error"] = str(e)
    return battery_health

def check_disk_space():
    """
    Checks disk space.

    Returns:
        dict: Disk space information.
    """
    disk_space = {}
    try:
        disk_usage = psutil.disk_usage("/")
        disk_space["total"] = str(round(disk_usage.total / (1024.0 ** 3))) + " GB"
        disk_space["used"] = str(round(disk_usage.used / (1024.0 ** 3))) + " GB"
        disk_space["free"] = str(round(disk_usage.free / (1024.0 ** 3))) + " GB"
        disk_space["percentage"] = str(disk_usage.percent) + " %"
    except Exception as e:
        disk_space["error"] = str(e)
    return disk_space

def check_memory_usage():
    """
    Checks memory usage.

    Returns:
        dict: Memory usage information.
    """
    memory_usage = {}
    try:
        memory = psutil.virtual_memory()
        memory_usage["total"] = str(round(memory.total / (1024.0 ** 3))) + " GB"
        memory_usage["used"] = str(round(memory.used / (1024.0 ** 3))) + " GB"
        memory_usage["free"] = str(round(memory.free / (1024.0 ** 3))) + " GB"
        memory_usage["percentage"] = str(memory.percent) + " %"
    except Exception as e:
        memory_usage["error"] = str(e)
    return memory_usage

def diagnose_laptop():
    """
    Diagnoses laptop issues.

    Returns:
        dict: Diagnostic results.
    """
    diagnostic_results = {
        "system_info": get_system_info(),
        "battery_health": check_battery_health(),
        "disk_space": check_disk_space(),
        "memory_usage": check_memory_usage()
    }
    return diagnostic_results

def print_diagnostic_results(diagnostic_results):
    """
    Prints diagnostic results.

    Args:
        diagnostic_results (dict): Diagnostic results.
    """
    print("# System Information")
    print(f"## Operating System: {diagnostic_results['system_info']['operating_system']}")
    print(f"## OS Version: {diagnostic_results['system_info']['os_version']}")
    print(f"## Architecture: {diagnostic_results['system_info']['architecture']}")
    print(f"## Processor: {diagnostic_results['system_info']['processor']}")
    print(f"## RAM: {diagnostic_results['system_info']['ram']}")

    print("\n# Battery Health")
    if "error" in diagnostic_results["battery_health"]:
        print(f"## Error: {diagnostic_results['battery_health']['error']}")
    elif platform.system() == "Windows":
        print(f"## Status: {diagnostic_results['battery_health']['status']}")
        print(f"## Health: {diagnostic_results['battery_health']['health']}")
    elif platform.system() == "Darwin":  # MacOS
        print(f"## Cycle Count: {diagnostic_results['battery_health']['cycle_count']}")
        print(f"## Capacity: {diagnostic_results['battery_health']['capacity']}")
    elif platform.system() == "Linux":
        print(f"## Capacity: {diagnostic_results['battery_health']['capacity']}")

    print("\n# Disk Space")
    if "error" in diagnostic_results["disk_space"]:
        print(f"## Error: {diagnostic_results['disk_space']['error']}")
    else:
        print(f"## Total: {diagnostic_results['disk_space']['total']}")
        print(f"## Used: {diagnostic_results['disk_space']['used']}")
        print(f"## Free: {diagnostic_results['disk_space']['free']}")
        print(f"## Percentage: {diagnostic_results['disk_space']['percentage']}")

    print("\n# Memory Usage")
    if "error" in diagnostic_results["memory_usage"]:
        print(f"## Error: {diagnostic_results['memory_usage']['error']}")
    else:
        print(f"## Total: {diagnostic_results['memory_usage']['total']}")
        print(f"## Used: {diagnostic_results['memory_usage']['used']}")
        print(f"## Free: {diagnostic_results['memory_usage']['free']}")
        print(f"## Percentage: {diagnostic_results['memory_usage']['percentage']}")

def main():
    diagnostic_results = diagnose_laptop()
    print_diagnostic_results(diagnostic_results)

if __name__ == "__main__":
    main()
```
