"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Provide example code for setting up the TSC TTP 244 Pro Barcode Printer to print custom labels with product details in a POS system.
Generated: DETERMINISTIC_5008442a41877758
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

class BarcodePrinter:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        """
        Initializes the BarcodePrinter instance.

        :param port: The serial port to which the printer is connected (default: '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial communication (default: 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the Barcode Printer.
        
        Raises:
            ConnectionError: If unable to connect to the printer.
        """
        try:
            self.connection = serial.Serial(self.port, self.baudrate)
            print(f"Connected to printer on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to printer: {e}")

    def disconnect(self):
        """
        Closes the connection to the Barcode Printer.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Disconnected from printer.")

    def print_label(self, product_details):
        """
        Sends label print command to the Barcode Printer.

        :param product_details: A dictionary containing product details to print on the label.
        
        Raises:
            ValueError: If product_details is not a valid dictionary.
        """
        if not isinstance(product_details, dict):
            raise ValueError("Product details must be a dictionary.")

        label_content = self.format_label(product_details)
        self.send_to_printer(label_content)

    def format_label(self, product_details):
        """
        Formats the label contents based on product details.

        :param product_details: A dictionary containing product details.
        :return: A formatted string to be printed on the label.
        """
        label_lines = []
        for key, value in product_details.items():
            label_lines.append(f"{key}: {value}")
        return "\n".join(label_lines)

    def send_to_printer(self, content):
        """
        Sends the formatted content to the printer.

        :param content: The formatted string content to print.
        
        Raises:
            RuntimeError: If there is an error during the print operation.
        """
        if self.connection and self.connection.is_open:
            try:
                self.connection.write(content.encode('utf-8'))
                print("Label sent to printer successfully.")
            except Exception as e:
                raise RuntimeError(f"Error while printing label: {e}")
        else:
            raise RuntimeError("Printer is not connected.")

def main():
    # Example usage of the BarcodePrinter class
    printer = BarcodePrinter(port='/dev/ttyUSB0', baudrate=9600)

    try:
        printer.connect()
        
        # Define product details
        product_details = {
            'Product Name': 'Sample Product',
            'SKU': '12345',
            'Price': '$9.99'
        }
        
        # Print the label
        printer.print_label(product_details)

    except Exception as e:
        print(e)

    finally:
        printer.disconnect()

if __name__ == "__main__":
    main()
```
