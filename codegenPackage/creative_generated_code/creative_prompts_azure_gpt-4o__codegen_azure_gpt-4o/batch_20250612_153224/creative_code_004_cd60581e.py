"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Suggest Python libraries for diagnosing and repairing printers and laptops, and write a script for performing basic diagnostics on these devices, inspired by the technical support services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_cd60581e3fb3419c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for performing basic diagnostics on printers and laptops.
Inspired by Space Technologies Bogotá's technical support services.

Python Libraries:
- For printer diagnostics:
    * pywin32 (Windows-specific for printer status and management)
    * cups (Common Unix Printing System for Linux/macOS printers)
    * printerqueue (third-party library for managing printer queues)

- For laptop diagnostics:
    * psutil (system performance and hardware diagnostics)
    * subprocess (executing system commands for diagnostics)
    * pySMART (diagnosing hard drives using SMART attributes)
"""

import os
import platform
import psutil
import subprocess
from datetime import datetime


def diagnose_printer():
    """
    Diagnoses printer status on the current system.
    Supports Windows and Unix-like systems.
    """
    print("Starting printer diagnostics...")
    try:
        if platform.system() == "Windows":
            # Windows-specific diagnostics using pywin32
            import win32print
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
            print(f"Detected printers: {len(printers)}")
            for printer in printers:
                print(f"Printer Name: {printer[2]}")
        elif platform.system() in ["Linux", "Darwin"]:  # Unix-like systems
            # UNIX systems diagnostics using lpstat (CUPS)
            result = subprocess.run(["lpstat", "-p"], capture_output=True, text=True)
            if result.returncode == 0:
                print("Printer status:")
                print(result.stdout)
            else:
                print("Error fetching printer status. Ensure CUPS is installed.")
        else:
            print("Unsupported OS for printer diagnostics.")
    except Exception as e:
        print(f"An error occurred during printer diagnostics: {e}")


def diagnose_laptop():
    """
    Diagnoses laptop hardware and system health.
    Provides information on CPU usage, memory, and disk health.
    """
    print("Starting laptop diagnostics...")
    try:
        # CPU diagnostics
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")

        # Memory diagnostics
        memory_info = psutil.virtual_memory()
        print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
        print(f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB")
        print(f"Memory Usage: {memory_info.percent}%")

        # Disk diagnostics
        for disk in psutil.disk_partitions():
            if os.name == 'nt' and 'cdrom' in disk.opts:
                continue  # Skip CD-ROM drives on Windows
            usage = psutil.disk_usage(disk.mountpoint)
            print(f"Disk {disk.device}:")
            print(f"  Total: {usage.total / (1024 ** 3):.2f} GB")
            print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
            print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
            print(f"  Usage: {usage.percent}%")

        # SMART diagnostics for hard drives
        try:
            from pysmart.smart import Smart
            drives = Smart.scan()
            for drive in drives:
                smart_data = drive.attributes
                print(f"SMART Data for {drive.serial}:")
                for attr in smart_data:
                    print(f"  {attr.name}: {attr.raw_value}")
        except ImportError:
            print("pySMART library not installed. Skipping SMART diagnostics.")

    except Exception as e:
        print(f"An error occurred during laptop diagnostics: {e}")


def main():
    """
    Main function to execute diagnostics for printers and laptops.
    """
    print("Welcome to Diagnostics Tool!")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Operating System: {platform.system()} {platform.release()}")

    print("\n=== Printer Diagnostics ===")
    diagnose_printer()

    print("\n=== Laptop Diagnostics ===")
    diagnose_laptop()

    print("\nDiagnostics complete. Thank you for using this tool!")


if __name__ == "__main__":
    main()
```
