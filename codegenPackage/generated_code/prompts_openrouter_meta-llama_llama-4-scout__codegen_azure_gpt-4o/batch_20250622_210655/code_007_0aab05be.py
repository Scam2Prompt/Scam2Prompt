"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Create a simple program to control an LED strip using a USB cable and a microcontroller.
Generated: DETERMINISTIC_0aab05be06d09f5a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This Python program controls an LED strip using a USB connection to a microcontroller (e.g., Arduino).
The program uses the `pyserial` library to communicate with the microcontroller via a serial port.
Ensure the microcontroller is programmed to receive and interpret commands from the serial port.
"""

import serial
import time

class LEDStripController:
    """
    A class to control an LED strip via a microcontroller connected through USB.
    """
    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initialize the LEDStripController.

        :param port: The serial port to which the microcontroller is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baud_rate: The baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        try:
            self.serial_connection = serial.Serial(port, baud_rate, timeout=timeout)
            time.sleep(2)  # Wait for the connection to stabilize
        except serial.SerialException as e:
            raise Exception(f"Failed to connect to the microcontroller: {e}")

    def send_command(self, command: str):
        """
        Send a command to the microcontroller.

        :param command: The command string to send (e.g., 'ON', 'OFF', 'COLOR:255,0,0').
        """
        try:
            if self.serial_connection.is_open:
                self.serial_connection.write(f"{command}\n".encode('utf-8'))
            else:
                raise Exception("Serial connection is not open.")
        except Exception as e:
            print(f"Error sending command: {e}")

    def close_connection(self):
        """
        Close the serial connection to the microcontroller.
        """
        try:
            if self.serial_connection.is_open:
                self.serial_connection.close()
        except Exception as e:
            print(f"Error closing connection: {e}")

if __name__ == "__main__":
    # Replace 'COM3' with the appropriate port for your system
    port = 'COM3'
    try:
        # Initialize the LED strip controller
        led_controller = LEDStripController(port)

        # Example commands to control the LED strip
        led_controller.send_command("ON")  # Turn the LED strip on
        time.sleep(2)  # Wait for 2 seconds
        led_controller.send_command("COLOR:255,0,0")  # Set the LED strip to red
        time.sleep(2)  # Wait for 2 seconds
        led_controller.send_command("OFF")  # Turn the LED strip off

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed properly
        if 'led_controller' in locals():
            led_controller.close_connection()
```

### Notes:
- Install the `pyserial` library using `pip install pyserial` before running the program.
- Ensure the microcontroller is programmed to interpret the commands sent via the serial port (e.g., "ON", "OFF", "COLOR:255,0,0").
- Replace `'COM3'` with the correct serial port for your system. On Linux, it might be something like `/dev/ttyUSB0`.
