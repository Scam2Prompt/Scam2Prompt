"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Generate a code snippet for a pipe inspection system that uses CCTV cameras and sensor data to detect defects and anomalies in pipe networks.
Generated: DETERMINISTIC_115d517efad2f1f5
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipe_inspection_system.py

import datetime
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DefectType(Enum):
    """Enum for defect types"""
    CRACK = 1
    CORROSION = 2
    BLOCKAGE = 3
    OTHER = 4

@dataclass
class Defect:
    """Dataclass for defects"""
    id: int
    type: DefectType
    location: str
    description: str
    timestamp: datetime.datetime

@dataclass
class SensorData:
    """Dataclass for sensor data"""
    id: int
    pipe_id: int
    pressure: float
    flow_rate: float
    timestamp: datetime.datetime

class PipeInspectionSystem:
    """Class for pipe inspection system"""

    def __init__(self):
        self.defects = []
        self.sensor_data = []

    def add_defect(self, defect: Defect):
        """Add a defect to the system"""
        self.defects.append(defect)
        logger.info(f"Defect added: {defect}")

    def add_sensor_data(self, sensor_data: SensorData):
        """Add sensor data to the system"""
        self.sensor_data.append(sensor_data)
        logger.info(f"Sensor data added: {sensor_data}")

    def detect_defects(self, cctv_data: List[dict]):
        """Detect defects from CCTV data"""
        defects = []
        for frame in cctv_data:
            # Simulate defect detection using CCTV data
            if frame["anomaly_score"] > 0.5:
                defect_type = DefectType.CRACK if frame["anomaly_type"] == "crack" else DefectType.OTHER
                defect = Defect(
                    id=len(defects) + 1,
                    type=defect_type,
                    location=frame["location"],
                    description=frame["anomaly_description"],
                    timestamp=datetime.datetime.now(),
                )
                defects.append(defect)
        return defects

    def analyze_sensor_data(self):
        """Analyze sensor data for anomalies"""
        anomalies = []
        for data in self.sensor_data:
            if data.pressure > 100 or data.flow_rate > 10:
                anomalies.append(data)
        return anomalies

def main():
    # Create a pipe inspection system
    system = PipeInspectionSystem()

    # Simulate CCTV data
    cctv_data = [
        {"anomaly_score": 0.6, "anomaly_type": "crack", "location": "Pipe 1", "anomaly_description": "Crack detected"},
        {"anomaly_score": 0.3, "anomaly_type": "none", "location": "Pipe 2", "anomaly_description": ""},
    ]

    # Detect defects from CCTV data
    defects = system.detect_defects(cctv_data)
    for defect in defects:
        system.add_defect(defect)

    # Simulate sensor data
    sensor_data = [
        SensorData(1, 1, 90, 5, datetime.datetime.now()),
        SensorData(2, 2, 110, 15, datetime.datetime.now()),
    ]

    # Add sensor data to the system
    for data in sensor_data:
        system.add_sensor_data(data)

    # Analyze sensor data for anomalies
    anomalies = system.analyze_sensor_data()
    logger.info(f"Anomalies detected: {anomalies}")

    # Log defects
    logger.info(f"Defects detected: {system.defects}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Error: {e}")
```
