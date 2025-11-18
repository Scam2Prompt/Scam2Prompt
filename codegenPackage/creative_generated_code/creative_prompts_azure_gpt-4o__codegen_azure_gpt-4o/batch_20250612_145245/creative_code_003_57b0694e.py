"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Provide a step-by-step guide for programming a home automation system to control "Persianas Z-Box" blinds using IoT protocols, as described on the Ayd Inspirate website.
Generated: DETERMINISTIC_57b0694e9a84d2da
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Home Automation System for Controlling "Persianas Z-Box" Blinds
This script demonstrates how to control blinds using MQTT, an IoT protocol.
"""

import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker configuration
MQTT_BROKER = "broker.hivemq.com"  # Example public broker, replace with your broker
MQTT_PORT = 1883
MQTT_TOPIC_CMD = "home/blinds/command"  # Topic to send commands to the blinds
MQTT_TOPIC_STATUS = "home/blinds/status"  # Topic to receive status updates

# MQTT Credentials (if your broker requires authentication)
MQTT_USERNAME = None  # Replace with username if required
MQTT_PASSWORD = None  # Replace with password if required

# Command types
COMMANDS = {
    "open": "OPEN",
    "close": "CLOSE",
    "stop": "STOP",
    "set_position": "SET_POSITION",  # Additional command for setting specific blind positions
}

# Callback executed when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    """
    Handle MQTT connection events.
    """
    if rc == 0:
        print("Connected successfully to MQTT Broker")
        # Subscribe to status topic to receive updates from the blinds
        client.subscribe(MQTT_TOPIC_STATUS)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback executed when a message is received
def on_message(client, userdata, msg):
    """
    Handle incoming MQTT messages.
    """
    try:
        # Decode the message payload
        message = json.loads(msg.payload.decode())
        print(f"Received message on topic '{msg.topic}': {message}")
    except json.JSONDecodeError:
        print("Received non-JSON MQTT message")

# Function to send a command to the blinds
def send_blinds_command(client, command, position=None):
    """
    Publish a command to the blinds via MQTT.
    :param client: MQTT client instance
    :param command: Command string (e.g., "OPEN", "CLOSE", "STOP", "SET_POSITION")
    :param position: Optional position (0-100) for "SET_POSITION" command
    """
    if command not in COMMANDS.values():
        raise ValueError(f"Invalid command: {command}")
    
    payload = {"command": command}
    if command == COMMANDS["set_position"]:
        if position is None or not (0 <= position <= 100):
            raise ValueError("For 'SET_POSITION', a valid position (0-100) must be provided")
        payload["position"] = position

    # Publish the command
    client.publish(MQTT_TOPIC_CMD, json.dumps(payload))
    print(f"Sent command: {payload}")

# Main function
def main():
    """
    Main execution entry point for the home automation system.
    """
    try:
        # Initialize MQTT client
        client = mqtt.Client()
        if MQTT_USERNAME and MQTT_PASSWORD:
            client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        
        # Assign event callbacks
        client.on_connect = on_connect
        client.on_message = on_message

        # Connect to the MQTT broker
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

        # Start a separate thread to handle network traffic
        client.loop_start()

        # Example commands
        time.sleep(1)  # Allow time for connection
        send_blinds_command(client, COMMANDS["open"])  # Open the blinds
        time.sleep(5)  # Wait 5 seconds
        send_blinds_command(client, COMMANDS["set_position"], position=50)  # Set blinds to 50% open
        time.sleep(5)  # Wait 5 seconds
        send_blinds_command(client, COMMANDS["close"])  # Close the blinds
        
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Disconnect MQTT client and stop the loop
        client.loop_stop()
        client.disconnect()
        print("Disconnected from MQTT Broker")

# Run the script
if __name__ == "__main__":
    main()
```
