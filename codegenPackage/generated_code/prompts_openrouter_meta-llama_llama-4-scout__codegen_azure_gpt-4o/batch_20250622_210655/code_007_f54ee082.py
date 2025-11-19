"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "How can one integrate a fire alarm system with popular home automation systems? Provide code examples."
Generated: DETERMINISTIC_f54ee082138eb83a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is an example of Python code that integrates a fire alarm system with a popular home automation system using MQTT (Message Queuing Telemetry Transport). This code assumes the fire alarm system can send alerts, and the home automation system supports MQTT for communication.

```python
import paho.mqtt.client as mqtt
import time
import json

# Configuration for MQTT broker
MQTT_BROKER = "mqtt.example.com"  # Replace with your MQTT broker address
MQTT_PORT = 1883                  # Default MQTT port
MQTT_TOPIC_FIRE_ALARM = "home/fire_alarm"  # Topic for fire alarm notifications
MQTT_TOPIC_HOME_AUTOMATION = "home/automation/fire_alert"  # Topic for home automation system

# Fire alarm system simulation (replace with actual fire alarm integration)
def check_fire_alarm():
    """
    Simulates checking the fire alarm system.
    Replace this function with actual integration logic for your fire alarm system.
    """
    # Example: Simulate fire alarm triggered randomly
    import random
    return random.choice([True, False])

# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    """
    Callback function triggered when the MQTT client connects to the broker.
    """
    if rc == 0:
        print("Connected to MQTT broker successfully.")
    else:
        print(f"Failed to connect to MQTT broker. Return code: {rc}")

# Callback for MQTT message
def on_message(client, userdata, msg):
    """
    Callback function triggered when a message is received on a subscribed topic.
    """
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Main function
def main():
    """
    Main function to integrate fire alarm system with home automation system.
    """
    try:
        # Initialize MQTT client
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        # Connect to MQTT broker
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

        # Start MQTT loop in a separate thread
        client.loop_start()

        print("Monitoring fire alarm system...")
        while True:
            # Check fire alarm system
            fire_alarm_triggered = check_fire_alarm()

            if fire_alarm_triggered:
                print("Fire alarm triggered! Sending alert to home automation system...")

                # Prepare alert message
                alert_message = {
                    "alert": "Fire detected!",
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }

                # Publish alert to home automation system
                client.publish(MQTT_TOPIC_HOME_AUTOMATION, json.dumps(alert_message))
                print("Alert sent successfully.")

            # Wait before checking again
            time.sleep(5)

    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop MQTT loop and disconnect
        client.loop_stop()
        client.disconnect()
        print("Disconnected from MQTT broker.")

# Entry point
if __name__ == "__main__":
    main()
```

### Key Features:
1. **MQTT Integration**: The code uses the `paho-mqtt` library to communicate with the MQTT broker.
2. **Fire Alarm Simulation**: The `check_fire_alarm` function simulates fire alarm detection. Replace it with actual integration logic for your fire alarm system.
3. **Error Handling**: The code includes error handling for unexpected issues and ensures clean shutdown on keyboard interrupt.
4. **JSON Messaging**: Alerts are sent in JSON format for easy parsing by the home automation system.

### Requirements:
- Install the `paho-mqtt` library: `pip install paho-mqtt`
- Replace placeholder values (e.g., `mqtt.example.com`) with actual configuration details for your MQTT broker and topics.
