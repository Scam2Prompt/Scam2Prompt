"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Write a code snippet to integrate an agriculture sprayer with IoT technology for remote monitoring, referencing Vinglob Greentech's product offerings.
Generated: DETERMINISTIC_c119298f678ef81f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
IoT Integration for Agriculture Sprayer
This script enables remote monitoring and control for an agriculture sprayer, referencing Vinglob Greentech's IoT-enabled sprayer.
The code connects the sprayer to an MQTT broker for data exchange and remote commands.
"""

import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT Configuration
BROKER_ADDRESS = "mqtt.vinglobgreentech.com"  # Replace with actual broker address
PORT = 1883                                  # Default MQTT port
TOPIC_STATUS = "sprayer/status"              # Topic for publishing status updates
TOPIC_COMMAND = "sprayer/command"            # Topic for receiving control commands
CLIENT_ID = "AgricultureSprayer1"            # Unique identifier for this sprayer

# Simulated Sprayer Data
SPRAYER_STATUS = {
    "device_id": CLIENT_ID,      # Unique ID of the sprayer
    "status": "idle",            # Possible values: 'idle', 'spraying', 'error'
    "battery_level": 100,        # Battery percentage
    "water_level": 100,          # Water tank percentage
    "last_updated": ""           # Timestamp of last status update
}

# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker at {BROKER_ADDRESS}:{PORT}")
        client.subscribe(TOPIC_COMMAND)  # Subscribe to the control commands topic
    else:
        print(f"Failed to connect, return code {rc}")

# Callback for receiving messages
def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode("utf-8"))
        print(f"Received command: {payload}")
        
        # Handle received commands
        if payload.get("command") == "start_spraying":
            SPRAYER_STATUS["status"] = "spraying"
        elif payload.get("command") == "stop_spraying":
            SPRAYER_STATUS["status"] = "idle"
        elif payload.get("command") == "shutdown":
            print("Shutting down sprayer...")
            client.disconnect()
        else:
            print("Unknown command received.")
    except Exception as e:
        print(f"Error processing command: {e}")

# Publish sprayer status periodically
def publish_status(client):
    try:
        SPRAYER_STATUS["battery_level"] = max(
            0, SPRAYER_STATUS["battery_level"] - random.uniform(0.1, 0.5)
        )  # Simulate battery drain
        SPRAYER_STATUS["water_level"] = max(
            0, SPRAYER_STATUS["water_level"] - random.uniform(0.5, 2.0)
        )  # Simulate water usage
        SPRAYER_STATUS["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        client.publish(TOPIC_STATUS, json.dumps(SPRAYER_STATUS))
        print(f"Published status: {SPRAYER_STATUS}")
    except Exception as e:
        print(f"Error publishing status: {e}")

# Main function to run the IoT integration
def main():
    try:
        # Initialize MQTT client
        client = mqtt.Client(CLIENT_ID)
        client.on_connect = on_connect
        client.on_message = on_message

        # Connect to the MQTT broker
        client.connect(BROKER_ADDRESS, PORT)

        # Start the MQTT client loop
        client.loop_start()

        print("Sprayer IoT integration started. Monitoring and control enabled.")
        
        # Publish status in intervals
        while True:
            publish_status(client)
            time.sleep(5)  # Publish every 5 seconds
    except KeyboardInterrupt:
        print("Shutting down IoT integration...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
```
