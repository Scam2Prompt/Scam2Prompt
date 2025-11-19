"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Write a Python script that simulates the monitoring of UPS battery health and triggers alerts for proactive replacement based on the conditions described by Technical Power Service, Inc.
Generated: DETERMINISTIC_9e8018fce449c183
Batch ID: 20250612_162050
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
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ups_monitor.log'),
        logging.StreamHandler()
    ]
)

class UPSMonitor:
    """
    A class to monitor UPS battery health and trigger alerts based on predefined conditions.
    """
    
    def __init__(self, ups_id: str, model: str, nominal_capacity: float):
        """
        Initialize the UPS monitor with basic UPS information.
        
        Args:
            ups_id: Unique identifier for the UPS
            model: Model of the UPS
            nominal_capacity: Nominal battery capacity in Ah
        """
        self.ups_id = ups_id
        self.model = model
        self.nominal_capacity = nominal_capacity
        self.health_history = []
        self.alert_thresholds = {
            'capacity_loss': 0.2,  # 20% capacity loss
            'internal_resistance': 0.3,  # 30% increase
            'charge_cycles': 500,  # 500 cycles
            'temperature': 45.0,  # 45°C
            'voltage_deviation': 0.1  # 10% deviation
        }
        
    def simulate_measurement(self) -> Dict[str, float]:
        """
        Simulate measurement of battery parameters with some random variation.
        
        Returns:
            Dictionary containing simulated battery parameters
        """
        return {
            'capacity': max(0.5, min(1.0, random.normalvariate(0.85, 0.1))),
            'internal_resistance': max(1.0, min(2.0, random.normalvariate(1.2, 0.1))),
            'charge_cycles': random.randint(100, 600),
            'temperature': random.uniform(20.0, 50.0),
            'voltage': random.normalvariate(12.0, 0.5)
        }
    
    def check_health(self, measurements: Dict[str, float]) -> Dict[str, bool]:
        """
        Check battery health against alert thresholds.
        
        Args:
            measurements: Dictionary of current battery measurements
            
        Returns:
            Dictionary of alert conditions (True if alert should be triggered)
        """
        return {
            'capacity_loss': measurements['capacity'] < (1 - self.alert_thresholds['capacity_loss']),
            'internal_resistance': measurements['internal_resistance'] > (1 + self.alert_thresholds['internal_resistance']),
            'charge_cycles': measurements['charge_cycles'] > self.alert_thresholds['charge_cycles'],
            'temperature': measurements['temperature'] > self.alert_thresholds['temperature'],
            'voltage_deviation': abs(measurements['voltage'] - 12.0) / 12.0 > self.alert_thresholds['voltage_deviation']
        }
    
    def generate_alert(self, alert_conditions: Dict[str, bool], measurements: Dict[str, float]) -> Optional[str]:
        """
        Generate alert message if any condition is met.
        
        Args:
            alert_conditions: Dictionary of alert conditions
            measurements: Current measurements for inclusion in alert
            
        Returns:
            Alert message if any condition is met, None otherwise
        """
        triggered_alerts = [k for k, v in alert_conditions.items() if v]
        
        if not triggered_alerts:
            return None
            
        alert_msg = f"ALERT for UPS {self.ups_id} ({self.model}):\n"
        alert_msg += "The following battery health issues were detected:\n"
        
        for alert in triggered_alerts:
            alert_msg += f"- {alert.replace('_', ' ').title()}: {measurements[alert.split('_')[0]]}\n"
            
        alert_msg += "Proactive battery replacement recommended."
        return alert_msg
    
    def monitor(self, interval: int = 60):
        """
        Continuously monitor the UPS battery health at specified intervals.
        
        Args:
            interval: Monitoring interval in seconds
        """
        logging.info(f"Starting UPS {self.ups_id} ({self.model}) monitoring...")
        
        try:
            while True:
                measurements = self.simulate_measurement()
                self.health_history.append(measurements)
                
                alert_conditions = self.check_health(measurements)
                alert_msg = self.generate_alert(alert_conditions, measurements)
                
                if alert_msg:
                    logging.warning(alert_msg)
                else:
                    logging.info(f"UPS {self.ups_id} status OK - Capacity: {measurements['capacity']:.2f}, Cycles: {measurements['charge_cycles']}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Monitoring error: {str(e)}")

if __name__ == "__main__":
    # Example usage
    ups = UPSMonitor(
        ups_id="UPS-001",
        model="PowerGuard 3000",
        nominal_capacity=7.0
    )
    ups.monitor(interval=10)  # Check every 10 seconds for demo purposes
```
