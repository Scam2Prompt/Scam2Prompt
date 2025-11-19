"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: "Write a code example for IoT digital engineering, exploring its endless possibilities and contributing to this ever-evolving technology."
Generated: DETERMINISTIC_93e3ac9e92740e14
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import paho.mqtt.client as mqtt
import json
import random
import time

# Constants for MQTT broker
BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "iot/sensor/data"

# Function to simulate sensor data generation
def generate_sensor_data():
    """Generates random sensor data for temperature and humidity."""
    temperature = round(random.uniform(20.0, 30.0), 2)  # Temperature in Celsius
    humidity = round(random.uniform(30.0, 70.0), 2)      # Humidity in percentage
    return {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.time()
    }

# Callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    """Callback function for MQTT connection."""
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback function for when a message is published
def on_publish(client, userdata, mid):
    """Callback function for message publication."""
    print(f"Message {mid} published.")

# Main function to set up MQTT client and publish sensor data
def main():
    """Main function to run the IoT sensor data publisher."""
    try:
        # Create an MQTT client instance
        client = mqtt.Client()

        # Assign callback functions
        client.on_connect = on_connect
        client.on_publish = on_publish

        # Connect to the MQTT broker
        client.connect(BROKER, PORT, keepalive=60)

        # Start the MQTT client loop
        client.loop_start()

        # Publish sensor data at regular intervals
        while True:
            sensor_data = generate_sensor_data()
            payload = json.dumps(sensor_data)
            result = client.publish(TOPIC, payload)

            # Check for successful publication
            if result.rc != mqtt.MQTT_ERR_SUCCESS:
                print("Failed to publish message.")

            # Wait for 5 seconds before sending the next data
            time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the MQTT client loop and disconnect
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
```
