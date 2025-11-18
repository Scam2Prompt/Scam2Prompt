"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Develop a script to control multiple smart home devices interoperably, referencing the integration techniques discussed on vigilanciadomotica.es.
Generated: DETERMINISTIC_d2ea6c066dd8e515
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to control multiple smart home devices interoperably using MQTT for communication.
This script assumes smart home devices are configured to subscribe to specific MQTT topics.
The script allows controlling lights, thermostats, and door locks.

Prerequisites:
1. Install the paho-mqtt library (`pip install paho-mqtt`).
2. Configure MQTT broker details, and ensure devices are properly subscribed to topics.
"""

import paho.mqtt.client as mqtt
import json

# MQTT Broker Configuration
BROKER_ADDRESS = "mqtt.example.com"  # Replace with your MQTT broker address
BROKER_PORT = 1883
BROKER_USERNAME = "username"        # Replace with your MQTT username
BROKER_PASSWORD = "password"        # Replace with your MQTT password

# MQTT Topics for Devices
TOPICS = {
    "lights": "home/lights",
    "thermostat": "home/thermostat",
    "door_lock": "home/door_lock"
}

# MQTT Client Setup
client = mqtt.Client("SmartHomeController")  # Unique client ID
client.username_pw_set(BROKER_USERNAME, BROKER_PASSWORD)

# Callback for connection
def on_connect(client, userdata, flags, rc):
    """
    Callback function for MQTT connection.
    """
    if rc == 0:
        print("Connected successfully to MQTT broker.")
    else:
        print(f"Failed to connect. Error code: {rc}")

# Error Handling
def send_command(topic, message):
    """
    Send a command to a specific topic.

    Args:
        topic (str): MQTT topic to publish to.
        message (dict): Message to send (as a dictionary).

    Returns:
        None
    """
    try:
        payload = json.dumps(message)  # Convert dictionary to JSON format
        client.publish(topic, payload)
        print(f"Command sent: {message} -> Topic: {topic}")
    except Exception as e:
        print(f"Error sending command to {topic}: {e}")

# Controlling Lights
def control_lights(action):
    """
    Control lights. Action can be 'on', 'off', or 'dim' with a brightness level.

    Args:
        action (str): The action to perform (e.g., 'on', 'off', or 'dim').

    Returns:
        None
    """
    if action not in ['on', 'off', 'dim']:
        print("Invalid action for lights.")
        return

    message = {"action": action}
    if action == "dim":
        brightness = int(input("Enter brightness level (0-100): "))
        message["brightness"] = brightness

    send_command(TOPICS["lights"], message)

# Controlling Thermostat
def control_thermostat(temp):
    """
    Set the thermostat to a specific temperature.

    Args:
        temp (float): Desired temperature.

    Returns:
        None
    """
    if not isinstance(temp, (int, float)) or temp < 10 or temp > 35:
        print("Invalid temperature. Must be between 10°C and 35°C.")
        return

    message = {"temperature": temp}
    send_command(TOPICS["thermostat"], message)

# Controlling Door Lock
def control_door_lock(state):
    """
    Lock or unlock the door.

    Args:
        state (str): The state ('lock' or 'unlock').

    Returns:
        None
    """
    if state not in ['lock', 'unlock']:
        print("Invalid state for door lock.")
        return

    message = {"state": state}
    send_command(TOPICS["door_lock"], message)

# Menu for User Interaction
def main_menu():
    """
    Main menu for controlling smart home devices.
    """
    while True:
        print("\nSmart Home Controller Menu")
        print("1. Control Lights")
        print("2. Control Thermostat")
        print("3. Control Door Lock")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            action = input("Enter action (on/off/dim): ").lower()
            control_lights(action)
        elif choice == "2":
            temp = float(input("Enter desired temperature (°C): "))
            control_thermostat(temp)
        elif choice == "3":
            state = input("Enter state (lock/unlock): ").lower()
            control_door_lock(state)
        elif choice == "4":
            print("Exiting Smart Home Controller...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Execution
if __name__ == "__main__":
    # Set up MQTT callbacks
    client.on_connect = on_connect

    # Connect to MQTT broker
    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT)
        client.loop_start()  # Start MQTT loop in a separate thread
        main_menu()
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
    finally:
        client.loop_stop()
        client.disconnect()
```
