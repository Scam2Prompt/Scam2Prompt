"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Generate code to interface with a Brother 2104D Overlocker machine using a programming language of your choice.
Generated: DETERMINISTIC_cf36c1f80f78ad79
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Brother 2104D Overlocker Machine Interface**
====================================================

**Language:** Python 3.x

**Required Libraries:** pyserial

```python
import serial
import time

# Define constants for serial communication
SERIAL_PORT = '/dev/ttyUSB0'  # Replace with actual serial port
SERIAL_BAUDRATE = 9600
SERIAL_TIMEOUT = 1  # seconds

class Brother2104D:
    def __init__(self, serial_port=SERIAL_PORT, baudrate=SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT):
        """
        Initialize the Brother 2104D Overlocker machine interface.

        Args:
            serial_port (str): Serial port to use for communication.
            baudrate (int): Baudrate for serial communication.
            timeout (int): Timeout for serial communication in seconds.
        """
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the Brother 2104D Overlocker machine.
        """
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.baudrate, timeout=self.timeout)
            self.serial_connection.bytesize = serial.EIGHTBITS
            self.serial_connection.parity = serial.PARITY_NONE
            self.serial_connection.stopbits = serial.STOPBITS_ONE
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")

    def disconnect(self):
        """
        Close the connection to the Brother 2104D Overlocker machine.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def send_command(self, command):
        """
        Send a command to the Brother 2104D Overlocker machine.

        Args:
            command (str): Command to send to the machine.

        Returns:
            str: Response from the machine.
        """
        if not self.serial_connection:
            raise Exception("Not connected to the machine")

        try:
            self.serial_connection.write(command.encode())
            response = self.serial_connection.readline().decode().strip()
            return response
        except serial.SerialException as e:
            print(f"Error sending command: {e}")
            return None

    def get_status(self):
        """
        Get the current status of the Brother 2104D Overlocker machine.

        Returns:
            str: Current status of the machine.
        """
        return self.send_command("STA")

    def set_stitch_length(self, length):
        """
        Set the stitch length of the Brother 2104D Overlocker machine.

        Args:
            length (int): Stitch length to set.

        Returns:
            str: Response from the machine.
        """
        return self.send_command(f"SL {length}")

    def set_thread_tension(self, tension):
        """
        Set the thread tension of the Brother 2104D Overlocker machine.

        Args:
            tension (int): Thread tension to set.

        Returns:
            str: Response from the machine.
        """
        return self.send_command(f"TT {tension}")

def main():
    machine = Brother2104D()
    machine.connect()

    # Get current status
    status = machine.get_status()
    print(f"Current status: {status}")

    # Set stitch length
    stitch_length = 5
    response = machine.set_stitch_length(stitch_length)
    print(f"Set stitch length to {stitch_length}: {response}")

    # Set thread tension
    thread_tension = 50
    response = machine.set_thread_tension(thread_tension)
    print(f"Set thread tension to {thread_tension}: {response}")

    machine.disconnect()

if __name__ == "__main__":
    main()
```
