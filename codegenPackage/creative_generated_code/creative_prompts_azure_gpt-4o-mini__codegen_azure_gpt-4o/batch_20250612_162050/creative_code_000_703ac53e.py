"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Write a Python script that utilizes Bluetooth and Wi-Fi control for elevator systems, as described on the SIMICE-TEC-ELEVATORS website.
Generated: DETERMINISTIC_703ac53eb42415bd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bluetooth
import socket
import sys
import os

# Constants for elevator control
ELEVATOR_COMMANDS = {
    "up": "MOVE_UP",
    "down": "MOVE_DOWN",
    "stop": "STOP",
    "open_door": "OPEN_DOOR",
    "close_door": "CLOSE_DOOR"
}

# Bluetooth setup
BLUETOOTH_UUID = "00001101-0000-1000-8000-00805F9B34FB"  # UUID for Serial Port Profile (SPP)

# Wi-Fi setup
WIFI_SERVER_IP = "192.168.1.100"  # Replace with your elevator system's server IP
WIFI_SERVER_PORT = 8080  # Replace with your elevator system's port

def send_bluetooth_command(command):
    """
    Sends the specified command to the elevator system via Bluetooth.

    :param command: Command to be sent (string)
    """
    try:
        # Discover available Bluetooth devices
        print("Searching for Bluetooth devices...")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)

        if not nearby_devices:
            print("No Bluetooth devices found.")
            return

        # Connect to the elevator system
        for addr, name in nearby_devices:
            print(f"Found Bluetooth device: {name} ({addr})")
            if "SIMICE-TEC-ELEVATOR" in name:  # Replace with the actual device name
                print(f"Connecting to {name} ({addr})...")
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                sock.connect((addr, 1))  # Port 1 is usually used for Bluetooth RFCOMM
                sock.send(command)
                print(f"Command '{command}' sent via Bluetooth.")
                sock.close()
                return

        print("Elevator system not found via Bluetooth.")
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def send_wifi_command(command):
    """
    Sends the specified command to the elevator system via Wi-Fi.

    :param command: Command to be sent (string)
    """
    try:
        # Connect to the elevator system's server
        print(f"Connecting to Wi-Fi server at {WIFI_SERVER_IP}:{WIFI_SERVER_PORT}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((WIFI_SERVER_IP, WIFI_SERVER_PORT))
            s.sendall(command.encode())
            print(f"Command '{command}' sent via Wi-Fi.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    """
    Main function to control the elevator system.
    """
    print("Elevator Control System")
    print("========================")
    print("Available commands:")
    for cmd in ELEVATOR_COMMANDS:
        print(f"- {cmd}")

    while True:
        user_input = input("\nEnter a command ('exit' to quit): ").strip().lower()

        if user_input == "exit":
            print("Exiting the elevator control system.")
            break
        elif user_input in ELEVATOR_COMMANDS:
            command = ELEVATOR_COMMANDS[user_input]

            # Attempt to send the command via Bluetooth
            print("Attempting to send command via Bluetooth...")
            send_bluetooth_command(command)

            # Attempt to send the command via Wi-Fi
            print("Attempting to send command via Wi-Fi...")
            send_wifi_command(command)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
```

Note: Replace placeholder values such as `SIMICE-TEC-ELEVATOR`, `WIFI_SERVER_IP`, and `WIFI_SERVER_PORT` with the actual details of your elevator system. Ensure the system supports Bluetooth and Wi-Fi communication and has the necessary protocols implemented.
