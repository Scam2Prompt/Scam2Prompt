"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Suggest IoT device configurations and software tools for building a system similar to Hooshmand Teb's SEMS (Smart Emergency Medical System) for real-time health monitoring.
Generated: DETERMINISTIC_70c64ae8c38241ce
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python code snippet that outlines an IoT device configuration and software tools setup for a real-time health monitoring system similar to a Smart Emergency Medical System (SEMS). This example assumes the use of popular libraries for handling IoT device integration, data collection, and real-time monitoring.

```python
import time
import json
import random
import paho.mqtt.client as mqtt
from typing import Dict, Any

# MQTT Broker configuration
BROKER_ADDRESS = "mqtt.example.com"  # Replace with actual broker address
TOPIC = "health_monitoring/data"

# Device configuration
DEVICE_ID = "device_001"  # Unique identifier for the IoT device
SENSOR_TYPES = ["heart_rate", "temperature", "blood_pressure"]
SENSOR_DATA = {
    "heart_rate": (60, 100),  # Normal heart rate range
    "temperature": (36.5, 37.5),  # Normal temperature range
    "blood_pressure": (90, 120)  # Normal systolic range
}

# MQTT Client instance
client = mqtt.Client(DEVICE_ID)

def connect_broker():
    """Connect to the MQTT broker."""
    try:
        client.connect(BROKER_ADDRESS)
        client.loop_start()  # Start the loop to process incoming and outgoing messages
        print(f"{DEVICE_ID} connected to broker at {BROKER_ADDRESS}")
    except Exception as e:
        print(f"Error connecting to MQTT Broker: {e}")

def generate_sensor_data() -> Dict[str, Any]:
    """Generate mock sensor data for health monitoring."""
    data = {}
    for sensor in SENSOR_TYPES:
        lower, upper = SENSOR_DATA[sensor]
        data[sensor] = random.randint(lower, upper)
    
    return data

def publish_sensor_data(data: Dict[str, Any]):
    """Publish the sensor data to the MQTT topic."""
    try:
        message = json.dumps(data)
        client.publish(TOPIC, message)
        print(f"Published data: {message}")
    except Exception as e:
        print(f"Error publishing data: {e}")

def main():
    """Main function to run the health monitoring system."""
    connect_broker()

    try:
        while True:
            sensor_data = generate_sensor_data()
            publish_sensor_data(sensor_data)
            time.sleep(5)  # Adjust the frequency of data collection as needed
    except KeyboardInterrupt:
        print("Stopping the data collection.")
    finally:
        client.loop_stop()  # Stop the loop
        client.disconnect()  # Disconnect from the broker
        print(f"{DEVICE_ID} disconnected from broker.")

if __name__ == "__main__":
    main()
```

### Note:
- Replace `BROKER_ADDRESS` with the actual MQTT broker address you intend to use.
- This code simulates health data collection from sensors and publishes the data to an MQTT broker.
- Ensure the `paho-mqtt` library is installed by running `pip install paho-mqtt`.
