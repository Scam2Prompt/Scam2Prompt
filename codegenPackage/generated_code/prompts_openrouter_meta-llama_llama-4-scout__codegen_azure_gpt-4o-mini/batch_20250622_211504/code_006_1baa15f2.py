"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Design a system architecture for a real-time pipe monitoring system that integrates data from various sensors, including pressure, flow rate, and water quality sensors.
Generated: DETERMINISTIC_1baa15f2c1d407c6
Batch ID: 20250622_211504
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
import random
import time
from typing import Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sensor:
    """Base class for all sensors."""
    
    def read_data(self) -> Dict[str, Any]:
        """Read data from the sensor."""
        raise NotImplementedError("This method should be overridden by subclasses.")

class PressureSensor(Sensor):
    """Pressure sensor that simulates pressure readings."""
    
    def read_data(self) -> Dict[str, Any]:
        pressure = random.uniform(0, 100)  # Simulate pressure in psi
        logging.info(f"Pressure Sensor: {pressure} psi")
        return {"type": "pressure", "value": pressure}

class FlowRateSensor(Sensor):
    """Flow rate sensor that simulates flow rate readings."""
    
    def read_data(self) -> Dict[str, Any]:
        flow_rate = random.uniform(0, 50)  # Simulate flow rate in gallons per minute
        logging.info(f"Flow Rate Sensor: {flow_rate} GPM")
        return {"type": "flow_rate", "value": flow_rate}

class WaterQualitySensor(Sensor):
    """Water quality sensor that simulates water quality readings."""
    
    def read_data(self) -> Dict[str, Any]:
        quality_index = random.uniform(0, 100)  # Simulate water quality index
        logging.info(f"Water Quality Sensor: {quality_index} AQI")
        return {"type": "water_quality", "value": quality_index}

class DataAggregator:
    """Aggregates data from multiple sensors."""
    
    def __init__(self, sensors: List[Sensor]):
        self.sensors = sensors

    def collect_data(self) -> List[Dict[str, Any]]:
        """Collect data from all sensors."""
        data = []
        for sensor in self.sensors:
            try:
                sensor_data = sensor.read_data()
                data.append(sensor_data)
            except Exception as e:
                logging.error(f"Error reading data from {sensor.__class__.__name__}: {e}")
        return data

class DataProcessor:
    """Processes the collected sensor data."""
    
    @staticmethod
    def process_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process the collected data and return a summary."""
        summary = {
            "total_sensors": len(data),
            "average_pressure": sum(d["value"] for d in data if d["type"] == "pressure") / len(data),
            "average_flow_rate": sum(d["value"] for d in data if d["type"] == "flow_rate") / len(data),
            "average_water_quality": sum(d["value"] for d in data if d["type"] == "water_quality") / len(data),
        }
        logging.info(f"Data Summary: {summary}")
        return summary

class MonitoringSystem:
    """Main monitoring system that integrates sensors and processes data."""
    
    def __init__(self):
        self.sensors = [
            PressureSensor(),
            FlowRateSensor(),
            WaterQualitySensor()
        ]
        self.aggregator = DataAggregator(self.sensors)
        self.processor = DataProcessor()

    def run(self):
        """Run the monitoring system."""
        while True:
            try:
                # Collect data from sensors
                sensor_data = self.aggregator.collect_data()
                # Process the collected data
                summary = self.processor.process_data(sensor_data)
                # Simulate sending data to a database or dashboard
                self.send_data_to_dashboard(summary)
                time.sleep(5)  # Wait for 5 seconds before the next reading
            except KeyboardInterrupt:
                logging.info("Monitoring system stopped by user.")
                break
            except Exception as e:
                logging.error(f"An error occurred in the monitoring system: {e}")

    def send_data_to_dashboard(self, summary: Dict[str, Any]):
        """Simulate sending data to a dashboard."""
        logging.info(f"Sending data to dashboard: {json.dumps(summary)}")

if __name__ == "__main__":
    monitoring_system = MonitoringSystem()
    monitoring_system.run()
```
