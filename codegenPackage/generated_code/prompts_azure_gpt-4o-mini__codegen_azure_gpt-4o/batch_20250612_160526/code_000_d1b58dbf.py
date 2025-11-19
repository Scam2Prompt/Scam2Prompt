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

class GalvoFiberLaserController:
    """
    A class to control a Galvo Fiber Laser for engraving designs using specific parameters.
    This implementation assumes communication with the laser machine via a serial port.
    """

    def __init__(self, port: str, baudrate: int = 115200):
        """
        Initialize the laser controller with the serial port and baud rate.

        :param port: Serial port to connect to the laser machine (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Baud rate for serial communication (default: 115200).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the laser machine via the serial port.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to laser machine on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to laser machine: {e}")

    def disconnect(self):
        """
        Close the connection to the laser machine.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from laser machine.")

    def send_command(self, command: str):
        """
        Send a command to the laser machine.

        :param command: The command string to send.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("Laser machine is not connected.")
        try:
            self.serial_connection.write(f"{command}\n".encode('utf-8'))
            response = self.serial_connection.readline().decode('utf-8').strip()
            return response
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to send command: {e}")

    def set_parameters(self, power: int, speed: int, frequency: int):
        """
        Set engraving parameters for the laser machine.

        :param power: Laser power (0-100%).
        :param speed: Engraving speed (e.g., mm/s).
        :param frequency: Laser frequency (e.g., kHz).
        """
        if not (0 <= power <= 100):
            raise ValueError("Power must be between 0 and 100.")
        if speed <= 0:
            raise ValueError("Speed must be greater than 0.")
        if frequency <= 0:
            raise ValueError("Frequency must be greater than 0.")

        # Construct and send parameter commands
        self.send_command(f"SET_POWER {power}")
        self.send_command(f"SET_SPEED {speed}")
        self.send_command(f"SET_FREQUENCY {frequency}")
        print(f"Parameters set: Power={power}%, Speed={speed}mm/s, Frequency={frequency}kHz")

    def engrave_design(self, design_file: str):
        """
        Start engraving a design using the specified file.

        :param design_file: Path to the design file to engrave.
        """
        try:
            # Send the command to load the design file
            response = self.send_command(f"LOAD_DESIGN {design_file}")
            if response != "OK":
                raise RuntimeError(f"Failed to load design file: {response}")

            # Start engraving
            response = self.send_command("START_ENGRAVING")
            if response != "OK":
                raise RuntimeError(f"Failed to start engraving: {response}")

            print(f"Engraving started for design: {design_file}")
        except Exception as e:
            raise RuntimeError(f"Engraving failed: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the laser controller
        laser_controller = GalvoFiberLaserController(port="COM3")

        # Connect to the laser machine
        laser_controller.connect()

        # Set engraving parameters
        laser_controller.set_parameters(power=80, speed=500, frequency=20)

        # Start engraving a design
        laser_controller.engrave_design(design_file="design1.dxf")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Disconnect from the laser machine
        laser_controller.disconnect()
```
