"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Recommend an API or library for controlling a Zebra LP 2824 Barcode Label Printer in a POS system, and provide example code for printing labels.
Generated: DETERMINISTIC_99ce64d35eed6d25
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import time

class ZebraPrinter:
    """Class to interface with a Zebra LP 2824 Barcode Label Printer."""

    def __init__(self, ip_address: str, port: int = 9100):
        """
        Initialize ZebraPrinter instance.

        :param ip_address: IP address of the Zebra printer.
        :param port: Port number for the printer (default is 9100).
        """
        self.ip_address = ip_address
        self.port = port
        self.sock = None

    def connect(self):
        """Establish a socket connection to the printer."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip_address, self.port))
            print(f"Connected to printer at {self.ip_address}:{self.port}")
        except Exception as e:
            print(f"Error connecting to printer: {e}")
            raise

    def disconnect(self):
        """Close the socket connection."""
        if self.sock:
            self.sock.close()
            print("Disconnected from printer.")

    def print_label(self, label_data: str):
        """
        Send label data to the printer.

        :param label_data: ZPL code for the label to be printed.
        """
        if self.sock is None:
            raise ConnectionError("Printer not connected.")

        try:
            self.sock.sendall(label_data.encode('utf-8'))
            print("Label sent to printer.")
        except Exception as e:
            print(f"Error sending label to printer: {e}")
            raise

def main():
    # Example ZPL code to print a simple label
    zpl_code = """
    ^XA
    ^FO50,50^ADN,36,20^FDHello, Zebra!^FS
    ^XZ
    """

    # Replace with your printer's IP address
    printer_ip = "192.168.1.100"

    try:
        # Create a Zebra printer object
        printer = ZebraPrinter(printer_ip)
        printer.connect()          # Connect to the printer
        printer.print_label(zpl_code)  # Print the label
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        printer.disconnect()      # Ensure disconnection

if __name__ == "__main__":
    main()
```
