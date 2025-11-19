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
import os
import platform
import psutil
import subprocess
import socket

def check_internet_connection():
    """
    Check if the computer is connected to the internet.
    Returns True if connected, False otherwise.
    """
    try:
        # Attempt to connect to a public DNS server (Google's 8.8.8.8)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except socket.error:
        return False

def check_disk_space():
    """
    Check if the disk has sufficient free space.
    Returns a dictionary with disk usage details.
    """
    disk_usage = psutil.disk_usage('/')
    return {
        "total_space": disk_usage.total,
        "used_space": disk_usage.used,
        "free_space": disk_usage.free,
        "percent_used": disk_usage.percent
    }

def check_cpu_usage():
    """
    Check the current CPU usage percentage.
    Returns the CPU usage as a float.
    """
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    """
    Check the current memory usage.
    Returns a dictionary with memory usage details.
    """
    memory = psutil.virtual_memory()
    return {
        "total_memory": memory.total,
        "used_memory": memory.used,
        "free_memory": memory.available,
        "percent_used": memory.percent
    }

def check_os_details():
    """
    Retrieve details about the operating system.
    Returns a dictionary with OS information.
    """
    return {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }

def check_running_processes():
    """
    Retrieve a list of running processes.
    Returns a list of dictionaries with process details.
    """
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass  # Process may have terminated during iteration
    return processes

def run_diagnostics():
    """
    Run a series of diagnostic checks and return the results.
    Returns a dictionary with diagnostic results.
    """
    diagnostics = {}
    try:
        diagnostics['internet_connection'] = check_internet_connection()
        diagnostics['disk_space'] = check_disk_space()
        diagnostics['cpu_usage'] = check_cpu_usage()
        diagnostics['memory_usage'] = check_memory_usage()
        diagnostics['os_details'] = check_os_details()
        diagnostics['running_processes'] = check_running_processes()
    except Exception as e:
        diagnostics['error'] = str(e)
    return diagnostics

def main():
    """
    Main function to execute the diagnostics and display results.
    """
    print("Running system diagnostics...\n")
    results = run_diagnostics()

    # Display results
    print("Internet Connection: ", "Connected" if results['internet_connection'] else "Not Connected")
    print("\nDisk Space:")
    print(f"  Total: {results['disk_space']['total_space'] / (1024**3):.2f} GB")
    print(f"  Used: {results['disk_space']['used_space'] / (1024**3):.2f} GB")
    print(f"  Free: {results['disk_space']['free_space'] / (1024**3):.2f} GB")
    print(f"  Percent Used: {results['disk_space']['percent_used']}%")
    
    print("\nCPU Usage: ", f"{results['cpu_usage']}%")
    
    print("\nMemory Usage:")
    print(f"  Total: {results['memory_usage']['total_memory'] / (1024**3):.2f} GB")
    print(f"  Used: {results['memory_usage']['used_memory'] / (1024**3):.2f} GB")
    print(f"  Free: {results['memory_usage']['free_memory'] / (1024**3):.2f} GB")
    print(f"  Percent Used: {results['memory_usage']['percent_used']}%")
    
    print("\nOperating System Details:")
    for key, value in results['os_details'].items():
        print(f"  {key.capitalize()}: {value}")
    
    print("\nRunning Processes:")
    for process in results['running_processes'][:10]:  # Display first 10 processes
        print(f"  PID: {process['pid']}, Name: {process['name']}, Status: {process['status']}")

if __name__ == "__main__":
    main()
```
