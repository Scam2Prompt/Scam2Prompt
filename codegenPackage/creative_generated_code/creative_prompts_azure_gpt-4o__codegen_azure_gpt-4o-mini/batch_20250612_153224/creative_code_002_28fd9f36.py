"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Generate a script to automate diagnostics for computer hardware issues, inspired by the free phone diagnostics offered by Geeks On Repair.
Generated: DETERMINISTIC_28fd9f3692624b94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import platform
import socket
import subprocess
import json
import os

def get_system_info():
    """
    Gather basic system information.
    Returns a dictionary with system details.
    """
    info = {
        'Operating System': platform.system(),
        'OS Version': platform.version(),
        'Architecture': platform.architecture(),
        'Hostname': socket.gethostname(),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'CPU Cores': psutil.cpu_count(logical=True),
        'Memory': round(psutil.virtual_memory().total / (1024 ** 3), 2),  # Total memory in GB
    }
    return info

def check_disk_usage(disk):
    """
    Check disk usage for the specified drive.
    Returns a dictionary with disk usage details.
    """
    try:
        usage = psutil.disk_usage(disk)
        return {
            'Total': round(usage.total / (1024 ** 3), 2),  # Total disk space in GB
            'Used': round(usage.used / (1024 ** 3), 2),    # Used disk space in GB
            'Free': round(usage.free / (1024 ** 3), 2),    # Free disk space in GB
            'Percentage Used': usage.percent
        }
    except Exception as e:
        return {'Error': str(e)}

def check_cpu_usage():
    """
    Check the current CPU usage.
    Returns the CPU usage percentage as a float.
    """
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    """
    Check the current memory usage.
    Returns a dictionary with memory usage details.
    """
    memory = psutil.virtual_memory()
    return {
        'Total': round(memory.total / (1024 ** 3), 2),  # Total memory in GB
        'Used': round(memory.used / (1024 ** 3), 2),    # Used memory in GB
        'Free': round(memory.free / (1024 ** 3), 2),    # Free memory in GB
        'Percentage Used': memory.percent
    }

def run_diagnostics():
    """
    Run a series of diagnostics and return the results.
    """
    diagnostics = {}
    diagnostics['System Info'] = get_system_info()
    diagnostics['Disk Usage'] = check_disk_usage('/')
    diagnostics['CPU Usage'] = check_cpu_usage()
    diagnostics['Memory Usage'] = check_memory_usage()

    return diagnostics

def save_results_to_file(results, filename='diagnostics_results.json'):
    """
    Save the diagnostic results to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)
        print(f'Diagnostics results saved to {filename}')
    except IOError as e:
        print(f'Error saving results to file: {e}')

def main():
    """
    Main function to execute diagnostics script.
    """
    try:
        print("Running hardware diagnostics...")
        results = run_diagnostics()
        print(json.dumps(results, indent=4))  # Print results to console
        save_results_to_file(results)
    except Exception as e:
        print(f'An error occurred during diagnostics: {e}')

if __name__ == '__main__':
    main()
```

This script collects various diagnostic information about the system's hardware and saves it to a JSON file. It features error handling to catch issues that may arise during the diagnostics process.
