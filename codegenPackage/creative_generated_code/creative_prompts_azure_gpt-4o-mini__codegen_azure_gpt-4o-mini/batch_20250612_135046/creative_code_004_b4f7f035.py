"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openspa.info
Prompt: How do I reset a blocked Octagon receiver using RS232 in OpenSPA?
Generated: DETERMINISTIC_b4f7f03558723e6f
Batch ID: 20250612_135046
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

class OctagonReceiver:
    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initialize the OctagonReceiver with the specified serial port settings.

        :param port: The COM port to which the receiver is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baud_rate: The baud rate for the serial communication (default is 9600).
        :param timeout: Timeout for read operations (default is 1.0 seconds).
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """Establish a serial connection to the receiver."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            time.sleep(2)  # Wait for the connection to settle
            print("Connected to Octagon receiver.")
        except serial.SerialException as e:
            print(f"Error connecting to serial port {self.port}: {e}")
            raise

    def reset_receiver(self):
        """Send a reset command to the Octagon receiver."""
        if not self.serial_connection or not self.serial_connection.is_open:
            raise RuntimeError("Serial connection is not established. Please connect first.")

        reset_command = b'\x1B\x4D'  # Example reset command, replace with actual command as needed
        try:
            self.serial_connection.write(reset_command)
            print("Reset command sent to the receiver.")
            time.sleep(1)  # Delay to allow the receiver to process the command

            # Optionally, read response to confirm reset (if applicable)
            response = self.serial_connection.read(100)  # Read up to 100 bytes
            print(f"Response from receiver: {response.decode('utf-8', errors='ignore')}")

        except serial.SerialException as e:
            print(f"Error sending reset command: {e}")
            raise

    def disconnect(self):
        """Close the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from Octagon receiver.")

if __name__ == "__main__":
    try:
        # Replace 'COM3' with the actual port where the Octagon receiver is connected
        receiver = OctagonReceiver(port='COM3')
        receiver.connect()
        receiver.reset_receiver()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        receiver.disconnect()
```
