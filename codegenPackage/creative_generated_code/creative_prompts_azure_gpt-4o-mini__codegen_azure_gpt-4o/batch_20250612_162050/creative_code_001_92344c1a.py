"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write a Python script to automate the process of cutting cardboard tubes to specific sizes using a PLC-controlled machine.
Generated: DETERMINISTIC_92344c1a096595a8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import serial

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TubeCuttingMachine:
    """
    A class to control and automate the process of cutting cardboard tubes using a PLC-controlled machine.
    """

    def __init__(self, serial_port: str, baud_rate: int = 9600):
        """
        Initializes the tube cutting machine object with communication settings.
        
        :param serial_port: The serial port connected to the PLC (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baud_rate: The baud rate for the serial communication (default is 9600).
        """
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.connection = None

    def connect_to_plc(self):
        """
        Establishes a connection to the PLC via the serial port.
        """
        try:
            self.connection = serial.Serial(self.serial_port, self.baud_rate, timeout=2)
            logging.info("Successfully connected to PLC on port %s.", self.serial_port)
        except serial.SerialException as e:
            logging.error("Failed to connect to PLC: %s", str(e))
            raise

    def send_command(self, command: str):
        """
        Sends a command to the PLC.
        
        :param command: The command string to be sent to the PLC.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("PLC connection is not open.")
        
        try:
            self.connection.write(command.encode('utf-8'))
            logging.info("Command sent to PLC: %s", command)
        except serial.SerialException as e:
            logging.error("Failed to send command to PLC: %s", str(e))
            raise

    def read_response(self) -> str:
        """
        Reads the response from the PLC.
        
        :return: The response string from the PLC.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("PLC connection is not open.")
        
        try:
            response = self.connection.readline().decode('utf-8').strip()
            logging.info("Response received from PLC: %s", response)
            return response
        except serial.SerialException as e:
            logging.error("Failed to read response from PLC: %s", str(e))
            raise

    def cut_tube(self, length: float):
        """
        Sends a command to the PLC to cut a cardboard tube to the specified length.
        
        :param length: The length (in millimeters) to cut the tube.
        """
        if length <= 0:
            raise ValueError("Length must be greater than zero.")
        
        command = f"CUT:{length}"
        self.send_command(command)
        response = self.read_response()
        
        if response != "OK":
            logging.error("Failed to cut tube. PLC response: %s", response)
            raise RuntimeError(f"PLC error: {response}")
        
        logging.info("Tube cutting successful for length: %.2f mm", length)

    def disconnect_from_plc(self):
        """
        Closes the connection to the PLC.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            logging.info("Disconnected from PLC.")

def main():
    """
    The main function to automate the tube cutting process.
    """
    # Configuration
    serial_port = "COM3"  # Modify as necessary
    tube_lengths = [500.0, 750.0, 1000.0]  # Example tube lengths to cut (in mm)

    # Initialize the machine
    machine = TubeCuttingMachine(serial_port)

    try:
        # Connect to the PLC
        machine.connect_to_plc()

        # Process each tube length
        for length in tube_lengths:
            logging.info("Starting tube cutting for length: %.2f mm", length)
            machine.cut_tube(length)
            time.sleep(1)  # Delay to ensure the PLC has time to complete the cut

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
    finally:
        # Disconnect from the PLC
        machine.disconnect_from_plc()

if __name__ == "__main__":
    main()
```
