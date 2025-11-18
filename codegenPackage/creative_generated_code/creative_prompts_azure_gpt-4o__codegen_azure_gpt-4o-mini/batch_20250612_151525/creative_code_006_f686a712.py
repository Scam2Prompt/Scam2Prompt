"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Write code to automate adhesive dispensing using Nordson's MiniSquirt machine for small-scale operations.
Generated: DETERMINISTIC_f686a7123d223226
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import serial

class MiniSquirtController:
    """
    Class to control the Nordson MiniSquirt adhesive dispensing machine.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the MiniSquirtController with the specified serial port.

        Parameters:
            port (str): The serial port to which the MiniSquirt is connected.
            baudrate (int): Baud rate for serial communication. Default is 9600.
            timeout (int): Timeout for serial communication in seconds. Default is 1 second.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        self._connect()

    def _connect(self):
        """
        Establishes a connection to the MiniSquirt machine.
        """
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to MiniSquirt on {self.port}")
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to MiniSquirt: {e}")

    def dispense(self, volume, duration):
        """
        Dispenses adhesive using the MiniSquirt machine.

        Parameters:
            volume (float): The volume of adhesive to dispense in milliliters.
            duration (float): The duration to dispense the adhesive in seconds.

        Raises:
            ValueError: If volume or duration are not positive numbers.
        """
        if volume <= 0 or duration <= 0:
            raise ValueError("Volume and duration must be positive numbers.")

        try:
            # Command format: "DISPENSE <volume> <duration>"
            command = f"DISPENSE {volume} {duration}\n"
            self.connection.write(command.encode('utf-8'))
            print(f"Dispensing {volume}ml for {duration}s...")
            time.sleep(duration)  # Simulate dispensing time
            print("Dispensing completed.")
        except Exception as e:
            raise RuntimeError(f"Error during dispensing: {e}")

    def stop(self):
        """
        Stops the dispensing operation.
        """
        try:
            self.connection.write(b"STOP\n")
            print("Dispensing stopped.")
        except Exception as e:
            raise RuntimeError(f"Error while stopping the dispensing: {e}")

    def close(self):
        """
        Closes the serial connection to the MiniSquirt machine.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Connection to MiniSquirt closed.")

if __name__ == "__main__":
    try:
        # Example usage
        port = "/dev/ttyUSB0"  # Update with the correct port for your system
        mini_squirt = MiniSquirtController(port)

        # Dispense 5ml of adhesive for 2 seconds
        mini_squirt.dispense(volume=5.0, duration=2.0)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mini_squirt.close()
```
