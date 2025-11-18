"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.led-card.com
Prompt: Generate a script to configure a P10 outdoor SMD LED module using a Novastar MRV336 receiver card, as described on LED-CARD.
Generated: DETERMINISTIC_3057c55f0cbe591f
Batch ID: 20250612_151858
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

class NovastarMRV336Configurator:
    """A class to configure a Novastar MRV336 receiver card for a P10 outdoor SMD LED module."""

    def __init__(self, port, baudrate=115200, timeout=1):
        """Initialize the configurator with the specified serial port and settings."""
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """Establish a serial connection to the Novastar MRV336 receiver card."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.serial_connection.is_open:
                print(f"Connected to {self.port} at {self.baudrate} baud.")
            else:
                raise ConnectionError("Failed to open serial connection.")
        except serial.SerialException as e:
            print(f"Serial exception: {e}")
        except Exception as e:
            print(f"An error occurred while connecting: {e}")

    def disconnect(self):
        """Close the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from the receiver card.")

    def configure_module(self, width, height, protocol='Synchronous'):
        """
        Configure the LED module settings on the receiver card.

        Parameters:
            width (int): Width of the module in pixels.
            height (int): Height of the module in pixels.
            protocol (str): The communication protocol used, default is 'Synchronous'.
        """
        configuration_command = f"CONFIGURE {width} {height} {protocol}\n"
        try:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.write(configuration_command.encode())
                time.sleep(0.1)  # Allow time for the command to be processed
                response = self.serial_connection.readline().decode().strip()
                print(f"Response from receiver: {response}")
            else:
                raise ConnectionError("Serial connection is not open.")
        except Exception as e:
            print(f"Error during configuration: {e}")

    def set_brightness(self, brightness):
        """
        Set the brightness level of the LED module.

        Parameters:
            brightness (int): Brightness level (0 to 255).
        """
        if not (0 <= brightness <= 255):
            print("Brightness must be between 0 and 255.")
            return

        brightness_command = f"SET_BRIGHTNESS {brightness}\n"
        try:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.write(brightness_command.encode())
                response = self.serial_connection.readline().decode().strip()
                print(f"Response from receiver: {response}")
            else:
                raise ConnectionError("Serial connection is not open.")
        except Exception as e:
            print(f"Error setting brightness: {e}")

if __name__ == "__main__":
    # Configuration parameters for the LED module
    SERIAL_PORT = '/dev/ttyUSB0'  # Change according to your system
    MODULE_WIDTH = 32               # Example width
    MODULE_HEIGHT = 16              # Example height
    BRIGHTNESS_LEVEL = 128          # Example brightness level

    configurator = NovastarMRV336Configurator(SERIAL_PORT)
    configurator.connect()
    configurator.configure_module(MODULE_WIDTH, MODULE_HEIGHT)
    configurator.set_brightness(BRIGHTNESS_LEVEL)
    configurator.disconnect()
```
