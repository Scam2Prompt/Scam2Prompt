"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a script to monitor and analyze network performance for security systems, inspired by the security and network services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_e8e0379b3a4d8269
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# network_performance_monitor.py

import os
import platform
import psutil
import time
from datetime import datetime

# Define constants
NETWORK_INTERFACES = ['eth0', 'wlan0']  # Default network interfaces to monitor
MONITOR_INTERVAL = 60  # Monitor interval in seconds

def get_network_io_counters(interface):
    """
    Get network I/O counters for a given interface.

    Args:
        interface (str): Network interface name (e.g., 'eth0')

    Returns:
        psutil.net_io_counters: Network I/O counters
    """
    try:
        return psutil.net_io_counters(pernic=True)[interface]
    except KeyError:
        print(f"Error: Interface '{interface}' not found.")
        return None

def calculate_network_throughput(counters_prev, counters_curr, interval):
    """
    Calculate network throughput.

    Args:
        counters_prev (psutil.net_io_counters): Previous network I/O counters
        counters_curr (psutil.net_io_counters): Current network I/O counters
        interval (float): Time interval between measurements

    Returns:
        tuple: Throughput in bytes/s (sent, recv)
    """
    bytes_sent = (counters_curr.bytes_sent - counters_prev.bytes_sent) / interval
    bytes_recv = (counters_curr.bytes_recv - counters_prev.bytes_recv) / interval
    return bytes_sent, bytes_recv

def monitor_network_performance(interfaces, interval):
    """
    Monitor network performance.

    Args:
        interfaces (list): List of network interfaces to monitor
        interval (int): Monitor interval in seconds

    Returns:
        None
    """
    # Initialize previous counters
    prev_counters = {}
    for interface in interfaces:
        prev_counters[interface] = get_network_io_counters(interface)

    while True:
        # Get current counters
        curr_counters = {}
        for interface in interfaces:
            curr_counters[interface] = get_network_io_counters(interface)

        # Calculate throughput
        for interface in interfaces:
            if prev_counters[interface] and curr_counters[interface]:
                bytes_sent, bytes_recv = calculate_network_throughput(
                    prev_counters[interface], curr_counters[interface], interval
                )
                print(
                    f"Interface: {interface}, "
                    f"Throughput: {bytes_sent:.2f} bytes/s (sent), "
                    f"{bytes_recv:.2f} bytes/s (recv)"
                )

        # Update previous counters
        for interface in interfaces:
            prev_counters[interface] = curr_counters[interface]

        # Wait for the next interval
        time.sleep(interval)

def main():
    # Get platform information
    print(f"Platform: {platform.system()} {platform.release()} {platform.version()}")

    # Monitor network performance
    try:
        monitor_network_performance(NETWORK_INTERFACES, MONITOR_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopping network performance monitor...")

if __name__ == "__main__":
    main()
```
