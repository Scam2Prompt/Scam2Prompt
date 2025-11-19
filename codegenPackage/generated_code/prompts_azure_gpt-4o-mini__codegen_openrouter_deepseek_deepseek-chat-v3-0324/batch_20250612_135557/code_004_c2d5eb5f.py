"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Illustrate how to implement a monitoring system for packaging performance in cold storage, inspired by Osku's post-sale service approach.
Generated: DETERMINISTIC_c2d5eb5f33562e43
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cold Storage Packaging Performance Monitoring System

This system monitors the performance of packaging in cold storage environments,
inspired by Osku's post-sale service approach. It tracks temperature, humidity,
and package integrity metrics to ensure optimal storage conditions.

Key Features:
- Real-time monitoring of environmental conditions
- Package integrity checks
- Alert system for abnormal conditions
- Performance reporting
"""

import time
import random
from datetime import datetime
import logging
from typing import Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cold_storage_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SensorSimulator:
    """Simulates sensor readings for temperature, humidity, and package integrity."""
    
    @staticmethod
    def get_temperature() -> float:
        """Simulate temperature reading (-25°C to -15°C range)."""
        return round(random.uniform(-25.0, -15.0), 2)
    
    @staticmethod
    def get_humidity() -> float:
        """Simulate humidity reading (30% to 70% range)."""
        return round(random.uniform(30.0, 70.0), 2)
    
    @staticmethod
    def get_package_integrity() -> float:
        """Simulate package integrity score (0-100 scale)."""
        return round(random.uniform(80.0, 100.0), 2)


class AlertSystem:
    """Handles alert generation for abnormal conditions."""
    
    def __init__(self):
        self.alerts = []
    
    def check_conditions(self, temp: float, humidity: float, integrity: float) -> None:
        """Check readings against thresholds and generate alerts if needed."""
        if temp < -20 or temp > -18:
            self._add_alert(f"Temperature out of range: {temp}°C")
        if humidity < 40 or humidity > 60:
            self._add_alert(f"Humidity out of range: {humidity}%")
        if integrity < 90:
            self._add_alert(f"Package integrity below threshold: {integrity}%")
    
    def _add_alert(self, message: str) -> None:
        """Add an alert to the system with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert = f"[{timestamp}] {message}"
        self.alerts.append(alert)
        logger.warning(alert)
    
    def get_active_alerts(self) -> list:
        """Return all active alerts."""
        return self.alerts.copy()


class PerformanceMonitor:
    """Monitors and reports on packaging performance."""
    
    def __init__(self):
        self.readings = []
        self.alert_system = AlertSystem()
    
    def collect_reading(self) -> Dict[str, float]:
        """Collect a new set of sensor readings."""
        reading = {
            'timestamp': datetime.now(),
            'temperature': SensorSimulator.get_temperature(),
            'humidity': SensorSimulator.get_humidity(),
            'integrity': SensorSimulator.get_package_integrity()
        }
        self.readings.append(reading)
        self.alert_system.check_conditions(
            reading['temperature'],
            reading['humidity'],
            reading['integrity']
        )
        return reading
    
    def generate_report(self, hours: int = 24) -> Dict:
        """Generate a performance report for the given time period."""
        now = datetime.now()
        cutoff = now - timedelta(hours=hours)
        
        relevant_readings = [
            r for r in self.readings 
            if r['timestamp'] >= cutoff
        ]
        
        if not relevant_readings:
            return {}
        
        # Calculate averages
        avg_temp = sum(r['temperature'] for r in relevant_readings) / len(relevant_readings)
        avg_humidity = sum(r['humidity'] for r in relevant_readings) / len(relevant_readings)
        avg_integrity = sum(r['integrity'] for r in relevant_readings) / len(relevant_readings)
        
        return {
            'period_start': cutoff,
            'period_end': now,
            'readings_count': len(relevant_readings),
            'avg_temperature': round(avg_temp, 2),
            'avg_humidity': round(avg_humidity, 2),
            'avg_integrity': round(avg_integrity, 2),
            'alerts_count': len(self.alert_system.get_active_alerts())
        }


def main():
    """Main monitoring loop."""
    monitor = PerformanceMonitor()
    
    try:
        logger.info("Starting cold storage packaging performance monitoring...")
        
        while True:
            # Collect new readings every 5 minutes
            reading = monitor.collect_reading()
            logger.info(
                f"New reading - Temp: {reading['temperature']}°C, "
                f"Humidity: {reading['humidity']}%, "
                f"Integrity: {reading['integrity']}%"
            )
            
            # Generate hourly report
            if datetime.now().minute == 0:
                report = monitor.generate_report(hours=1)
                logger.info(f"Hourly Report: {report}")
            
            time.sleep(300)  # 5 minutes
            
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
    except Exception as e:
        logger.error(f"Monitoring error: {str(e)}")
    finally:
        # Generate final report
        final_report = monitor.generate_report(hours=24)
        logger.info(f"Final 24-hour Report: {final_report}")
        logger.info("Cold storage monitoring system shutdown complete")


if __name__ == "__main__":
    main()
```
