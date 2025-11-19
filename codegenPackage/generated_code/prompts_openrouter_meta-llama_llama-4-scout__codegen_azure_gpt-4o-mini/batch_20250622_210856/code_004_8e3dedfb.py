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

```python
import time
import random
import json
import paho.mqtt.client as mqtt

# Constants for MQTT broker
BROKER_ADDRESS = "mqtt.example.com"
TOPIC = "safety/compliance"

# Thresholds for electrical safety
VOLTAGE_THRESHOLD = 240  # Volts
CURRENT_THRESHOLD = 30    # Amperes

# Function to simulate reading from IoT sensors
def read_sensor_data():
    """Simulate reading voltage and current from IoT sensors."""
    voltage = random.uniform(200, 300)  # Simulated voltage reading
    current = random.uniform(10, 50)     # Simulated current reading
    return voltage, current

# Function to check compliance
def check_compliance(voltage, current):
    """Check if the voltage and current readings are within safe limits."""
    if voltage > VOLTAGE_THRESHOLD:
        return False, "Voltage exceeds safe limit!"
    if current > CURRENT_THRESHOLD:
        return False, "Current exceeds safe limit!"
    return True, "All readings are within safe limits."

# MQTT callback function for connection
def on_connect(client, userdata, flags, rc):
    """Callback function for MQTT connection."""
    print("Connected to MQTT broker with result code: " + str(rc))

# MQTT callback function for publishing messages
def on_publish(client, userdata, mid):
    """Callback function for message publishing."""
    print("Message published with ID: " + str(mid))

# Main function to run the compliance system
def main():
    """Main function to run the electrical safety compliance system."""
    # Initialize MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    try:
        # Connect to the MQTT broker
        client.connect(BROKER_ADDRESS)
        client.loop_start()

        while True:
            # Read sensor data
            voltage, current = read_sensor_data()
            print(f"Voltage: {voltage:.2f} V, Current: {current:.2f} A")

            # Check compliance
            compliant, message = check_compliance(voltage, current)
            print(message)

            # Prepare data for publishing
            data = {
                "voltage": voltage,
                "current": current,
                "compliant": compliant,
                "message": message
            }

            # Publish data to MQTT topic
            client.publish(TOPIC, json.dumps(data))

            # Wait before the next reading
            time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up and disconnect from MQTT broker
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
```
