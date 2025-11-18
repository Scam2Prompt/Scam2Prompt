"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Write Python code to integrate a barcode validation system using Nordson's barcode confirmation machine, as described on the Nordson Vietnam website.
Generated: DETERMINISTIC_c89acd9843bef667
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial

class BarcodeValidator:
    """
    A class to integrate and validate barcodes using Nordson's barcode confirmation machine.

    This class communicates with the Nordson machine via a serial connection.
    """

    def __init__(self, port: str, baud_rate: int = 9600, timeout: int = 2):
        """
        Initialize the BarcodeValidator.

        Args:
            port (str): Serial port to which the machine is connected (e.g., 'COM3' or '/dev/ttyUSB0').
            baud_rate (int): Baud rate for serial communication (default is 9600).
            timeout (int): Timeout for serial communication in seconds (default is 2).
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establish a serial connection to the Nordson barcode machine.

        Raises:
            Exception: If unable to establish a serial connection.
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout,
            )
            if self.connection.is_open:
                print(f"Connected to Nordson barcode machine on {self.port}")
        except serial.SerialException as e:
            raise Exception(f"Failed to connect to the Nordson machine: {e}")

    def validate_barcode(self, barcode: str) -> bool:
        """
        Validate a barcode using the Nordson machine.

        Args:
            barcode (str): The barcode string to validate.

        Returns:
            bool: True if the barcode is valid, False otherwise.

        Raises:
            Exception: If unable to communicate with the machine.
        """
        if not self.connection or not self.connection.is_open:
            raise Exception("Connection to the Nordson machine is not established.")

        try:
            # Send the barcode string to the machine
            self.connection.write(f"{barcode}\n".encode())

            # Read the response from the machine
            response = self.connection.readline().decode().strip()

            # Interpret the machine's response
            if response == "VALID":
                return True
            elif response == "INVALID":
                return False
            else:
                raise Exception(f"Unexpected response from Nordson machine: {response}")
        except Exception as e:
            raise Exception(f"Error during barcode validation: {e}")

    def disconnect(self):
        """
        Close the serial connection to the Nordson machine.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print(f"Disconnected from Nordson barcode machine on {self.port}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the BarcodeValidator
        validator = BarcodeValidator(port="COM3", baud_rate=9600)

        # Connect to the machine
        validator.connect()

        # Validate a test barcode
        test_barcode = "123456789"
        is_valid = validator.validate_barcode(test_barcode)
        if is_valid:
            print(f"Barcode {test_barcode} is VALID.")
        else:
            print(f"Barcode {test_barcode} is INVALID.")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        # Disconnect from the machine
        validator.disconnect()
```
