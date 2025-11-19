"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a program to simulate leak detection in water pipelines using techniques such as acoustic sensors or gas detection, inspired by Aktiv Rørteknikk AS's leak detection services.
Generated: DETERMINISTIC_8318cb3c20a5b2f1
Batch ID: 20250612_154209
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pipeline:
    def __init__(self, id, length, leak_probability):
        """
        Initialize a pipeline with an ID, length, and leak probability.

        :param id: Unique identifier for the pipeline
        :param length: Length of the pipeline in meters
        :param leak_probability: Probability of a leak occurring (0 to 1)
        """
        self.id = id
        self.length = length
        self.leak_probability = leak_probability
        self.is_leaking = False

    def check_for_leak(self):
        """
        Simulate a leak detection check using a random number generator.
        If a randomly generated number is less than the leak probability,
        a leak is detected.
        """
        if random.random() < self.leak_probability:
            self.is_leaking = True
            logging.warning(f"Leak detected in pipeline {self.id}!")
        else:
            self.is_leaking = False
            logging.info(f"No leak detected in pipeline {self.id}.")

class LeakDetectionSystem:
    def __init__(self):
        """
        Initialize the leak detection system with an empty list of pipelines.
        """
        self.pipelines = []

    def add_pipeline(self, pipeline):
        """
        Add a pipeline to the leak detection system.

        :param pipeline: An instance of the Pipeline class
        """
        self.pipelines.append(pipeline)
        logging.info(f"Pipeline {pipeline.id} added to the system.")

    def monitor_pipelines(self):
        """
        Monitor all pipelines for leaks at regular intervals.
        """
        try:
            while True:
                for pipeline in self.pipelines:
                    pipeline.check_for_leak()
                time.sleep(5)  # Check every 5 seconds
        except KeyboardInterrupt:
            logging.info("Leak detection monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Create a leak detection system
    leak_detection_system = LeakDetectionSystem()

    # Add pipelines to the system
    leak_detection_system.add_pipeline(Pipeline(id=1, length=100, leak_probability=0.1))
    leak_detection_system.add_pipeline(Pipeline(id=2, length=150, leak_probability=0.05))
    leak_detection_system.add_pipeline(Pipeline(id=3, length=200, leak_probability=0.2))

    # Start monitoring the pipelines for leaks
    leak_detection_system.monitor_pipelines()
```
