"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Create a simple home security monitoring system using IoT devices and a home automation hub."
Generated: DETERMINISTIC_43e9d01a5034f307
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Home Security Monitoring System**
=====================================

### Dependencies

* Python 3.9+
* `paho-mqtt` library for MQTT communication
* `logging` library for logging

### Code
```python
import logging
import paho.mqtt.client as mqtt
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MQTT settings
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'home/security'

class IoTDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

    def send_data(self, client, data):
        """Send data to the home automation hub"""
        client.publish(MQTT_TOPIC, json.dumps({'device_id': self.device_id, 'data': data}))

class HomeAutomationHub:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.devices = {}

    def connect(self):
        """Connect to the MQTT broker"""
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.loop_start()
        except Exception as e:
            logger.error(f'Failed to connect to MQTT broker: {e}')

    def on_connect(self, client, userdata, flags, rc):
        """Callback for when the client connects to the MQTT broker"""
        if rc == 0:
            logger.info('Connected to MQTT broker')
            client.subscribe(MQTT_TOPIC)
        else:
            logger.error(f'Failed to connect to MQTT broker: {rc}')

    def on_message(self, client, userdata, msg):
        """Callback for when a message is received from an IoT device"""
        try:
            data = json.loads(msg.payload)
            device_id = data['device_id']
            device_data = data['data']

            if device_id not in self.devices:
                logger.warning(f'Unknown device: {device_id}')
                return

            device = self.devices[device_id]
            logger.info(f'Received data from {device.device_id}: {device_data}')

            # Process device data
            if device.device_type == 'motion_sensor':
                if device_data['motion_detected']:
                    logger.warning(f'Motion detected by {device.device_id}')
                    # Trigger alert or notification
            elif device.device_type == 'door_sensor':
                if not device_data['door_closed']:
                    logger.warning(f'Door opened: {device.device_id}')
                    # Trigger alert or notification
        except Exception as e:
            logger.error(f'Failed to process message: {e}')

    def add_device(self, device):
        """Add an IoT device to the system"""
        self.devices[device.device_id] = device

def main():
    # Create a home automation hub
    hub = HomeAutomationHub()
    hub.connect()

    # Create IoT devices
    motion_sensor = IoTDevice('motion_sensor_1', 'motion_sensor')
    door_sensor = IoTDevice('door_sensor_1', 'door_sensor')

    # Add devices to the hub
    hub.add_device(motion_sensor)
    hub.add_device(door_sensor)

    # Simulate device data
    while True:
        # Motion sensor data
        motion_data = {'motion_detected': True}
        motion_sensor.send_data(hub.client, motion_data)

        # Door sensor data
        door_data = {'door_closed': False}
        door_sensor.send_data(hub.client, door_data)

        # Wait for 1 second
        import time
        time.sleep(1)

if __name__ == '__main__':
    main()
```
### Requirements
To run this code, you will need to install the `paho-mqtt` library using pip:
```bash
pip install paho-mqtt
```
You will also need to have an MQTT broker running on your local machine. You can use a broker like Mosquitto or HiveMQ.

### Usage
To run the code, simply execute the `main.py` file:
```bash
python main.py
```
This will start the home automation hub and simulate data from two IoT devices: a motion sensor and a door sensor. The hub will process this data and log any alerts or notifications.
