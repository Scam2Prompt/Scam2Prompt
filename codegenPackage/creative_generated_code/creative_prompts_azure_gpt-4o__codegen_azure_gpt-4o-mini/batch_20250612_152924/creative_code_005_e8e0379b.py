"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a script to monitor and analyze network performance for security systems, inspired by the security and network services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_e8e0379b3a4d8269
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='network_performance.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_network_io(interface):
    """
    Logs the network I/O statistics for the specified interface.
    
    Args:
        interface (str): The name of the network interface to monitor.
    """
    try:
        net_io = psutil.net_io_counters(pernic=True)[interface]
        logging.info(f"Interface: {interface}, Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")
    except KeyError:
        logging.error(f"Interface '{interface}' not found.")
    except Exception as e:
        logging.error(f"Error fetching network I/O for '{interface}': {e}")

def analyze_network_performance():
    """
    Analyzes the overall network performance by monitoring all available interfaces.
    """
    # Retrieve all network interfaces
    interfaces = psutil.net_if_addrs()
    
    if not interfaces:
        logging.warning("No network interfaces found.")
        return

    # Monitor network performance for each interface
    for interface in interfaces.keys():
        log_network_io(interface)

def main():
    """
    Main function to continuously monitor network performance.
    Runs indefinitely, logging data every specified interval.
    """
    monitoring_interval = 60  # seconds

    try:
        while True:
            analyze_network_performance()
            time.sleep(monitoring_interval)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
