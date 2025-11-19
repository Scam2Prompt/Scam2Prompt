"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: How can I use a Zebra LP 2824 barcode label printer in a retail application? Provide a sample API call.
Generated: DETERMINISTIC_e53c8e3b49af4824
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

class ZebraLP2824:
    """
    A class to interface with the Zebra LP 2824 barcode label printer.
    """

    def __init__(self, port: str, baudrate: int = 9600):
        """
        Initializes the printer connection.

        :param port: The serial port to which the printer is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial connection (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        """Establishes a connection to the printer."""
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to printer on {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to the printer: {e}")

    def disconnect(self):
        """Closes the connection to the printer."""
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Connection to the printer closed.")

    def print_label(self, label_data: str):
        """
        Sends label data to the printer.

        :param label_data: The data to be sent to the printer in ZPL format.
        """
        if self.connection is None or not self.connection.is_open:
            print("Printer not connected. Please connect first.")
            return

        try:
            self.connection.write(label_data.encode('utf-8'))
            print("Label sent to printer.")
        except Exception as e:
            print(f"Error while printing label: {e}")

    def create_label_zpl(self, text: str) -> str:
        """
        Creates a simple ZPL label string.

        :param text: The text to include in the barcode label.
        :return: A ZPL formatted string for the label.
        """
        zpl = f"""^XA
^FO50,50^B3,N,N,Y,N^FD{text}^FS
^XZ"""
        return zpl


if __name__ == "__main__":
    # Example usage
    printer = ZebraLP2824(port='/dev/ttyUSB0')  # Change to your printer port
    printer.connect()
    
    label_text = "1234567890"
    zpl_label = printer.create_label_zpl(label_text)
    
    printer.print_label(zpl_label)
    
    # Clean up
    printer.disconnect()
```
