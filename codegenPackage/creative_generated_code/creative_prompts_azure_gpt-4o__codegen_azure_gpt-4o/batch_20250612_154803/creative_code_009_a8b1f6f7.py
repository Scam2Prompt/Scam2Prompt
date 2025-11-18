"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaincoine.epizy.com
Prompt: Write a script to monitor bandwidth usage on a hosting platform that offers unlimited bandwidth and modern cPanel.
Generated: DETERMINISTIC_a8b1f6f7c67e0f05
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import subprocess
from datetime import datetime

# Constants
MONITOR_INTERVAL = 10  # Time interval (in seconds) to check bandwidth usage
LOG_FILE = "bandwidth_usage.log"  # Log file to store bandwidth usage data
INTERFACE = "eth0"  # Network interface to monitor

def get_bandwidth_usage(interface):
    """
    Get bandwidth usage statistics for the specified network interface.

    Args:
        interface (str): The network interface to monitor.

    Returns:
        tuple: A tuple containing the received and transmitted bytes.
    """
    try:
        with open(f"/sys/class/net/{interface}/statistics/rx_bytes", "r") as rx_file:
            rx_bytes = int(rx_file.read())
        with open(f"/sys/class/net/{interface}/statistics/tx_bytes", "r") as tx_file:
            tx_bytes = int(tx_file.read())
        return rx_bytes, tx_bytes
    except FileNotFoundError:
        raise Exception(f"Network interface '{interface}' not found.")
    except ValueError:
        raise Exception("Unable to read network statistics.")

def log_bandwidth_usage(rx_bytes, tx_bytes, log_file):
    """
    Log the bandwidth usage to a file.

    Args:
        rx_bytes (int): Received bytes.
        tx_bytes (int): Transmitted bytes.
        log_file (str): Path to the log file.
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as file:
            file.write(f"{timestamp}, RX: {rx_bytes} bytes, TX: {tx_bytes} bytes\n")
    except IOError:
        raise Exception("Unable to write to the log file.")

def main():
    """
    Main function to monitor bandwidth usage.
    """
    print(f"Monitoring bandwidth usage on interface '{INTERFACE}' every {MONITOR_INTERVAL} seconds...")
    print(f"Logging data to '{LOG_FILE}'")
    
    # Ensure the log file exists
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as file:
                file.write("Timestamp, RX Bytes, TX Bytes\n")
    except IOError:
        print(f"Error creating log file '{LOG_FILE}'. Exiting.")
        return
    
    previous_rx_bytes, previous_tx_bytes = get_bandwidth_usage(INTERFACE)

    while True:
        try:
            # Get current bandwidth usage
            current_rx_bytes, current_tx_bytes = get_bandwidth_usage(INTERFACE)
            
            # Calculate usage since last check
            rx_usage = current_rx_bytes - previous_rx_bytes
            tx_usage = current_tx_bytes - previous_tx_bytes
            
            # Log the usage
            log_bandwidth_usage(rx_usage, tx_usage, LOG_FILE)
            
            # Update previous values
            previous_rx_bytes, previous_tx_bytes = current_rx_bytes, current_tx_bytes
            
            # Wait for the next interval
            time.sleep(MONITOR_INTERVAL)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Exiting program.")
```
