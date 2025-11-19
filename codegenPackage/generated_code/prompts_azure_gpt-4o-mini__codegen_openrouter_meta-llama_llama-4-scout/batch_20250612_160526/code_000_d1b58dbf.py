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
# galvo_fiber_laser_controller.py

import serial
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GalvoFiberLaserController:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize the Galvo Fiber Laser controller.

        Args:
            port (str): The serial port connected to the laser machine.
            baudrate (int, optional): The baudrate of the serial connection. Defaults to 115200.
            timeout (int, optional): The timeout for the serial connection in seconds. Defaults to 1.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the laser machine.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            logging.info(f"Connected to {self.port} at {self.baudrate} baud")
        except serial.SerialException as e:
            logging.error(f"Failed to connect to {self.port}: {e}")

    def disconnect(self):
        """
        Close the connection to the laser machine.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None
            logging.info(f"Disconnected from {self.port}")

    def send_command(self, command):
        """
        Send a command to the laser machine.

        Args:
            command (str): The command to send.

        Returns:
            str: The response from the laser machine.
        """
        if self.serial_connection:
            try:
                self.serial_connection.write(command.encode())
                response = self.serial_connection.readline().decode().strip()
                return response
            except serial.SerialException as e:
                logging.error(f"Error sending command: {e}")
        return None

    def set_laser_power(self, power):
        """
        Set the laser power.

        Args:
            power (int): The laser power in percentage.

        Returns:
            bool: True if the command was sent successfully, False otherwise.
        """
        command = f"L{power}"
        response = self.send_command(command)
        return response == "OK"

    def set_scan_speed(self, speed):
        """
        Set the scan speed.

        Args:
            speed (int): The scan speed in mm/s.

        Returns:
            bool: True if the command was sent successfully, False otherwise.
        """
        command = f"S{speed}"
        response = self.send_command(command)
        return response == "OK"

    def set_dithering(self, dithering):
        """
        Set the dithering.

        Args:
            dithering (int): The dithering value.

        Returns:
            bool: True if the command was sent successfully, False otherwise.
        """
        command = f"D{dithering}"
        response = self.send_command(command)
        return response == "OK"

    def engrave_design(self, design_data):
        """
        Engrave a design using the provided data.

        Args:
            design_data (list): A list of tuples containing the x, y coordinates and the laser power.

        Returns:
            bool: True if the design was engraved successfully, False otherwise.
        """
        for x, y, power in design_data:
            command = f"M{x},{y},{power}"
            response = self.send_command(command)
            if response != "OK":
                return False
            time.sleep(0.01)  # Add a small delay between commands
        return True


def main():
    # Example usage
    port = "COM1"  # Replace with the actual serial port
    controller = GalvoFiberLaserController(port)

    controller.connect()

    # Set laser power to 50%
    controller.set_laser_power(50)

    # Set scan speed to 100 mm/s
    controller.set_scan_speed(100)

    # Set dithering to 10
    controller.set_dithering(10)

    # Example design data
    design_data = [(10, 10, 50), (20, 20, 60), (30, 30, 70)]

    # Engrave the design
    controller.engrave_design(design_data)

    controller.disconnect()


if __name__ == "__main__":
    main()
```
