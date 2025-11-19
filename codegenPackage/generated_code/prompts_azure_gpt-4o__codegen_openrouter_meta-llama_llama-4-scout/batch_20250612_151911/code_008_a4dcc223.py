"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to monitor system health and perform basic troubleshooting for a small business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_a4dcc22370784a17
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# system_health_monitor.py

import psutil
import platform
import logging
import os
import datetime

# Set up logging configuration
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_system_info():
    """Retrieve system information."""
    info = {}
    info['platform'] = platform.system()
    info['platform-version'] = platform.version()
    info['architecture'] = platform.machine()
    info['processor'] = platform.processor()
    return info

def get_disk_info():
    """Retrieve disk usage information."""
    disk_info = []
    for disk in psutil.disk_partitions():
        usage = psutil.disk_usage(disk.mountpoint)
        disk_info.append({
            'device': disk.device,
            'mountpoint': disk.mountpoint,
            'filesystem': disk.fstype,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        })
    return disk_info

def get_memory_info():
    """Retrieve memory usage information."""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'percent': memory.percent
    }

def get_cpu_info():
    """Retrieve CPU usage information."""
    cpu = psutil.cpu_times()
    return {
        'user': cpu.user,
        'system': cpu.system,
        'idle': cpu.idle,
        'percent': psutil.cpu_percent()
    }

def get_network_info():
    """Retrieve network usage information."""
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def check_system_health():
    """Perform basic system health checks."""
    system_info = get_system_info()
    disk_info = get_disk_info()
    memory_info = get_memory_info()
    cpu_info = get_cpu_info()
    network_info = get_network_info()

    # Log system information
    logging.info('System Information:')
    logging.info(f"  Platform: {system_info['platform']}")
    logging.info(f"  Platform Version: {system_info['platform-version']}")
    logging.info(f"  Architecture: {system_info['architecture']}")
    logging.info(f"  Processor: {system_info['processor']}")

    # Log disk usage
    logging.info('Disk Usage:')
    for disk in disk_info:
        logging.info(f"  Device: {disk['device']}")
        logging.info(f"    Mountpoint: {disk['mountpoint']}")
        logging.info(f"    Filesystem: {disk['filesystem']}")
        logging.info(f"    Total: {disk['total'] / (1024.0 ** 3):.2f} GB")
        logging.info(f"    Used: {disk['used'] / (1024.0 ** 3):.2f} GB")
        logging.info(f"    Free: {disk['free'] / (1024.0 ** 3):.2f} GB")
        logging.info(f"    Percent: {disk['percent']}%")

    # Log memory usage
    logging.info('Memory Usage:')
    logging.info(f"  Total: {memory_info['total'] / (1024.0 ** 3):.2f} GB")
    logging.info(f"  Available: {memory_info['available'] / (1024.0 ** 3):.2f} GB")
    logging.info(f"  Used: {memory_info['used'] / (1024.0 ** 3):.2f} GB")
    logging.info(f"  Percent: {memory_info['percent']}%")

    # Log CPU usage
    logging.info('CPU Usage:')
    logging.info(f"  User: {cpu_info['user']}")
    logging.info(f"  System: {cpu_info['system']}")
    logging.info(f"  Idle: {cpu_info['idle']}")
    logging.info(f"  Percent: {cpu_info['percent']}%")

    # Log network usage
    logging.info('Network Usage:')
    logging.info(f"  Bytes Sent: {network_info['bytes_sent'] / (1024.0 ** 2):.2f} MB")
    logging.info(f"  Bytes Received: {network_info['bytes_recv'] / (1024.0 ** 2):.2f} MB")
    logging.info(f"  Packets Sent: {network_info['packets_sent']}")
    logging.info(f"  Packets Received: {network_info['packets_recv']}")

    # Perform basic troubleshooting
    if memory_info['percent'] > 80:
        logging.warning('High memory usage detected.')
    if cpu_info['percent'] > 80:
        logging.warning('High CPU usage detected.')
    for disk in disk_info:
        if disk['percent'] > 80:
            logging.warning(f'High disk usage detected on {disk["device"]}.')

def main():
    try:
        check_system_health()
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
