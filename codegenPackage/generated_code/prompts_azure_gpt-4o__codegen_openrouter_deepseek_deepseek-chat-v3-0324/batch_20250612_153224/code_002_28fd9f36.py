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
#!/usr/bin/env python3
"""
Computer Hardware Diagnostics Tool
Inspired by Geeks On Repair phone diagnostics
"""

import os
import sys
import platform
import subprocess
import time
import psutil
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hardware_diagnostics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class HardwareDiagnostics:
    def __init__(self):
        self.system_info = {}
        self.diagnostics_results = {}
        self.start_time = datetime.now()
        
    def get_system_info(self):
        """Collect basic system information"""
        try:
            self.system_info = {
                'os': platform.system(),
                'os_version': platform.version(),
                'os_release': platform.release(),
                'architecture': platform.machine(),
                'processor': platform.processor(),
                'hostname': platform.node(),
                'cpu_cores': os.cpu_count(),
                'total_ram': round(psutil.virtual_memory().total / (1024 ** 3), 2),
                'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
            }
            logger.info("System information collected successfully")
            return True
        except Exception as e:
            logger.error(f"Error collecting system info: {str(e)}")
            return False

    def check_disk_health(self):
        """Check disk health and space"""
        try:
            disk_info = {}
            partitions = psutil.disk_partitions()
            
            for partition in partitions:
                if partition.fstype:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info[partition.device] = {
                        'mountpoint': partition.mountpoint,
                        'fstype': partition.fstype,
                        'total_gb': round(usage.total / (1024 ** 3), 2),
                        'used_gb': round(usage.used / (1024 ** 3), 2),
                        'free_gb': round(usage.free / (1024 ** 3), 2),
                        'percent_used': usage.percent
                    }
            
            # Run SMART check if available
            if platform.system() == 'Linux':
                try:
                    smart_output = subprocess.run(
                        ['smartctl', '--scan'],
                        capture_output=True,
                        text=True
                    )
                    if smart_output.returncode == 0:
                        disk_info['smart_available'] = True
                except FileNotFoundError:
                    disk_info['smart_available'] = False
            
            self.diagnostics_results['disk_health'] = disk_info
            logger.info("Disk health check completed")
            return True
        except Exception as e:
            logger.error(f"Error checking disk health: {str(e)}")
            return False

    def check_cpu_health(self):
        """Check CPU health and performance"""
        try:
            cpu_info = {
                'usage_percent': psutil.cpu_percent(interval=1),
                'load_avg': os.getloadavg() if hasattr(os, 'getloadavg') else None,
                'temperature': None,
                'frequency': psutil.cpu_freq().current if hasattr(psutil, 'cpu_freq') else None
            }
            
            # Try to get CPU temperature (platform specific)
            if platform.system() == 'Linux':
                try:
                    temp = None
                    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                        temp = float(f.read()) / 1000
                    cpu_info['temperature'] = temp
                except (FileNotFoundError, PermissionError):
                    pass
            
            self.diagnostics_results['cpu_health'] = cpu_info
            logger.info("CPU health check completed")
            return True
        except Exception as e:
            logger.error(f"Error checking CPU health: {str(e)}")
            return False

    def check_memory_health(self):
        """Check RAM health and usage"""
        try:
            virtual_mem = psutil.virtual_memory()
            swap_mem = psutil.swap_memory()
            
            memory_info = {
                'total_ram_gb': round(virtual_mem.total / (1024 ** 3), 2),
                'available_ram_gb': round(virtual_mem.available / (1024 ** 3), 2),
                'used_ram_gb': round(virtual_mem.used / (1024 ** 3), 2),
                'ram_percent_used': virtual_mem.percent,
                'swap_total_gb': round(swap_mem.total / (1024 ** 3), 2),
                'swap_used_gb': round(swap_mem.used / (1024 ** 3), 2),
                'swap_percent_used': swap_mem.percent
            }
            
            self.diagnostics_results['memory_health'] = memory_info
            logger.info("Memory health check completed")
            return True
        except Exception as e:
            logger.error(f"Error checking memory health: {str(e)}")
            return False

    def check_network_health(self):
        """Check network connectivity and speed"""
        try:
            net_info = {
                'interfaces': {},
                'connectivity': {}
            }
            
            # Get network interface information
            interfaces = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            
            for interface, addrs in interfaces.items():
                net_info['interfaces'][interface] = {
                    'is_up': stats[interface].isup if interface in stats else False,
                    'speed': stats[interface].speed if interface in stats else 0,
                    'addresses': [addr.address for addr in addrs]
                }
            
            # Basic connectivity checks
            try:
                # Check localhost
                subprocess.run(['ping', '-c', '1', '127.0.0.1'], check=True, stdout=subprocess.PIPE)
                net_info['connectivity']['localhost'] = True
                
                # Check gateway (Linux/Mac)
                if platform.system() in ['Linux', 'Darwin']:
                    try:
                        gateway = subprocess.run(
                            ['ip', 'route', 'show', 'default'],
                            capture_output=True,
                            text=True
                        ).stdout.split()[2]
                        subprocess.run(['ping', '-c', '1', gateway], check=True, stdout=subprocess.PIPE)
                        net_info['connectivity']['gateway'] = True
                    except Exception:
                        net_info['connectivity']['gateway'] = False
                
                # Check public DNS
                subprocess.run(['ping', '-c', '1', '8.8.8.8'], check=True, stdout=subprocess.PIPE)
                net_info['connectivity']['public_dns'] = True
                
                # Check domain resolution
                subprocess.run(['ping', '-c', '1', 'google.com'], check=True, stdout=subprocess.PIPE)
                net_info['connectivity']['dns_resolution'] = True
                
            except subprocess.CalledProcessError:
                net_info['connectivity']['localhost'] = False
                net_info['connectivity']['public_dns'] = False
                net_info['connectivity']['dns_resolution'] = False
            
            self.diagnostics_results['network_health'] = net_info
            logger.info("Network health check completed")
            return True
        except Exception as e:
            logger.error(f"Error checking network health: {str(e)}")
            return False

    def check_battery_health(self):
        """Check battery health if available"""
        try:
            if hasattr(psutil, 'sensors_battery'):
                battery = psutil.sensors_battery()
                if battery:
                    self.diagnostics_results['battery_health'] = {
                        'percent': battery.percent,
                        'power_plugged': battery.power_plugged,
                        'seconds_left': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None
                    }
                    logger.info("Battery health check completed")
                    return True
            logger.info("No battery detected - skipping check")
            return False
        except Exception as e:
            logger.error(f"Error checking battery health: {str(e)}")
            return False

    def run_stress_test(self, duration=60):
        """Run a simple CPU stress test"""
        try:
            logger.info(f"Starting CPU stress test for {duration} seconds...")
            start_time = time.time()
            end_time = start_time + duration
            
            while time.time() < end_time:
                # Simple CPU stress
                [x*x for x in range(1000000)]
                
                # Check temperature during stress
                if 'cpu_health' in self.diagnostics_results and self.diagnostics_results['cpu_health']['temperature']:
                    current_temp = self.diagnostics_results['cpu_health']['temperature']
                    if current_temp > 85:  # Threshold in Celsius
                        logger.warning(f"High CPU temperature detected: {current
