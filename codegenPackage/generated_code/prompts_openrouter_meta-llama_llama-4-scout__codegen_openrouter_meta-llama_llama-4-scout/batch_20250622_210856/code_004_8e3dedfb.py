"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: "Design an electrical safety compliance system using IoT sensors and provide a code example in C++ or Python."
Generated: DETERMINISTIC_8e3dedfb1fe487fe
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Electrical Safety Compliance System using IoT Sensors**
===========================================================

**System Requirements**
------------------------

* Python 3.8+
* `paho-mqtt` library for MQTT communication
* `numpy` library for data processing

**Code**
------

```python
import paho.mqtt.client as mqtt
import numpy as np
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'electrical_safety'

class ElectricalSafetySystem:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect_to_mqtt(self):
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.loop_start()
        except Exception as e:
            logger.error(f'Failed to connect to MQTT broker: {e}')

    def on_connect(self, client, userdata, flags, rc):
        logger.info(f'Connected to MQTT broker with result code {rc}')
        client.subscribe(MQTT_TOPIC)

    def on_message(self, client, userdata, msg):
        try:
            data = np.frombuffer(msg.payload, dtype=np.float32)
            voltage = data[0]
            current = data[1]
            temperature = data[2]

            # Check electrical safety compliance
            if voltage > 240 or current > 10:
                logger.warning('Electrical safety compliance issue detected!')
                self.send_alert('Electrical safety compliance issue detected!')

            # Check temperature compliance
            if temperature > 50:
                logger.warning('Temperature compliance issue detected!')
                self.send_alert('Temperature compliance issue detected!')

        except Exception as e:
            logger.error(f'Failed to process message: {e}')

    def send_alert(self, message):
        try:
            # Send alert to designated MQTT topic
            alert_topic = 'electrical_safety/alert'
            self.client.publish(alert_topic, message)
        except Exception as e:
            logger.error(f'Failed to send alert: {e}')

    def run(self):
        self.connect_to_mqtt()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.client.loop_stop()
            self.client.disconnect()

if __name__ == '__main__':
    system = ElectricalSafetySystem()
    system.run()
```

**IoT Sensor Simulation Code (for testing purposes)**
------------------------------------------------

```python
import paho.mqtt.client as mqtt
import numpy as np
import time
import random

# Set up MQTT client
client = mqtt.Client()
client.connect('localhost', 1883)

try:
    while True:
        # Simulate IoT sensor data
        voltage = 230 + random.uniform(-10, 10)
        current = 5 + random.uniform(-1, 1)
        temperature = 40 + random.uniform(-5, 5)

        # Send data to MQTT topic
        data = np.array([voltage, current, temperature], dtype=np.float32)
        client.publish('electrical_safety', data.tobytes())
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
```
