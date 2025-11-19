"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Create a Python script to monitor and log the performance metrics (e.g., power consumption, speed, load) of a KPT拖揽供电平车 in real-time.
Generated: DETERMINISTIC_087bdcfa39fa54f3
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from datetime import datetime
import psutil
import platform
import socket
import json
from typing import Dict, Any

# Configuration
LOG_FILE = 'kpt_monitor.log'
MONITOR_INTERVAL = 5  # seconds
METRICS_TO_MONITOR = ['cpu_percent', 'memory_percent', 'disk_io_counters', 'net_io_counters']

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('KPTMonitor')

class KPTMonitor:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.system_info = self._get_system_info()
        logger.info(f"Initializing KPT Monitor on {self.hostname}")
        logger.info(f"System Info: {json.dumps(self.system_info, indent=2)}")

    def _get_system_info(self) -> Dict[str, Any]:
        """Get basic system information."""
        return {
            'system': platform.system(),
            'node': platform.node(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'cpu_cores': psutil.cpu_count(logical=False),
            'logical_cpus': psutil.cpu_count(logical=True),
            'total_memory': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        }

    def _get_metrics(self) -> Dict[str, Any]:
        """Collect all relevant performance metrics."""
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'hostname': self.hostname,
        }

        try:
            # CPU Metrics
            metrics['cpu'] = {
                'percent': psutil.cpu_percent(interval=1),
                'freq': psutil.cpu_freq().current if hasattr(psutil, 'cpu_freq') else None,
                'load_avg': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None,
            }

            # Memory Metrics
            mem = psutil.virtual_memory()
            metrics['memory'] = {
                'percent': mem.percent,
                'used_gb': round(mem.used / (1024 ** 3), 2),
                'available_gb': round(mem.available / (1024 ** 3), 2),
            }

            # Disk Metrics
            disk = psutil.disk_io_counters()
            metrics['disk'] = {
                'read_count': disk.read_count,
                'write_count': disk.write_count,
                'read_bytes': disk.read_bytes,
                'write_bytes': disk.write_bytes,
            }

            # Network Metrics
            net = psutil.net_io_counters()
            metrics['network'] = {
                'bytes_sent': net.bytes_sent,
                'bytes_recv': net.bytes_recv,
                'packets_sent': net.packets_sent,
                'packets_recv': net.packets_recv,
            }

            # Power Metrics (if available)
            if hasattr(psutil, 'sensors_battery'):
                battery = psutil.sensors_battery()
                if battery:
                    metrics['power'] = {
                        'percent': battery.percent,
                        'power_plugged': battery.power_plugged,
                    }

        except Exception as e:
            logger.error(f"Error collecting metrics: {str(e)}")
            metrics['error'] = str(e)

        return metrics

    def log_metrics(self):
        """Log collected metrics to file and console."""
        metrics = self._get_metrics()
        logger.info(f"Metrics: {json.dumps(metrics, indent=2)}")

    def run(self):
        """Main monitoring loop."""
        logger.info("Starting KPT monitoring...")
        try:
            while True:
                self.log_metrics()
                time.sleep(MONITOR_INTERVAL)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Monitoring error: {str(e)}")

if __name__ == "__main__":
    monitor = KPTMonitor()
    monitor.run()
```
