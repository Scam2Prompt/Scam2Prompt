"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write Python code to simulate GPS tracking and temperature monitoring for a fleet of refrigerated vans, as described on RefrigeratorTransport.com.
Generated: DETERMINISTIC_8aae455f22a6659d
Batch ID: 20250612_153246
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
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GPSDevice(ABC):
    """Abstract base class for GPS devices"""
    @abstractmethod
    def get_current_location(self) -> Dict[str, float]:
        pass

class TemperatureSensor(ABC):
    """Abstract base class for temperature sensors"""
    @abstractmethod
    def get_current_temperature(self) -> float:
        pass

class SimulatedGPS(GPSDevice):
    """Simulated GPS device that generates random coordinates"""
    def __init__(self, initial_lat: float, initial_lon: float):
        self.latitude = initial_lat
        self.longitude = initial_lon
        
    def get_current_location(self) -> Dict[str, float]:
        # Simulate small movements
        self.latitude += random.uniform(-0.001, 0.001)
        self.longitude += random.uniform(-0.001, 0.001)
        
        # Ensure coordinates stay within valid ranges
        self.latitude = max(-90, min(90, self.latitude))
        self.longitude = max(-180, min(180, self.longitude))
        
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'timestamp': datetime.utcnow().isoformat()
        }

class SimulatedTemperatureSensor(TemperatureSensor):
    """Simulated temperature sensor for refrigerated vans"""
    def __init__(self, min_temp: float, max_temp: float):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.current_temp = (min_temp + max_temp) / 2
        
    def get_current_temperature(self) -> float:
        # Simulate temperature fluctuations
        temp_change = random.uniform(-0.5, 0.5)
        self.current_temp += temp_change
        
        # Ensure temperature stays within bounds
        self.current_temp = max(self.min_temp, min(self.max_temp, self.current_temp))
        
        return round(self.current_temp, 2)

class RefrigeratedVan:
    """Class representing a refrigerated van with GPS and temperature monitoring"""
    def __init__(self, van_id: str, gps_device: GPSDevice, temp_sensor: TemperatureSensor):
        self.van_id = van_id
        self.gps_device = gps_device
        self.temp_sensor = temp_sensor
        self.alerts = []
        
    def get_status(self) -> Dict:
        """Get current status of the van including location and temperature"""
        try:
            location = self.gps_device.get_current_location()
            temperature = self.temp_sensor.get_current_temperature()
            
            status = {
                'van_id': self.van_id,
                'location': location,
                'temperature': temperature,
                'timestamp': datetime.utcnow().isoformat()
            }
            
            # Check for temperature anomalies
            self._check_temperature(temperature)
            
            return status
        except Exception as e:
            logger.error(f"Error getting status for van {self.van_id}: {str(e)}")
            raise
            
    def _check_temperature(self, current_temp: float) -> None:
        """Check for temperature anomalies and generate alerts if needed"""
        # These thresholds would normally be configurable per van
        temp_threshold_low = -20.0
        temp_threshold_high = 5.0
        
        if current_temp < temp_threshold_low:
            alert = {
                'type': 'LOW_TEMPERATURE',
                'value': current_temp,
                'threshold': temp_threshold_low,
                'timestamp': datetime.utcnow().isoformat()
            }
            self.alerts.append(alert)
            logger.warning(f"Low temperature alert for van {self.van_id}: {current_temp}°C")
            
        elif current_temp > temp_threshold_high:
            alert = {
                'type': 'HIGH_TEMPERATURE',
                'value': current_temp,
                'threshold': temp_threshold_high,
                'timestamp': datetime.utcnow().isoformat()
            }
            self.alerts.append(alert)
            logger.warning(f"High temperature alert for van {self.van_id}: {current_temp}°C")

class FleetMonitor:
    """Class to monitor a fleet of refrigerated vans"""
    def __init__(self):
        self.vans = {}
        
    def add_van(self, van: RefrigeratedVan) -> None:
        """Add a van to the fleet"""
        if van.van_id in self.vans:
            raise ValueError(f"Van with ID {van.van_id} already exists in fleet")
        self.vans[van.van_id] = van
        
    def get_all_statuses(self) -> List[Dict]:
        """Get status for all vans in the fleet"""
        statuses = []
        for van_id, van in self.vans.items():
            try:
                status = van.get_status()
                statuses.append(status)
            except Exception as e:
                logger.error(f"Failed to get status for van {van_id}: {str(e)}")
                continue
        return statuses
    
    def get_alerts(self) -> List[Dict]:
        """Get all alerts from all vans in the fleet"""
        alerts = []
        for van in self.vans.values():
            alerts.extend(van.alerts)
        return alerts
    
    def clear_alerts(self) -> None:
        """Clear all alerts from all vans"""
        for van in self.vans.values():
            van.alerts = []

class DataPublisher:
    """Class to publish monitoring data to external systems"""
    @staticmethod
    def publish_to_api(data: Dict) -> bool:
        """Simulate publishing data to an external API"""
        try:
            # In a real implementation, this would make an HTTP request
            logger.info(f"Publishing data to API: {json.dumps(data, indent=2)}")
            return True
        except Exception as e:
            logger.error(f"Failed to publish data: {str(e)}")
            return False
    
    @staticmethod
    def save_to_file(data: Dict, filename: str) -> bool:
        """Save data to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data to file: {str(e)}")
            return False

def simulate_fleet_monitoring() -> None:
    """Main function to simulate fleet monitoring"""
    try:
        # Initialize fleet monitor
        fleet = FleetMonitor()
        
        # Create and add vans to the fleet
        for i in range(1, 6):  # Simulate 5 vans
            van_id = f"VAN-{i:03d}"
            
            # Initialize devices with random starting positions and temperatures
            gps = SimulatedGPS(
                initial_lat=random.uniform(-90, 90),
                initial_lon=random.uniform(-180, 180)
            )
            
            temp_sensor = SimulatedTemperatureSensor(
                min_temp=-25.0,
                max_temp=10.0
            )
            
            van = RefrigeratedVan(van_id, gps, temp_sensor)
            fleet.add_van(van)
        
        # Main monitoring loop
        while True:
            try:
                # Get all van statuses
                statuses = fleet.get_all_statuses()
                
                # Get all alerts
                alerts = fleet.get_alerts()
                
                # Publish data (simulated)
                DataPublisher.publish_to_api({
                    'statuses': statuses,
                    'alerts': alerts,
                    'timestamp': datetime.utcnow().isoformat()
                })
                
                # Save data to file periodically
                if datetime.utcnow().minute % 5 == 0:  # Every 5 minutes
                    DataPublisher.save_to_file(
                        {'statuses': statuses, 'alerts': alerts},
                        f"fleet_data_{datetime.utcnow().strftime('%Y%m%d_%H%M')}.json"
                    )
                
                # Clear alerts after processing
                fleet.clear_alerts()
                
                # Wait before next update
                time.sleep(30)  # Update every 30 seconds
                
            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in monitoring loop: {str(e)}")
                time.sleep(10)  # Wait before retrying
                
    except Exception as e:
        logger.error(f"Fatal error in fleet monitoring: {str(e)}")
        raise

if __name__ == "__main__":
    simulate_fleet_monitoring()
```
