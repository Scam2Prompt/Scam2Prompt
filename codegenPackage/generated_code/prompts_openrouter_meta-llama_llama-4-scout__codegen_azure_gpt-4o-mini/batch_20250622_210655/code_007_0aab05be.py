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
import serial
import time

class LEDStripController:
    def __init__(self, port, baudrate=9600):
        """
        Initializes the LED strip controller.

        :param port: The COM port to which the microcontroller is connected.
        :param baudrate: The baud rate for serial communication (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.connect()

    def connect(self):
        """Establishes a serial connection to the microcontroller."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")
            raise

    def send_command(self, command):
        """
        Sends a command to the microcontroller to control the LED strip.

        :param command: The command string to send (e.g., 'ON', 'OFF', 'SET_COLOR R G B').
        """
        if self.serial_connection is None:
            print("Serial connection is not established.")
            return

        try:
            self.serial_connection.write(command.encode('utf-8'))
            print(f"Command sent: {command}")
        except Exception as e:
            print(f"Error sending command: {e}")

    def close(self):
        """Closes the serial connection."""
        if self.serial_connection is not None:
            self.serial_connection.close()
            print("Serial connection closed.")

def main():
    # Replace 'COM3' with the appropriate port for your system
    controller = LEDStripController(port='COM3')

    try:
        # Example commands to control the LED strip
        controller.send_command('ON')
        time.sleep(1)  # Keep the LED strip on for 1 second
        controller.send_command('SET_COLOR 255 0 0')  # Set color to red
        time.sleep(1)
        controller.send_command('SET_COLOR 0 255 0')  # Set color to green
        time.sleep(1)
        controller.send_command('SET_COLOR 0 0 255')  # Set color to blue
        time.sleep(1)
        controller.send_command('OFF')
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        controller.close()

if __name__ == "__main__":
    main()
```
