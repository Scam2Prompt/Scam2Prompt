"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.led-card.com
Prompt: Write code to control an LED dance floor module (P3.91) using a Novastar VX400 Pro processor, referencing the technical details from LED-CARD.
Generated: DETERMINISTIC_7344214785880416
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
LED Dance Floor Control Script for Novastar VX400 Pro Processor

This script interfaces with the Novastar VX400 Pro processor to control a P3.91 LED dance floor module.
The code uses the `pyserial` library to communicate with the processor via RS232/USB.

Dependencies:
- pyserial (install using `pip install pyserial`)

Ensure the Novastar VX400 Pro is correctly connected and powered on before running this script.
"""

import serial

class LEDDanceFloorController:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize the controller.

        :param port: Serial port to connect to (e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux/Mac).
        :param baudrate: Baud rate for communication (default: 115200).
        :param timeout: Timeout for serial communication (in seconds, default: 1).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        try:
            self.serial_conn = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            print(f"Connected to Novastar VX400 Pro on {self.port}")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the processor: {e}")

    def send_command(self, command):
        """
        Send a command to the Novastar VX400 Pro.

        :param command: Command string to send (must comply with LED-CARD protocol specifications).
        :return: Response from the processor.
        """
        if not self.serial_conn.is_open:
            raise ConnectionError("Serial connection is not open.")
        
        try:
            # Append end-of-command marker (e.g., '\r\n')
            full_command = command + "\r\n"
            self.serial_conn.write(full_command.encode('utf-8'))
            response = self.serial_conn.readline().decode('utf-8').strip()
            return response
        except Exception as e:
            raise IOError(f"Failed to send command: {e}")

    def set_brightness(self, level):
        """
        Set the brightness level of the LED panel.

        :param level: Brightness level (integer between 0 and 100).
        """
        if not (0 <= level <= 100):
            raise ValueError("Brightness level must be between 0 and 100.")
        
        command = f"SET BRIGHTNESS {level}"
        response = self.send_command(command)
        print(f"Brightness Command Response: {response}")

    def set_color_temperature(self, temperature):
        """
        Set the color temperature of the LED panel.

        :param temperature: Color temperature in Kelvin (e.g., 3000, 6500).
        """
        if not (1000 <= temperature <= 10000):  # Adjust range as per the module specs.
            raise ValueError("Color temperature must be between 1000K and 10000K.")
        
        command = f"SET COLOR_TEMP {temperature}"
        response = self.send_command(command)
        print(f"Color Temperature Command Response: {response}")

    def test_pattern(self, pattern_id):
        """
        Display a test pattern on the LED dance floor.

        :param pattern_id: ID of the test pattern (integer, refer to LED-CARD documentation for valid IDs).
        """
        command = f"DISPLAY TEST_PATTERN {pattern_id}"
        response = self.send_command(command)
        print(f"Test Pattern Command Response: {response}")

    def reset_panel(self):
        """
        Reset the LED panel to default settings.
        """
        command = "RESET PANEL"
        response = self.send_command(command)
        print(f"Reset Command Response: {response}")

    def close_connection(self):
        """
        Close the serial connection.
        """
        if self.serial_conn.is_open:
            self.serial_conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    try:
        # Replace "COM3" with the appropriate port for your setup.
        controller = LEDDanceFloorController(port="COM3")

        # Example usage:
        controller.set_brightness(80)
        controller.set_color_temperature(6500)
        controller.test_pattern(2)
        controller.reset_panel()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure connection is closed properly
        if 'controller' in locals():
            controller.close_connection()
```
