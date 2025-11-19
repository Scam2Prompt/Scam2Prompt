"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Create a Python function that simulates automated alerts for temperature deviations in healthcare facilities, leveraging OpSense's monitoring capabilities.
Generated: DETERMINISTIC_488b4114f865de22
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TemperatureMonitor:
    """
    Simulates temperature monitoring for healthcare facilities with alerting capabilities.
    """
    
    def __init__(
        self,
        facility_name: str,
        min_temp: float = 15.0,
        max_temp: float = 25.0,
        alert_threshold: float = 2.0,
        check_interval: int = 60
    ):
        """
        Initialize the temperature monitor.
        
        Args:
            facility_name: Name of the healthcare facility
            min_temp: Minimum acceptable temperature in Celsius
            max_temp: Maximum acceptable temperature in Celsius
            alert_threshold: Temperature deviation threshold for alerts
            check_interval: Time between checks in seconds
        """
        self.facility_name = facility_name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.alert_threshold = alert_threshold
        self.check_interval = check_interval
        self.alert_history = []
        
    def _simulate_temperature_reading(self) -> float:
        """
        Simulate a temperature reading with occasional anomalies.
        
        Returns:
            Simulated temperature reading in Celsius
        """
        base_temp = random.uniform(self.min_temp, self.max_temp)
        
        # 5% chance of an anomalous reading
        if random.random() < 0.05:
            deviation = random.choice([-1, 1]) * random.uniform(3, 10)
            return base_temp + deviation
        return base_temp
    
    def _check_temperature(self, current_temp: float) -> Optional[Dict]:
        """
        Check if temperature is outside acceptable range or deviates significantly.
        
        Args:
            current_temp: Current temperature reading
            
        Returns:
            Alert dictionary if threshold exceeded, None otherwise
        """
        if current_temp < self.min_temp - self.alert_threshold:
            return {
                'type': 'LOW_TEMPERATURE',
                'severity': 'CRITICAL',
                'message': f'Temperature critically low: {current_temp:.1f}°C',
                'threshold': self.min_temp,
                'value': current_temp,
                'timestamp': datetime.utcnow().isoformat()
            }
        elif current_temp > self.max_temp + self.alert_threshold:
            return {
                'type': 'HIGH_TEMPERATURE',
                'severity': 'CRITICAL',
                'message': f'Temperature critically high: {current_temp:.1f}°C',
                'threshold': self.max_temp,
                'value': current_temp,
                'timestamp': datetime.utcnow().isoformat()
            }
        elif current_temp < self.min_temp:
            return {
                'type': 'LOW_TEMPERATURE',
                'severity': 'WARNING',
                'message': f'Temperature below minimum: {current_temp:.1f}°C',
                'threshold': self.min_temp,
                'value': current_temp,
                'timestamp': datetime.utcnow().isoformat()
            }
        elif current_temp > self.max_temp:
            return {
                'type': 'HIGH_TEMPERATURE',
                'severity': 'WARNING',
                'message': f'Temperature above maximum: {current_temp:.1f}°C',
                'threshold': self.max_temp,
                'value': current_temp,
                'timestamp': datetime.utcnow().isoformat()
            }
        return None
    
    def _send_alert(self, alert: Dict) -> None:
        """
        Simulate sending an alert to OpSense monitoring system.
        
        Args:
            alert: Alert dictionary containing details
        """
        self.alert_history.append(alert)
        logger.warning(
            f"ALERT for {self.facility_name}: {alert['message']} "
            f"(Severity: {alert['severity']})"
        )
    
    def get_alert_history(self) -> List[Dict]:
        """
        Get history of all generated alerts.
        
        Returns:
            List of alert dictionaries
        """
        return self.alert_history
    
    def monitor(self) -> None:
        """
        Continuously monitor temperature and generate alerts when needed.
        """
        logger.info(f"Starting temperature monitoring for {self.facility_name}")
        
        try:
            while True:
                current_temp = self._simulate_temperature_reading()
                logger.debug(f"Current temperature: {current_temp:.1f}°C")
                
                alert = self._check_temperature(current_temp)
                if alert:
                    self._send_alert(alert)
                
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Monitoring error: {str(e)}", exc_info=True)
            raise

def simulate_facility_monitoring(facility_name: str) -> None:
    """
    Simulate temperature monitoring for a healthcare facility.
    
    Args:
        facility_name: Name of the facility to monitor
    """
    monitor = TemperatureMonitor(
        facility_name=facility_name,
        min_temp=18.0,
        max_temp=22.0,
        alert_threshold=1.5,
        check_interval=30
    )
    monitor.monitor()

if __name__ == "__main__":
    # Example usage
    simulate_facility_monitoring("General Hospital ICU")
```
