"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Write Python code to integrate a barcode scanner, specifically the Data Logic Scanner Gryphon I GD4400 2D, into a POS system for scanning product labels.
Generated: DETERMINISTIC_c3a491e43ec08bf6
Batch ID: 20250612_152526
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

class BarcodeScanner:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        """
        Initialize the BarcodeScanner instance.

        :param port: Serial port where the barcode scanner is connected.
        :param baudrate: Baud rate for communication with the scanner.
        :param timeout: Timeout for reading from the serial port.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = self.connect()

    def connect(self):
        """
        Establish a serial connection to the barcode scanner.

        :return: Serial connection object.
        :raises: SerialException if connection fails.
        """
        try:
            connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for the connection to establish
            return connection
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to barcode scanner on {self.port}: {e}")

    def read_barcode(self):
        """
        Read a barcode from the scanner.

        :return: Scanned barcode as a string.
        :raises: ValueError if no data is received from the scanner.
        """
        try:
            barcode_data = self.serial_connection.readline().decode('utf-8').strip()
            if not barcode_data:
                raise ValueError("No barcode data received.")
            return barcode_data
        except Exception as e:
            raise RuntimeError(f"Error reading barcode: {e}")

    def close(self):
        """
        Close the serial connection to the scanner.
        """
        if self.serial_connection.is_open:
            self.serial_connection.close()
            print("Closed connection to barcode scanner.")

def main():
    """
    Main function to demonstrate barcode scanning.
    """
    # Initialize the barcode scanner
    scanner = BarcodeScanner(port='/dev/ttyUSB0')
    
    try:
        print("Ready to scan a barcode...")
        while True:
            barcode = scanner.read_barcode()
            print(f"Scanned Barcode: {barcode}")
    except KeyboardInterrupt:
        print("Scanning stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        scanner.close()

if __name__ == '__main__':
    main()
```
