"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Generate a script to automate diagnostics for computer hardware issues, inspired by the free phone diagnostics offered by Geeks On Repair.
Generated: DETERMINISTIC_28fd9f3692624b94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hardware_diagnostics.py

import platform
import psutil
import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_system_info():
    """Retrieve system information."""
    system_info = {
        'platform': platform.system(),
        'platform-version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'ram': str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    }
    return system_info

def get_disk_info():
    """Retrieve disk information."""
    disk_info = []
    for disk in psutil.disk_partitions():
        usage = psutil.disk_usage(disk.mountpoint)
        disk_info.append({
            'device': disk.device,
            'mountpoint': disk.mountpoint,
            'file_system_type': disk.fstype,
            'total_size': str(round(usage.total / (1024.0 **3)))+" GB",
            'used': str(round(usage.used / (1024.0 **3)))+" GB",
            'free': str(round(usage.free / (1024.0 **3)))+" GB",
            'percentage': str(usage.percent)+"%"
        })
    return disk_info

def get_network_info():
    """Retrieve network information."""
    network_info = []
    for net in psutil.net_if_addrs():
        network_info.append({
            'interface': net,
            'addresses': [
                {'address': addr.address, 'netmask': addr.netmask, 'broadcast': addr.broadcast} 
                for addr in psutil.net_if_addrs()[net] if addr.address
            ]
        })
    return network_info

def get_cpu_info():
    """Retrieve CPU information."""
    cpu_info = {
        'physical_cores': psutil.cpu_count(logical=False),
        'total_cores': psutil.cpu_count(logical=True),
        'current_frequency': str(psutil.cpu_freq().current)+" Mhz",
        'max_frequency': str(psutil.cpu_freq().max)+" Mhz",
        'min_frequency': str(psutil.cpu_freq().min)+" Mhz",
        'cpu_usage': str(psutil.cpu_percent())+"%"
    }
    return cpu_info

def get_memory_info():
    """Retrieve memory information."""
    memory_info = {
        'total': str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB",
        'available': str(round(psutil.virtual_memory().available / (1024.0 **3)))+" GB",
        'used': str(round(psutil.virtual_memory().used / (1024.0 **3)))+" GB",
        'percentage': str(psutil.virtual_memory().percent)+"%"
    }
    return memory_info

def run_diagnostics():
    """Run hardware diagnostics."""
    try:
        logging.info("Running diagnostics...")
        
        system_info = get_system_info()
        logging.info("System Information:")
        for key, value in system_info.items():
            logging.info(f"{key.capitalize().replace('_', ' ')}: {value}")

        disk_info = get_disk_info()
        logging.info("\nDisk Information:")
        for i, disk in enumerate(disk_info):
            logging.info(f"Disk {i+1}:")
            for key, value in disk.items():
                logging.info(f"  {key.capitalize().replace('_', ' ')}: {value}")

        network_info = get_network_info()
        logging.info("\nNetwork Information:")
        for i, net in enumerate(network_info):
            logging.info(f"Interface {i+1}: {net['interface']}")
            for addr in net['addresses']:
                logging.info(f"  Address: {addr['address']}, Netmask: {addr['netmask']}, Broadcast: {addr['broadcast']}")

        cpu_info = get_cpu_info()
        logging.info("\nCPU Information:")
        for key, value in cpu_info.items():
            logging.info(f"{key.capitalize().replace('_', ' ')}: {value}")

        memory_info = get_memory_info()
        logging.info("\nMemory Information:")
        for key, value in memory_info.items():
            logging.info(f"{key.capitalize().replace('_', ' ')}: {value}")

        logging.info("\nDiagnostics complete.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run_diagnostics()
```
