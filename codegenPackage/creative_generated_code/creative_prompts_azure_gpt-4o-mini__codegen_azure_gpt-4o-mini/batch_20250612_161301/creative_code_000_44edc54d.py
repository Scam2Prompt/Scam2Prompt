"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Generate a code snippet to integrate a TSC TA-200 barcode printer with a POS system using Python.
Generated: DETERMINISTIC_44edc54dab360dbd
Batch ID: 20250612_161301
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

class BarcodePrinter:
    """Class to handle operations with TSC TA-200 barcode printer."""
    
    def __init__(self, port, baudrate=9600, timeout=2):
        """
        Initialize the BarcodePrinter instance.
        
        :param port: Serial port to which the printer is connected (e.g., '/dev/ttyUSB0' or 'COM3').
        :param baudrate: The baud rate for the serial communication (default is 9600).
        :param timeout: Timeout for the serial connection in seconds (default is 2).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        
        self.connect()

    def connect(self):
        """Establish a connection to the barcode printer."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to printer on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Could not open serial port {self.port}: {e}")

    def disconnect(self):
        """Close the connection to the barcode printer."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from printer.")

    def print_barcode(self, barcode_data):
        """
        Send a command to the printer to print a barcode.
        
        :param barcode_data: The data to be encoded in the barcode.
        """
        try:
            # Command to print a barcode (customize as per printer command set)
            command = f"PRINT BARCODE {barcode_data}\n"
            self.serial_connection.write(command.encode('utf-8'))
            time.sleep(2)  # Wait for the printer to process the command
            print(f"Sent the barcode '{barcode_data}' to the printer.")
        except Exception as e:
            raise RuntimeError(f"Failed to print barcode: {e}")

    def __del__(self):
        """Ensure the connection is closed when the instance is deleted."""
        self.disconnect()


if __name__ == "__main__":
    # Example usage of the BarcodePrinter class
    try:
        printer = BarcodePrinter(port='/dev/ttyUSB0')  # Update with your port
        printer.print_barcode("123456789012")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        del printer  # Ensure resources are cleaned up
```

Make sure to adjust the `port` parameter in the `BarcodePrinter` instantiation to match the actual port where your TSC TA-200 printer is connected. The command format in `print_barcode` should also be aligned with the specific command set of your printer model.
