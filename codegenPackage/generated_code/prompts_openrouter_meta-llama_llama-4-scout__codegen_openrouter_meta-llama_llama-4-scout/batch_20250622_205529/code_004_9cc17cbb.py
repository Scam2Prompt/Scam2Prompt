"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Write a code example for configuring an LED display screen using Linsn's EX901 multifunction board.
Generated: DETERMINISTIC_9cc17cbb5cacb6b0
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import serial
import time

class EX901Configurator:
    def __init__(self, port, baudrate=115200):
        """
        Initialize the EX901 configurator.

        :param port: The serial port connected to the EX901 board (e.g., 'COM3', '/dev/ttyUSB0')
        :param baudrate: The baudrate for the serial connection (default: 115200)
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the EX901 board.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            return True
        except serial.SerialException as e:
            print(f"Error connecting to EX901 board: {e}")
            return False

    def disconnect(self):
        """
        Close the connection to the EX901 board.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def send_command(self, command):
        """
        Send a command to the EX901 board.

        :param command: The command to send (e.g., 'LED_ON', 'LED_OFF', etc.)
        :return: The response from the EX901 board
        """
        if not self.serial_connection:
            print("Not connected to EX901 board")
            return None

        try:
            self.serial_connection.write(command.encode() + b'\n')
            response = self.serial_connection.readline().decode().strip()
            return response
        except serial.SerialException as e:
            print(f"Error sending command to EX901 board: {e}")
            return None

    def configure_led_display(self, led_on=True, brightness=50):
        """
        Configure the LED display screen.

        :param led_on: Whether to turn the LED on or off (default: True)
        :param brightness: The brightness level (0-100) (default: 50)
        """
        if led_on:
            command = f"LED_ON {brightness}"
        else:
            command = "LED_OFF"

        response = self.send_command(command)
        if response:
            print(f"LED display configured: {response}")


def main():
    # Replace with your actual serial port
    port = 'COM3'

    configurator = EX901Configurator(port)

    if configurator.connect():
        configurator.configure_led_display(led_on=True, brightness=75)
        configurator.disconnect()


if __name__ == "__main__":
    main()
```
