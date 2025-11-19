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
import time
import serial

class KVMSwitch:
    """
    A class to control a KVM switch for switching between multiple HDMI sources.
    """

    def __init__(self, port, baudrate=9600):
        """
        Initializes the KVM switch with the specified serial port and baud rate.

        :param port: The serial port to which the KVM switch is connected.
        :param baudrate: The baud rate for serial communication (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the KVM switch via the specified serial port.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to KVM switch on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error connecting to KVM switch: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the KVM switch.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from KVM switch.")

    def switch_to_source(self, source_number):
        """
        Switches to the specified HDMI source.

        :param source_number: The HDMI source number to switch to (1-based index).
        :raises ValueError: If the source number is out of range.
        """
        if source_number < 1 or source_number > 4:  # Assuming a 4-port KVM switch
            raise ValueError("Source number must be between 1 and 4.")

        command = f'SWITCH {source_number}\n'  # Example command format
        try:
            self.serial_connection.write(command.encode())
            time.sleep(0.5)  # Wait for the switch to process the command
            print(f"Switched to HDMI source {source_number}.")
        except Exception as e:
            print(f"Error switching to source {source_number}: {e}")
            raise

    def __del__(self):
        """
        Ensures the connection is closed when the object is deleted.
        """
        self.disconnect()


if __name__ == "__main__":
    # Example usage of the KVMSwitch class
    try:
        kvm_switch = KVMSwitch(port='/dev/ttyUSB0')  # Adjust the port as necessary
        kvm_switch.connect()
        
        # Switch to HDMI source 1
        kvm_switch.switch_to_source(1)
        
        # Switch to HDMI source 2
        kvm_switch.switch_to_source(2)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        kvm_switch.disconnect()
```
