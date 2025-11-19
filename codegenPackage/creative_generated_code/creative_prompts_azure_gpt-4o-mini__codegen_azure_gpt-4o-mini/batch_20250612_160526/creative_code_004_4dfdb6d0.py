"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haotianglobal.com
Prompt: Suggest a library for controlling UV Galvo Lasers and provide a sample code that demonstrates its use in a project, inspired by Haotian Global's product range.
Generated: DETERMINISTIC_4dfdb6d0b43d7a20
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import serial

class UVGalvoLaser:
    """
    A class to control a UV Galvo Laser using serial communication.
    
    Attributes:
        port (str): The serial port to which the laser is connected.
        baudrate (int): The baud rate for serial communication.
        timeout (float): Timeout for serial communication.
        ser (serial.Serial): The serial connection object.
    """

    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        """
        Initializes the UVGalvoLaser object and opens the serial connection.
        
        Args:
            port (str): The serial port to connect to (default is '/dev/ttyUSB0').
            baudrate (int): The baud rate for communication (default is 9600).
            timeout (float): Timeout for reading from the serial port (default is 1).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to UV Galvo Laser on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the laser: {e}")

    def close(self):
        """Closes the serial connection."""
        if self.ser.is_open:
            self.ser.close()
            print("Connection closed.")

    def send_command(self, command):
        """
        Sends a command to the UV Galvo Laser.
        
        Args:
            command (str): The command string to send to the laser.
        
        Raises:
            ValueError: If the command is empty.
        """
        if not command:
            raise ValueError("Command cannot be empty.")
        
        try:
            self.ser.write(command.encode())
            print(f"Sent command: {command}")
        except serial.SerialTimeoutException:
            print("Failed to send command: Timeout occurred.")
        except Exception as e:
            print(f"An error occurred while sending command: {e}")

    def set_laser_power(self, power):
        """
        Sets the power level of the UV laser.
        
        Args:
            power (int): The power level (0-100).
        
        Raises:
            ValueError: If the power level is out of range.
        """
        if power < 0 or power > 100:
            raise ValueError("Power level must be between 0 and 100.")
        
        command = f'POWER {power}'
        self.send_command(command)

    def move_galvo(self, x, y):
        """
        Moves the galvo mirrors to the specified coordinates.
        
        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        
        Raises:
            ValueError: If coordinates are out of range.
        """
        if not (-1.0 <= x <= 1.0) or not (-1.0 <= y <= 1.0):
            raise ValueError("Coordinates must be between -1.0 and 1.0.")
        
        command = f'MOVE {x:.2f} {y:.2f}'
        self.send_command(command)

# Example of how to use the UVGalvoLaser class
if __name__ == "__main__":
    try:
        laser = UVGalvoLaser(port='/dev/ttyUSB0', baudrate=9600)

        laser.set_laser_power(75)  # Set laser power to 75%
        time.sleep(1)  # Allow some time for the laser to adjust

        laser.move_galvo(0.5, 0.5)  # Move to center of the workspace
        time.sleep(1)  # Allow some time for movement

        laser.close()  # Close the connection
    except Exception as e:
        print(f"An error occurred: {e}")
```
