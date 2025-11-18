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
import paho.mqtt.client as mqtt
import json
import time

# Constants for the MQTT broker
BROKER_ADDRESS = "mqtt.example.com"  # Replace with your MQTT broker address
TOPIC = "home/automation/persianas"  # Replace with your intended MQTT topic

# Function to send a command to the blinds
def send_blinds_command(command):
    """
    Sends a command to the Persianas Z-Box blinds via MQTT.

    Args:
        command (str): The command to be sent (e.g., "open", "close").
    """
    try:
        # Initialize MQTT client
        client = mqtt.Client()

        # Connect to the MQTT broker
        client.connect(BROKER_ADDRESS)

        # Create the payload with command
        payload = json.dumps({"command": command})

        # Publish the command to the specified topic
        client.publish(TOPIC, payload)

        print(f"Command '{command}' sent successfully.")
    except Exception as e:
        print(f"Failed to send command '{command}': {e}")
    finally:
        # Disconnect the client after the command is sent
        client.disconnect()

# Main function to control the blinds
def main():
    """
    Main function to control the Persianas Z-Box blinds.
    It provides a simple menu to open, close, or stop the blinds.
    """
    while True:
        print("\n--- Persianas Z-Box Control ---")
        print("1. Open Blinds")
        print("2. Close Blinds")
        print("3. Stop Blinds")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            send_blinds_command("open")
        elif choice == '2':
            send_blinds_command("close")
        elif choice == '3':
            send_blinds_command("stop")
        elif choice == '4':
            print("Exiting the home automation system.")
            break
        else:
            print("Invalid choice. Please try again.")

        # Optional: Delay for a short period to avoid flooding the MQTT broker
        time.sleep(1)

if __name__ == "__main__":
    main()
```
