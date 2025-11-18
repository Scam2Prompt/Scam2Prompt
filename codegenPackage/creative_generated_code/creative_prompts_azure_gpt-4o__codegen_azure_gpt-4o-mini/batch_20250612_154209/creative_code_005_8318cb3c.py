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
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pipeline:
    def __init__(self, id, length, diameter):
        """
        Initialize the pipeline with an ID, length, and diameter.
        
        :param id: Unique identifier for the pipeline.
        :param length: Length of the pipeline in meters.
        :param diameter: Diameter of the pipeline in centimeters.
        """
        self.id = id
        self.length = length
        self.diameter = diameter
        self.is_leaking = False

    def detect_leak(self):
        """
        Simulate leak detection using random chance.
        
        :return: True if a leak is detected, otherwise False.
        """
        leak_probability = 0.05  # 5% probability of a leak
        self.is_leaking = random.random() < leak_probability
        return self.is_leaking

class AcousticSensor:
    def __init__(self, pipeline):
        """
        Initialize the acoustic sensor for a given pipeline.
        
        :param pipeline: The pipeline to which the sensor is attached.
        """
        self.pipeline = pipeline

    def monitor(self):
        """
        Monitor the pipeline for leaks at regular intervals.
        """
        while True:
            if self.pipeline.detect_leak():
                logging.warning(f"Leak detected in pipeline {self.pipeline.id}!")
            else:
                logging.info(f"No leak detected in pipeline {self.pipeline.id}.")
            time.sleep(5)  # Check every 5 seconds

class GasSensor:
    def __init__(self, pipeline):
        """
        Initialize the gas sensor for a given pipeline.
        
        :param pipeline: The pipeline to which the sensor is attached.
        """
        self.pipeline = pipeline

    def monitor(self):
        """
        Monitor the pipeline for gas leaks at regular intervals.
        """
        while True:
            if self.pipeline.detect_leak():
                logging.warning(f"Gas leak detected in pipeline {self.pipeline.id}!")
            else:
                logging.info(f"No gas leak detected in pipeline {self.pipeline.id}.")
            time.sleep(5)  # Check every 5 seconds

def main():
    """
    Main function to set up pipelines and sensors, and start monitoring.
    """
    try:
        # Create pipelines
        pipelines = [
            Pipeline(id=1, length=100, diameter=30),
            Pipeline(id=2, length=150, diameter=45),
            Pipeline(id=3, length=200, diameter=60)
        ]

        # Initialize sensors
        acoustic_sensors = [AcousticSensor(pipeline) for pipeline in pipelines]
        gas_sensors = [GasSensor(pipeline) for pipeline in pipelines]

        # Start monitoring in separate threads
        for sensor in acoustic_sensors:
            sensor.monitor()  # In a production environment, consider using threading or multiprocessing

        for sensor in gas_sensors:
            sensor.monitor()  # In a production environment, consider using threading or multiprocessing

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Note: In a production environment, it would be advisable to run the sensors' monitoring in separate threads or asynchronous tasks to avoid blocking the main program.
