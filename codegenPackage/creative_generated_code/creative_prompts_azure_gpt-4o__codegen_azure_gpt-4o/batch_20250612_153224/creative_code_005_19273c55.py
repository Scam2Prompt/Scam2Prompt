"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Create a script for managing telematics and office automation tasks, including network monitoring and resource allocation, based on the outsourcing services in telematics and ofimatica provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_19273c55511ed2b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for managing telematics and office automation tasks with functionalities
for network monitoring and resource allocation. This script is designed based on
the outsourcing services in telematics and office automation provided by Space Technologies Bogotá.

Author: Professional Software Developer
Date: 2023
"""

import os
import logging
import psutil
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define constants
NETWORK_INTERFACE = 'eth0'  # Replace with your network interface name, e.g., 'wlan0' or 'en0'
RESOURCE_THRESHOLD_PERCENT = 80  # Alert when CPU/RAM usage exceeds this percentage

# Define exceptions
class NetworkMonitoringError(Exception):
    """Custom exception for network monitoring errors."""
    pass

class ResourceAllocationError(Exception):
    """Custom exception for resource allocation errors."""
    pass

def monitor_network(interface):
    """
    Monitor network traffic for a given interface.
    
    :param interface: Name of the network interface to monitor.
    :return: Dictionary containing network stats.
    """
    try:
        net_io = psutil.net_io_counters(pernic=True)
        if interface in net_io:
            stats = net_io[interface]
            return {
                "bytes_sent": stats.bytes_sent,
                "bytes_received": stats.bytes_recv,
                "packets_sent": stats.packets_sent,
                "packets_received": stats.packets_recv
            }
        else:
            raise NetworkMonitoringError(f"Interface '{interface}' not found.")
    except Exception as e:
        logging.error(f"Error in network monitoring: {e}")
        raise

def monitor_system_resources():
    """
    Monitor system resources like CPU and memory usage.
    
    :return: Dictionary containing resource usage stats.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        
        resource_stats = {
            "cpu_usage_percent": cpu_usage,
            "memory_usage_percent": memory_usage
        }
        
        # Log warnings if thresholds exceeded
        if cpu_usage > RESOURCE_THRESHOLD_PERCENT:
            logging.warning("CPU usage exceeded threshold: {}%".format(cpu_usage))
        if memory_usage > RESOURCE_THRESHOLD_PERCENT:
            logging.warning("Memory usage exceeded threshold: {}%".format(memory_usage))
        
        return resource_stats
    except Exception as e:
        logging.error(f"Error in system resource monitoring: {e}")
        raise ResourceAllocationError(f"System resource monitoring failed: {e}")

def allocate_resources(task_name, required_cpu, required_ram):
    """
    Allocate resources for a specific task.
    
    :param task_name: Name of the task.
    :param required_cpu: Percentage of CPU required.
    :param required_ram: Percentage of RAM required.
    :return: Boolean indicating success or failure.
    """
    try:
        current_resources = monitor_system_resources()
        if current_resources["cpu_usage_percent"] + required_cpu > 100:
            raise ResourceAllocationError(f"Insufficient CPU resources for task '{task_name}'.")
        if current_resources["memory_usage_percent"] + required_ram > 100:
            raise ResourceAllocationError(f"Insufficient RAM resources for task '{task_name}'.")
        
        # Simulate resource allocation (replace with actual implementation if needed)
        logging.info(f"Task '{task_name}' successfully allocated {required_cpu}% CPU and {required_ram}% RAM.")
        return True
    except ResourceAllocationError as e:
        logging.error(f"Resource allocation failed: {e}")
        return False

def main():
    """
    Main function to execute telematics and office automation tasks.
    """
    try:
        # Monitor network traffic
        network_stats = monitor_network(NETWORK_INTERFACE)
        logging.info(f"Network stats for interface '{NETWORK_INTERFACE}': {network_stats}")
        
        # Monitor system resources
        system_stats = monitor_system_resources()
        logging.info(f"System resource stats: {system_stats}")
        
        # Allocate resources for a specific task
        task_name = "Data Processing"
        task_success = allocate_resources(task_name, required_cpu=20, required_ram=30)
        if task_success:
            print(f"Task '{task_name}' was successfully allocated resources.")
        else:
            print(f"Task '{task_name}' failed due to insufficient resources.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
