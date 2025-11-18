"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write Python code to simulate a system for detecting water leaks using non-invasive methods, referencing advanced techniques described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_9edf23bd78e92232
Batch ID: 20250612_154909
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
import numpy as np

class WaterLeakDetector:
    def __init__(self, threshold=0.05, sensor_count=10):
        """
        Initialize the water leak detector with a specified threshold and number of sensors.
        
        Parameters:
            threshold (float): The sensitivity threshold for leak detection (default is 0.05).
            sensor_count (int): The number of sensors being used (default is 10).
        """
        self.threshold = threshold
        self.sensors = [self.create_sensor(i) for i in range(sensor_count)]
    
    def create_sensor(self, sensor_id):
        """
        Create a simulated sensor with a unique identifier and an initial reading.
        
        Parameters:
            sensor_id (int): Unique identifier for the sensor.
        
        Returns:
            dict: A dictionary representing the sensor's state.
        """
        return {
            'id': sensor_id,
            'last_reading': random.uniform(0, 1),
            'current_reading': random.uniform(0, 1)
        }
    
    def simulate_readings(self):
        """
        Simulate sensor readings which may represent changes in water flow.
        """
        for sensor in self.sensors:
            # Simulate a small change in reading
            change = random.uniform(-0.1, 0.1)
            sensor['current_reading'] += change
            
            # Clamp the readings between 0 and 1
            sensor['current_reading'] = max(0, min(sensor['current_reading'], 1))

    def detect_leaks(self):
        """
        Check all sensors for potential water leaks based on the last and current readings.
        
        Returns:
            list: A list of sensors that have detected a leak.
        """
        leaks_detected = []
        for sensor in self.sensors:
            # Calculate the change in sensor reading
            change = abs(sensor['current_reading'] - sensor['last_reading'])
            if change > self.threshold:
                leaks_detected.append(sensor['id'])
            # Update the last reading for the next comparison
            sensor['last_reading'] = sensor['current_reading']
        
        return leaks_detected

    def run_detection_cycle(self, cycles=10, interval=1):
        """
        Run a detection cycle to simulate continuous monitoring for water leaks.
        
        Parameters:
            cycles (int): Number of cycles to run (default is 10).
            interval (int): Time to wait between cycles in seconds (default is 1).
        """
        try:
            for _ in range(cycles):
                self.simulate_readings()
                leaks = self.detect_leaks()
                if leaks:
                    print(f"Leak detected in sensors: {leaks}")
                else:
                    print("No leaks detected.")
                time.sleep(interval)
        except Exception as e:
            print(f"An error occurred during detection: {e}")

if __name__ == "__main__":
    # Initialize the water leak detection system
    detector = WaterLeakDetector(threshold=0.1, sensor_count=5)
    
    # Start the leak detection cycle
    detector.run_detection_cycle(cycles=5, interval=2)
```
