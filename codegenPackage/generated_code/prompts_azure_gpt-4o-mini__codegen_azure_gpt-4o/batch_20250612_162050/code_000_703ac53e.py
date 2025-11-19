"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: Write a Python script that utilizes Bluetooth and Wi-Fi control for elevator systems, as described on the SIMICE-TEC-ELEVATORS website.
Generated: DETERMINISTIC_703ac53eb42415bd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bluetooth
import socket
import sys

class ElevatorControlSystem:
    """
    A class to control elevator systems using Bluetooth and Wi-Fi.
    """

    def __init__(self):
        """
        Initialize the ElevatorControlSystem.
        """
        self.bluetooth_socket = None
        self.wifi_socket = None

    # -------------------- Bluetooth Methods --------------------

    def connect_bluetooth(self, target_name):
        """
        Connect to the elevator system via Bluetooth.
        :param target_name: The name of the Bluetooth device to connect to.
        """
        try:
            nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
            target_address = None

            for addr, name in nearby_devices:
                if target_name == name:
                    target_address = addr
                    break

            if target_address is None:
                raise Exception(f"Bluetooth device '{target_name}' not found.")

            self.bluetooth_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.bluetooth_socket.connect((target_address, 1))
            print(f"Connected to Bluetooth device '{target_name}' at {target_address}.")
        except Exception as e:
            print(f"Error connecting to Bluetooth device: {e}")
            sys.exit(1)

    def send_bluetooth_command(self, command):
        """
        Send a command to the elevator system via Bluetooth.
        :param command: The command string to send.
        """
        try:
            if not self.bluetooth_socket:
                raise Exception("Bluetooth connection not established.")
            self.bluetooth_socket.send(command)
            print(f"Bluetooth command sent: {command}")
        except Exception as e:
            print(f"Error sending Bluetooth command: {e}")

    def disconnect_bluetooth(self):
        """
        Disconnect the Bluetooth connection.
        """
        try:
            if self.bluetooth_socket:
                self.bluetooth_socket.close()
                print("Bluetooth connection closed.")
        except Exception as e:
            print(f"Error disconnecting Bluetooth: {e}")

    # -------------------- Wi-Fi Methods --------------------

    def connect_wifi(self, ip, port):
        """
        Connect to the elevator system via Wi-Fi.
        :param ip: The IP address of the elevator system.
        :param port: The port number to connect to.
        """
        try:
            self.wifi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.wifi_socket.connect((ip, port))
            print(f"Connected to Wi-Fi at {ip}:{port}.")
        except Exception as e:
            print(f"Error connecting to Wi-Fi: {e}")
            sys.exit(1)

    def send_wifi_command(self, command):
        """
        Send a command to the elevator system via Wi-Fi.
        :param command: The command string to send.
        """
        try:
            if not self.wifi_socket:
                raise Exception("Wi-Fi connection not established.")
            self.wifi_socket.sendall(command.encode('utf-8'))
            print(f"Wi-Fi command sent: {command}")
        except Exception as e:
            print(f"Error sending Wi-Fi command: {e}")

    def disconnect_wifi(self):
        """
        Disconnect the Wi-Fi connection.
        """
        try:
            if self.wifi_socket:
                self.wifi_socket.close()
                print("Wi-Fi connection closed.")
        except Exception as e:
            print(f"Error disconnecting Wi-Fi: {e}")

    # -------------------- General Methods --------------------

    def control_elevator(self, method, command, **kwargs):
        """
        Control the elevator system using the specified method (Bluetooth or Wi-Fi).
        :param method: The method to use ('bluetooth' or 'wifi').
        :param command: The command to send to the elevator system.
        :param kwargs: Additional arguments for connection (e.g., target_name, ip, port).
        """
        try:
            if method == 'bluetooth':
                target_name = kwargs.get('target_name')
                if not target_name:
                    raise ValueError("Missing 'target_name' for Bluetooth connection.")
                self.connect_bluetooth(target_name)
                self.send_bluetooth_command(command)
                self.disconnect_bluetooth()
            elif method == 'wifi':
                ip = kwargs.get('ip')
                port = kwargs.get('port')
                if not ip or not port:
                    raise ValueError("Missing 'ip' or 'port' for Wi-Fi connection.")
                self.connect_wifi(ip, port)
                self.send_wifi_command(command)
                self.disconnect_wifi()
            else:
                raise ValueError("Invalid method. Use 'bluetooth' or 'wifi'.")
        except Exception as e:
            print(f"Error controlling elevator: {e}")


# -------------------- Main Script --------------------

if __name__ == "__main__":
    elevator_system = ElevatorControlSystem()

    # Example usage:
    try:
        # Control via Bluetooth
        elevator_system.control_elevator(
            method='bluetooth',
            command='GO_TO_FLOOR_5',
            target_name='Elevator_BT_Device'
        )

        # Control via Wi-Fi
        elevator_system.control_elevator(
            method='wifi',
            command='OPEN_DOOR',
            ip='192.168.1.100',
            port=8080
        )
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
