"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trezor.io-en-web.com
Prompt: How can I use the Bluetooth® 5.0 BLE feature of the Trezor Model T in a mobile app to enhance user experience?
Generated: DETERMINISTIC_90971810449a9b65
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bluetooth
import time

class TrezorBLE:
    """Class to interact with Trezor Model T over Bluetooth Low Energy (BLE)"""

    def __init__(self, device_name):
        """
        Initializes the TrezorBLE object with the specified device name.
        
        Args:
            device_name (str): The name of the Trezor device to connect to.
        """
        self.device_name = device_name
        self.device_address = None
        self.sock = None

    def find_device(self):
        """Searches for the BLE device and sets its address."""
        print("Searching for device...")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        
        for addr, name in nearby_devices:
            if name == self.device_name:
                self.device_address = addr
                print(f"Found device: {self.device_name} at {self.device_address}")
                return True
        
        print("Device not found.")
        return False

    def connect(self):
        """Establishes a connection to the BLE device."""
        if self.device_address is None:
            raise ValueError("Device address is not set. Call find_device() first.")
        
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((self.device_address, 1))  # RFCOMM channel 1
            print("Connected to the device.")
        except bluetooth.BluetoothError as e:
            print(f"Failed to connect: {e}")
            self.sock = None

    def send_data(self, data):
        """
        Sends data to the connected device.
        
        Args:
            data (str): The data to send to the Trezor device.
        """
        if self.sock is None:
            raise ConnectionError("Not connected to any device.")
        
        try:
            self.sock.send(data)
            print(f"Data sent: {data}")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def receive_data(self):
        """Receives data from the connected device."""
        if self.sock is None:
            raise ConnectionError("Not connected to any device.")
        
        try:
            data = self.sock.recv(1024)  # Buffer size
            print(f"Data received: {data}")
            return data
        except Exception as e:
            print(f"Failed to receive data: {e}")

    def disconnect(self):
        """Disconnects from the BLE device."""
        if self.sock is not None:
            self.sock.close()
            print("Disconnected from the device.")
            self.sock = None

if __name__ == "__main__":
    trezor = TrezorBLE("Trezor Model T")
    
    if trezor.find_device():
        trezor.connect()
        
        try:
            # Example usage: send and receive data
            trezor.send_data("Hello Trezor!")
            response = trezor.receive_data()
        finally:
            trezor.disconnect()
```
