"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Provide a step-by-step guide for programming a home automation system to control "Persianas Z-Box" blinds using IoT protocols, as described on the Ayd Inspirate website.
Generated: DETERMINISTIC_57b0694e9a84d2da
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Automation System for Persianas Z-Box Blinds Control via IoT Protocols

This script provides a step-by-step implementation to control Z-Box blinds
using MQTT protocol for IoT communication.

Requirements:
- paho-mqtt
- python-dotenv
"""

import os
import time
import json
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt.eclipseprojects.io")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "")
MQTT_PASS = os.getenv("MQTT_PASS", "")
DEVICE_ID = os.getenv("DEVICE_ID", "zbox_blinds_1")
TOPIC_CONTROL = f"home/blinds/{DEVICE_ID}/control"
TOPIC_STATUS = f"home/blinds/{DEVICE_ID}/status"

class ZBoxBlindsController:
    def __init__(self):
        self.client = mqtt.Client(client_id=DEVICE_ID)
        self.client.username_pw_set(MQTT_USER, MQTT_PASS)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.current_position = 0  # 0-100% (0=closed, 100=open)

    def _on_connect(self, client, userdata, flags, rc):
        """Callback when connected to MQTT broker"""
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.subscribe(TOPIC_CONTROL)
            self._publish_status()
        else:
            print(f"Failed to connect, return code {rc}")

    def _on_disconnect(self, client, userdata, rc):
        """Callback when disconnected from MQTT broker"""
        print(f"Disconnected from MQTT Broker (rc: {rc})")
        if rc != 0:
            print("Attempting to reconnect...")
            self._reconnect()

    def _on_message(self, client, userdata, msg):
        """Callback when message is received on subscribed topic"""
        try:
            payload = json.loads(msg.payload.decode())
            command = payload.get("command")
            value = payload.get("value")

            if command == "set_position":
                self._set_position(value)
            elif command == "open":
                self._set_position(100)
            elif command == "close":
                self._set_position(0)
            elif command == "stop":
                print("Blinds movement stopped")
            elif command == "get_status":
                self._publish_status()
            else:
                print(f"Unknown command: {command}")

        except json.JSONDecodeError:
            print("Error: Invalid JSON payload")
        except Exception as e:
            print(f"Error processing message: {str(e)}")

    def _set_position(self, position):
        """Set blinds position (0-100%)"""
        try:
            position = max(0, min(100, int(position)))
            print(f"Setting blinds position to {position}%")
            # Simulate movement delay
            time.sleep(abs(self.current_position - position) * 0.01)
            self.current_position = position
            self._publish_status()
        except ValueError:
            print("Error: Position must be an integer between 0 and 100")

    def _publish_status(self):
        """Publish current status to MQTT broker"""
        status = {
            "device_id": DEVICE_ID,
            "position": self.current_position,
            "timestamp": time.time()
        }
        self.client.publish(TOPIC_STATUS, json.dumps(status))

    def _reconnect(self):
        """Attempt to reconnect to MQTT broker"""
        retry_count = 0
        max_retries = 5
        while retry_count < max_retries:
            try:
                self.client.reconnect()
                return
            except Exception:
                retry_count += 1
                wait_time = min(2 ** retry_count, 30)
                print(f"Retry {retry_count}/{max_retries} in {wait_time} seconds...")
                time.sleep(wait_time)
        print("Max retries reached. Could not reconnect.")

    def start(self):
        """Start the MQTT client and connect to broker"""
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
            self.client.loop_forever()
        except KeyboardInterrupt:
            print("Shutting down...")
            self.client.disconnect()
        except Exception as e:
            print(f"Error starting MQTT client: {str(e)}")

if __name__ == "__main__":
    controller = ZBoxBlindsController()
    controller.start()
```
