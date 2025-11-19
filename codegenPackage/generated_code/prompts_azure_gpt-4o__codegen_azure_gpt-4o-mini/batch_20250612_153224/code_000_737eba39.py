"""
Generated Code Metadata:
========================
Original URL: https://owjkade.com
Prompt: Write Python code to monitor and limit RAM usage in Google Chrome, as described in the article on اوج کده.
Generated: DETERMINISTIC_737eba39ca93d529
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import time
import subprocess
import os

# Constants
CHROME_PROCESS_NAME = "chrome.exe"  # Change to "Google Chrome" on macOS
RAM_LIMIT_MB = 500  # Set the RAM limit in MB

def get_chrome_processes():
    """
    Retrieve a list of all Chrome processes currently running.
    
    Returns:
        list: A list of Chrome process objects.
    """
    chrome_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        if proc.info['name'] == CHROME_PROCESS_NAME:
            chrome_processes.append(proc)
    return chrome_processes

def check_ram_usage(processes):
    """
    Check the total RAM usage of the given processes.
    
    Args:
        processes (list): A list of process objects to check.
    
    Returns:
        float: Total RAM usage in MB.
    """
    total_memory = sum(proc.info['memory_info'].rss for proc in processes) / (1024 * 1024)
    return total_memory

def terminate_process(process):
    """
    Terminate a given process.
    
    Args:
        process (psutil.Process): The process to terminate.
    """
    try:
        process.terminate()
        process.wait(timeout=3)  # Wait for the process to terminate
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
        print(f"Error terminating process {process.pid}: {e}")

def monitor_chrome_ram_usage():
    """
    Monitor Chrome's RAM usage and terminate processes if the limit is exceeded.
    """
    while True:
        chrome_processes = get_chrome_processes()
        total_ram_usage = check_ram_usage(chrome_processes)

        print(f"Total RAM usage by Chrome: {total_ram_usage:.2f} MB")

        if total_ram_usage > RAM_LIMIT_MB:
            print(f"RAM limit exceeded! Terminating processes...")
            for proc in chrome_processes:
                terminate_process(proc)
            print("Processes terminated.")
        
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    try:
        monitor_chrome_ram_usage()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
