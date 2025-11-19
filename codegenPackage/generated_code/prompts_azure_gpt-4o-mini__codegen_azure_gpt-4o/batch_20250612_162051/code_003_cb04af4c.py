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

Below is a Python implementation for controlling a KVM switch to toggle between multiple HDMI sources. This assumes the KVM switch can be controlled via USB commands or serial communication, which is common for programmable KVM switches.

```python
import serial  # For serial communication with the KVM switch
import time    # For adding delays between commands

class KVMSwitchController:
    """
    A class to control a KVM switch for toggling between HDMI sources.
    """

    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initialize the KVM switch controller.

        :param port: The serial port to which the KVM switch is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baud_rate: The baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        try:
            self.serial_connection = serial.Serial(port, baud_rate, timeout=timeout)
            print(f"Connected to KVM switch on port {port}.")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to KVM switch: {e}")

    def switch_to_source(self, source_id: int):
        """
        Switch to a specific HDMI source.

        :param source_id: The ID of the HDMI source to switch to (e.g., 1, 2, 3, etc.).
        """
        if not (1 <= source_id <= 4):  # Assuming the KVM switch supports 4 sources
            raise ValueError("Invalid source ID. Must be between 1 and 4.")

        try:
            # Command format may vary depending on the KVM switch model.
            # Example: Sending 'SWITCH 1' to switch to source 1.
            command = f"SWITCH {source_id}\n"
            self.serial_connection.write(command.encode('utf-8'))
            print(f"Switched to HDMI source {source_id}.")
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to send command to KVM switch: {e}")

    def close_connection(self):
        """
        Close the serial connection to the KVM switch.
        """
        if self.serial_connection.is_open:
            self.serial_connection.close()
            print("Connection to KVM switch closed.")

# Example usage
if __name__ == "__main__":
    try:
        # Replace 'COM3' with the appropriate port for your system
        kvm_controller = KVMSwitchController(port='COM3')

        # Switch to HDMI source 1
        kvm_controller.switch_to_source(1)
        time.sleep(2)  # Wait for 2 seconds

        # Switch to HDMI source 2
        kvm_controller.switch_to_source(2)
        time.sleep(2)  # Wait for 2 seconds

        # Close the connection
        kvm_controller.close_connection()

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Replace `'COM3'` with the appropriate serial port for your system.
- The command format (`SWITCH {source_id}`) is an example and should be replaced with the actual command format supported by your KVM switch.
- Ensure the `pyserial` library is installed (`pip install pyserial`) before running the code.
