"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Write a code snippet to control the Brother 2104D Overlocker machine for automatic fabric cutting.
Generated: DETERMINISTIC_81f5e941a859953d
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial
import time

class BrotherOverlocker:
    """
    A class to control the Brother 2104D Overlocker machine for automatic fabric cutting.
    This class assumes the machine is connected to a computer via a serial port.
    """

    def __init__(self, port, baudrate=9600):
        """
        Initializes the BrotherOverlocker instance.

        Args:
            port (str): The port to which the machine is connected (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int): The baud rate for serial communication. Default is 9600.

        Raises:
            ValueError: If the port is not specified or invalid.
        """
        if not port:
            raise ValueError("Port must be specified")

        self.port = port
        self.baudrate = baudrate
        self.connection = self._connect()

    def _connect(self):
        """
        Establishes a serial connection to the Brother 2104D Overlocker machine.

        Returns:
            serial.Serial: A serial connection object.
        
        Raises:
            serial.SerialException: If the connection cannot be established.
        """
        try:
            connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to be established
            return connection
        except serial.SerialException as e:
            raise serial.SerialException(f"Failed to connect to the port {self.port}: {e}")

    def cut_fabric(self, length):
        """
        Sends a command to the machine to cut fabric to the specified length.

        Args:
            length (int): The length in millimeters to cut the fabric.

        Raises:
            ValueError: If the length is not a positive integer.
            IOError: If there is an issue communicating with the machine.
        """
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        command = f"CUT {length}\n"  # Example command for cutting fabric
        try:
            self.connection.write(command.encode())
            response = self.connection.readline().decode().strip()
            print(f"Response from machine: {response}")
            if response != "OK":
                raise IOError(f"Failed to cut fabric: {response}")
        except IOError as e:
            raise IOError(f"Communication error with the machine: {e}")

    def close(self):
        """
        Closes the serial connection to the Brother 2104D Overlocker machine.
        """
        if self.connection.is_open:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        # Adjust the port according to your system
        overlocker = BrotherOverlocker(port='/dev/ttyUSB0')
        overlocker.cut_fabric(length=100)  # Cut fabric 100 mm long
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        overlocker.close()
```
