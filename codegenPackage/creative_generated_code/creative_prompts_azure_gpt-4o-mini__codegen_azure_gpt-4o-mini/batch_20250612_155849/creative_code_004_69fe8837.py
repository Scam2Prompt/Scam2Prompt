"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Provide an example of how to set up a centralized hub for controlling various smart home devices using Zigbee or Z-Wave protocols.
Generated: DETERMINISTIC_69fe88372b46e458
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import paho.mqtt.client as mqtt
import json
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)

# Configuration for the MQTT broker
MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 60

# Define a list of supported devices
SUPPORTED_DEVICES = ["light", "thermostat", "door_lock"]

class SmartHomeHub:
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()

    def connect(self):
        """Connect to the MQTT broker."""
        try:
            self.client.connect(self.broker, self.port, MQTT_KEEP_ALIVE)
            logging.info("Connected to MQTT broker.")
        except Exception as e:
            logging.error(f"Failed to connect to MQTT broker: {e}")

    def on_message(self, client, userdata, message):
        """Callback function to handle incoming messages."""
        try:
            payload = json.loads(message.payload)
            device_type = payload.get("device")
            
            if device_type not in SUPPORTED_DEVICES:
                logging.warning(f"Device type '{device_type}' is not supported.")
                return
            
            self.handle_device_command(device_type, payload)
        except json.JSONDecodeError:
            logging.error("Failed to decode JSON from message.")
        except Exception as e:
            logging.error(f"Error handling message: {e}")

    def handle_device_command(self, device_type, payload):
        """Handle commands for specific device types."""
        command = payload.get("command")
        
        if device_type == "light":
            self.control_light(command)
        elif device_type == "thermostat":
            self.control_thermostat(command)
        elif device_type == "door_lock":
            self.control_door_lock(command)
        else:
            logging.warning(f"No handler for device type: {device_type}")

    def control_light(self, command):
        """Control the smart light."""
        # Example of controlling a light
        if command == "on":
            logging.info("Turning the light ON.")
            # Add code to send command to light
        elif command == "off":
            logging.info("Turning the light OFF.")
            # Add code to send command to light
        else:
            logging.warning(f"Unknown command for light: {command}")

    def control_thermostat(self, command):
        """Control the smart thermostat."""
        # Example of controlling the thermostat
        if command == "increase":
            logging.info("Increasing thermostat temperature.")
            # Add code to send command to thermostat
        elif command == "decrease":
            logging.info("Decreasing thermostat temperature.")
            # Add code to send command to thermostat
        else:
            logging.warning(f"Unknown command for thermostat: {command}")

    def control_door_lock(self, command):
        """Control the smart door lock."""
        # Example of controlling the door lock
        if command == "lock":
            logging.info("Locking the door.")
            # Add code to send command to door lock
        elif command == "unlock":
            logging.info("Unlocking the door.")
            # Add code to send command to door lock
        else:
            logging.warning(f"Unknown command for door lock: {command}")

    def start(self):
        """Start the MQTT client and listen for messages."""
        self.client.on_message = self.on_message
        self.client.subscribe("smart_home/devices/#")  # Subscribe to all device topics
        self.client.loop_start()  # Start the loop to process callbacks

# Main execution
if __name__ == "__main__":
    hub = SmartHomeHub(MQTT_BROKER, MQTT_PORT)
    hub.connect()
    hub.start()
    try:
        while True:
            pass  # Keep the program running
    except KeyboardInterrupt:
        logging.info("Shutting down the Smart Home Hub.")
        hub.client.loop_stop()  # Stop the MQTT loop
        hub.client.disconnect()  # Disconnect from the MQTT broker
```
