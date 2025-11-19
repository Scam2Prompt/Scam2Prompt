"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Write a program to monitor and control the lighting system in an industrial facility, such as a petrochemical plant, using IoT protocols."
Generated: DETERMINISTIC_bdda70e41c04a096
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lighting_control_system.py

import logging
import time
from typing import Dict

# Import required libraries for IoT communication
import paho.mqtt.client as mqtt

# Define constants for MQTT connection
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC_LIGHTING = "industrial/facility/lighting"

# Define a class for Lighting System Control
class LightingSystemControl:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create an MQTT client instance
        self.client = mqtt.Client()

        # Define a dictionary to store lighting zone status
        self.lighting_zones: Dict[str, bool] = {
            "zone_1": False,
            "zone_2": False,
            "zone_3": False,
        }

    def on_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection"""
        if rc == 0:
            self.logger.info("Connected to MQTT broker")
            client.subscribe(MQTT_TOPIC_LIGHTING)
        else:
            self.logger.error(f"Failed to connect to MQTT broker, return code {rc}")

    def on_message(self, client, userdata, msg):
        """Callback for MQTT message reception"""
        try:
            # Parse received MQTT message
            message = msg.payload.decode("utf-8")
            zone, status = message.split(",")

            # Update lighting zone status
            if zone in self.lighting_zones:
                self.lighting_zones[zone] = status.lower() == "on"
                self.logger.info(f"Updated {zone} to {status}")
            else:
                self.logger.warning(f"Unknown zone: {zone}")
        except Exception as e:
            self.logger.error(f"Error processing MQTT message: {e}")

    def connect_to_mqtt(self):
        """Establish a connection to the MQTT broker"""
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.loop_start()
        except Exception as e:
            self.logger.error(f"Error connecting to MQTT broker: {e}")

    def control_lighting(self, zone: str, status: bool):
        """Control lighting for a specific zone"""
        if zone in self.lighting_zones:
            self.lighting_zones[zone] = status
            message = f"{zone},{'on' if status else 'off'}"
            self.client.publish(MQTT_TOPIC_LIGHTING, message)
            self.logger.info(f"Published message: {message}")
        else:
            self.logger.warning(f"Unknown zone: {zone}")

    def run(self):
        """Start the lighting control system"""
        self.connect_to_mqtt()

        # Simulate initial lighting zone status
        for zone, status in self.lighting_zones.items():
            self.control_lighting(zone, status)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("Exiting lighting control system")
            self.client.loop_stop()
            self.client.disconnect()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    lighting_control = LightingSystemControl()
    lighting_control.run()
```
