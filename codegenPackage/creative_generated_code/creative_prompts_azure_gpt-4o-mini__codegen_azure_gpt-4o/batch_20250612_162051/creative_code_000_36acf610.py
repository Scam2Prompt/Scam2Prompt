"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Generate a Python script that automates the process of diagnosing common computer issues, similar to the free diagnostics offered by Geeks on Repair.
Generated: DETERMINISTIC_36acf6103755747b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import platform
import os
import psutil
import shutil
import socket

def get_system_info():
    """
    Gather basic system information.
    """
    try:
        system_info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.architecture()[0],
            "Processor": platform.processor(),
            "Hostname": socket.gethostname(),
            "IP Address": socket.gethostbyname(socket.gethostname())
        }
        return system_info
    except Exception as e:
        return {"error": f"Failed to retrieve system info: {e}"}

def check_disk_usage():
    """
    Check disk usage for all partitions.
    """
    try:
        disk_usage = []
        for partition in psutil.disk_partitions():
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage.append({
                "Mount Point": partition.mountpoint,
                "Total Space (GB)": round(usage.total / (1024 ** 3), 2),
                "Used Space (GB)": round(usage.used / (1024 ** 3), 2),
                "Free Space (GB)": round(usage.free / (1024 ** 3), 2),
                "Usage (%)": usage.percent
            })
        return disk_usage
    except Exception as e:
        return {"error": f"Failed to check disk usage: {e}"}

def check_memory_usage():
    """
    Check the system's memory usage.
    """
    try:
        memory = psutil.virtual_memory()
        memory_info = {
            "Total Memory (GB)": round(memory.total / (1024 ** 3), 2),
            "Used Memory (GB)": round(memory.used / (1024 ** 3), 2),
            "Available Memory (GB)": round(memory.available / (1024 ** 3), 2),
            "Usage (%)": memory.percent
        }
        return memory_info
    except Exception as e:
        return {"error": f"Failed to retrieve memory usage: {e}"}

def check_cpu_load():
    """
    Check the CPU load percentage over the last 1, 5, and 15 minutes.
    """
    try:
        cpu_load = {
            "CPU Load (1 min)": psutil.getloadavg()[0],
            "CPU Load (5 min)": psutil.getloadavg()[1],
            "CPU Load (15 min)": psutil.getloadavg()[2],
            "CPU Usage (%)": psutil.cpu_percent(interval=1)
        }
        return cpu_load
    except Exception as e:
        return {"error": f"Failed to retrieve CPU load: {e}"}

def check_network_status():
    """
    Check basic network connectivity.
    """
    try:
        # Test connectivity to Google DNS
        host = "8.8.8.8"
        port = 53
        timeout = 3
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return {"Connectivity": "Internet connection is working"}
    except Exception as e:
        return {"Connectivity": f"No internet connection: {e}"}

def run_diagnostics():
    """
    Run diagnostics and return results for system issues.
    """
    diagnostics_results = {
        "System Info": get_system_info(),
        "Disk Usage": check_disk_usage(),
        "Memory Usage": check_memory_usage(),
        "CPU Load": check_cpu_load(),
        "Network Status": check_network_status()
    }
    return diagnostics_results

def main():
    """
    Main function to run diagnostics and display results.
    """
    print("Running system diagnostics...\n")
    diagnostics = run_diagnostics()
    for category, result in diagnostics.items():
        print(f"{category}:")
        if isinstance(result, list):
            for item in result:
                print(f"  {item}")
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"  {key}: {value}")
        else:
            print(f"  {result}")
        print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
