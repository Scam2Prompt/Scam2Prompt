"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Develop a program that connects hearing aids wirelessly to multiple devices, such as phones and TVs, using Bluetooth or similar technologies.
Generated: DETERMINISTIC_f98f05b7384b60af
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code demonstrating how to use Bluetooth Low Energy (BLE) to connect hearing aids to multiple devices like phones or TVs. This implementation uses the `bleak` library for Bluetooth communication:

```python
import asyncio
from bleak import BleakScanner, BleakClient

class HearingAidConnector:
    def __init__(self):
        self.connected_devices = {}

    async def scan_for_devices(self):
        """Scan for nearby Bluetooth devices."""
        print("Scanning for Bluetooth devices...")
        devices = await BleakScanner.discover()
        for idx, device in enumerate(devices):
            print(f"{idx + 1}. {device.name} ({device.address})")
        return devices

    async def connect_to_device(self, device_address):
        """Connect to a Bluetooth device via its address."""
        try:
            print(f"Connecting to device with address: {device_address}...")
            client = BleakClient(device_address)
            await client.connect()

            # Verify connection
            if client.is_connected:
                print(f"Connected to {device_address}")
                self.connected_devices[device_address] = client
            else:
                print(f"Failed to connect to {device_address}")
        except Exception as e:
            print(f"Error connecting to device: {e}")

    async def disconnect_device(self, device_address):
        """Disconnect a connected Bluetooth device."""
        try:
            client = self.connected_devices.get(device_address)
            if client:
                print(f"Disconnecting from {device_address}...")
                await client.disconnect()
                del self.connected_devices[device_address]
                print(f"Disconnected from {device_address}")
            else:
                print(f"Device with address {device_address} not connected.")
        except Exception as e:
            print(f"Error disconnecting device: {e}")

    async def list_connected_devices(self):
        """List currently connected devices."""
        print("Connected devices:")
        for address, client in self.connected_devices.items():
            print(f"- {address} (connected: {client.is_connected})")

    async def run(self):
        """Main program loop to connect hearing aids to devices."""
        devices = await self.scan_for_devices()

        print("\nSelect a device to connect to:")
        try:
            choice = int(input("Enter the device number (or 0 to exit): "))
            if choice == 0:
                print("Exiting...")
                return
            selected_device = devices[choice - 1]
            await self.connect_to_device(selected_device.address)

            print("\nActions:")
            print("1. List connected devices")
            print("2. Disconnect a device")
            print("3. Exit")

            while True:
                action = int(input("Choose an action: "))
                if action == 1:
                    await self.list_connected_devices()
                elif action == 2:
                    device_address = input("Enter the device address to disconnect: ")
                    await self.disconnect_device(device_address)
                elif action == 3:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Exiting program...")
        except IndexError:
            print("Invalid device selection. Exiting program...")
        finally:
            # Ensure all devices are disconnected before exiting
            for address in list(self.connected_devices.keys()):
                await self.disconnect_device(address)
            print("Program terminated cleanly.")

# Entry point for the program
if __name__ == "__main__":
    connector = HearingAidConnector()
    asyncio.run(connector.run())
```

### Instructions:
- Install the `bleak` library with `pip install bleak`.
- Run the program on a machine that supports BLE (Bluetooth Low Energy).
- Follow the interactive prompts to scan, connect, list, and disconnect devices.

### Features:
- Well-commented code for readability.
- Proper error handling for Bluetooth operations.
- Production-ready structure with a `HearingAidConnector` class encapsulating functionality.
