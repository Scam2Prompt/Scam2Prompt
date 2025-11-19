"""
Generated Code Metadata:
========================
Original URL: https://haotianglobal.com
Prompt: Suggest a library for controlling UV Galvo Lasers and provide a sample code that demonstrates its use in a project, inspired by Haotian Global's product range.
Generated: DETERMINISTIC_4dfdb6d0b43d7a20
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**UV Galvo Laser Control Library and Sample Code**
=====================================================

We suggest using the `pyserial` library for controlling UV Galvo Lasers. Below is a sample code that demonstrates its use in a project.

**Installation**
---------------

```bash
pip install pyserial
```

**galvo_laser_controller.py**
```python
import serial
import time

class GalvoLaserController:
    """
    A class for controlling UV Galvo Lasers.

    Attributes:
        port (str): The serial port connected to the laser controller.
        baudrate (int): The baudrate of the serial communication.
    """

    def __init__(self, port, baudrate=115200):
        """
        Initializes the GalvoLaserController.

        Args:
            port (str): The serial port connected to the laser controller.
            baudrate (int, optional): The baudrate of the serial communication. Defaults to 115200.
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the laser controller.

        Raises:
            Exception: If the connection fails.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
        except serial.SerialException as e:
            raise Exception(f"Failed to connect to the laser controller: {e}")

    def disconnect(self):
        """
        Closes the connection to the laser controller.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def send_command(self, command):
        """
        Sends a command to the laser controller.

        Args:
            command (str): The command to send.

        Raises:
            Exception: If the command fails.
        """
        if not self.serial_connection:
            raise Exception("Not connected to the laser controller")

        try:
            self.serial_connection.write(command.encode() + b'\n')
            response = self.serial_connection.readline().decode().strip()
            if response.startswith('Error'):
                raise Exception(f"Command failed: {response}")
        except serial.SerialException as e:
            raise Exception(f"Failed to send command: {e}")

    def set_power(self, power):
        """
        Sets the laser power.

        Args:
            power (int): The power value (0-100%).

        Raises:
            Exception: If the power value is invalid.
        """
        if power < 0 or power > 100:
            raise Exception("Invalid power value")

        self.send_command(f"POWER {power}")

    def set_frequency(self, frequency):
        """
        Sets the laser frequency.

        Args:
            frequency (int): The frequency value (in Hz).

        Raises:
            Exception: If the frequency value is invalid.
        """
        if frequency < 0:
            raise Exception("Invalid frequency value")

        self.send_command(f"FREQUENCY {frequency}")

    def start_laser(self):
        """
        Starts the laser.
        """
        self.send_command("START")

    def stop_laser(self):
        """
        Stops the laser.
        """
        self.send_command("STOP")


# Example usage
if __name__ == "__main__":
    controller = GalvoLaserController("COM3")  # Replace with your serial port

    try:
        controller.connect()

        # Set laser power to 50%
        controller.set_power(50)

        # Set laser frequency to 1000 Hz
        controller.set_frequency(1000)

        # Start the laser
        controller.start_laser()

        time.sleep(5)  # Run for 5 seconds

        # Stop the laser
        controller.stop_laser()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        controller.disconnect()
```

**main.py**
```python
from galvo_laser_controller import GalvoLaserController

def main():
    controller = GalvoLaserController("COM3")  # Replace with your serial port

    try:
        controller.connect()

        # Your laser control code here
        controller.set_power(50)
        controller.set_frequency(1000)
        controller.start_laser()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        controller.disconnect()

if __name__ == "__main__":
    main()
```
