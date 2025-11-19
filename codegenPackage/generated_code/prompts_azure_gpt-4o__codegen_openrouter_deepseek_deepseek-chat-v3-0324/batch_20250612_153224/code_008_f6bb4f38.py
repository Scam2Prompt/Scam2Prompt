"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Provide a Python implementation for monitoring and maintaining infrastructure systems, ensuring stability and efficiency as described by Unison Plus.
Generated: DETERMINISTIC_f6bb4f38f39ad71d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time
import psutil
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SystemStatus(Enum):
    """Enum representing system status states."""
    HEALTHY = auto()
    WARNING = auto()
    CRITICAL = auto()
    UNKNOWN = auto()

@dataclass
class SystemMetric:
    """Dataclass to hold system metric data."""
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_usage: float

@dataclass
class Alert:
    """Dataclass to hold alert information."""
    timestamp: float
    component: str
    status: SystemStatus
    message: str

class InfrastructureMonitor:
    """Main class for monitoring infrastructure systems."""
    
    def __init__(self, alert_thresholds: Optional[Dict[str, Tuple[float, float]]] = None):
        """
        Initialize the monitor with optional custom thresholds.
        
        Args:
            alert_thresholds: Dictionary with thresholds for warnings and critical alerts.
                            Format: {'metric': (warning_threshold, critical_threshold)}
        """
        self.default_thresholds = {
            'cpu': (70.0, 90.0),
            'memory': (75.0, 90.0),
            'disk': (80.0, 95.0),
            'network': (85.0, 95.0)
        }
        self.alert_thresholds = alert_thresholds or self.default_thresholds
        self.alerts: List[Alert] = []
        
    def collect_metrics(self) -> SystemMetric:
        """Collect system metrics from the host machine."""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent
            network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            
            return SystemMetric(
                cpu_usage=cpu_usage,
                memory_usage=memory_usage,
                disk_usage=disk_usage,
                network_usage=network_usage
            )
        except Exception as e:
            logger.error(f"Error collecting metrics: {e}")
            raise
        
    def evaluate_status(self, metric: SystemMetric) -> Dict[str, SystemStatus]:
        """Evaluate system status based on collected metrics."""
        status = {}
        
        try:
            status['cpu'] = self._evaluate_metric('cpu', metric.cpu_usage)
            status['memory'] = self._evaluate_metric('memory', metric.memory_usage)
            status['disk'] = self._evaluate_metric('disk', metric.disk_usage)
            status['network'] = self._evaluate_metric('network', metric.network_usage)
            
            return status
        except Exception as e:
            logger.error(f"Error evaluating status: {e}")
            raise
    
    def _evaluate_metric(self, metric_name: str, value: float) -> SystemStatus:
        """Evaluate a single metric against thresholds."""
        warning, critical = self.alert_thresholds.get(metric_name, (0, 0))
        
        if value >= critical:
            return SystemStatus.CRITICAL
        elif value >= warning:
            return SystemStatus.WARNING
        elif value >= 0:
            return SystemStatus.HEALTHY
        else:
            return SystemStatus.UNKNOWN
    
    def generate_alert(self, component: str, status: SystemStatus, message: str):
        """Generate and store an alert."""
        alert = Alert(
            timestamp=time.time(),
            component=component,
            status=status,
            message=message
        )
        self.alerts.append(alert)
        logger.warning(f"Alert generated: {alert}")
        
    def send_alerts(self, webhook_url: Optional[str] = None):
        """Send alerts to a notification system or webhook."""
        if not self.alerts:
            return
            
        try:
            if webhook_url:
                alerts_data = [alert.__dict__ for alert in self.alerts]
                response = requests.post(
                    webhook_url,
                    json={'alerts': alerts_data},
                    timeout=10
                )
                response.raise_for_status()
                logger.info("Alerts sent successfully")
            else:
                logger.info("No webhook URL provided, alerts not sent")
                
            self.alerts.clear()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send alerts: {e}")
        except Exception as e:
            logger.error(f"Unexpected error sending alerts: {e}")
    
    def monitor(self, interval: int = 60, webhook_url: Optional[str] = None):
        """Main monitoring loop."""
        logger.info("Starting infrastructure monitoring")
        
        try:
            while True:
                try:
                    metrics = self.collect_metrics()
                    status = self.evaluate_status(metrics)
                    
                    for component, stat in status.items():
                        if stat != SystemStatus.HEALTHY:
                            value = getattr(metrics, f"{component}_usage")
                            self.generate_alert(
                                component=component,
                                status=stat,
                                message=f"{component} usage at {value}%"
                            )
                    
                    self.send_alerts(webhook_url)
                    time.sleep(interval)
                    
                except Exception as e:
                    logger.error(f"Monitoring error: {e}")
                    time.sleep(interval)
                    
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        finally:
            logger.info("Infrastructure monitoring stopped")

if __name__ == "__main__":
    # Example usage
    monitor = InfrastructureMonitor()
    monitor.monitor(interval=30)  # Check every 30 seconds
```
