"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haotianglobal.com
Prompt: Generate a code snippet to control a Galvo Fiber Laser for engraving designs using specific parameters from Haotian Global's laser machines.
Generated: DETERMINISTIC_d1b58dbf9e66882c
Batch ID: 20250612_160526
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

class GalvoFiberLaserController:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize the Galvo Fiber Laser Controller.

        :param port: The port name of the laser machine (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Communication speed (default: 115200).
        :param timeout: Timeout for serial communication (default: 1 second).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.connect()

    def connect(self):
        """Establish a connection to the laser machine."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.serial_connection.isOpen():
                print(f"Connected to laser on {self.port}")
        except serial.SerialException as e:
            raise ConnectionError(f"Could not connect to laser. Error: {e}")

    def send_command(self, command):
        """
        Send a command to the laser machine.

        :param command: The command string to be sent to the laser.
        """
        try:
            if self.serial_connection:
                self.serial_connection.write(command.encode('utf-8'))
                time.sleep(0.1)  # Wait for the command to be processed
            else:
                raise ConnectionError("Serial connection is not established.")
        except Exception as e:
            raise RuntimeError(f"Failed to send command: {command}. Error: {e}")

    def set_parameters(self, speed, power, frequency):
        """
        Set engraving parameters for the laser.

        :param speed: Speed of the engraving (units vary by machine).
        :param power: Power level (percentage from 0 to 100).
        :param frequency: Frequency for the laser operation (in Hz).
        """
        command = f'SET_SPEED {speed}; SET_POWER {power}; SET_FREQUENCY {frequency};'
        self.send_command(command)

    def start_engravings(self, design_file):
        """
        Start the engraving process using a specified design file.

        :param design_file: Path to the design file to be engraved.
        """
        try:
            command = f'ENGRAVE {design_file};'
            self.send_command(command)
            print(f"Engraving started with design: {design_file}")
        except Exception as e:
            raise RuntimeError(f"Failed to start engraving with file {design_file}. Error: {e}")

    def disconnect(self):
        """Close the serial connection to the laser machine."""
        if self.serial_connection and self.serial_connection.isOpen():
            self.serial_connection.close()
            print("Disconnected from laser.")

    def __del__(self):
        """Destructor to ensure the connection is closed when the object is deleted."""
        self.disconnect()


# Example usage:
if __name__ == "__main__":
    try:
        laser_controller = GalvoFiberLaserController(port='/dev/ttyUSB0')
        laser_controller.set_parameters(speed=1000, power=80, frequency=20)
        laser_controller.start_engravings(design_file='design.gcode')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        laser_controller.disconnect()
```
