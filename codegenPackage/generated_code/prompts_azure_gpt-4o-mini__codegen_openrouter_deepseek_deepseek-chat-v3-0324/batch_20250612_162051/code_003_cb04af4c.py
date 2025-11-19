"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: How can I implement a solution to switch between multiple HDMI sources using a KVM switch as described on FullPort?
Generated: DETERMINISTIC_cb04af4c21a33b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import time
from typing import Optional

class KVMSwitchController:
    """
    A class to control a KVM switch for switching between multiple HDMI sources.
    This implementation assumes the KVM switch is connected via a serial port.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the KVM switch controller.

        Args:
            port: The serial port to which the KVM switch is connected (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: The baud rate for serial communication (default: 9600)
            timeout: The timeout for serial operations in seconds (default: 1.0)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self) -> bool:
        """
        Establish connection to the KVM switch.

        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Allow time for connection to establish
            return True
        except serial.SerialException as e:
            print(f"Failed to connect to KVM switch: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection to the KVM switch."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def switch_source(self, source_number: int) -> bool:
        """
        Switch to the specified HDMI source.

        Args:
            source_number: The HDMI source number to switch to (1-based index)

        Returns:
            bool: True if command was sent successfully, False otherwise
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            print("Not connected to KVM switch")
            return False

        if source_number < 1:
            print("Source number must be at least 1")
            return False

        # Example command format (adjust based on your KVM switch protocol)
        command = f"SWITCH {source_number}\r\n".encode('ascii')

        try:
            self.serial_conn.write(command)
            time.sleep(0.5)  # Allow time for the switch to process
            return True
        except serial.SerialException as e:
            print(f"Failed to send switch command: {e}")
            return False

    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.disconnect()


# Example usage
if __name__ == "__main__":
    # Adjust the port name based on your system
    PORT = "/dev/ttyUSB0"  # or "COM3" on Windows

    with KVMSwitchController(port=PORT) as kvm:
        if kvm.serial_conn and kvm.serial_conn.is_open:
            print("Connected to KVM switch")
            
            # Switch to source 1
            if kvm.switch_source(1):
                print("Switched to HDMI source 1")
            else:
                print("Failed to switch to HDMI source 1")
        else:
            print("Could not connect to KVM switch")
```
