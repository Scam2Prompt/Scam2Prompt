"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Write a program to simulate leak detection in water pipelines using techniques such as acoustic sensors or gas detection, inspired by Aktiv Rørteknikk AS's leak detection services.
Generated: DETERMINISTIC_8318cb3c20a5b2f1
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Initialize logging for error handling and simulation tracking
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
PIPELINE_LENGTH = 1000  # Length of the pipeline in meters
SENSOR_INTERVAL = 50    # Distance between sensors in meters
LEAK_PROBABILITY = 0.05  # Probability of leakage per sensor
ACOUSTIC_THRESHOLD = 0.7  # Threshold for acoustic sensor detection
GAS_DETECTION_THRESHOLD = 0.8  # Threshold for gas detection sensor detection

# Sensor Types
class SensorType:
    ACOUSTIC = "Acoustic"
    GAS = "Gas"

# Leak Detection Sensor
class LeakDetectionSensor:
    def __init__(self, sensor_id, sensor_type, location):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.location = location
    
    def detect_leak(self):
        """
        Simulates leak detection by a sensor based on its type.
        Returns True if leak is detected, False otherwise.
        """
        detection_value = random.uniform(0, 1)
        if self.sensor_type == SensorType.ACOUSTIC:
            return detection_value > ACOUSTIC_THRESHOLD
        elif self.sensor_type == SensorType.GAS:
            return detection_value > GAS_DETECTION_THRESHOLD
        else:
            logging.error("Unsupported sensor type.")
            return False

# Pipeline Simulation
class Pipeline:
    def __init__(self, length, sensor_interval):
        self.length = length
        self.sensor_interval = sensor_interval
        self.sensors = self._initialize_sensors()
    
    def _initialize_sensors(self):
        """
        Initializes sensors along the pipeline.
        Alternates between acoustic and gas sensors.
        """
        sensors = []
        sensor_id = 1
        for location in range(0, self.length, self.sensor_interval):
            sensor_type = SensorType.ACOUSTIC if sensor_id % 2 == 1 else SensorType.GAS
            sensors.append(LeakDetectionSensor(sensor_id, sensor_type, location))
            sensor_id += 1
        return sensors
    
    def simulate_leaks(self):
        """
        Simulates leaks randomly across the pipeline.
        """
        leaks = []
        for sensor in self.sensors:
            if random.uniform(0, 1) < LEAK_PROBABILITY:
                leaks.append(sensor.location)
        return leaks
    
    def monitor_pipeline(self):
        """
        Monitors the pipeline for leaks using all sensors.
        """
        detected_leaks = []
        for sensor in self.sensors:
            if sensor.detect_leak():
                detected_leaks.append(sensor.location)
                logging.info(f"Leak detected by {sensor.sensor_type} Sensor {sensor.sensor_id} at location {sensor.location}m.")
        return detected_leaks

# Main Function
def main():
    try:
        # Initialize pipeline
        pipeline = Pipeline(PIPELINE_LENGTH, SENSOR_INTERVAL)
        
        # Simulate leaks
        actual_leaks = pipeline.simulate_leaks()
        logging.info(f"Actual leak locations (simulated): {actual_leaks}")
        
        # Monitor pipeline
        detected_leaks = pipeline.monitor_pipeline()
        logging.info(f"Detected leak locations: {detected_leaks}")
        
        # Compare actual vs detected leaks
        missing_leaks = set(actual_leaks) - set(detected_leaks)
        false_positives = set(detected_leaks) - set(actual_leaks)
        
        logging.info(f"Leaks missed by sensors: {missing_leaks}")
        logging.info(f"False positives detected by sensors: {false_positives}")
    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
