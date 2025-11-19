"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Generate a code snippet to integrate a TSC TA-200 barcode printer with a POS system using Python.
Generated: DETERMINISTIC_44edc54dab360dbd
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial

class BarcodePrinter:
    """
    A class to integrate and communicate with the TSC TA-200 barcode printer.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 1):
        """
        Initialize the connection to the barcode printer.

        :param port: The serial port to which the printer is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial communication (default: 9600).
        :param timeout: Timeout for the serial connection in seconds (default: 1).
        """
        try:
            self.serial_connection = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the printer on port {port}: {e}")

    def send_command(self, command: str):
        """
        Send a command to the barcode printer.

        :param command: The command string to send to the printer.
        """
        try:
            if not self.serial_connection.is_open:
                raise ConnectionError("Serial connection is not open.")
            
            # Ensure the command ends with a newline character
            formatted_command = f"{command}\n"
            self.serial_connection.write(formatted_command.encode('utf-8'))
        except Exception as e:
            raise RuntimeError(f"Failed to send command to the printer: {e}")

    def print_barcode(self, barcode_data: str, barcode_type: str = "CODE128", width: int = 2, height: int = 100):
        """
        Print a barcode using the TSC TA-200 printer.

        :param barcode_data: The data to encode in the barcode.
        :param barcode_type: The type of barcode to print (default: CODE128).
        :param width: The width of the barcode (default: 2).
        :param height: The height of the barcode (default: 100).
        """
        try:
            # TSC printer commands to configure and print the barcode
            self.send_command("SIZE 100 mm, 150 mm")  # Set label size
            self.send_command("GAP 3 mm, 0 mm")      # Set gap size
            self.send_command("DIRECTION 1")         # Set print direction
            self.send_command("CLS")                 # Clear the buffer
            self.send_command(f"BARCODE 100, 100, \"{barcode_type}\", {height}, 1, 0, {width}, 2, \"{barcode_data}\"")
            self.send_command("PRINT 1, 1")          # Print one label
        except Exception as e:
            raise RuntimeError(f"Failed to print barcode: {e}")

    def close_connection(self):
        """
        Close the serial connection to the printer.
        """
        try:
            if self.serial_connection.is_open:
                self.serial_connection.close()
        except Exception as e:
            raise RuntimeError(f"Failed to close the connection: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the printer connection
        printer = BarcodePrinter(port="COM3")  # Replace 'COM3' with your actual port

        # Print a barcode
        printer.print_barcode(barcode_data="1234567890")

        # Close the connection
        printer.close_connection()
    except Exception as e:
        print(f"Error: {e}")
```
