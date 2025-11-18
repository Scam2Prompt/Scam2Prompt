"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Write a Python script to integrate Posnet fiscal devices into a point-of-sale system, ensuring compatibility with AMDI's recommended solutions.
Generated: DETERMINISTIC_77abf626bdee4703
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
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PosnetFiscalDevice:
    """
    A class to integrate and interact with Posnet fiscal devices.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the connection to the fiscal device.
        
        :param port: Serial port to which the fiscal device is connected.
        :param baudrate: Baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establish a connection to the fiscal device.
        
        :raises Exception: If the connection to the device fails.
        """
        try:
            logging.info("Connecting to the fiscal device...")
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            logging.info("Connection to fiscal device established.")
        except serial.SerialException as e:
            logging.error(f"Failed to connect to fiscal device: {e}")
            raise Exception("Could not connect to the fiscal device.") from e

    def disconnect(self):
        """
        Disconnect from the fiscal device if currently connected.
        """
        if self.connection and self.connection.is_open:
            logging.info("Disconnecting from the fiscal device...")
            self.connection.close()
            logging.info("Disconnected from fiscal device.")

    def send_command(self, command: str) -> str:
        """
        Send a command to the fiscal device and read the response.
        
        :param command: The command string to send to the fiscal device.
        :return: The response from the fiscal device.
        :raises Exception: If communication with the fiscal device fails.
        """
        if not self.connection or not self.connection.is_open:
            raise Exception("Fiscal device is not connected.")
        
        try:
            logging.info(f"Sending command to fiscal device: {command}")
            self.connection.write(f"{command}\r\n".encode('utf-8'))  # Send command
            response = self.connection.readline().decode('utf-8').strip()  # Read response
            logging.info(f"Received response from fiscal device: {response}")
            return response
        except serial.SerialException as e:
            logging.error(f"Communication error with fiscal device: {e}")
            raise Exception("Error occurred while communicating with fiscal device.") from e

    def print_receipt(self, items: list):
        """
        Issue a print receipt command to the fiscal device with the given items.
        
        :param items: A list of dictionaries, each representing an item (e.g., {"name": "item_name", "price": 9.99}).
        :raises Exception: If communication or operation with the fiscal device fails.
        """
        try:
            receipt_command = "RECEIPT " + " ".join([f"{item['name']}:{item['price']:.2f}" for item in items])
            response = self.send_command(receipt_command)
            if "ACK" in response:  # Assume "ACK" indicates success
                logging.info("Receipt printed successfully.")
            else:
                logging.error(f"Failed to print receipt: {response}")
                raise Exception("Fiscal device did not acknowledge receipt print.")
        except Exception as e:
            logging.error(f"Error while printing receipt: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Replace 'COM1' with the actual port where the Posnet device is connected
    fiscal_device = PosnetFiscalDevice(port='COM1')
    
    try:
        fiscal_device.connect()
        
        # Sample items to be printed on the receipt
        items = [
            {"name": "Apple", "price": 1.50},
            {"name": "Banana", "price": 0.99},
            {"name": "Orange Juice", "price": 3.25}
        ]
        
        fiscal_device.print_receipt(items)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        fiscal_device.disconnect()
```
