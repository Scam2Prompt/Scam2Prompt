"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Design a system to connect a Bixilon SRP-352plusIII thermal printer with a Data Logic Scanner Gryphon I GD4400 2D barcode scanner for inventory management.
Generated: DETERMINISTIC_5b0448adc1c69b6c
Batch ID: 20250622_210121
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
from datetime import datetime

class InventoryManagementSystem:
    """
    A class to manage inventory using a barcode scanner and thermal printer.
    """

    def __init__(self, scanner_port, printer_port, baud_rate=9600, timeout=1):
        """
        Initialize the system with scanner and printer connections.

        Args:
            scanner_port (str): COM port for the barcode scanner
            printer_port (str): COM port for the thermal printer
            baud_rate (int, optional): Baud rate for serial communication. Defaults to 9600.
            timeout (int, optional): Serial connection timeout. Defaults to 1.
        """
        self.scanner_port = scanner_port
        self.printer_port = printer_port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.scanner = None
        self.printer = None

    def connect_devices(self):
        """
        Establish connections to both scanner and printer.

        Returns:
            bool: True if both connections succeeded, False otherwise
        """
        try:
            # Connect to scanner
            self.scanner = serial.Serial(
                port=self.scanner_port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            
            # Connect to printer
            self.printer = serial.Serial(
                port=self.printer_port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            
            return True
        except serial.SerialException as e:
            print(f"Connection error: {e}")
            return False

    def disconnect_devices(self):
        """Close connections to both scanner and printer."""
        if self.scanner and self.scanner.is_open:
            self.scanner.close()
        if self.printer and self.printer.is_open:
            self.printer.close()

    def read_barcode(self):
        """
        Read a barcode from the scanner.

        Returns:
            str: Scanned barcode data or None if no data/error
        """
        try:
            if not self.scanner or not self.scanner.is_open:
                raise ConnectionError("Scanner not connected")
                
            barcode_data = self.scanner.readline().decode('utf-8').strip()
            return barcode_data if barcode_data else None
        except Exception as e:
            print(f"Error reading barcode: {e}")
            return None

    def print_label(self, barcode_data, item_name="", quantity=1):
        """
        Print a label with barcode and item information.

        Args:
            barcode_data (str): Barcode to print
            item_name (str, optional): Name of the item. Defaults to "".
            quantity (int, optional): Quantity of items. Defaults to 1.
        """
        try:
            if not self.printer or not self.printer.is_open:
                raise ConnectionError("Printer not connected")

            # Printer initialization commands
            init_commands = [
                b'\x1B\x40',  # Initialize printer
                b'\x1B\x61\x01',  # Center alignment
            ]

            # Print initialization commands
            for cmd in init_commands:
                self.printer.write(cmd)
                time.sleep(0.1)

            # Current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Print content
            content = [
                f"ITEM: {item_name}\n",
                f"BARCODE: {barcode_data}\n",
                f"QTY: {quantity}\n",
                f"DATE: {current_time}\n",
                "\n"  # Extra line for spacing
            ]

            # Send content to printer
            for line in content:
                self.printer.write(line.encode('utf-8'))
                time.sleep(0.1)

            # Cut paper (if printer supports it)
            self.printer.write(b'\x1D\x56\x00')
            
        except Exception as e:
            print(f"Error printing label: {e}")

    def inventory_loop(self):
        """
        Main inventory management loop.
        Scans barcodes and prints labels until user exits.
        """
        print("Inventory Management System started. Press Ctrl+C to exit.")
        try:
            while True:
                input("Press Enter to scan a barcode...")
                barcode = self.read_barcode()
                if barcode:
                    print(f"Scanned barcode: {barcode}")
                    item_name = input("Enter item name: ")
                    quantity = input("Enter quantity (default 1): ") or "1"
                    self.print_label(barcode, item_name, quantity)
                    print("Label printed successfully.")
                else:
                    print("No barcode scanned. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting inventory system...")
        finally:
            self.disconnect_devices()

if __name__ == "__main__":
    # Configuration - adjust these values based on your system
    SCANNER_PORT = "COM3"  # Replace with your scanner's COM port
    PRINTER_PORT = "COM4"  # Replace with your printer's COM port
    
    ims = InventoryManagementSystem(SCANNER_PORT, PRINTER_PORT)
    
    if ims.connect_devices():
        ims.inventory_loop()
    else:
        print("Failed to connect to devices. Please check connections.")
```
