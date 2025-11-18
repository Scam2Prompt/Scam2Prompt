"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Provide an example of how to use Hengstler industrial printers, like the eXtendo X-80 series, for automated kiosk printing in Python.
Generated: DETERMINISTIC_44dac170f37675ca
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial
import time

class HengstlerPrinter:
    """
    A class to interface with Hengstler industrial printers, specifically the eXtendo X-80 series.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the printer connection.
        
        :param port: The serial port to which the printer is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial communication.
        :param timeout: Timeout for the serial communication.
        """
        self.port = port
        self.baudrate = baudrate
        
        try:
            # Establish the serial connection
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=timeout)
            time.sleep(2)  # Allow time for the connection to initialize
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to printer on {self.port}: {e}")

    def send_print_command(self, data: str) -> None:
        """
        Sends a print command to the printer.

        :param data: The data to be printed, formatted according to the printer's requirements.
        :raises ValueError: If the data is empty or invalid.
        :raises RuntimeError: If the print command fails.
        """
        if not data:
            raise ValueError("Data to print cannot be empty.")

        try:
            # Send the print command
            self.serial_connection.write(data.encode('utf-8'))
            self.serial_connection.flush()  # Ensure all data is sent
            time.sleep(1)  # Wait for the printer to process the data
        except serial.SerialTimeoutException:
            raise RuntimeError("Printing timed out. Please check the printer connection.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while printing: {e}")

    def close(self) -> None:
        """
        Closes the serial connection to the printer.
        """
        if self.serial_connection.is_open:
            self.serial_connection.close()

def main() -> None:
    """
    Main function to demonstrate the usage of the HengstlerPrinter class for printing.
    """
    # Configure the printer connection (update with the correct port)
    printer = HengstlerPrinter(port='/dev/ttyUSB0')

    try:
        # Define the data to print
        data_to_print = "Sample Print Job for Hengstler Printer"
        
        # Send the print command
        printer.send_print_command(data_to_print)
        print("Print command sent successfully.")
        
    except (ValueError, RuntimeError) as error:
        print(f"Error: {error}")
    finally:
        # Ensure the printer connection is closed
        printer.close()

if __name__ == "__main__":
    main()
```
