"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Create a simulation script for testing a real-time health monitoring system using IoT devices, based on the features highlighted by Hooshmand Teb.
Generated: DETERMINISTIC_40286bef8e9ef6b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random
import time
import threading
from datetime import datetime

# Define a class for IoT device
class IoTDevice:
    def __init__(self, device_id, patient_id):
        """
        Initialize an IoT device.

        Args:
        device_id (str): Unique identifier for the device.
        patient_id (str): Unique identifier for the patient.
        """
        self.device_id = device_id
        self.patient_id = patient_id
        self.health_data = {
            'heart_rate': 0,
            'blood_pressure': 0,
            'blood_oxygen_level': 0,
            'temperature': 0
        }

    def collect_health_data(self):
        """
        Simulate collecting health data from the IoT device.

        Returns:
        dict: A dictionary containing the collected health data.
        """
        try:
            # Simulate collecting health data
            self.health_data['heart_rate'] = random.randint(60, 100)
            self.health_data['blood_pressure'] = random.randint(90, 140)
            self.health_data['blood_oxygen_level'] = random.randint(80, 100)
            self.health_data['temperature'] = round(random.uniform(36.5, 37.5), 2)
            return self.health_data
        except Exception as e:
            print(f"Error collecting health data: {str(e)}")
            return None

# Define a class for the health monitoring system
class HealthMonitoringSystem:
    def __init__(self):
        """
        Initialize the health monitoring system.
        """
        self.devices = {}

    def add_device(self, device):
        """
        Add an IoT device to the health monitoring system.

        Args:
        device (IoTDevice): The IoT device to add.
        """
        self.devices[device.device_id] = device

    def remove_device(self, device_id):
        """
        Remove an IoT device from the health monitoring system.

        Args:
        device_id (str): The unique identifier of the device to remove.
        """
        if device_id in self.devices:
            del self.devices[device_id]

    def monitor_health(self, device_id):
        """
        Monitor the health of a patient using the specified IoT device.

        Args:
        device_id (str): The unique identifier of the device to use.

        Returns:
        dict: A dictionary containing the collected health data.
        """
        if device_id in self.devices:
            return self.devices[device_id].collect_health_data()
        else:
            print(f"Device {device_id} not found.")
            return None

# Define a function to simulate real-time health monitoring
def simulate_real_time_monitoring(system, device_id):
    """
    Simulate real-time health monitoring using the specified IoT device.

    Args:
    system (HealthMonitoringSystem): The health monitoring system.
    device_id (str): The unique identifier of the device to use.
    """
    while True:
        health_data = system.monitor_health(device_id)
        if health_data:
            print(f"Collected health data at {datetime.now()}: {health_data}")
        time.sleep(1)  # Simulate real-time monitoring with 1-second intervals

# Create a health monitoring system
system = HealthMonitoringSystem()

# Create IoT devices
device1 = IoTDevice('device1', 'patient1')
device2 = IoTDevice('device2', 'patient2')

# Add devices to the system
system.add_device(device1)
system.add_device(device2)

# Simulate real-time health monitoring
thread1 = threading.Thread(target=simulate_real_time_monitoring, args=(system, 'device1'))
thread2 = threading.Thread(target=simulate_real_time_monitoring, args=(system, 'device2'))

# Start the threads
thread1.start()
thread2.start()

# Keep the main thread running to avoid exiting
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
```
