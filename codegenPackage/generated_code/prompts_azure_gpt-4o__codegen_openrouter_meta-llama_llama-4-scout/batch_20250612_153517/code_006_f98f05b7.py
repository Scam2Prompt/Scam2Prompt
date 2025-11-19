"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Develop a program that connects hearing aids wirelessly to multiple devices, such as phones and TVs, using Bluetooth or similar technologies.
Generated: DETERMINISTIC_f98f05b7384b60af
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hearing_aid_connector.py

import bluetooth
import threading

class HearingAidConnector:
    """
    Connects hearing aids wirelessly to multiple devices using Bluetooth.
    """

    def __init__(self):
        self.devices = {}
        self.lock = threading.Lock()

    def start_scan(self):
        """
        Start scanning for available Bluetooth devices.
        """
        print("Scanning for available devices...")
        devices = bluetooth.discover_devices(duration=8, lookup_names=True)
        print("Found devices:")
        for addr, name in devices:
            print(f"{name} ({addr})")

    def connect_device(self, address):
        """
        Connect to a device with the given address.

        Args:
            address (str): The address of the device to connect to.
        """
        try:
            with self.lock:
                if address in self.devices:
                    print(f"Already connected to {address}")
                    return

                # Create a new thread for the connection
                thread = threading.Thread(target=self._connect_device, args=(address,))
                thread.start()

        except Exception as e:
            print(f"Error connecting to {address}: {e}")

    def _connect_device(self, address):
        """
        Establish a connection to a device.

        Args:
            address (str): The address of the device to connect to.
        """
        try:
            # Establish a connection to the device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.bind(("", bluetooth.PORT_ANY))
            sock.listen(1)

            print(f"Connecting to {address}...")
            client_sock, client_info = sock.accept()
            print(f"Connected to {address}")

            # Store the connected device
            with self.lock:
                self.devices[address] = client_sock

            # Handle incoming data from the device
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                print(f"Received data from {address}: {data}")

        except Exception as e:
            print(f"Error connecting to {address}: {e}")
        finally:
            # Close the connection
            if address in self.devices:
                self.devices[address].close()
                del self.devices[address]

    def disconnect_device(self, address):
        """
        Disconnect from a device with the given address.

        Args:
            address (str): The address of the device to disconnect from.
        """
        try:
            with self.lock:
                if address not in self.devices:
                    print(f"Not connected to {address}")
                    return

                # Close the connection
                self.devices[address].close()
                del self.devices[address]

        except Exception as e:
            print(f"Error disconnecting from {address}: {e}")

def main():
    connector = HearingAidConnector()

    while True:
        print("\nOptions:")
        print("1. Scan for devices")
        print("2. Connect to device")
        print("3. Disconnect from device")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            connector.start_scan()
        elif choice == "2":
            address = input("Enter the address of the device to connect to: ")
            connector.connect_device(address)
        elif choice == "3":
            address = input("Enter the address of the device to disconnect from: ")
            connector.disconnect_device(address)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
