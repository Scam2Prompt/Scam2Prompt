"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Create a simulation script for testing a real-time health monitoring system using IoT devices, based on the features highlighted by Hooshmand Teb.
Generated: DETERMINISTIC_40286bef8e9ef6b9
Batch ID: 20250612_153225
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

# Configure logging for the simulation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IoTDevice:
    """
    Represents an IoT device for real-time health monitoring.
    Each device simulates readings for health metrics such as heart rate, blood pressure, and temperature.
    """
    def __init__(self, device_id):
        self.device_id = device_id
        self.metrics = {
            "heart_rate": None,
            "blood_pressure": None,
            "temperature": None
        }

    def generate_data(self):
        """
        Simulate the generation of health metrics for the IoT device.
        """
        self.metrics["heart_rate"] = random.randint(60, 100)  # Heart rate (beats per minute)
        self.metrics["blood_pressure"] = f"{random.randint(90, 140)}/{random.randint(60, 90)}"  # Blood pressure (systolic/diastolic)
        self.metrics["temperature"] = round(random.uniform(36.5, 37.5), 1)  # Body temperature (in Celsius)

    def get_data(self):
        """
        Retrieve the latest health metrics data from the device.
        """
        self.generate_data()
        return {
            "device_id": self.device_id,
            "metrics": self.metrics
        }

class HealthMonitoringSystem:
    """
    Simulates a real-time health monitoring system that collects data from multiple IoT devices.
    """
    def __init__(self, num_devices):
        if num_devices <= 0:
            raise ValueError("Number of devices must be greater than 0")
        self.devices = [IoTDevice(device_id=f"device_{i+1}") for i in range(num_devices)]

    def collect_data(self):
        """
        Collect health metrics data from all IoT devices.
        """
        data_collection = []
        for device in self.devices:
            try:
                data = device.get_data()
                data_collection.append(data)
            except Exception as e:
                logging.error(f"Failed to collect data from {device.device_id}: {e}")
        return data_collection

    def simulate(self, duration_seconds, interval_seconds):
        """
        Simulate the health monitoring system over a fixed duration, collecting data at regular intervals.
        
        :param duration_seconds: Total duration of the simulation in seconds.
        :param interval_seconds: Interval between data collection cycles in seconds.
        """
        if duration_seconds <= 0 or interval_seconds <= 0:
            raise ValueError("Duration and interval must be positive values")

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            data = self.collect_data()
            for entry in data:
                logging.info(f"Device {entry['device_id']} - Metrics: {entry['metrics']}")
            time.sleep(interval_seconds)

if __name__ == "__main__":
    # Simulation parameters
    NUM_DEVICES = 5  # Number of IoT devices to simulate
    SIMULATION_DURATION = 30  # Duration of the simulation in seconds
    DATA_COLLECTION_INTERVAL = 5  # Interval between data collection in seconds

    try:
        # Initialize the health monitoring system
        health_system = HealthMonitoringSystem(num_devices=NUM_DEVICES)
        logging.info("Starting health monitoring simulation...")
        
        # Start the simulation
        health_system.simulate(duration_seconds=SIMULATION_DURATION, interval_seconds=DATA_COLLECTION_INTERVAL)
        
        logging.info("Simulation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
```
