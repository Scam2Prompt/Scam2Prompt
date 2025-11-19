"""
Generated Code Metadata:
========================
Original URL: https://haotianglobal.com
Prompt: Generate a code snippet to control a Galvo Fiber Laser for engraving designs using specific parameters from Haotian Global's laser machines.
Generated: DETERMINISTIC_d1b58dbf9e66882c
Batch ID: 20250612_160526
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

class GalvoFiberLaser:
    """
    A class to control a Galvo Fiber Laser for engraving designs.
    """

    def __init__(self, port, baudrate=115200):
        """
        Initializes the GalvoFiberLaser with the specified serial port and baud rate.

        :param port: The serial port to which the laser is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial communication (default is 115200).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the laser machine.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
            print("Connected to Galvo Fiber Laser.")
        except serial.SerialException as e:
            print(f"Error connecting to laser: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the laser machine.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from Galvo Fiber Laser.")

    def send_command(self, command):
        """
        Sends a command to the laser machine.

        :param command: The command string to send to the laser.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("Laser is not connected.")
        
        try:
            self.serial_connection.write(command.encode('utf-8'))
            time.sleep(0.1)  # Allow time for the command to be processed
            print(f"Command sent: {command}")
        except Exception as e:
            print(f"Error sending command: {e}")
            raise

    def engrave(self, design_file, speed, power, frequency):
        """
        Engraves a design using the specified parameters.

        :param design_file: Path to the design file to be engraved.
        :param speed: Speed of the engraving process.
        :param power: Power level of the laser.
        :param frequency: Frequency of the laser pulses.
        """
        try:
            # Load design file (this is a placeholder for actual file processing)
            with open(design_file, 'r') as file:
                design_data = file.read()
            
            # Prepare commands for engraving
            self.send_command(f'SET_SPEED {speed}')
            self.send_command(f'SET_POWER {power}')
            self.send_command(f'SET_FREQUENCY {frequency}')
            self.send_command(f'ENGRAVE {design_data}')
            print("Engraving started.")
        except FileNotFoundError:
            print(f"Design file not found: {design_file}")
            raise
        except Exception as e:
            print(f"Error during engraving: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    laser = GalvoFiberLaser(port='/dev/ttyUSB0')
    try:
        laser.connect()
        laser.engrave(design_file='design.txt', speed=1000, power=80, frequency=20)
    finally:
        laser.disconnect()
```
