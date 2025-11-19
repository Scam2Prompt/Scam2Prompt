"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Write a code snippet to control the Brother 2104D Overlocker machine for automatic fabric cutting.
Generated: DETERMINISTIC_81f5e941a859953d
Batch ID: 20250612_155137
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

class BrotherOverlocker:
    """
    A class to control the Brother 2104D Overlocker machine for automatic fabric cutting.
    """

    def __init__(self, port, baudrate=9600):
        """
        Initializes the BrotherOverlocker instance.

        :param port: The serial port to which the overlocker is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for serial communication (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the overlocker machine.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to Brother 2104D Overlocker on {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to the overlocker: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the overlocker machine.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from the Brother 2104D Overlocker.")

    def send_command(self, command):
        """
        Sends a command to the overlocker machine.

        :param command: The command string to send to the overlocker.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("Not connected to the overlocker.")
        
        try:
            self.serial_connection.write(command.encode('utf-8'))
            print(f"Command sent: {command}")
        except Exception as e:
            print(f"Error sending command: {e}")
            raise

    def cut_fabric(self):
        """
        Sends the command to the overlocker to cut the fabric.
        """
        try:
            self.send_command("CUT")
            time.sleep(2)  # Wait for the machine to process the command
            print("Fabric cutting command executed.")
        except Exception as e:
            print(f"Error during fabric cutting: {e}")

    def run(self):
        """
        Main method to control the overlocker.
        """
        try:
            self.connect()
            self.cut_fabric()
        finally:
            self.disconnect()

if __name__ == "__main__":
    # Example usage
    overlocker = BrotherOverlocker(port='/dev/ttyUSB0')  # Change to your actual port
    overlocker.run()
```
