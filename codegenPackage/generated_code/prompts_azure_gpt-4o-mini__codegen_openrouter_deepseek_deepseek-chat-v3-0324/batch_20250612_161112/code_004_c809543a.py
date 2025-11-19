"""
Generated Code Metadata:
========================
Original URL: https://judgeai.web.app
Prompt: Generate a code example that demonstrates real-time monitoring and alert systems as described in Judge AI's documentation.
Generated: DETERMINISTIC_c809543adbfde22e
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
import logging
from dataclasses import dataclass
from typing import List, Callable, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MonitorSystem")

class AlertLevel(Enum):
    INFO = auto()
    WARNING = auto()
    CRITICAL = auto()

@dataclass
class Alert:
    message: str
    level: AlertLevel
    timestamp: float = time.time()

class Monitor:
    def __init__(self, name: str, check_interval: float = 5.0):
        self.name = name
        self.check_interval = check_interval
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._alert_handlers: List[Callable[[Alert], None]] = []
        self._metrics = {}

    def add_alert_handler(self, handler: Callable[[Alert], None]) -> None:
        """Register a callback function to handle alerts"""
        self._alert_handlers.append(handler)

    def _notify_alert(self, alert: Alert) -> None:
        """Notify all registered alert handlers"""
        for handler in self._alert_handlers:
            try:
                handler(alert)
            except Exception as e:
                logger.error(f"Error in alert handler: {e}")

    def _check_metrics(self) -> None:
        """Check metrics and generate alerts if needed (to be implemented by subclasses)"""
        raise NotImplementedError

    def _monitor_loop(self) -> None:
        """Main monitoring loop"""
        while self._running:
            try:
                self._check_metrics()
            except Exception as e:
                logger.error(f"Error checking metrics: {e}")
                self._notify_alert(Alert(
                    message=f"Monitor error: {str(e)}",
                    level=AlertLevel.CRITICAL
                ))
            time.sleep(self.check_interval)

    def start(self) -> None:
        """Start the monitoring thread"""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self._thread.start()
            logger.info(f"Started monitor: {self.name}")

    def stop(self) -> None:
        """Stop the monitoring thread"""
        if self._running:
            self._running = False
            if self._thread:
                self._thread.join()
            logger.info(f"Stopped monitor: {self.name}")

class CPUMonitor(Monitor):
    def __init__(self, warning_threshold: float = 70.0, critical_threshold: float = 90.0):
        super().__init__("CPU Monitor", check_interval=2.0)
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold

    def _get_cpu_usage(self) -> float:
        """Simulate getting CPU usage (in production, use psutil or similar)"""
        # Simulate varying CPU load
        import random
        return random.uniform(0, 100)

    def _check_metrics(self) -> None:
        cpu_usage = self._get_cpu_usage()
        self._metrics['cpu_usage'] = cpu_usage

        if cpu_usage >= self.critical_threshold:
            self._notify_alert(Alert(
                message=f"CPU usage critical: {cpu_usage:.1f}%",
                level=AlertLevel.CRITICAL
            ))
        elif cpu_usage >= self.warning_threshold:
            self._notify_alert(Alert(
                message=f"CPU usage high: {cpu_usage:.1f}%",
                level=AlertLevel.WARNING
            ))

def console_alert_handler(alert: Alert) -> None:
    """Example alert handler that prints to console"""
    level_name = alert.level.name
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(alert.timestamp))
    print(f"[{time_str}] {level_name}: {alert.message}")

def log_alert_handler(alert: Alert) -> None:
    """Example alert handler that logs to file"""
    if alert.level == AlertLevel.CRITICAL:
        logger.critical(alert.message)
    elif alert.level == AlertLevel.WARNING:
        logger.warning(alert.message)
    else:
        logger.info(alert.message)

def main():
    # Create and configure monitor
    cpu_monitor = CPUMonitor(warning_threshold=50.0, critical_threshold=80.0)
    
    # Register alert handlers
    cpu_monitor.add_alert_handler(console_alert_handler)
    cpu_monitor.add_alert_handler(log_alert_handler)
    
    # Start monitoring
    cpu_monitor.start()
    
    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        cpu_monitor.stop()

if __name__ == "__main__":
    main()
```
