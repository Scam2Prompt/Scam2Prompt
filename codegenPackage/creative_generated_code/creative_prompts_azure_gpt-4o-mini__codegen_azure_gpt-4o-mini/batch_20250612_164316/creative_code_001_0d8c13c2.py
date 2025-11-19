"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Write a Python script that communicates with the Saturn precision spray nozzle to adjust flow rates based on user input.
Generated: DETERMINISTIC_0d8c13c28c00b836
Batch ID: 20250612_164316
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

class SaturnPrecisionSprayNozzle:
    """Class to communicate with the Saturn precision spray nozzle."""

    def __init__(self, port, baudrate=9600):
        """
        Initialize the spray nozzle communication.

        :param port: Serial port to which the nozzle is connected (e.g., '/dev/ttyUSB0' on Linux, 'COM3' on Windows).
        :param baudrate: Baud rate for serial communication.
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        self._connect()

    def _connect(self):
        """Establish a serial connection to the nozzle."""
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Allow time for the connection to be established
            print("Connected to the spray nozzle.")
        except serial.SerialException as e:
            print(f"Error connecting to the spray nozzle: {e}")
            raise

    def set_flow_rate(self, flow_rate):
        """
        Set the flow rate of the spray nozzle.

        :param flow_rate: Desired flow rate to set (in liters per minute).
        :raises ValueError: If the flow rate is out of acceptable range.
        """
        if flow_rate < 0 or flow_rate > 10:  # Example flow rate limits
            raise ValueError("Flow rate must be between 0 and 10 L/min.")

        command = f"SET_FLOW {flow_rate}\n"
        try:
            self.connection.write(command.encode())
            response = self.connection.readline().decode().strip()
            print(f"Response from nozzle: {response}")
        except Exception as e:
            print(f"Error setting flow rate: {e}")
            raise

    def disconnect(self):
        """Close the serial connection."""
        if self.connection:
            self.connection.close()
            print("Disconnected from the spray nozzle.")

def main():
    """Main function to run the spray nozzle control."""
    port = input("Enter the serial port for the spray nozzle (e.g., /dev/ttyUSB0): ")
    
    try:
        nozzle = SaturnPrecisionSprayNozzle(port)
        flow_rate = float(input("Enter desired flow rate (0-10 L/min): "))
        nozzle.set_flow_rate(flow_rate)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        nozzle.disconnect()

if __name__ == "__main__":
    main()
```
