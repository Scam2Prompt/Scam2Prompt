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
import os
import time

# Define the maximum allowed RAM usage in MB
MAX_RAM_USAGE_MB = 2048  # 2 GB

def get_chrome_processes():
    """
    Returns a list of Chrome process IDs.
    """
    try:
        # Use psutil to get all running processes
        processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
        # Filter processes by name 'chrome.exe' or 'google-chrome'
        chrome_processes = [p for p in processes if p['name'] in ['chrome.exe', 'google-chrome']]
        return [p['pid'] for p in chrome_processes]
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return []

def get_process_ram_usage(pid):
    """
    Returns the RAM usage of a process in MB.
    """
    try:
        process = psutil.Process(pid)
        return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return 0

def limit_ram_usage():
    """
    Monitors and limits RAM usage of Google Chrome processes.
    """
    chrome_pids = get_chrome_processes()
    total_ram_usage_mb = sum(get_process_ram_usage(pid) for pid in chrome_pids)

    if total_ram_usage_mb > MAX_RAM_USAGE_MB:
        # Sort Chrome processes by RAM usage in descending order
        chrome_processes = sorted([(pid, get_process_ram_usage(pid)) for pid in chrome_pids], key=lambda x: x[1], reverse=True)

        # Close processes until RAM usage is within the limit
        for pid, ram_usage_mb in chrome_processes:
            if total_ram_usage_mb <= MAX_RAM_USAGE_MB:
                break
            try:
                # Terminate the process
                os.kill(pid, 9)  # SIGKILL
                print(f"Terminated Chrome process {pid} using {ram_usage_mb:.2f} MB RAM")
                total_ram_usage_mb -= ram_usage_mb
            except OSError as e:
                print(f"Error terminating process {pid}: {e}")

def main():
    while True:
        limit_ram_usage()
        time.sleep(60)  # Monitor every 1 minute

if __name__ == "__main__":
    main()
```
