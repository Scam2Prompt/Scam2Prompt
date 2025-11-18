"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Generate code to connect and print receipts using the EPSON TM-T82II Thermal Receipt Printer via USB in a Python-based POS application.
Generated: DETERMINISTIC_bec230a9324825d4
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import usb.core
import usb.util


class EpsonPrinter:
    """
    A class to handle communication with the EPSON TM-T82II Thermal Receipt Printer via USB.
    """

    def __init__(self, vendor_id: int = 0x04b8, product_id: int = 0x0202):
        """
        Initialize the printer connection.

        Args:
            vendor_id (int): USB Vendor ID for EPSON (default is 0x04b8).
            product_id (int): USB Product ID for TM-T82II (default is 0x0202).
        """
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = None
        self.endpoint_out = None

    def connect(self):
        """
        Connect to the EPSON TM-T82II printer via USB.

        Raises:
            RuntimeError: If the printer device is not found or cannot be configured.
        """
        # Find USB device with vendor and product IDs
        self.device = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)

        if self.device is None:
            raise RuntimeError("Epson Printer not found. Please check the USB connection.")

        try:
            # Detach kernel driver if necessary
            if self.device.is_kernel_driver_active(0):
                self.device.detach_kernel_driver(0)

            # Set configuration and endpoint
            self.device.set_configuration()
            cfg = self.device.get_active_configuration()
            interface = cfg[(0, 0)]
            self.endpoint_out = usb.util.find_descriptor(
                interface,
                custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT,
            )

            if self.endpoint_out is None:
                raise RuntimeError("Unable to find output endpoint on the printer.")
        except usb.core.USBError as e:
            raise RuntimeError(f"Failed to connect to the printer: {str(e)}")

    def print_receipt(self, content: str):
        """
        Print a receipt with the given content.

        Args:
            content (str): The content to print on the receipt.
        
        Raises:
            ValueError: If content is empty.
            RuntimeError: If unable to send data to the printer.
        """
        if not content:
            raise ValueError("Content to print cannot be empty.")

        # Prepare the content by adding necessary printer commands
        ESC_POS_INITIALIZE = b'\x1b@'  # Initialize printer
        ESC_POS_CUT = b'\x1dV\x00'    # Cut paper

        try:
            # Send initialization command
            self.endpoint_out.write(ESC_POS_INITIALIZE)

            # Send the main receipt content
            receipt_data = content.encode('utf-8') + b'\n'
            self.endpoint_out.write(receipt_data)

            # Send the cut paper command
            self.endpoint_out.write(ESC_POS_CUT)
        except usb.core.USBError as e:
            raise RuntimeError(f"Failed to print receipt: {str(e)}")

    def disconnect(self):
        """
        Release resources and disconnect from the printer.
        """
        if self.device:
            usb.util.dispose_resources(self.device)
            self.device = None


# Example usage
if __name__ == "__main__":
    try:
        printer = EpsonPrinter()
        printer.connect()
        receipt_content = "Thank you for shopping!\nDate: 2023-10-03\nTotal: $25.00\n"
        printer.print_receipt(receipt_content)
        print("Receipt printed successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        printer.disconnect()
```
