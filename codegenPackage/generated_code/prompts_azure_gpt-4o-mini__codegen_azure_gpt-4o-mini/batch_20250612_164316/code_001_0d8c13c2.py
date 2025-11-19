"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Write a Python script that communicates with the Saturn precision spray nozzle to adjust flow rates based on user input.
Generated: DETERMINISTIC_0d8c13c28c00b836
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import time

class SaturnSprayNozzle:
    """
    A class to represent the Saturn precision spray nozzle.
    It handles communication with the nozzle to adjust flow rates.
    """

    def __init__(self, port: str, baudrate: int = 9600):
        """
        Initializes the SaturnSprayNozzle with the specified serial port and baud rate.

        :param port: The serial port to which the nozzle is connected.
        :param baudrate: The baud rate for serial communication (default is 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None

    def connect(self):
        """Establishes a connection to the spray nozzle."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
            print("Connected to the Saturn spray nozzle.")
        except serial.SerialException as e:
            print(f"Error connecting to the nozzle: {e}")
            raise

    def disconnect(self):
        """Closes the connection to the spray nozzle."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from the Saturn spray nozzle.")

    def set_flow_rate(self, flow_rate: float):
        """
        Sends a command to the nozzle to set the flow rate.

        :param flow_rate: The desired flow rate in liters per minute.
        :raises ValueError: If the flow rate is out of the acceptable range.
        """
        if flow_rate < 0 or flow_rate > 10:  # Assuming 0-10 L/min is the valid range
            raise ValueError("Flow rate must be between 0 and 10 liters per minute.")

        command = f"SET_FLOW_RATE {flow_rate}\n"
        try:
            self.serial_connection.write(command.encode())
            response = self.serial_connection.readline().decode().strip()
            print(f"Response from nozzle: {response}")
        except Exception as e:
            print(f"Error setting flow rate: {e}")
            raise

def main():
    """Main function to run the spray nozzle control script."""
    nozzle = SaturnSprayNozzle(port='/dev/ttyUSB0')  # Update with the correct port

    try:
        nozzle.connect()
        flow_rate = float(input("Enter the desired flow rate (0-10 L/min): "))
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
