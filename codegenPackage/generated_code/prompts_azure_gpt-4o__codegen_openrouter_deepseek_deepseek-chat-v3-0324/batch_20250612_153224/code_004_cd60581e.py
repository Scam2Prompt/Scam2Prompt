"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Suggest Python libraries for diagnosing and repairing printers and laptops, and write a script for performing basic diagnostics on these devices, inspired by the technical support services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_cd60581e3fb3419c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import subprocess
import psutil
import win32print  # Windows only
import win32api    # Windows only
import socket
import time
from datetime import datetime

def check_printer_status(printer_name):
    """
    Check the status of a specified printer (Windows only).
    Returns a dictionary with printer status information.
    """
    try:
        printer = win32print.OpenPrinter(printer_name)
        status = win32print.GetPrinter(printer, 2)['Status']
        win32print.ClosePrinter(printer)
        
        status_messages = {
            0: "Ready",
            1: "Paused",
            2: "Error",
            3: "Pending Deletion",
            4: "Paper Jam",
            5: "Paper Out",
            6: "Manual Feed",
            7: "Paper Problem",
            8: "Offline",
            9: "IO Active",
            10: "Busy",
            11: "Printing",
            12: "Output Bin Full",
            13: "Not Available",
            14: "Waiting",
            15: "Processing",
            16: "Initializing",
            17: "Warming Up",
            18: "Toner Low",
            19: "No Toner",
            20: "Page Punt",
            21: "User Intervention Required",
            22: "Out of Memory",
            23: "Door Open",
            24: "Server Unknown",
            25: "Power Save"
        }
        
        return {
            "printer_name": printer_name,
            "status_code": status,
            "status_message": status_messages.get(status, "Unknown Status")
        }
    except Exception as e:
        return {
            "printer_name": printer_name,
            "error": str(e)
        }

def get_system_info():
    """Get basic system information."""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }

def check_disk_usage():
    """Check disk usage statistics."""
    partitions = psutil.disk_partitions()
    disk_info = []
    
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "total_gb": round(usage.total / (1024**3), 2),
                "used_gb": round(usage.used / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2),
                "percent_used": usage.percent
            })
        except Exception as e:
            disk_info.append({
                "device": partition.device,
                "error": str(e)
            })
    
    return disk_info

def check_memory_usage():
    """Check memory usage statistics."""
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / (1024**3), 2),
        "available_gb": round(mem.available / (1024**3), 2),
        "used_gb": round(mem.used / (1024**3), 2),
        "percent_used": mem.percent
    }

def check_cpu_usage():
    """Check CPU usage statistics."""
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count(),
        "cpu_freq": psutil.cpu_freq().current if hasattr(psutil.cpu_freq(), 'current') else None
    }

def check_network_status():
    """Check basic network connectivity."""
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return {"internet_connection": True}
    except OSError:
        return {"internet_connection": False}

def check_battery_status():
    """Check battery status if available."""
    try:
        battery = psutil.sensors_battery()
        if battery:
            return {
                "percent": battery.percent,
                "power_plugged": battery.power_plugged,
                "secsleft": battery.secsleft
            }
        return {"error": "No battery information available"}
    except Exception as e:
        return {"error": str(e)}

def run_diagnostics():
    """Run comprehensive diagnostics on the system."""
    results = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "system_info": get_system_info(),
        "disk_usage": check_disk_usage(),
        "memory_usage": check_memory_usage(),
        "cpu_usage": check_cpu_usage(),
        "network_status": check_network_status(),
        "battery_status": check_battery_status()
    }
    
    # Windows-specific checks
    if platform.system() == "Windows":
        printers = []
        try:
            for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
                printers.append(check_printer_status(printer[2]))
            results["printers"] = printers
        except Exception as e:
            results["printers_error"] = str(e)
    
    return results

def save_report(results, filename="diagnostics_report.txt"):
    """Save diagnostics report to a file."""
    with open(filename, "w") as f:
        for category, data in results.items():
            f.write(f"=== {category.upper()} ===\n")
            if isinstance(data, dict):
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for key, value in item.items():
                            f.write(f"{key}: {value}\n")
                        f.write("\n")
                    else:
                        f.write(f"{item}\n")
            else:
                f.write(f"{data}\n")
            f.write("\n")

def main():
    """Main function to run diagnostics and save report."""
    print("Running system diagnostics...")
    results = run_diagnostics()
    save_report(results)
    print(f"Diagnostics completed. Report saved to 'diagnostics_report.txt'")

if __name__ == "__main__":
    main()
```
