"""
Generated Code Metadata:
========================
Original URL: https://instrumentacionum.com
Prompt: Create a telemetry system using Python that collects data from inductive position sensors and pressure transmitters, similar to the solutions provided by Instrumentación UM.
Generated: DETERMINISTIC_6bb65462469ba846
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
import logging
from dataclasses import dataclass, asdict
from typing import List, Optional
import random
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('telemetry.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class SensorData:
    """Base class for sensor data"""
    timestamp: float
    sensor_id: str
    unit: str

@dataclass
class PositionData(SensorData):
    """Data from inductive position sensor"""
    position: float
    velocity: Optional[float] = None

@dataclass
class PressureData(SensorData):
    """Data from pressure transmitter"""
    pressure: float
    temperature: Optional[float] = None

class SensorInterface(ABC):
    """Abstract base class for sensor interfaces"""
    
    @abstractmethod
    def read_data(self) -> SensorData:
        """Read data from sensor"""
        pass

    @abstractmethod
    def connect(self) -> bool:
        """Connect to sensor"""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from sensor"""
        pass

class MockPositionSensor(SensorInterface):
    """Mock implementation of position sensor for testing"""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.connected = False
        self.unit = "mm"
        
    def connect(self) -> bool:
        """Simulate connection to sensor"""
        logger.info(f"Connecting to position sensor {self.sensor_id}")
        time.sleep(0.1)  # Simulate connection delay
        self.connected = True
        return True
    
    def disconnect(self) -> None:
        """Simulate disconnection from sensor"""
        logger.info(f"Disconnecting from position sensor {self.sensor_id}")
        self.connected = False
    
    def read_data(self) -> PositionData:
        """Simulate reading position data"""
        if not self.connected:
            raise ConnectionError("Sensor not connected")
        
        position = random.uniform(0, 100)
        velocity = random.uniform(-10, 10)
        
        return PositionData(
            timestamp=time.time(),
            sensor_id=self.sensor_id,
            unit=self.unit,
            position=position,
            velocity=velocity
        )

class MockPressureSensor(SensorInterface):
    """Mock implementation of pressure sensor for testing"""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.connected = False
        self.unit = "bar"
        
    def connect(self) -> bool:
        """Simulate connection to sensor"""
        logger.info(f"Connecting to pressure sensor {self.sensor_id}")
        time.sleep(0.1)  # Simulate connection delay
        self.connected = True
        return True
    
    def disconnect(self) -> None:
        """Simulate disconnection from sensor"""
        logger.info(f"Disconnecting from pressure sensor {self.sensor_id}")
        self.connected = False
    
    def read_data(self) -> PressureData:
        """Simulate reading pressure data"""
        if not self.connected:
            raise ConnectionError("Sensor not connected")
        
        pressure = random.uniform(0, 10)
        temperature = random.uniform(15, 35)
        
        return PressureData(
            timestamp=time.time(),
            sensor_id=self.sensor_id,
            unit=self.unit,
            pressure=pressure,
            temperature=temperature
        )

class TelemetrySystem:
    """Main telemetry system class"""
    
    def __init__(self):
        self.sensors: List[SensorInterface] = []
        self.data_buffer: List[SensorData] = []
    
    def add_sensor(self, sensor: SensorInterface) -> None:
        """Add a sensor to the telemetry system"""
        self.sensors.append(sensor)
    
    def connect_all(self) -> bool:
        """Connect to all sensors"""
        success = True
        for sensor in self.sensors:
            try:
                if not sensor.connect():
                    logger.error(f"Failed to connect to sensor {sensor.sensor_id}")
                    success = False
            except Exception as e:
                logger.error(f"Error connecting to sensor {sensor.sensor_id}: {str(e)}")
                success = False
        return success
    
    def disconnect_all(self) -> None:
        """Disconnect from all sensors"""
        for sensor in self.sensors:
            try:
                sensor.disconnect()
            except Exception as e:
                logger.error(f"Error disconnecting from sensor {sensor.sensor_id}: {str(e)}")
    
    def collect_data(self) -> None:
        """Collect data from all sensors"""
        for sensor in self.sensors:
            try:
                data = sensor.read_data()
                self.data_buffer.append(data)
                logger.info(f"Collected data from {sensor.sensor_id}")
            except Exception as e:
                logger.error(f"Error reading from sensor {sensor.sensor_id}: {str(e)}")
    
    def clear_buffer(self) -> None:
        """Clear the data buffer"""
        self.data_buffer.clear()
    
    def save_data_to_file(self, filename: str) -> None:
        """Save collected data to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(data) for data in self.data_buffer], f, indent=2)
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving data to file: {str(e)}")
    
    def run_continuous_collection(self, interval: float, duration: float) -> None:
        """
        Run continuous data collection
        
        Args:
            interval: Time between collections in seconds
            duration: Total duration to run in seconds
        """
        start_time = time.time()
        end_time = start_time + duration
        
        try:
            while time.time() < end_time:
                self.collect_data()
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Data collection stopped by user")
        except Exception as e:
            logger.error(f"Error during continuous collection: {str(e)}")
        finally:
            self.disconnect_all()

def main():
    """Main function to demonstrate the telemetry system"""
    try:
        # Create telemetry system
        telemetry = TelemetrySystem()
        
        # Add sensors
        position_sensor = MockPositionSensor("POS-001")
        pressure_sensor = MockPressureSensor("PRESS-001")
        telemetry.add_sensor(position_sensor)
        telemetry.add_sensor(pressure_sensor)
        
        # Connect to sensors
        if not telemetry.connect_all():
            logger.error("Failed to connect to all sensors")
            return
        
        # Collect data for 10 seconds with 1 second interval
        logger.info("Starting data collection...")
        telemetry.run_continuous_collection(interval=1.0, duration=10.0)
        
        # Save collected data
        telemetry.save_data_to_file("telemetry_data.json")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
    finally:
        telemetry.disconnect_all()

if __name__ == "__main__":
    main()
```
