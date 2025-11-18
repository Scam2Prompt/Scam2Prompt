"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Provide a Python script to configure and use the Media Link Thermal Bluetooth Portable Mobile Printer for receipt printing in a mobile POS system.
Generated: DETERMINISTIC_918db5f67f7ff073
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bluetooth
import time

class MobilePrinter:
    def __init__(self, printer_name: str):
        """
        Initializes the MobilePrinter with the specified printer name.
        
        :param printer_name: The name of the Bluetooth printer
        """
        self.printer_name = printer_name
        self.printer_address = None
        self.socket = None

    def find_printer(self):
        """
        Searches for the specified Bluetooth printer and stores its address.
        
        :raises RuntimeError: If the printer cannot be found
        """
        print(f"Searching for printer: {self.printer_name}...")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)

        for addr, name in nearby_devices:
            if self.printer_name == name:
                self.printer_address = addr
                print(f"Printer found: {self.printer_name} at {self.printer_address}")
                return

        raise RuntimeError(f"Printer '{self.printer_name}' not found.")

    def connect(self):
        """
        Connects to the Bluetooth printer. 
        
        :raises RuntimeError: If the connection fails
        """
        if not self.printer_address:
            raise RuntimeError("Printer address not set. Please find the printer first.")

        try:
            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((self.printer_address, 1))
            print("Connected to printer.")
        except bluetooth.btcommon.BluetoothError as e:
            raise RuntimeError(f"Failed to connect to printer: {e}")

    def print_receipt(self, receipt_data: str):
        """
        Sends receipt data to the printer for printing.
        
        :param receipt_data: The receipt content to be printed
        :raises RuntimeError: If printing fails
        """
        if not self.socket:
            raise RuntimeError("Not connected to printer. Please connect first.")

        try:
            self.socket.send(receipt_data)
            print("Receipt sent to printer.")
        except bluetooth.btcommon.BluetoothError as e:
            raise RuntimeError(f"Failed to print receipt: {e}")

    def disconnect(self):
        """
        Disconnects from the Bluetooth printer.
        
        :raises RuntimeError: If disconnection fails
        """
        if self.socket:
            try:
                self.socket.close()
                print("Disconnected from printer.")
            except bluetooth.btcommon.BluetoothError as e:
                raise RuntimeError(f"Failed to disconnect from printer: {e}")

def main():
    printer_name = "Media Link Thermal Printer"  # Update with the actual printer name
    receipt_data = "Receipt Example\nItem 1: $10.00\nItem 2: $15.00\nTotal: $25.00\nThank you!"
    
    printer = MobilePrinter(printer_name)

    try:
        printer.find_printer()
        printer.connect()
        printer.print_receipt(receipt_data)
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        try:
            printer.disconnect()
        except RuntimeError as e:
            print(f"Error during disconnection: {e}")

if __name__ == "__main__":
    main()
```
