"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Generate a Python script that automates the process of diagnosing common computer issues, similar to the free diagnostics offered by Geeks on Repair.
Generated: DETERMINISTIC_36acf6103755747b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# diagnostics_tool.py

import os
import platform
import psutil
import socket
import subprocess
from datetime import datetime

def get_system_info():
    """Retrieve system information."""
    system_info = {
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "ram": str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
    }
    return system_info

def check_internet_connection():
    """Check if there is an active internet connection."""
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def check_disk_space():
    """Check if there is sufficient disk space."""
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > 80:
        return False
    return True

def check_for_malware():
    """Scan for malware using the built-in Windows Defender or ClamAV on Linux."""
    if platform.system() == "Windows":
        try:
            subprocess.run(["mpcmd.exe", "scan", "-a", "quick"], check=True)
        except FileNotFoundError:
            print("Windows Defender not found.")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error scanning for malware: {e}")
    elif platform.system() == "Linux":
        try:
            subprocess.run(["clamscan", "-i", "/"], check=True)
        except FileNotFoundError:
            print("ClamAV not found.")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error scanning for malware: {e}")

def check_for_software_updates():
    """Check for available software updates."""
    if platform.system() == "Windows":
        try:
            subprocess.run(["wuauclt", "/detectnow", "/updatenow"], check=True)
        except FileNotFoundError:
            print("Windows Update not found.")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error checking for updates: {e}")
    elif platform.system() == "Linux":
        try:
            subprocess.run(["apt-get", "update"], check=True)
            subprocess.run(["apt-get", "-s", "upgrade"], check=True)
        except FileNotFoundError:
            print("APT not found.")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error checking for updates: {e}")

def diagnose_issues():
    """Run diagnostics and report issues."""
    issues = []
    system_info = get_system_info()
    internet_connection = check_internet_connection()
    disk_space = check_disk_space()

    print("# System Information")
    for key, value in system_info.items():
        print(f"- {key.capitalize().replace('_', ' ')}: {value}")

    print("\n# Diagnostics Results")
    if not internet_connection:
        issues.append("No internet connection.")
        print("- No internet connection.")
    else:
        print("- Internet connection: OK")

    if not disk_space:
        issues.append("Low disk space.")
        print("- Low disk space.")
    else:
        print("- Disk space: OK")

    print("\n# Scanning for Malware...")
    check_for_malware()

    print("\n# Checking for Software Updates...")
    check_for_software_updates()

    if issues:
        print("\n# Issues Found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\n# No issues found.")

if __name__ == "__main__":
    diagnose_issues()
```
