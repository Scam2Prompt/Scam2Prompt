"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Recommend an API or library for implementing SIS (Safety Instrumented Systems) in industrial plants, considering Puma Ipce's focus on automation and control systems.
Generated: DETERMINISTIC_5f159327aaf37bb1
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Safety Instrumented Systems (SIS) Implementation using Python

This script demonstrates how to integrate safety instrumented systems (SIS) 
with a focus on industrial automation and control systems.

For this example, we'll use the `paho-mqtt` library for communication and 
`numpy` for data handling. Make sure to install these libraries using:
pip install paho-mqtt numpy
"""

import paho.mqtt.client as mqtt
import numpy as np
import logging
import time

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyInstrumentedSystem:
    def __init__(self, broker_address, topic):
        """Initialize the SIS with MQTT broker details and the topic for communication."""
        self.broker_address = broker_address
        self.topic = topic
        self.client = mqtt.Client()

        # Setup MQTT client callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.setup_connection()

    def setup_connection(self):
        """Establish connection to the MQTT broker."""
        try:
            self.client.connect(self.broker_address)
            self.client.loop_start()
            logging.info(f"Connected to MQTT broker at {self.broker_address}")
        except Exception as e:
            logging.error(f"Could not connect to broker: {e}")

    def on_connect(self, client, userdata, flags, rc):
        """Callback when the client connects to the broker."""
        logging.info(f"Connected with result code: {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, message):
        """Callback when a message is received."""
        logging.info(f"Message received: {message.payload.decode()}")
        # Handle the message according to SIS requirements
        self.process_message(message.payload.decode())

    def process_message(self, message):
        """Process the incoming message for safety checks."""
        try:
            data = np.fromstring(message, sep=',')
            # Example safety checks (thresholds and conditions)
            if np.any(data > 100):  # Simulated safety threshold
                self.trigger_alarm(data)
            else:
                logging.info("No safety issues detected.")
        except Exception as e:
            logging.error(f"Error processing message: {e}")

    def trigger_alarm(self, data):
        """Trigger an alarm in case of a safety issue."""
        logging.warning(f"Safety alarm triggered! Data: {data}")

    def run(self):
        """Keep the SIS running to listen for messages."""
        try:
            while True:
                time.sleep(1)  # Maintain a running loop
        except KeyboardInterrupt:
            logging.info("Disconnecting from MQTT broker.")
            self.client.loop_stop()
            self.client.disconnect()

if __name__ == "__main__":
    # Replace with your actual MQTT broker address and topic
    BROKER_ADDRESS = "mqtt.example.com"  # Example MQTT broker
    TOPIC = "safety/instrumented_system"

    sis = SafetyInstrumentedSystem(BROKER_ADDRESS, TOPIC)
    sis.run()
```
