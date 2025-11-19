"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Provide an example of a decision-making system that integrates multimodal sensor data (e.g., optical cameras, thermal cameras, and microwave barriers) for security and surveillance applications, as described in the Metis Project.
Generated: DETERMINISTIC_ca48d454a9237641
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
import time
from abc import ABC, abstractmethod
import json
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SensorData:
    """Base class for sensor data."""
    timestamp: float
    sensor_id: str
    data: np.ndarray

@dataclass
class OpticalCameraData(SensorData):
    """Optical camera data with RGB channels."""
    resolution: Tuple[int, int]
    color_space: str = "RGB"

@dataclass
class ThermalCameraData(SensorData):
    """Thermal camera data with temperature readings."""
    temperature_range: Tuple[float, float]
    unit: str = "Celsius"

@dataclass
class MicrowaveBarrierData(SensorData):
    """Microwave barrier data with signal strength."""
    signal_strength: float
    frequency: float

class SensorInterface(ABC):
    """Abstract base class for sensor interfaces."""
    
    @abstractmethod
    def read_data(self) -> SensorData:
        """Read data from the sensor."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if sensor is available."""
        pass

class OpticalCamera(SensorInterface):
    """Optical camera implementation."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.resolution = (1920, 1080)
    
    def read_data(self) -> OpticalCameraData:
        """Simulate reading optical camera data."""
        try:
            # Simulate RGB image data
            data = np.random.randint(
                0, 256, 
                size=(self.resolution[1], self.resolution[0], 3), 
                dtype=np.uint8
            )
            return OpticalCameraData(
                timestamp=time.time(),
                sensor_id=self.sensor_id,
                data=data,
                resolution=self.resolution
            )
        except Exception as e:
            logger.error(f"Error reading optical camera data: {e}")
            raise
    
    def is_available(self) -> bool:
        """Simulate sensor availability check."""
        return True

class ThermalCamera(SensorInterface):
    """Thermal camera implementation."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.temperature_range = (-20.0, 100.0)
    
    def read_data(self) -> ThermalCameraData:
        """Simulate reading thermal camera data."""
        try:
            # Simulate thermal image data
            data = np.random.uniform(
                self.temperature_range[0],
                self.temperature_range[1],
                size=(480, 640)
            )
            return ThermalCameraData(
                timestamp=time.time(),
                sensor_id=self.sensor_id,
                data=data,
                temperature_range=self.temperature_range
            )
        except Exception as e:
            logger.error(f"Error reading thermal camera data: {e}")
            raise
    
    def is_available(self) -> bool:
        """Simulate sensor availability check."""
        return True

class MicrowaveBarrier(SensorInterface):
    """Microwave barrier implementation."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.frequency = 24.125  # GHz
    
    def read_data(self) -> MicrowaveBarrierData:
        """Simulate reading microwave barrier data."""
        try:
            # Simulate signal strength
            signal_strength = np.random.uniform(0.0, 1.0)
            return MicrowaveBarrierData(
                timestamp=time.time(),
                sensor_id=self.sensor_id,
                data=np.array([signal_strength]),
                signal_strength=signal_strength,
                frequency=self.frequency
            )
        except Exception as e:
            logger.error(f"Error reading microwave barrier data: {e}")
            raise
    
    def is_available(self) -> bool:
        """Simulate sensor availability check."""
        return True

class DataFusionEngine:
    """Core engine for fusing multimodal sensor data."""
    
    def __init__(self):
        self.sensors: Dict[str, SensorInterface] = {}
    
    def add_sensor(self, sensor: SensorInterface) -> None:
        """Register a sensor with the fusion engine."""
        self.sensors[sensor.sensor_id] = sensor
    
    def collect_data(self) -> Dict[str, SensorData]:
        """Collect data from all registered sensors."""
        sensor_data = {}
        for sensor_id, sensor in self.sensors.items():
            try:
                if sensor.is_available():
                    sensor_data[sensor_id] = sensor.read_data()
                else:
                    logger.warning(f"Sensor {sensor_id} is not available")
            except Exception as e:
                logger.error(f"Failed to collect data from {sensor_id}: {e}")
        return sensor_data
    
    def fuse_data(self, sensor_data: Dict[str, SensorData]) -> Dict:
        """Fuse data from multiple sensors and make decisions."""
        try:
            # Initialize fusion result
            fusion_result = {
                "timestamp": time.time(),
                "sensors": {},
                "alerts": [],
                "confidence": 0.0
            }
            
            # Process each sensor's data
            for sensor_id, data in sensor_data.items():
                fusion_result["sensors"][sensor_id] = {
                    "type": data.__class__.__name__,
                    "timestamp": data.timestamp
                }
                
                # Example fusion logic
                if isinstance(data, OpticalCameraData):
                    # Simple motion detection (for demonstration)
                    if np.mean(data.data) > 150:
                        fusion_result["alerts"].append(
                            f"Motion detected by {sensor_id}"
                        )
                
                elif isinstance(data, ThermalCameraData):
                    # Heat signature detection
                    if np.max(data.data) > 50.0:  # Threshold in Celsius
                        fusion_result["alerts"].append(
                            f"Heat signature detected by {sensor_id}"
                        )
                
                elif isinstance(data, MicrowaveBarrierData):
                    # Barrier breach detection
                    if data.signal_strength < 0.3:
                        fusion_result["alerts"].append(
                            f"Barrier breach detected by {sensor_id}"
                        )
            
            # Calculate overall confidence
            if fusion_result["alerts"]:
                fusion_result["confidence"] = min(
                    1.0, len(fusion_result["alerts"]) * 0.4
                )
            
            return fusion_result
        
        except Exception as e:
            logger.error(f"Data fusion failed: {e}")
            raise

class DecisionSystem:
    """Main decision-making system for security applications."""
    
    def __init__(self):
        self.fusion_engine = DataFusionEngine()
        self.alert_history = []
    
    def initialize_sensors(self) -> None:
        """Initialize all sensors."""
        try:
            # Add example sensors
            self.fusion_engine.add_sensor(OpticalCamera("optical_cam_1"))
            self.fusion_engine.add_sensor(ThermalCamera("thermal_cam_1"))
            self.fusion_engine.add_sensor(MicrowaveBarrier("microwave_barrier_1"))
            logger.info("Sensors initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize sensors: {e}")
            raise
    
    def run_cycle(self) -> Dict:
        """Run one cycle of data collection and decision-making."""
        try:
            # Collect data from all sensors
            sensor_data = self.fusion_engine.collect_data()
            
            # Fuse data and make decisions
            fusion_result = self.fusion_engine.fuse_data(sensor_data)
            
            # Log and store alerts
            if fusion_result["alerts"]:
                self.alert_history.extend(fusion_result["alerts"])
                for alert in fusion_result["alerts"]:
                    logger.warning(f"ALERT: {alert}")
            
            return fusion_result
        
        except Exception as e:
            logger.error(f"Decision cycle failed: {e}")
            raise
    
    def get_alert_history(self) -> List[str]:
        """Get the history of alerts."""
        return self.alert_history

def main():
    """Main function to demonstrate the decision system."""
    try:
        # Initialize the decision system
        decision_system = DecisionSystem()
        decision_system.initialize_sensors()
        
        # Run several cycles
        for i in range(5):
            logger.info(f"Running decision cycle {i+1}")
            result = decision_system.run_cycle()
            logger.info(f"Cycle result: {json.dumps(result, indent=2)}")
            time.sleep(1)
        
        # Print alert history
        logger.info("Alert history:")
        for alert in decision_system.get_alert_history():
            logger.info(f"- {alert}")
    
    except KeyboardInterrupt:
        logger.info("System shutdown requested")
    except Exception as e:
        logger.error(f"System failure: {e}")

if __name__ == "__main__":
    main()
```
