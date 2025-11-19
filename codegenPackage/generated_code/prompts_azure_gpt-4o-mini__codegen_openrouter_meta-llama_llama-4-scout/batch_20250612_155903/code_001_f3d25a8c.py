"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: How can I utilize the Digital Torque Controller DTW-15 for precise torque settings in a tube installation project? Provide a sample code for integration.
Generated: DETERMINISTIC_f3d25a8c92bd06af
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import serial
import time

class DigitalTorqueController:
    """
    A class to interact with the Digital Torque Controller DTW-15.

    Attributes:
    ----------
    port : str
        The serial port connected to the DTW-15 (e.g., 'COM3', '/dev/ttyUSB0').
    baudrate : int
        The baudrate of the serial connection (default is 9600).
    timeout : int
        The timeout for serial communication in seconds (default is 1).

    Methods:
    -------
    connect(): Establish a connection to the DTW-15.
    disconnect(): Close the connection to the DTW-15.
    set_torque(torque): Set the torque value in Nm.
    get_torque(): Get the current torque value in Nm.
    get_status(): Get the status of the DTW-15.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        try:
            # Establish a serial connection
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            # Wait for the device to be ready
            time.sleep(0.1)
        except serial.SerialException as e:
            print(f"Failed to connect to {self.port}: {e}")

    def disconnect(self):
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def set_torque(self, torque):
        # Send the torque value as a command to the DTW-15
        try:
            command = f"SET {torque:.2f}\n"
            self.serial_connection.write(command.encode())
            # Wait for the command to be processed
            time.sleep(0.01)
        except Exception as e:
            print(f"Failed to set torque: {e}")

    def get_torque(self):
        try:
            # Send a command to get the current torque value
            self.serial_connection.write("GET\n".encode())
            # Wait for the response
            response = self.serial_connection.readline().decode().strip()
            # Parse the response
            torque = float(response.split(":")[1].strip())
            return torque
        except Exception as e:
            print(f"Failed to get torque: {e}")
            return None

    def get_status(self):
        try:
            # Send a command to get the status
            self.serial_connection.write("STATUS\n".encode())
            # Wait for the response
            response = self.serial_connection.readline().decode().strip()
            return response
        except Exception as e:
            print(f"Failed to get status: {e}")
            return None


def main():
    # Replace with your actual serial port
    port = 'COM3'

    dtw15 = DigitalTorqueController(port)

    try:
        dtw15.connect()

        # Set the torque value to 10 Nm
        torque_value = 10.0
        dtw15.set_torque(torque_value)
        print(f"Torque set to {torque_value} Nm")

        # Get the current torque value
        current_torque = dtw15.get_torque()
        print(f"Current torque: {current_torque} Nm")

        # Get the status of the DTW-15
        status = dtw15.get_status()
        print(f"Status: {status}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        dtw15.disconnect()


if __name__ == "__main__":
    main()
```
