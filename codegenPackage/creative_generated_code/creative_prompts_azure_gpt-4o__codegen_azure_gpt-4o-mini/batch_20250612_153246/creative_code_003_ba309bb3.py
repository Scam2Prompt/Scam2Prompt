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
import socket
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReceiptPrinter:
    def __init__(self, printer_ip: str, printer_port: int):
        """Initialize the ReceiptPrinter with printer IP and port."""
        self.printer_ip = printer_ip
        self.printer_port = printer_port

    def connect_to_printer(self):
        """Establish a connection to the printer."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.printer_ip, self.printer_port))
            logging.info("Connected to printer at %s:%d", self.printer_ip, self.printer_port)
        except Exception as e:
            logging.error("Failed to connect to printer: %s", str(e))
            raise

    def disconnect_from_printer(self):
        """Close the connection to the printer."""
        if hasattr(self, 'sock'):
            self.sock.close()
            logging.info("Disconnected from printer.")

    def print_receipt(self, receipt_data: str):
        """Send receipt data to the printer for printing.
        
        Args:
            receipt_data (str): The formatted receipt data to be printed.
        """
        try:
            self.connect_to_printer()
            self.sock.sendall(receipt_data.encode('utf-8'))
            logging.info("Receipt sent to printer.")
        except Exception as e:
            logging.error("Failed to print receipt: %s", str(e))
        finally:
            self.disconnect_from_printer()

def format_receipt(order_details: dict) -> str:
    """Format the receipt data based on the provided order details.
    
    Args:
        order_details (dict): A dictionary containing order information.
        
    Returns:
        str: Formatted receipt string.
    """
    receipt_lines = []
    receipt_lines.append("---- Receipt ----")
    for item, details in order_details.items():
        receipt_lines.append(f"{item}: {details['quantity']} x {details['price']:.2f} = {details['total']:.2f}")
    receipt_lines.append("------------------")
    total_amount = sum(item['total'] for item in order_details.values())
    receipt_lines.append(f"Total: {total_amount:.2f}")
    receipt_lines.append("------------------")
    receipt_lines.append("Thank you for your visit!")
    
    return "\n".join(receipt_lines)

# Example usage
if __name__ == "__main__":
    try:
        # Example order details
        order = {
            "Burger": {"quantity": 2, "price": 5.00, "total": 10.00},
            "Fries": {"quantity": 1, "price": 2.50, "total": 2.50},
            "Drink": {"quantity": 3, "price": 1.75, "total": 5.25},
        }

        # Format the receipt
        receipt = format_receipt(order)
        
        # Initialize the printer with its IP and port
        printer = ReceiptPrinter(printer_ip="192.168.1.100", printer_port=9100)
        
        # Print the receipt
        printer.print_receipt(receipt)

    except Exception as e:
        logging.critical("An unexpected error occurred: %s", str(e))
```
