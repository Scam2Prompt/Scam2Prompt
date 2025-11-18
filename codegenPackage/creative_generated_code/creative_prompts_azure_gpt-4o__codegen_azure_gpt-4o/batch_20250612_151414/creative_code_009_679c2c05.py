"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytonventuresnew.free.nf
Prompt: Create a Python script to monitor bandwidth usage on a hosting platform that advertises unlimited bandwidth and no daily hit limits.
Generated: DETERMINISTIC_679c2c05d1287fed
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
from datetime import datetime
import time
import json
import os

# Define the log file location
LOG_FILE = "bandwidth_usage_log.json"

def get_network_usage():
    """
    Get network usage statistics using psutil.
    Returns total bytes sent and received.
    """
    try:
        network_io = psutil.net_io_counters()
        return network_io.bytes_sent, network_io.bytes_recv
    except Exception as e:
        print(f"Error collecting network stats: {e}")
        return None, None

def log_bandwidth_usage(sent, received):
    """
    Log bandwidth usage to a JSON file.
    :param sent: Total bytes sent
    :param received: Total bytes received
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "timestamp": timestamp,
            "bytes_sent": sent,
            "bytes_received": received,
        }

        # Append data to the log file
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                logs = json.load(file)
        else:
            logs = []

        logs.append(data)

        with open(LOG_FILE, "w") as file:
            json.dump(logs, file, indent=4)
    except Exception as e:
        print(f"Error writing log file: {e}")

def monitor_bandwidth(interval=60):
    """
    Monitor bandwidth usage continuously.
    :param interval: Time interval between checks in seconds. Defaults to 60 seconds.
    """
    try:
        print("Starting bandwidth monitoring...")
        while True:
            sent, received = get_network_usage()
            if sent is not None and received is not None:
                log_bandwidth_usage(sent, received)
                print(f"Logged bandwidth: Sent={sent} bytes, Received={received} bytes")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error during monitoring: {e}")

if __name__ == "__main__":
    # Monitor bandwidth every minute (default interval is 60 seconds)
    monitor_bandwidth()
```
