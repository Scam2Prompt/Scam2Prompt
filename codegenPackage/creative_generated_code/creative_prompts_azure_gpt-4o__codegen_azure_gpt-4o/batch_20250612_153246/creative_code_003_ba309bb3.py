"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Develop a script to automate receipt printing using DemirSoft's "Termal Adisyon Yazıcı" and integrate it with a restaurant POS system.
Generated: DETERMINISTIC_ba309bb3eb289322
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial
import sys

class ReceiptPrinter:
    """
    A class to handle receipt printing using DemirSoft's "Termal Adisyon Yazıcı".

    Attributes:
        port (str): Serial port used for communication with the printer
        baudrate (int): Baudrate for the serial connection
        timeout (int): Timeout for the serial connection
    """

    def __init__(self, port="COM1", baudrate=9600, timeout=2):
        """
        Initializes the ReceiptPrinter class.

        Args:
            port (str): Serial port used for communication
            baudrate (int): Baudrate for the communication
            timeout (int): Timeout for the serial connection
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection with the thermal receipt printer.

        Raises:
            Exception: If the connection fails
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
        except Exception as e:
            raise Exception(f"Failed to connect to printer: {e}")

    def disconnect(self):
        """
        Closes the connection with the thermal receipt printer.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def print_receipt(self, receipt_data):
        """
        Sends receipt data to the printer.

        Args:
            receipt_data (str): The formatted string containing receipt information

        Raises:
            Exception: If the receipt printing fails
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise Exception("Printer is not connected.")
        
        try:
            # Send receipt data to the printer
            self.serial_connection.write(receipt_data.encode('utf-8'))
        except Exception as e:
            raise Exception(f"Failed to print receipt: {e}")

    @staticmethod
    def format_receipt(order_details, total_price):
        """
        Formats order details and total price into a printable receipt string.

        Args:
            order_details (list): List of tuples (item_name, quantity, price)
            total_price (float): Total price of the order

        Returns:
            str: Formatted string for receipt
        """
        receipt_lines = ["Restaurant XYZ", "----------------------"]
        for item_name, quantity, price in order_details:
            receipt_lines.append(f"{item_name} x{quantity} - {price:.2f} TL")
        receipt_lines.append("----------------------")
        receipt_lines.append(f"Total: {total_price:.2f} TL")
        receipt_lines.append("----------------------")
        receipt_lines.append("Thank you for your visit!")
        return "\n".join(receipt_lines)


if __name__ == "__main__":
    # Example order details
    order = [
        ("Burger", 2, 50.0),
        ("Fries", 1, 30.0),
        ("Drink", 2, 20.0)
    ]
    total = sum(item[1] * item[2] for item in order)

    # Format receipt data
    receipt_content = ReceiptPrinter.format_receipt(order, total)

    # Printer setup
    printer = ReceiptPrinter(port="COM3")  # Replace "COM3" with the actual port of your printer

    try:
        # Connect to printer
        printer.connect()

        # Print the receipt
        printer.print_receipt(receipt_content)

        print("Receipt printed successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Disconnect from printer
        printer.disconnect()
```
