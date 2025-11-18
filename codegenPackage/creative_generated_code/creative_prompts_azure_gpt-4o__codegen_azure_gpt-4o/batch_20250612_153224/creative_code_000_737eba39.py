"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Write Python code to monitor and limit RAM usage in Google Chrome, as described in the article on اوج کده.
Generated: DETERMINISTIC_737eba39ca93d529
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
import os
import time
import signal

# Configuration
CHROME_PROCESS_NAME = "chrome"  # Name of the Google Chrome process
RAM_LIMIT_MB = 500  # Maximum allowed RAM usage in MB
CHECK_INTERVAL_SECONDS = 10  # Time interval to check RAM usage

def find_chrome_processes():
    """
    Finds all processes related to Google Chrome.

    Returns:
        List of tuples containing PID and memory usage in MB for Chrome processes.
    """
    chrome_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            if CHROME_PROCESS_NAME.lower() in proc.info['name'].lower():
                chrome_processes.append((proc.info['pid'], proc.info['memory_info'].rss / 1024 / 1024))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that are no longer accessible
            continue
    return chrome_processes

def terminate_process(pid):
    """
    Terminates a process by its PID.

    Args:
        pid (int): Process ID to terminate.
    """
    try:
        os.kill(pid, signal.SIGTERM)  # Gracefully terminate the process
        print(f"Terminated process with PID {pid}")
    except OSError as e:
        print(f"Error terminating process {pid}: {e}")

def monitor_and_limit_chrome_ram():
    """
    Monitors Google Chrome processes and terminates those exceeding the RAM limit.
    """
    while True:
        chrome_processes = find_chrome_processes()
        for pid, ram_usage in chrome_processes:
            if ram_usage > RAM_LIMIT_MB:
                print(f"Process {pid} is using {ram_usage:.2f} MB of RAM (limit: {RAM_LIMIT_MB} MB). Terminating...")
                terminate_process(pid)
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    try:
        print("Starting Chrome RAM monitor...")
        monitor_and_limit_chrome_ram()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
