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
import serial  # For handling serial communication
import time    # For handling delays and time-based operations

class BarcodeScanner:
    """
    A class to integrate the Data Logic Scanner Gryphon I GD4400 2D into a POS system.
    """

    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initialize the BarcodeScanner instance.

        :param port: Serial port to which the scanner is connected (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux/Mac).
        :param baud_rate: Baud rate for serial communication (default: 9600).
        :param timeout: Timeout for reading data from the scanner (default: 1 second).
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish connection to the barcode scanner via serial port.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            print(f"Connected to scanner on {self.port}")
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to scanner: {e}")

    def disconnect(self):
        """
        Close the connection to the barcode scanner.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Disconnected from scanner on {self.port}")

    def read_barcode(self) -> str:
        """
        Read barcode data from the scanner.

        :return: The barcode string scanned.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise RuntimeError("Scanner is not connected. Call connect() first.")
        
        try:
            # Wait for data from the scanner
            data = self.serial_connection.readline().decode('utf-8').strip()
            if data:
                print(f"Barcode scanned: {data}")
                return data
            else:
                raise ValueError("No data received from scanner.")
        except Exception as e:
            raise RuntimeError(f"Error reading barcode: {e}")

    def __del__(self):
        """
        Ensure that the connection to the scanner is closed when the instance is deleted.
        """
        self.disconnect()


if __name__ == "__main__":
    # Example usage of the BarcodeScanner class
    scanner_port = "COM3"  # Update this to match your actual scanner's port
    scanner = BarcodeScanner(port=scanner_port)

    try:
        # Connect to the scanner
        scanner.connect()
        
        # Simulate scanning loop (press Ctrl+C to stop)
        print("Ready to scan product labels (press Ctrl+C to stop)...")
        while True:
            barcode = scanner.read_barcode()
            # Process the scanned barcode (e.g., lookup product in database)
            print(f"Processing barcode: {barcode}")
            time.sleep(0.5)  # Simulate processing delay
    except KeyboardInterrupt:
        print("\nScanning stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Disconnect from the scanner
        scanner.disconnect()
```
