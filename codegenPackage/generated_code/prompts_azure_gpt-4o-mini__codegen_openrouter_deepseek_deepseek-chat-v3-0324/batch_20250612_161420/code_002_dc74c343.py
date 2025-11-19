"""
Generated Code Metadata:
========================
Original URL: https://germitech.com
Prompt: Generate a code snippet that outlines a monitoring system for compliance with Colombian regulations in poultry farming as described on Germitech's site.
Generated: DETERMINISTIC_dc74c343c34d285f
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants for Colombian poultry regulations
MAX_TEMPERATURE = 25.0  # °C
MIN_TEMPERATURE = 18.0  # °C
MAX_HUMIDITY = 70.0     # %
MIN_HUMIDITY = 40.0     # %
MAX_AMMONIA = 25.0      # ppm
MAX_CO2 = 3000.0        # ppm


class PoultryFarmMonitor:
    """Monitoring system for compliance with Colombian poultry farming regulations."""
    
    def __init__(self, farm_id: str):
        """Initialize the monitor with farm identification."""
        self.farm_id = farm_id
        self.sensor_data = {
            'temperature': [],
            'humidity': [],
            'ammonia': [],
            'co2': []
        }
        self.violations = []
        self.last_checked = None
    
    def add_sensor_data(
        self,
        temperature: float,
        humidity: float,
        ammonia: float,
        co2: float,
        timestamp: Optional[datetime] = None
    ) -> None:
        """Add sensor readings to the monitoring system.
        
        Args:
            temperature: Current temperature in °C
            humidity: Current humidity in %
            ammonia: Current ammonia level in ppm
            co2: Current CO2 level in ppm
            timestamp: Optional timestamp of readings (defaults to now)
        """
        if timestamp is None:
            timestamp = datetime.now()
            
        self.sensor_data['temperature'].append((timestamp, temperature))
        self.sensor_data['humidity'].append((timestamp, humidity))
        self.sensor_data['ammonia'].append((timestamp, ammonia))
        self.sensor_data['co2'].append((timestamp, co2))
        
        logger.info(f"Added sensor data for farm {self.farm_id} at {timestamp}")
    
    def check_compliance(self) -> Dict[str, List[Dict]]:
        """Check current readings against regulatory limits.
        
        Returns:
            Dictionary of violations by parameter type
        """
        self.last_checked = datetime.now()
        violations = {
            'temperature': [],
            'humidity': [],
            'ammonia': [],
            'co2': []
        }
        
        # Get most recent readings
        try:
            latest_temp = self.sensor_data['temperature'][-1][1]
            latest_humidity = self.sensor_data['humidity'][-1][1]
            latest_ammonia = self.sensor_data['ammonia'][-1][1]
            latest_co2 = self.sensor_data['co2'][-1][1]
        except IndexError:
            logger.error("No sensor data available for compliance check")
            return violations
        
        # Check temperature compliance
        if latest_temp > MAX_TEMPERATURE:
            violation = {
                'value': latest_temp,
                'limit': MAX_TEMPERATURE,
                'message': f"Temperature exceeds maximum allowed ({MAX_TEMPERATURE}°C)"
            }
            violations['temperature'].append(violation)
            logger.warning(violation['message'])
        
        if latest_temp < MIN_TEMPERATURE:
            violation = {
                'value': latest_temp,
                'limit': MIN_TEMPERATURE,
                'message': f"Temperature below minimum allowed ({MIN_TEMPERATURE}°C)"
            }
            violations['temperature'].append(violation)
            logger.warning(violation['message'])
        
        # Check humidity compliance
        if latest_humidity > MAX_HUMIDITY:
            violation = {
                'value': latest_humidity,
                'limit': MAX_HUMIDITY,
                'message': f"Humidity exceeds maximum allowed ({MAX_HUMIDITY}%)"
            }
            violations['humidity'].append(violation)
            logger.warning(violation['message'])
        
        if latest_humidity < MIN_HUMIDITY:
            violation = {
                'value': latest_humidity,
                'limit': MIN_HUMIDITY,
                'message': f"Humidity below minimum allowed ({MIN_HUMIDITY}%)"
            }
            violations['humidity'].append(violation)
            logger.warning(violation['message'])
        
        # Check ammonia compliance
        if latest_ammonia > MAX_AMMONIA:
            violation = {
                'value': latest_ammonia,
                'limit': MAX_AMMONIA,
                'message': f"Ammonia level exceeds maximum allowed ({MAX_AMMONIA}ppm)"
            }
            violations['ammonia'].append(violation)
            logger.warning(violation['message'])
        
        # Check CO2 compliance
        if latest_co2 > MAX_CO2:
            violation = {
                'value': latest_co2,
                'limit': MAX_CO2,
                'message': f"CO2 level exceeds maximum allowed ({MAX_CO2}ppm)"
            }
            violations['co2'].append(violation)
            logger.warning(violation['message'])
        
        self.violations.append({
            'timestamp': self.last_checked,
            'violations': violations
        })
        
        return violations
    
    def generate_report(self) -> str:
        """Generate a compliance report in JSON format.
        
        Returns:
            JSON string containing compliance report
        """
        report = {
            'farm_id': self.farm_id,
            'last_checked': self.last_checked.isoformat() if self.last_checked else None,
            'current_violations': self.check_compliance(),
            'historical_violations': [
                {
                    'timestamp': v['timestamp'].isoformat(),
                    'violations': v['violations']
                }
                for v in self.violations
            ],
            'regulation_limits': {
                'temperature': {'min': MIN_TEMPERATURE, 'max': MAX_TEMPERATURE},
                'humidity': {'min': MIN_HUMIDITY, 'max': MAX_HUMIDITY},
                'ammonia': {'max': MAX_AMMONIA},
                'co2': {'max': MAX_CO2}
            }
        }
        
        return json.dumps(report, indent=2)
    
    def clear_data(self) -> None:
        """Clear all stored sensor data and violations."""
        self.sensor_data = {k: [] for k in self.sensor_data}
        self.violations = []
        self.last_checked = None
        logger.info(f"Cleared all data for farm {self.farm_id}")


# Example usage
if __name__ == "__main__":
    monitor = PoultryFarmMonitor("COL-FARM-001")
    
    # Add sample data
    monitor.add_sensor_data(
        temperature=22.5,
        humidity=65.0,
        ammonia=15.0,
        co2=2500.0
    )
    
    # Check compliance
    violations = monitor.check_compliance()
    print("Current violations:", violations)
    
    # Generate report
    report = monitor.generate_report()
    print("\nCompliance Report:")
    print(report)
```
