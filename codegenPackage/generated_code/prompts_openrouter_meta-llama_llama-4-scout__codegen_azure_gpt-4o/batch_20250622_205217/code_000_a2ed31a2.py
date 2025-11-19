"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Write a Python script to control a Brother ScanNCut SDX135 machine for cutting custom designs.
Generated: DETERMINISTIC_a2ed31a25d0393dc
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import os

class BrotherScanNCutController:
    """
    A class to control the Brother ScanNCut SDX135 machine for cutting custom designs.
    """

    def __init__(self, port: str, baudrate: int = 9600):
        """
        Initialize the connection to the Brother ScanNCut machine.

        :param port: The serial port to connect to the machine (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for the serial connection (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        """
        Establish a serial connection to the Brother ScanNCut machine.
        """
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to Brother ScanNCut on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error connecting to Brother ScanNCut: {e}")
            raise

    def disconnect(self):
        """
        Close the serial connection to the Brother ScanNCut machine.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Disconnected from Brother ScanNCut.")

    def send_command(self, command: str):
        """
        Send a command to the Brother ScanNCut machine.

        :param command: The command string to send.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("No active connection to the Brother ScanNCut machine.")
        
        try:
            self.connection.write(command.encode('utf-8'))
            print(f"Command sent: {command}")
        except serial.SerialException as e:
            print(f"Error sending command: {e}")
            raise

    def upload_design(self, file_path: str):
        """
        Upload a design file to the Brother ScanNCut machine.

        :param file_path: The path to the design file (e.g., .fcm format).
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Design file not found: {file_path}")
        
        try:
            with open(file_path, 'rb') as file:
                design_data = file.read()
                self.connection.write(design_data)
                print(f"Design file '{file_path}' uploaded successfully.")
        except Exception as e:
            print(f"Error uploading design file: {e}")
            raise

    def start_cutting(self):
        """
        Send the command to start cutting the uploaded design.
        """
        try:
            self.send_command("START_CUT")
            print("Cutting started.")
        except Exception as e:
            print(f"Error starting cutting: {e}")
            raise

    def stop_cutting(self):
        """
        Send the command to stop cutting.
        """
        try:
            self.send_command("STOP_CUT")
            print("Cutting stopped.")
        except Exception as e:
            print(f"Error stopping cutting: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the controller
        controller = BrotherScanNCutController(port="COM3")

        # Connect to the machine
        controller.connect()

        # Upload a design file
        controller.upload_design("path/to/design.fcm")

        # Start cutting
        controller.start_cutting()

        # Stop cutting (optional, for demonstration purposes)
        controller.stop_cutting()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        controller.disconnect()
```

**Note:** This script assumes the Brother ScanNCut SDX135 machine communicates via a serial interface and accepts specific commands. You may need to adjust the commands and file format handling based on the actual machine's protocol and documentation.
